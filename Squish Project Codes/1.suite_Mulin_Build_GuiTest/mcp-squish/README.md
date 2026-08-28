# squish-mcp

An MCP server that exposes this Squish for Qt test suite to Claude: list the
test cases, read their scripts, run them against **MuLiN Creator**, and read the
results back.

- **Deployment model:** local stdio (see [Distributing it](#distributing-it))
- **Framework:** [FastMCP](https://gofastmcp.com) 3.x
- **Tool pattern:** one tool per action — the action surface is small
- **Auth:** none; everything runs as the local user

## Tools

| Tool | Kind | What it does |
| --- | --- | --- |
| `check_environment` | read-only | Resolves the Squish install, suite, and AUT registration and reports what is broken. Start here when anything fails. |
| `list_test_cases` | read-only | Test cases declared in `suite.conf`, plus AUT, language, and wrappers. |
| `read_test_script` | read-only | One test case's script, together with the `names.py` object map it imports. |
| `get_squish_info` | read-only | squishserver's registered AUTs and timeouts, read from `server.ini`. |
| `run_tests` | **destructive** | Runs test cases against the real GUI, then returns pass/fail per test. |
| `get_last_run_report` | read-only | Re-reads a previous run's results from disk. |
| `list_runs` | read-only | Recent runs, newest first, with pass/fail totals. |

`run_tests` is annotated `destructiveHint: true`, so hosts prompt before every
call. That is deliberate: it launches MuLiN Creator, drives it with synthetic
mouse and keyboard input, takes over the desktop for the duration, and builds
real projects on disk.

## Setup

Requires Python 3.11+, [uv](https://docs.astral.sh/uv/), and a local Squish for
Qt installation.

```bash
cd mcp-squish
uv sync
```

Register it with Claude Code:

```bash
claude mcp add squish -- uv --directory "C:\Users\IHJEON\Desktop\suite_MulinGuiTest\mcp-squish" run squish-mcp
```

Or add it to `.mcp.json` at the suite root (already provided):

```json
{
  "mcpServers": {
    "squish": {
      "command": "uv",
      "args": ["--directory", "mcp-squish", "run", "squish-mcp"]
    }
  }
}
```

For Claude Desktop, use the same command in
`claude_desktop_config.json`, with an absolute `--directory` path.

## Configuration

Every path is autodetected, and every one can be overridden:

| Variable | Default | Meaning |
| --- | --- | --- |
| `SQUISH_DIR` | newest `~/Squish for Qt *` | Directory containing `bin/squishrunner`. |
| `SQUISH_SUITE_DIR` | the parent of `mcp-squish/` | Directory containing `suite.conf`. |
| `SQUISH_MCP_RESULTS` | `<suite>/.squish-mcp-results` | Where run reports are written. |
| `SQUISH_SERVER_CONFIG` | `%APPDATA%/froglogic/Squish/ver1/server.ini` | squishserver config to read. |

Verified against Squish for Qt 9.2.2 with `SQUISH_DIR` autodetected to
`C:\Users\IHJEON\Squish for Qt 9.2.2`.

## How a run works

`run_tests` shells out to:

```
squishrunner --testsuite <suite> --local
             [--testcase <suite>/<case>]...
             --reportgen junit,<run-dir>/report.xml
             --reportgen stdout,<run-dir>/report.txt
             --resultdir <run-dir>
             --exitCodeOnFail 1
```

Three details are load-bearing:

- **`--local`** makes squishrunner start and stop its own squishserver, so
  nothing has to manage a background server.
- **Only file-based report generators are used.** Squish *errors out* if
  `--resultdir` is combined with a directory-based generator (`html`, `json*`,
  `xml3*`), and `--resultdir` is what collects failure screenshots and video.
- **JUnit is the machine-readable output.** It is a stable, well-known schema;
  the `stdout` report is kept alongside it for the human-readable log.

Each run gets a timestamped directory under `SQUISH_MCP_RESULTS` holding
`report.xml`, `report.txt`, `run.json`, and any screenshots. Because results are
on disk before the tool returns, a run whose tool call times out on the client
side is still recoverable with `get_last_run_report`.

On timeout, squishrunner is killed **with its whole process tree** — otherwise
MuLiN Creator would be left on screen holding the display and blocking the next
run.

### Note on `squishrunner --info`

It is not used, and cannot be: it requires an already-running squishserver and
fails with exit 127 otherwise. `get_squish_info` reads `server.ini` directly,
which is the same data without the dependency.

## Distributing it

Local stdio is right for "runs on our own machines", but it does mean every user
needs uv and a matching Squish install. To hand this to someone without a Python
toolchain, repackage it as an **MCPB** bundle (a local server shipped with its
runtime) — the code needs no changes, since all machine-specific paths are
already environment variables with autodetection.

The server can never be remote: it drives a GUI on the same desktop as the
tests.

## Possible next step

`run_tests` blocks for the length of the run. If runs grow past the point where
a blocking call is comfortable, split it into `start_run` / `get_run_status` and
poll — the on-disk run directory already carries all the state that would need.
