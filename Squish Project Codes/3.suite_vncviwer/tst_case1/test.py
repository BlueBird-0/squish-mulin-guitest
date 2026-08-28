# -*- coding: utf-8 -*-

import names
import re
import openpyxl

def login():
    mouseClick(waitForObject(names.login_pw))
    type(waitForObject(names.keyUI_edit), "")
    snooze(0.5)
    type(waitForObject(names.keyUI_edit), "123")
    snooze(0.5)
    mouseClick(waitForObject(names.keyUI_enter))
    snooze(0.5)
    mouseClick(waitForObject(names.login_connect))
    
def get_version(text, name):
    match = re.search(rf'\b{name}\s*:\s*([\d.]+(?:\s+[\d.]+)?)', text)
    return match.group(1).replace(' ', '') if match else None

def main():
    attachToApplication("VncViewer")
    
    snooze(1)
    if not object.exists(names.login_pw):
        mouseClick(waitForObject(names.viewer_connect))
        snooze(1)
        
    login()
       
    snooze(3)
    mouseClick(waitForObject(names.viewer_oriscreen))
    snooze(2)
    
    mouseClick(waitForImage("info.png", {'tolerant': True, 'threshold': 99.0}))
    snooze(1)
    
    viewer = waitForObject(names.viewer_win)
    img = object.grabScreenshot(viewer, {"delay": 0})
    ver_crop = img.copy(250, 130, 250, 150)
    ver_crop.save("ver_crop.png")
    text = getOcrText({"language": "English"}, ver_crop)
    tds_target = get_version(text, "TDS")
    os_target = get_version(text, "08")
    
    # open excel
    wb = openpyxl.load_workbook("TDS-SQC-2026-007.xlsx", data_only=True)
    tds_excel = wb["전송"]["C3"].value

    test.log("tds_target : " + tds_target)
    test.log("tds_excel : " + tds_excel)
    test.log("os_target : " + os_target)
    if tds_target == tds_excel:
        wb["전송"]["C3"] = "정상 작동"
        test.passes("test passed")
    else:
        wb["전송"]["C3"] = "이상 발견"
        test.fail("test fail")
    
    
