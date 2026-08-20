"""Invoking squishrunner and turning its reports back into structured data."""

from __future__ import annotations

import asyncio
import json
import os
import signal
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from collections.abc import Awaitable, Callable, Iterable
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from .config import SquishConfig

LineCallback = Callable[[str], Awaitable[None]]

JUNIT_REPORT = "report.xml"
STDOUT_REPORT = "report.txt"
RUN_META = "run.json"


class RunError(RuntimeError):
    """Raised when squishrunner could not be started at all."""


def _new_run_dir(config: SquishConfig) -> Path:
    # Local time, deliberately: these names are read by whoever ran the tests.
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")  # noqa: DTZ005
    run_dir = config.results_dir / stamp
    suffix = 1
    while run_dir.exists():
        suffix += 1
        run_dir = config.results_dir / f"{stamp}-{suffix}"
    run_dir.mkdir(parents=True)
    return run_dir


def build_command(
    config: SquishConfig,
    run_dir: Path,
    *,
    test_cases: Iterable[str] = (),
    snooze_factor: float | None = None,
    abort_on_fail: bool = False,
    retry: int | None = None,
    tags: Iterable[str] = (),
) -> list[str]:
    """Assemble the squishrunner argv for one run.

    Only file-based report generators are used (junit + stdout). That is
    deliberate: Squish rejects --resultdir when it is combined with a
    directory-based generator such as xml3.5 or html, and --resultdir is what
    collects failure screenshots and video.
    """
    cmd: list[str] = [
        str(config.runner),
        "--testsuite",
        str(config.suite_dir),
        # Start and stop a private squishserver for this run, so the caller
        # never has to manage a background server process.
        "--local",
    ]

    for name in test_cases:
        cmd += ["--testcase", str(config.suite_dir / name)]

    cmd += ["--reportgen", f"junit,{run_dir / JUNIT_REPORT}"]
    cmd += ["--reportgen", f"stdout,{run_dir / STDOUT_REPORT}"]
    cmd += ["--resultdir", str(run_dir)]

    envvars = config.envvars_file
    if envvars is not None and envvars.stat().st_size > 0:
        cmd += ["--envvars", str(envvars)]

    if snooze_factor is not None:
        cmd += ["--snoozeFactor", str(snooze_factor)]
    if abort_on_fail:
        cmd += ["--abortOnFail"]
    if retry is not None:
        cmd += ["--retry", str(retry)]
    for tag in tags:
        cmd += ["--tags", tag]

    # Make a test failure visible in the exit code as well as in the report.
    cmd += ["--exitCodeOnFail", "1"]
    return cmd


def _kill_tree(process: asyncio.subprocess.Process) -> None:
    """Kill squishrunner and its children (squishserver and the AUT).

    Killing only squishrunner would leave the application under test on screen,
    holding the display and blocking the next run.
    """
    if process.returncode is not None:
        return
    if os.name == "nt":
        subprocess.run(
            ["taskkill", "/F", "/T", "/PID", str(process.pid)],
            capture_output=True,
            check=False,
        )
    else:
        try:
            os.killpg(os.getpgid(process.pid), signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            process.kill()


async def _pump(
    stream: asyncio.StreamReader,
    sink: list[str],
    on_line: LineCallback | None,
) -> None:
    while True:
        raw = await stream.readline()
        if not raw:
            return
        line = raw.decode("utf-8", errors="replace").rstrip()
        sink.append(line)
        if on_line is not None:
            await on_line(line)


@dataclass
class RunResult:
    run_dir: Path
    command: list[str]
    exit_code: int | None
    timed_out: bool
    duration_seconds: float
    output_lines: list[str]

    def as_dict(self) -> dict[str, object]:
        return {
            "run_dir": str(self.run_dir),
            "command": self.command,
            "exit_code": self.exit_code,
            "timed_out": self.timed_out,
            "duration_seconds": round(self.duration_seconds, 1),
        }


async def run_suite(
    config: SquishConfig,
    *,
    test_cases: Iterable[str] = (),
    snooze_factor: float | None = None,
    abort_on_fail: bool = False,
    retry: int | None = None,
    tags: Iterable[str] = (),
    timeout_seconds: float = 900.0,
    on_line: LineCallback | None = None,
) -> RunResult:
    """Run the suite, or selected cases, to completion or until the timeout."""
    run_dir = _new_run_dir(config)
    cmd = build_command(
        config,
        run_dir,
        test_cases=test_cases,
        snooze_factor=snooze_factor,
        abort_on_fail=abort_on_fail,
        retry=retry,
        tags=tags,
    )

    started = time.monotonic()
    try:
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
            cwd=str(config.suite_dir),
            start_new_session=os.name != "nt",
        )
    except OSError as exc:  # squishrunner missing or not executable
        raise RunError(f"Could not start squishrunner: {exc}") from exc

    lines: list[str] = []
    assert process.stdout is not None
    pump = asyncio.create_task(_pump(process.stdout, lines, on_line))

    timed_out = False
    try:
        await asyncio.wait_for(process.wait(), timeout=timeout_seconds)
    except TimeoutError:
        timed_out = True
        _kill_tree(process)
        await process.wait()
    finally:
        pump.cancel()
        try:
            await pump
        except asyncio.CancelledError:
            pass

    result = RunResult(
        run_dir=run_dir,
        command=cmd,
        exit_code=process.returncode,
        timed_out=timed_out,
        duration_seconds=time.monotonic() - started,
        output_lines=lines,
    )

    # Persist metadata so the report can still be recovered after a client-side
    # timeout has discarded the tool result.
    (run_dir / RUN_META).write_text(
        json.dumps({**result.as_dict(), "python": sys.version}, indent=2),
        encoding="utf-8",
    )
    return result


def parse_junit(path: Path) -> dict[str, object]:
    """Parse a JUnit XML report into a summary plus per-test detail.

    Written defensively: every testcase element is collected however deeply it
    is nested, and the counters are recomputed from the elements themselves
    rather than read from the suite-level attributes.
    """
    root = ET.parse(path).getroot()
    tests: list[dict[str, object]] = []

    for node in root.iter("testcase"):
        failures = [c for c in node if c.tag in {"failure", "error"}]
        skipped = [c for c in node if c.tag == "skipped"]
        if failures:
            status = "fail"
        elif skipped:
            status = "skipped"
        else:
            status = "pass"
        tests.append(
            {
                "name": node.get("name"),
                "classname": node.get("classname"),
                "status": status,
                "time_seconds": float(node.get("time") or 0.0),
                "messages": [
                    (c.get("message") or (c.text or "")).strip()
                    for c in failures + skipped
                ],
            }
        )

    counts = {
        "total": len(tests),
        "passed": sum(t["status"] == "pass" for t in tests),
        "failed": sum(t["status"] == "fail" for t in tests),
        "skipped": sum(t["status"] == "skipped" for t in tests),
    }
    return {"summary": counts, "tests": tests}


def read_report(run_dir: Path, *, log_tail_lines: int = 80) -> dict[str, object]:
    """Collect everything known about one run directory."""
    report: dict[str, object] = {"run_dir": str(run_dir)}

    meta = run_dir / RUN_META
    if meta.is_file():
        try:
            report["run"] = json.loads(meta.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            report["run"] = None

    junit = run_dir / JUNIT_REPORT
    if junit.is_file():
        try:
            report["results"] = parse_junit(junit)
        except ET.ParseError as exc:
            report["results"] = None
            report["results_error"] = f"JUnit report is not valid XML: {exc}"
    else:
        report["results"] = None
        report["results_error"] = (
            "No JUnit report was written. The run probably failed before any "
            "test started; check the log."
        )

    stdout_report = run_dir / STDOUT_REPORT
    if stdout_report.is_file():
        text = stdout_report.read_text(encoding="utf-8", errors="replace")
        report["log_tail"] = "\n".join(text.splitlines()[-log_tail_lines:])
        report["log_path"] = str(stdout_report)

    attachments = [
        str(p.relative_to(run_dir))
        for p in run_dir.rglob("*")
        if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".mp4"}
    ]
    if attachments:
        report["attachments"] = attachments
    return report


def latest_run_dir(config: SquishConfig) -> Path | None:
    if not config.results_dir.is_dir():
        return None
    runs = [p for p in config.results_dir.iterdir() if p.is_dir()]
    return max(runs, key=lambda p: p.stat().st_mtime) if runs else None
