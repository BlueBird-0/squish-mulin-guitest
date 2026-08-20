"""Reading squishserver's own configuration files.

squishrunner --info requires a *running* squishserver, which makes it useless
for diagnostics before a run. The same facts live in server.ini, which
squishserver rewrites on every --config change, so the files are read directly
instead.
"""

from __future__ import annotations

import configparser
import os
from dataclasses import dataclass
from pathlib import Path

from .config import SquishConfig

SERVER_CONFIG_ENV = "SQUISH_SERVER_CONFIG"

_AUT_PREFIX = "AUT/"
_ATTACHABLE_PREFIX = "AttachableAUT/"


def _candidate_config_paths(config: SquishConfig) -> list[Path]:
    override = os.environ.get(SERVER_CONFIG_ENV)
    if override:
        return [Path(override)]

    candidates: list[Path] = []
    appdata = os.environ.get("APPDATA")
    if appdata:
        candidates.append(Path(appdata) / "froglogic" / "Squish" / "ver1" / "server.ini")
    candidates.append(Path.home() / ".squish" / "ver1" / "server.ini")
    candidates.append(config.squish_dir / "etc" / "server.ini")
    return candidates


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def _read_ini(path: Path) -> dict[str, str]:
    parser = configparser.ConfigParser(interpolation=None)
    # Keys are case-sensitive and contain '/', e.g. 'AUT/MuLiN Creator'.
    parser.optionxform = str  # type: ignore[assignment]
    parser.read(path, encoding="utf-8")
    values: dict[str, str] = {}
    for section in parser.sections():
        for key, value in parser.items(section):
            values[key] = _unquote(value)
    return values


@dataclass
class ServerConfig:
    """The parsed contents of squishserver's server.ini."""

    path: Path | None
    auts: dict[str, str]
    attachable_auts: dict[str, str]
    settings: dict[str, str]

    def aut_path(self, name: str) -> str | None:
        return self.auts.get(name)

    def as_dict(self) -> dict[str, object]:
        return {
            "config_file": str(self.path) if self.path else None,
            "registered_auts": self.auts,
            "attachable_auts": self.attachable_auts,
            "settings": self.settings,
        }


def load_server_config(config: SquishConfig) -> ServerConfig:
    """Load the first server.ini that exists, or an empty config if none do."""
    for path in _candidate_config_paths(config):
        if not path.is_file():
            continue
        values = _read_ini(path)
        auts: dict[str, str] = {}
        attachable: dict[str, str] = {}
        settings: dict[str, str] = {}
        for key, value in values.items():
            if key.startswith(_AUT_PREFIX):
                auts[key[len(_AUT_PREFIX) :]] = value
            elif key.startswith(_ATTACHABLE_PREFIX):
                attachable[key[len(_ATTACHABLE_PREFIX) :]] = value
            else:
                settings[key] = value
        return ServerConfig(
            path=path, auts=auts, attachable_auts=attachable, settings=settings
        )
    return ServerConfig(path=None, auts={}, attachable_auts={}, settings={})


def check_aut(config: SquishConfig, aut: str) -> dict[str, object]:
    """Report whether ``aut`` is registered and whether its executable is present.

    A registration pointing at a directory that no longer exists is the failure
    mode that produces the least obvious error at run time, so it is checked
    separately from registration itself.
    """
    server = load_server_config(config)
    registered_path = server.aut_path(aut)
    result: dict[str, object] = {
        "aut": aut,
        "registered": registered_path is not None,
        "registered_path": registered_path,
        "config_file": str(server.path) if server.path else None,
    }

    if registered_path is None:
        result["problem"] = (
            f'AUT "{aut}" is not registered with squishserver. Register it with: '
            f'squishserver --config addAUT "{aut}" <directory-containing-the-exe>'
        )
        return result

    directory = Path(registered_path)
    result["path_exists"] = directory.is_dir()
    if not directory.is_dir():
        result["problem"] = (
            f'AUT "{aut}" is registered as "{registered_path}", but that '
            "directory does not exist."
        )
        return result

    # Squish registers the containing directory; the executable is named after
    # the AUT on Windows.
    executable = directory / (f"{aut}.exe" if os.name == "nt" else aut)
    result["executable"] = str(executable)
    result["executable_exists"] = executable.is_file()
    if not executable.is_file():
        result["problem"] = (
            f"No executable named {executable.name} in {directory}. Check that "
            "the AUT name in suite.conf matches the executable name."
        )
    return result
