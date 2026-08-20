"""Reading the test suite's own metadata: suite.conf and the test case scripts."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from .config import SquishConfig

# suite.conf values that name multiple items, space separated.
_LIST_KEYS = frozenset({"TEST_CASES", "WRAPPERS", "AUTS"})

_SCRIPT_NAMES = ("test.py", "test.js", "test.pl", "test.rb", "test.tcl", "test.feature")


def _unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_suite_conf(path: Path) -> dict[str, object]:
    """Parse suite.conf into a dict, splitting the known list-valued keys.

    suite.conf is a flat KEY=VALUE file. Values may be quoted (the AUT name
    usually is, because it contains spaces).
    """
    parsed: dict[str, object] = {}
    text = path.read_text(encoding="utf-8", errors="replace")
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, raw = line.partition("=")
        key = key.strip()
        value = _unquote(raw.strip())
        parsed[key] = value.split() if key in _LIST_KEYS else value
    return parsed


@dataclass
class TestCase:
    """One test case directory inside the suite."""

    name: str
    path: Path
    script: Path | None = None
    exists: bool = True

    def as_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "path": str(self.path),
            "script": str(self.script) if self.script else None,
            "exists": self.exists,
        }


@dataclass
class Suite:
    """A parsed test suite."""

    path: Path
    conf: dict[str, object]
    test_cases: list[TestCase] = field(default_factory=list)

    @property
    def aut(self) -> str | None:
        value = self.conf.get("AUT")
        return value if isinstance(value, str) else None

    @property
    def language(self) -> str | None:
        value = self.conf.get("LANGUAGE")
        return value if isinstance(value, str) else None

    def case(self, name: str) -> TestCase | None:
        return next((c for c in self.test_cases if c.name == name), None)

    def as_dict(self) -> dict[str, object]:
        return {
            "suite_path": str(self.path),
            "aut": self.aut,
            "language": self.language,
            "wrappers": self.conf.get("WRAPPERS", []),
            "object_map_style": self.conf.get("OBJECTMAPSTYLE"),
            "hook_sub_processes": self.conf.get("HOOK_SUB_PROCESSES"),
            "test_cases": [c.as_dict() for c in self.test_cases],
        }


def _find_script(case_dir: Path) -> Path | None:
    for name in _SCRIPT_NAMES:
        candidate = case_dir / name
        if candidate.is_file():
            return candidate
    return None


def load_suite(config: SquishConfig) -> Suite:
    """Load the suite named by ``config``, resolving each declared test case."""
    conf = parse_suite_conf(config.suite_conf)
    declared = conf.get("TEST_CASES") or []
    if isinstance(declared, str):  # single, unsplit value
        declared = [declared]

    cases: list[TestCase] = []
    for name in declared:
        case_dir = config.suite_dir / name
        cases.append(
            TestCase(
                name=name,
                path=case_dir,
                script=_find_script(case_dir),
                exists=case_dir.is_dir(),
            )
        )
    return Suite(path=config.suite_dir, conf=conf, test_cases=cases)


def shared_scripts(config: SquishConfig) -> list[Path]:
    """Script files under the suite's shared/ directory, if there is one."""
    shared = config.suite_dir / "shared"
    if not shared.is_dir():
        return []
    return sorted(
        p
        for p in shared.rglob("*")
        if p.is_file()
        and p.suffix in {".py", ".js"}
        and "__pycache__" not in p.parts
    )


def find_object_map(config: SquishConfig, case: TestCase) -> Path | None:
    """Locate the script-based object map (names.py) that a test case imports.

    With OBJECTMAPSTYLE=script the object map is an importable module. It may
    sit next to the test script, but a suite that shares one map across cases
    keeps it in shared/scripts instead, which is where Squish adds the suite's
    script directory to the import path.
    """
    candidates = [
        case.path / "names.py",
        config.suite_dir / "shared" / "scripts" / "names.py",
        config.suite_dir / "shared" / "names.py",
    ]
    return next((c for c in candidates if c.is_file()), None)
