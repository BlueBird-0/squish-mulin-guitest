"""Resolution of the Squish installation, the test suite, and result locations.

Every path is overridable by environment variable so the server can be pointed at
another machine's Squish install or a different suite without a code change.
"""

from __future__ import annotations

import glob
import os
from dataclasses import dataclass
from pathlib import Path

SQUISH_DIR_ENV = "SQUISH_DIR"
SUITE_DIR_ENV = "SQUISH_SUITE_DIR"
RESULTS_DIR_ENV = "SQUISH_MCP_RESULTS"

# Globs checked when SQUISH_DIR is unset, in priority order.
_SQUISH_GLOBS = (
    str(Path.home() / "Squish for Qt *"),
    str(Path.home() / "Squish for *"),
    r"C:\Program Files\froglogic\Squish*",
    r"C:\Program Files (x86)\froglogic\Squish*",
    "/opt/squish*",
)


class ConfigError(RuntimeError):
    """Raised when the environment cannot support a Squish run."""


def _newest_match(patterns: tuple[str, ...]) -> Path | None:
    matches: list[Path] = []
    for pattern in patterns:
        matches.extend(Path(p) for p in glob.glob(pattern) if Path(p).is_dir())
    if not matches:
        return None
    # Highest version string wins, so "9.2.2" beats "7.1.0".
    return max(matches, key=lambda p: p.name)


def _exe(name: str) -> str:
    return f"{name}.exe" if os.name == "nt" else name


@dataclass(frozen=True)
class SquishConfig:
    """Fully resolved, validated locations for one server instance."""

    squish_dir: Path
    suite_dir: Path
    results_dir: Path

    @property
    def runner(self) -> Path:
        return self.squish_dir / "bin" / _exe("squishrunner")

    @property
    def server(self) -> Path:
        return self.squish_dir / "bin" / _exe("squishserver")

    @property
    def suite_conf(self) -> Path:
        return self.suite_dir / "suite.conf"

    @property
    def envvars_file(self) -> Path | None:
        candidate = self.suite_dir / "envvars"
        return candidate if candidate.is_file() else None


def load_config() -> SquishConfig:
    """Resolve paths from the environment, falling back to autodetection.

    Does not verify that the paths exist; call :func:`validate` for that. Keeping
    resolution and validation separate lets the diagnostic tool report *what*
    was resolved even when the resolution is wrong.
    """
    raw_squish = os.environ.get(SQUISH_DIR_ENV)
    squish_dir = Path(raw_squish) if raw_squish else _newest_match(_SQUISH_GLOBS)
    if squish_dir is None:
        raise ConfigError(
            "Could not find a Squish installation. Set the "
            f"{SQUISH_DIR_ENV} environment variable to the directory that "
            "contains bin/squishrunner."
        )

    raw_suite = os.environ.get(SUITE_DIR_ENV)
    # Default: this package lives at <suite>/mcp-squish/squish_mcp/config.py.
    suite_dir = Path(raw_suite) if raw_suite else Path(__file__).resolve().parents[2]

    raw_results = os.environ.get(RESULTS_DIR_ENV)
    results_dir = Path(raw_results) if raw_results else suite_dir / ".squish-mcp-results"

    return SquishConfig(
        squish_dir=squish_dir.expanduser(),
        suite_dir=suite_dir.expanduser(),
        results_dir=results_dir.expanduser(),
    )


def validate(config: SquishConfig) -> list[str]:
    """Return a list of human-readable problems; empty means good to run."""
    problems: list[str] = []
    if not config.squish_dir.is_dir():
        problems.append(f"Squish directory does not exist: {config.squish_dir}")
    elif not config.runner.is_file():
        problems.append(f"squishrunner not found at: {config.runner}")
    if not config.suite_conf.is_file():
        problems.append(f"No suite.conf found in suite directory: {config.suite_dir}")
    return problems


def require_runnable(config: SquishConfig) -> None:
    problems = validate(config)
    if problems:
        raise ConfigError("; ".join(problems))
