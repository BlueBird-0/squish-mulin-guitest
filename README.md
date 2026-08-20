# squish-mulin-guitest

GUI Test Project for MuLiN Creator (Software PLC) using Squish.

## Prerequisites

- [Squish for Qt 11](https://www.qt.io/product/testing-tools/squish) built with MSVC 2022
- MuLiN Creator installed and registered as AUT (`MuLiN_Creator`)

## Project Structure

```
suite_MuLiN_Creator/
├── suite.conf                  # Suite configuration
├── shared/
│   └── scripts/
│       └── helpers.py          # Shared helper functions
└── tst_startup/
    ├── test.py                 # Startup smoke test
    └── test.cfg                # Test case metadata
```

## Setup

1. Install Squish for Qt 11 (MSVC 2022 build).
2. Register the MuLiN Creator executable as AUT named `MuLiN_Creator` in Squish IDE or via:
   ```
   squishserver --config addAUT MuLiN_Creator "C:\Path\To\MuLiN_Creator.exe"
   ```
3. Open `suite_MuLiN_Creator` in Squish IDE or run from the command line.

## Running Tests

From the Squish IDE, open `suite_MuLiN_Creator/suite.conf` and run the desired test cases.

To run from the command line:
```
squishrunner --testsuite suite_MuLiN_Creator --testcase tst_startup
```
