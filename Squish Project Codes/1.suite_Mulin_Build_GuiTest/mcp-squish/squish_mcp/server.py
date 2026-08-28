"""MCP server exposing a Squish for Qt test suite as tools.

Tool design follows the one-tool-per-action pattern: the action surface is
small, so every operation gets its own tool with a precise schema. Read-only
tools are annotated as such, and the single tool that drives the real GUI is
annotated destructive so that hosts always ask before running it.
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated, Any

from fastmcp import Context, FastMCP
from fastmcp.exceptions import ToolError
from pydantic import Field

from . import runner, squishconfig, suite
from .config import ConfigError, SquishConfig, load_config, require_runnable, validate

mcp = FastMCP(
    name="squish",
    instructions=(
        "Runs and inspects a Squish for Qt GUI test suite. Use list_test_cases "
        "to see what exists, read_test_script to inspect a test, run_tests to "
        "execute tests against the real application, and get_last_run_report to "
        "read results from a previous run. run_tests launches the application "
        "under test and takes over the desktop, so it can take minutes."
    ),
)

MAX_SCRIPT_CHARS = 60_000


def _config() -> SquishConfig:
    """Load config, converting failures into a ToolError.

    ToolError is FastMCP's client-visible exception: the message of any other
    exception type is masked, which would leave the caller with no idea what to
    fix.
    """
    try:
        return load_config()
    except ConfigError as exc:
        raise ToolError(str(exc)) from exc


def _require(config: SquishConfig) -> None:
    try:
        require_runnable(config)
    except ConfigError as exc:
        raise ToolError(str(exc)) from exc


@mcp.tool(
    title="Check Squish environment",
    annotations={"readOnlyHint": True},
)
def check_environment() -> dict[str, Any]:
    """Verify that the Squish installation, test suite, and AUT registration are
    usable, and report the resolved paths. Call this first when any other tool
    fails, or to find out why a run cannot start."""
    try:
        config = load_config()
    except ConfigError as exc:
        return {"ok": False, "problems": [str(exc)], "hint": "Set SQUISH_DIR."}

    problems = validate(config)
    result: dict[str, Any] = {
        "ok": not problems,
        "problems": problems,
        "squish_dir": str(config.squish_dir),
        "squishrunner": str(config.runner),
        "suite_dir": str(config.suite_dir),
        "results_dir": str(config.results_dir),
    }

    if not problems:
        loaded = suite.load_suite(config)
        result["aut"] = loaded.aut
        result["test_case_count"] = len(loaded.test_cases)
        missing = [c.name for c in loaded.test_cases if not c.exists]
        if missing:
            result["missing_test_case_dirs"] = missing

        # An unregistered AUT, or one whose registered path has gone stale, is
        # the most common cause of a run that fails before the first test step.
        if loaded.aut:
            aut_check = squishconfig.check_aut(config, loaded.aut)
            result["aut_check"] = aut_check
            problem = aut_check.get("problem")
            if problem:
                problems.append(str(problem))
                result["ok"] = False
    return result


@mcp.tool(
    title="List test cases",
    annotations={"readOnlyHint": True},
)
def list_test_cases() -> dict[str, Any]:
    """List the test cases declared in the suite's suite.conf, along with the
    suite's application under test, scripting language, and Qt wrappers."""
    config = _config()
    _require(config)
    return suite.load_suite(config).as_dict()


@mcp.tool(
    title="Read a test script",
    annotations={"readOnlyHint": True},
)
def read_test_script(
    test_case: Annotated[
        str,
        Field(description='Test case directory name, e.g. "tst_project1_build_case".'),
    ],
    include_shared: Annotated[
        bool,
        Field(description="Also return the suite's shared script files."),
    ] = False,
) -> dict[str, Any]:
    """Return the source of one test case's script, so its steps and
    verification points can be reviewed without running it."""
    config = _config()
    _require(config)

    loaded = suite.load_suite(config)
    case = loaded.case(test_case)
    if case is None:
        known = ", ".join(c.name for c in loaded.test_cases) or "none"
        raise ToolError(f'Unknown test case "{test_case}". Declared cases: {known}.')
    if case.script is None:
        raise ToolError(f'Test case "{test_case}" has no script file in {case.path}.')

    result: dict[str, Any] = {
        "test_case": case.name,
        "script_path": str(case.script),
        "source": _read_text(case.script),
    }

    # With a script-based object map, names.py carries the symbolic names the
    # test refers to, so the script is not readable without it.
    names = suite.find_object_map(config, case)
    if names is not None:
        result["object_map_path"] = str(names)
        result["object_map_source"] = _read_text(names)

    if include_shared:
        result["shared_scripts"] = [
            {"path": str(p), "source": _read_text(p)}
            for p in suite.shared_scripts(config)
        ]
    return result


def _read_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) > MAX_SCRIPT_CHARS:
        return text[:MAX_SCRIPT_CHARS] + "\n... [truncated]"
    return text


@mcp.tool(
    title="Get squishserver configuration",
    annotations={"readOnlyHint": True},
)
def get_squish_info() -> dict[str, Any]:
    """Return squishserver's registered applications, attachable applications,
    and timeout settings, read from its server.ini configuration file. Use this
    to confirm an application is registered as an AUT and where it points."""
    config = _config()
    return squishconfig.load_server_config(config).as_dict()


@mcp.tool(
    title="Run GUI tests",
    annotations={"readOnlyHint": False, "destructiveHint": True, "idempotentHint": False},
)
async def run_tests(
    ctx: Context,
    test_cases: Annotated[
        list[str] | None,
        Field(
            description=(
                "Test case directory names to run. Omit or pass null to run "
                "every case declared in suite.conf."
            )
        ),
    ] = None,
    timeout_seconds: Annotated[
        float,
        Field(
            ge=30,
            le=7200,
            description=(
                "Give up and kill the run after this long. GUI tests that build "
                "a project need several minutes."
            ),
        ),
    ] = 900.0,
    snooze_factor: Annotated[
        float | None,
        Field(
            gt=0,
            description=(
                "Scale every snooze() delay in the scripts. Below 1 runs faster, "
                "above 1 runs slower on a loaded machine."
            ),
        ),
    ] = None,
    abort_on_fail: Annotated[
        bool,
        Field(description="Stop the whole run at the first failed verification."),
    ] = False,
    retry: Annotated[
        int | None,
        Field(ge=1, le=5, description="Retry each failing test case this many times."),
    ] = None,
) -> dict[str, Any]:
    """Execute Squish test cases against the real application, then return
    pass/fail results per test.

    This launches the application under test and drives its GUI with synthetic
    mouse and keyboard input, so it takes over the desktop for the duration and
    may modify whatever files those tests touch. Results are also written to
    disk and can be re-read later with get_last_run_report.
    """
    config = _config()
    _require(config)

    loaded = suite.load_suite(config)
    declared = {c.name for c in loaded.test_cases}
    selected = list(test_cases or [])
    unknown = [name for name in selected if name not in declared]
    if unknown:
        raise ToolError(
            f"Unknown test case(s): {', '.join(unknown)}. "
            f"Declared cases: {', '.join(sorted(declared)) or 'none'}."
        )

    total = len(selected) or len(loaded.test_cases)
    completed = 0
    await ctx.info(f"Starting {total} Squish test case(s) against {loaded.aut!r}.")

    async def on_line(line: str) -> None:
        nonlocal completed
        if not line.strip():
            return
        # squishrunner prints one line per test case as it finishes.
        if "tst_" in line and any(k in line for k in ("PASS", "FAIL", "ERROR", "Test")):
            completed = min(completed + 1, total)
            await ctx.report_progress(completed, total, line[:200])
        elif any(k in line for k in ("FAIL", "ERROR", "Exception")):
            await ctx.warning(line[:500])

    try:
        result = await runner.run_suite(
            config,
            test_cases=selected,
            snooze_factor=snooze_factor,
            abort_on_fail=abort_on_fail,
            retry=retry,
            timeout_seconds=timeout_seconds,
            on_line=on_line,
        )
    except runner.RunError as exc:
        raise ToolError(str(exc)) from exc

    report = runner.read_report(result.run_dir)
    report["timed_out"] = result.timed_out
    report["exit_code"] = result.exit_code
    report["duration_seconds"] = round(result.duration_seconds, 1)

    if result.timed_out:
        report["note"] = (
            f"Run exceeded timeout_seconds={timeout_seconds:g} and was killed, "
            "along with the application under test. Results below cover only "
            "the tests that finished."
        )
    elif not report.get("results"):
        # No parseable report: the raw output is the only diagnostic available.
        report["console_tail"] = "\n".join(result.output_lines[-60:])

    return report


@mcp.tool(
    title="Get last run report",
    annotations={"readOnlyHint": True},
)
def get_last_run_report(
    run_dir: Annotated[
        str | None,
        Field(
            description=(
                "A specific run directory to read. Omit to read the most "
                "recent run."
            )
        ),
    ] = None,
    log_tail_lines: Annotated[
        int,
        Field(ge=10, le=2000, description="How many trailing log lines to include."),
    ] = 80,
) -> dict[str, Any]:
    """Read the results of a previous run from disk. Use this when a run_tests
    call timed out on the client side but the run itself kept going, or to
    compare against an earlier run."""
    config = _config()
    target = Path(run_dir) if run_dir else runner.latest_run_dir(config)
    if target is None:
        raise ToolError(
            f"No runs found in {config.results_dir}. Use run_tests first."
        )
    if not target.is_dir():
        raise ToolError(f"Not a run directory: {target}")
    return runner.read_report(target, log_tail_lines=log_tail_lines)


@mcp.tool(
    title="List previous runs",
    annotations={"readOnlyHint": True},
)
def list_runs(
    limit: Annotated[
        int, Field(ge=1, le=100, description="Maximum number of runs to return.")
    ] = 10,
) -> dict[str, Any]:
    """List recent run directories, newest first, with their pass/fail totals."""
    config = _config()
    if not config.results_dir.is_dir():
        return {"results_dir": str(config.results_dir), "runs": []}

    dirs = sorted(
        (p for p in config.results_dir.iterdir() if p.is_dir()),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )[:limit]

    runs = []
    for path in dirs:
        entry: dict[str, Any] = {"run_dir": str(path)}
        junit = path / runner.JUNIT_REPORT
        if junit.is_file():
            try:
                entry["summary"] = runner.parse_junit(junit)["summary"]
            except Exception:  # noqa: BLE001 - a bad report must not hide the run
                entry["summary"] = None
        runs.append(entry)
    return {"results_dir": str(config.results_dir), "runs": runs}


def main() -> None:
    """stdio entry point. The banner is suppressed because stdio clients only
    ever show it as noise in their logs."""
    mcp.run(show_banner=False)


if __name__ == "__main__":
    main()
