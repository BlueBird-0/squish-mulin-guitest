def main():
    startApplication("MuLiN_Creator")
    test.verify(waitForObject(":MuLiN_Creator_QMainWindow").visible, "MuLiN Creator main window is visible")
    closeApplication()
