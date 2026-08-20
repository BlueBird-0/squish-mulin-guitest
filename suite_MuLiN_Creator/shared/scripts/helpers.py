"""
Shared helper utilities for MuLiN Creator GUI tests.
"""

def waitForMainWindow():
    """Wait for the MuLiN Creator main window to appear."""
    return waitForObject(":MuLiN_Creator_QMainWindow")
