# -*- coding: utf-8 -*-

import names
import os


def close_recovery_dialog_if_exists(): 
    if object.exists(names.recoveryDialog):
        clickButton(waitForObject(names.recoveryDialog_Close))
        test.log("복구 다이얼로그 닫음")
    else:
        test.log("복구 다이얼로그 없음")

def check_width(obj, expected_value):
    button = waitForObject(obj)
    width_value = button.width

    if width_value == expected_value:
        test.log("버튼 너비 " + str(expected_value) + " 맞음")
    else:
        test.fail("버튼 너비가 " + str(expected_value) + "가 아님, 실제 값: " + str(width_value))

# RESULT_LOG_PATH = r"C:\Users\DELL\Desktop\MuLiN PLC 비교\테스트 케이스\test_results.csv"
RESULT_LOG_PATH = r"C:\Users\User\Desktop\MuLiN PLC 비교\테스트 케이스\test_results.csv"

def reset_result_log():
    with open(RESULT_LOG_PATH, "w", encoding="utf-8") as f:
        pass

def log_result_to_file(sheet_name, row_number, passed):
    with open(RESULT_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(sheet_name + "," + str(row_number) + "," + ("정상 동작" if passed else "이상 발견") + "\n")

def check_variable_value_by_name(var_name, expected_value, description, sheet_name, row_number):
    name_cell = waitForObject({"column": 2, "container": names.variableTableFrame_treeView_MinervaD_MvCustomTreeView, "text": var_name, "type": "QModelIndex"}, 5000)
    treeView = waitForObject(names.variableTableFrame_treeView_MinervaD_MvCustomTreeView)
    treeView.scrollTo(name_cell)
    snooze(1)
    value_cell = waitForObject({"column": 5, "container": names.variableTableFrame_treeView_MinervaD_MvCustomTreeView, "row": name_cell.row, "type": "QModelIndex"}, 5000)
    actual = str(value_cell.text)
    passed = (actual == str(expected_value))
    if passed:
        test.log(description + " 값 일치함 (실제값: " + actual + ")")
    else:
        test.fail(description + " 값이 예상과 다름. 기대값: " + str(expected_value) + ", 실제값: " + actual)
    log_result_to_file(sheet_name, row_number, passed)
        
def scroll_variable_table_to_bottom():    # 휠 내리기
    scrollbar = waitForObject(names.treeView_QScrollBar)
    scrollbar.setValue(scrollbar.maximum)
    snooze(1)
    
    
def close_select_monitoring_fb_dialog_if_exists():
    if object.exists(names.mvSelectMonitoringFunctionBlockDialog_MinervaD_MvSelectMonitoringFunctionBlockDialog):
        nativeType("<Escape>")
        test.log("모니터링 FB 선택 다이얼로그 닫음 (ESC)")
    else:
        test.log("모니터링 FB 선택 다이얼로그 없음")  
    

def main():
    startApplication("\"MuLiN Creator\"")
    snooze(5)

    close_recovery_dialog_if_exists() #복구 다이얼로그

    activateItem(waitForObjectItem(names.menuBar, "파일"))
    activateItem(waitForObjectItem(names.fileMenu, "프로젝트 열기"))

    # ---- 여기부터 트리 클릭 대신 File name 입력창 사용 ----
    project_path = os.path.join(
        os.path.expanduser("~"), "Desktop",
        "MuLiN PLC 비교", "MuLiN 명령어 테스트 케이스", "MuLiN 명령어 테스트 케이스.mdp"
    )
    waitForObject(names.fileNameEdit_QLineEdit).setText(project_path) 
    clickButton(waitForObject(names.qFileDialog_Open_QPushButton))
    snooze(1)
    close_recovery_dialog_if_exists() #복구 다이얼로그
    test.log("메인창까지 정상적으로 열림")


    # ------------------------------------------------

    # sendEvent("QCloseEvent", waitForObject(names.projectMainWindow))

    clickButton(waitForObject(names.muLiN_Creator_C_Users_DELL_Desktop_MuLiN_PLC_MuLiN_MuLiN_mdp_Qtitan_ToolButton))
    clickButton(waitForObject(names.muLiN_Creator_C_Users_DELL_Desktop_MuLiN_PLC_MuLiN_MuLiN_mdp_Qtitan_ToolButton_2))
    clickButton(waitForObject(names.mvDownloadToDeviceDialog_QPushButton))
    check_width(names.o_QPushButton, 80)
    clickButton(waitForObject(names.o_QPushButton))    
    snooze(5)
    clickButton(waitForObject(names.muLiN_Creator_C_Users_DELL_Desktop_MuLiN_PLC_MuLiN_MuLiN_mdp_Qtitan_ToolButton_3))
    snooze(2)
    close_select_monitoring_fb_dialog_if_exists()
    test.log("모니터링 정상")
    
    # test.imagePresent("Arithmetic_pass.png", {"tolerant": True, "threshold": 95.0, "message": "Arithmetic 통과 이미지 확인"})  이미지 확인 방법
    snooze(2)
    doubleClick(waitForObjectItem(names.mvProjectTreeFrame_treeWidget_MinervaD_MvProjectTreeWidget, "MuLiN 명령어 테스트 케이스.POU.함수 블록.Arithmetic"), 59, 9, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_selectFBInstanceCheckBox_QCheckBox))
    mouseClick(waitForObjectItem(names.groupBox_listWidget_QListWidget, "Program1\\.TC1"), 60, 7, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_QPushButton))  
    test.log("FB1 진입")  
    
    
    reset_result_log()

    # FB1 (산술 연산)
    snooze(2)
    check_variable_value_by_name("ADD_OUT", 35, "ADD_OUT (35)", "산술 연산", 10)
    check_variable_value_by_name("SUB_OUT", "55.5", "SUB_OUT (55.5)", "산술 연산", 11)
    check_variable_value_by_name("MUL_OUT", 111, "MUL_OUT (111)", "산술 연산", 12)
    check_variable_value_by_name("DIV_OUT", 37, "DIV_OUT (37)", "산술 연산", 13)
    check_variable_value_by_name("MOD_OUT", 5, "MOD_OUT (5)", "산술 연산", 14)
    check_variable_value_by_name("EXPT_OUT", 32, "EXPT_OUT (32)", "산술 연산", 15)
    check_variable_value_by_name("PASS", "TRUE", "PASS (TRUE)", "산술 연산", 16)

    # FB2 (비트 이동)
    snooze(2)
    doubleClick(waitForObjectItem(names.mvProjectTreeFrame_treeWidget_MinervaD_MvProjectTreeWidget, "MuLiN 명령어 테스트 케이스.POU.함수 블록.Bit\\_Move"), 86, 7, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_selectFBInstanceCheckBox_QCheckBox))
    mouseClick(waitForObjectItem(names.groupBox_listWidget_QListWidget, "Program1\\.TC2"), 47, 11, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_QPushButton))   
    test.log("FB2 진입") 
    
    snooze(2)
    check_variable_value_by_name("SHL_OUT", 9024, "SHL_OUT (9024)", "비트 이동", 10)
    check_variable_value_by_name("SHR_OUT", 35, "SHR_OUT (35)", "비트 이동", 11)
    check_variable_value_by_name("ROL_OUT", 560, "ROL_OUT (560)", "비트 이동", 12)
    check_variable_value_by_name("ROR_OUT", 35, "ROR_OUT (35)", "비트 이동", 13)
    check_variable_value_by_name("MOV_BIT_OUT", 768, "MOV_BIT_OUT (768)", "비트 이동", 14)
    check_variable_value_by_name("MOV_DIGIT_OUT", 48, "MOV_DIGIT_OUT (48)", "비트 이동", 15)
    check_variable_value_by_name("PASS", "TRUE", "PASS (TRUE)", "비트 이동", 16)

    # FB3 (비트 연산)
    snooze(2)
    doubleClick(waitForObjectItem(names.mvProjectTreeFrame_treeWidget_MinervaD_MvProjectTreeWidget, "MuLiN 명령어 테스트 케이스.POU.함수 블록.Bit\\_Arithmetic"), 86, 10, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_selectFBInstanceCheckBox_QCheckBox))
    mouseClick(waitForObjectItem(names.groupBox_listWidget_QListWidget, "Program1\\.TC3"), 66, 12, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_QPushButton))    
    test.log("FB3 진입") 
    
    snooze(2)
    check_variable_value_by_name("AND_OUT", 3082, "AND_OUT (3082)", "비트 연산", 10)
    check_variable_value_by_name("OR_OUT", 64522, "OR_OUT (64522)", "비트 연산", 11)
    check_variable_value_by_name("XOR_OUT", 1013, "XOR_OUT (1013)", "비트 연산", 12)
    check_variable_value_by_name("NOT_OUT", 64522, "NOT_OUT (64522)", "비트 연산", 13)
    check_variable_value_by_name("NOR_OUT", 768, "NOR_OUT (768)", "비트 연산", 14)
    check_variable_value_by_name("XNR_OUT", 61131, "XNR_OUT (61131)", "비트 연산", 15)
    check_variable_value_by_name("PASS", "TRUE", "PASS (TRUE)", "비트 연산", 16)

    # FB4 (데이터형 선택+이동)
    snooze(2)
    doubleClick(waitForObjectItem(names.mvProjectTreeFrame_treeWidget_MinervaD_MvProjectTreeWidget, "MuLiN 명령어 테스트 케이스.POU.함수 블록.Data\\_Select\\_Move"), 38, 11, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_selectFBInstanceCheckBox_QCheckBox))
    mouseClick(waitForObjectItem(names.groupBox_listWidget_QListWidget, "Program1\\.TC4"), 52, 7, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_QPushButton))    
    test.log("FB4 진입") 
    
    snooze(2)
    check_variable_value_by_name("SEL_OUT", 42, "SEL_OUT (42)", "데이터형 선택+이동", 10)
    check_variable_value_by_name("MAX_OUT", 100, "MAX_OUT (100)", "데이터형 선택+이동", 11)
    check_variable_value_by_name("MIN_OUT", -30, "MIN_OUT (-30)", "데이터형 선택+이동", 12)
    check_variable_value_by_name("LIMIT_OUT", 0, "LIMIT_OUT (0)", "데이터형 선택+이동", 13)
    check_variable_value_by_name("MUX_OUT", -1, "MUX_OUT (-1)", "데이터형 선택+이동", 14)
    check_variable_value_by_name("MOVE_OUT", -1, "MOVE_OUT (-1)", "데이터형 선택+이동", 15)
    check_variable_value_by_name("PASS", "TRUE", "PASS (TRUE)", "데이터형 선택+이동", 16)
    
    # FB5 (데이터 비교)

    snooze(2)
    doubleClick(waitForObjectItem(names.mvProjectTreeFrame_treeWidget_MinervaD_MvProjectTreeWidget, "MuLiN 명령어 테스트 케이스.POU.함수 블록.Bit\\_Comparison"), 47, 6, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_selectFBInstanceCheckBox_QCheckBox))
    mouseClick(waitForObjectItem(names.groupBox_listWidget_QListWidget, "Program1\\.TC5"), 42, 17, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_QPushButton))    
    test.log("FB5 진입")
     
    snooze(2)
    check_variable_value_by_name("PASS_1", "TRUE", "PASS_1 (TRUE)", "데이터 비교", 15)
    check_variable_value_by_name("PASS_2", "TRUE", "PASS_2 (TRUE)", "데이터 비교", 18)
    
    # FB6 (수학+데이터형 변환)
     
    snooze(2)
    doubleClick(waitForObjectItem(names.mvProjectTreeFrame_treeWidget_MinervaD_MvProjectTreeWidget, "MuLiN 명령어 테스트 케이스.POU.함수 블록.Math\\_Data\\_Change"), 52, 5, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_selectFBInstanceCheckBox_QCheckBox))
    mouseClick(waitForObjectItem(names.groupBox_listWidget_QListWidget, "Program1\\.TC6"), 38, 10, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_QPushButton))     
    test.log("FB6 진입") 
    
    snooze(2)
    check_variable_value_by_name("AVG_OUT", -3.116667, "AVG_OUT (-3.116667)", "수학+데이터형 변환", 10)
    check_variable_value_by_name("TO_DINT_OUT", -3, "TO_DINT_OUT (-3)", "수학+데이터형 변환", 11)
    check_variable_value_by_name("INC_IN_OUT", -2, "INC_IN_OUT (-2)", "수학+데이터형 변환", 12)
    check_variable_value_by_name("TO_REAL_OUT", -2, "TO_REAL_OUT (-2)", "수학+데이터형 변환", 13)
    check_variable_value_by_name("DEC_IN_OUT", -3, "DEC_IN_OUT (-3)", "수학+데이터형 변환", 14)
    check_variable_value_by_name("TO_LINT_OUT", -3, "TO_LINT_OUT (-3)", "수학+데이터형 변환", 15)
    check_variable_value_by_name("ABS_OUT", 3, "ABS_OUT (3)", "수학+데이터형 변환", 16)
    check_variable_value_by_name("TO_LREAL_OUT", 3, "TO_LREAL_OUT (3)", "수학+데이터형 변환", 17)
    check_variable_value_by_name("NEG_OUT", -3, "NEG_OUT (-3)", "수학+데이터형 변환", 18)
    check_variable_value_by_name("TO_INT_OUT", -3, "TO_INT_OUT (-3)", "수학+데이터형 변환", 19)
    check_variable_value_by_name("EXP_OUT", 0.04978707, "EXP_OUT (0.04978707)", "수학+데이터형 변환", 20)
    check_variable_value_by_name("ROUND_OUT1", 0, "ROUND_OUT1 (0)", "수학+데이터형 변환", 21)
    check_variable_value_by_name("TO_SINT_OUT", 0, "TO_SINT_OUT (0)", "수학+데이터형 변환", 22)
    check_variable_value_by_name("ADD_OUT1", -17, "ADD_OUT1 (-17)", "수학+데이터형 변환", 23)
    check_variable_value_by_name("DIV_OUT", -4.25, "DIV_OUT (-4.25)", "수학+데이터형 변환", 24)
    check_variable_value_by_name("CEIL_OUT", -4, "CEIL_OUT (-4)", "수학+데이터형 변환", 25)
    check_variable_value_by_name("TO_UINT_OUT", 65532, "TO_UINT_OUT (65532)", "수학+데이터형 변환", 26)
    check_variable_value_by_name("SUB_OUT", 6.5, "SUB_OUT (6.5)", "수학+데이터형 변환", 27)
    check_variable_value_by_name("FLOOR_OUT", 6, "FLOOR_OUT (6)", "수학+데이터형 변환", 28)
    check_variable_value_by_name("TO_UDINT_OUT", 6, "TO_UDINT_OUT (6)", "수학+데이터형 변환", 29)
    check_variable_value_by_name("SQR_OUT", 36, "SQR_OUT (36)", "수학+데이터형 변환", 30)
    check_variable_value_by_name("TO_ULINT_OUT", 36, "TO_ULINT_OUT (36)", "수학+데이터형 변환", 31)
    check_variable_value_by_name("SQRT_OUT", 6, "SQRT_OUT (6)", "수학+데이터형 변환", 32)
    check_variable_value_by_name("TO_USINT_OUT", 6, "TO_USINT_OUT (6)", "수학+데이터형 변환", 33)
    check_variable_value_by_name("LN_OUT", 1.791759, "LN_OUT (1.791759)", "수학+데이터형 변환", 34)
    check_variable_value_by_name("TO_LWORD_OUT", 1, "TO_LWORD_OUT (1)", "수학+데이터형 변환", 35)
    check_variable_value_by_name("MUL_OUT", 2, "MUL_OUT (2)", "수학+데이터형 변환", 36)
    check_variable_value_by_name("LOG_OUT", 0.30103, "LOG_OUT (0.30103)", "수학+데이터형 변환", 37)
    check_variable_value_by_name("TO_DWORD_OUT", 0, "TO_DWORD_OUT (0)", "수학+데이터형 변환", 38)
    check_variable_value_by_name("TO_WORD_OUT", 0, "TO_WORD_OUT (0)", "수학+데이터형 변환", 39)
    check_variable_value_by_name("ADD_OUT2", 1, "ADD_OUT2 (1)", "수학+데이터형 변환", 40)
    check_variable_value_by_name("SIN_OUT", 0.841471, "SIN_OUT (0.841471)", "수학+데이터형 변환", 41)
    check_variable_value_by_name("BYTE_OUT", 0, "BYTE_OUT (0)", "수학+데이터형 변환", 42)
    check_variable_value_by_name("ADD_OUT3", 1, "ADD_OUT3 (1)", "수학+데이터형 변환", 43)
    check_variable_value_by_name("COS_OUT", 0.5403023, "COS_OUT (0.5403023)", "수학+데이터형 변환", 44)
    check_variable_value_by_name("TAN_OUT", 0.5998406, "TAN_OUT (0.5998406)", "수학+데이터형 변환", 45)
    check_variable_value_by_name("ASIN_OUT", 0.6433018, "ASIN_OUT (0.6433018)", "수학+데이터형 변환", 46)
    check_variable_value_by_name("ACOS_OUT", 0.8719931, "ACOS_OUT (0.8719931)", "수학+데이터형 변환", 47)
    check_variable_value_by_name("ATAN_OUT", 0.7171245, "ATAN_OUT (0.7171245)", "수학+데이터형 변환", 48)
    check_variable_value_by_name("ATAN2_OUT", 0.6221267, "ATAN2_OUT (0.6221267)", "수학+데이터형 변환", 49)
    check_variable_value_by_name("DEG_OUT", 35.64523, "DEG_OUT (35.64523)", "수학+데이터형 변환", 50)
    check_variable_value_by_name("RAD_OUT", 0.6221267, "RAD_OUT (0.6221267)", "수학+데이터형 변환", 51)
    check_variable_value_by_name("ROUND_OUT2", 1, "ROUND_OUT2 (1)", "수학+데이터형 변환", 52)
    check_variable_value_by_name("PASS", "TRUE", "PASS (TRUE)", "수학+데이터형 변환", 54)
    
    # FB7 모니터링 값 비교
    
    snooze(2)
    doubleClick(waitForObjectItem(names.mvProjectTreeFrame_treeWidget_MinervaD_MvProjectTreeWidget, "MuLiN 명령어 테스트 케이스.POU.함수 블록.String\\_Data\\_Change"), 88, 7, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_selectFBInstanceCheckBox_QCheckBox))
    mouseClick(waitForObjectItem(names.groupBox_listWidget_QListWidget, "Program1\\.TC7"), 62, 3, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_QPushButton))    
    test.log("FB7 진입") 
    
    snooze(2)
    check_variable_value_by_name("LEFT_OUT", '"MuLiN"', 'LEFT_OUT ("MuLiN")', "문자열+데이터형 변환", 10)
    check_variable_value_by_name("RIGHT_OUT", '" Test"', 'RIGHT_OUT (" Test")', "문자열+데이터형 변환", 11)
    check_variable_value_by_name("CONCAT_OUT", '"MuLiN Test"', 'CONCAT_OUT ("MuLiN Test")', "문자열+데이터형 변환", 12)
    check_variable_value_by_name("INSERT_OUT", '"MuLiN Creator Test"', 'INSERT_OUT ("MuLiN Creator Test")', "문자열+데이터형 변환", 13)
    check_variable_value_by_name("REPLACE_OUT", '"MuLiN-Creator-Test"', 'REPLACE_OUT ("MuLiN-Creator-Test")', "문자열+데이터형 변환", 14)
    check_variable_value_by_name("MID_OUT", '"-Creator-"', 'MID_OUT ("-Creator-")', "문자열+데이터형 변환", 15)
    check_variable_value_by_name("PASS_1", "TRUE", "PASS_1 (TRUE)", "문자열+데이터형 변환", 16)
    check_variable_value_by_name("DELETE_OUT", '"MuLiN Test"', 'DELETE_OUT ("MuLiN Test")', "문자열+데이터형 변환", 17)
    check_variable_value_by_name("TRIM_OUT", '"MuLiNTest"', 'TRIM_OUT ("MuLiNTest")', "문자열+데이터형 변환", 18)
    check_variable_value_by_name("TO_LOWER_OUT", '"mulintest"', 'TO_LOWER_OUT ("mulintest")', "문자열+데이터형 변환", 19)
    check_variable_value_by_name("TO_UPPER_OUT", '"MULINTEST"', 'TO_UPPER_OUT ("MULINTEST")', "문자열+데이터형 변환", 20)
    check_variable_value_by_name("TO_WSTRING_OUT", '"MULINTEST"', 'TO_WSTRING_OUT ("MULINTEST")', "문자열+데이터형 변환", 21)
    check_variable_value_by_name("TO_STRING_OUT", '"MULINTEST"', 'TO_STRING_OUT ("MULINTEST")', "문자열+데이터형 변환", 22)
    check_variable_value_by_name("PASS_2", "TRUE", "PASS_2 (TRUE)", "문자열+데이터형 변환", 23)
    check_variable_value_by_name("TRIM_LEFT_OUT", '"TRIM TEST "', 'TRIM_LEFT_OUT ("TRIM TEST ")', "문자열+데이터형 변환", 24)
    check_variable_value_by_name("TRIM_RIGHT_OUT", '" TRIM TEST"', 'TRIM_RIGHT_OUT (" TRIM TEST")', "문자열+데이터형 변환", 25)
    check_variable_value_by_name("LEN_OUT", 18, "LEN_OUT (18)", "문자열+데이터형 변환", 26)
    check_variable_value_by_name("PASS_3", "TRUE", "PASS_3 (TRUE)", "문자열+데이터형 변환", 27)
    check_variable_value_by_name("FIND_OUT", 6, "FIND_OUT (6)", "문자열+데이터형 변환", 28)
    check_variable_value_by_name("ARY_TO_STRING_OUT", '"MULINT"', 'ARY_TO_STRING_OUT ("MULINT")', "문자열+데이터형 변환", 30)
    check_variable_value_by_name("ARY_TO_WSTRING_OUT", '"MULINT"', 'ARY_TO_WSTRING_OUT ("MULINT")', "문자열+데이터형 변환", 32)
    check_variable_value_by_name("TO_WCHAR_OUT", '"M"', 'TO_WCHAR_OUT ("M")', "문자열+데이터형 변환", 33)
    check_variable_value_by_name("TO_CHAR_OUT", '"M"', 'TO_CHAR_OUT ("M")', "문자열+데이터형 변환", 34)
    check_variable_value_by_name("PASS_4", "TRUE", "PASS_4 (TRUE)", "문자열+데이터형 변환", 35)
    
    # FB8 모니터링 값 비교
    
    snooze(2)
    doubleClick(waitForObjectItem(names.mvProjectTreeFrame_treeWidget_MinervaD_MvProjectTreeWidget, "MuLiN 명령어 테스트 케이스.POU.함수 블록.Time\\_Date\\_Data\\_Change"), 129, 7, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_selectFBInstanceCheckBox_QCheckBox))
    mouseClick(waitForObjectItem(names.groupBox_listWidget_QListWidget, "Program1\\.TC8"), 43, 15, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.ladderEditorWidget_QPushButton))    
    test.log("FB8 진입") 
    
    check_variable_value_by_name("ADD_TIME_OUT", "1s_750ms", "ADD_TIME_OUT (1s_750ms)", "시간+날짜+데이터형 변환", 10)
    check_variable_value_by_name("SUB_TIME_OUT", "1s_500ms", "SUB_TIME_OUT (1s_500ms)", "시간+날짜+데이터형 변환", 11)
    check_variable_value_by_name("MUL_TIME_OUT", "3s_750ms", "MUL_TIME_OUT (3s_750ms)", "시간+날짜+데이터형 변환", 12)
    check_variable_value_by_name("DIV_TIME_OUT", "1s_500ms", "DIV_TIME_OUT (1s_500ms)", "시간+날짜+데이터형 변환", 13)
    check_variable_value_by_name("TO_LTIME_OUT", "1s_500ms_0us_0ns", "TO_LTIME_OUT (1s_500ms_0us_0ns)", "시간+날짜+데이터형 변환", 14)
    check_variable_value_by_name("ADD_LTIME_OUT", "2s_500ms_0us_0ns", "ADD_LTIME_OUT (2s_500ms_0us_0ns)", "시간+날짜+데이터형 변환", 15)
    check_variable_value_by_name("SUB_LTIME_OUT", "1s_500ms_0us_0ns", "SUB_LTIME_OUT (1s_500ms_0us_0ns)", "시간+날짜+데이터형 변환", 16)
    check_variable_value_by_name("MUL_LTIME_OUT", "3s_750ms_0us_128ns", "MUL_LTIME_OUT (3s_750ms_0us_128ns)", "시간+날짜+데이터형 변환", 17)
    check_variable_value_by_name("DIV_LTIME_OUT", "1s_500ms_0us_0ns", "DIV_LTIME_OUT (1s_500ms_0us_0ns)", "시간+날짜+데이터형 변환", 18)
    check_variable_value_by_name("TO_TIME_OUT", "1s_500ms", "TO_TIME_OUT (1s_500ms)", "시간+날짜+데이터형 변환", 19)
    check_variable_value_by_name("ADD_TOD_TIME_OUT", "09:00:01.500", "ADD_TOD_TIME_OUT (09:00:01.500)", "시간+날짜+데이터형 변환", 20)
    check_variable_value_by_name("SUB_TOD_TIME_OUT", "09:00:00.000", "SUB_TOD_TIME_OUT (09:00:00.000)", "시간+날짜+데이터형 변환", 21)
    check_variable_value_by_name("PASS_1", "TRUE", "PASS_1 (TRUE)", "시간+날짜+데이터형 변환", 22)
    check_variable_value_by_name("ADD_DT_TIME_OUT", "2026-01-01-09:00:01", "ADD_DT_TIME_OUT (2026-01-01-09:00:01)", "시간+날짜+데이터형 변환", 23)
    check_variable_value_by_name("SUB_DT_TIME_OUT", "2026-01-01-09:00:00", "SUB_DT_TIME_OUT (2026-01-01-09:00:00)", "시간+날짜+데이터형 변환", 24)
    check_variable_value_by_name("DT_TO_SEC_OUT", 1767258000, "DT_TO_SEC_OUT (1767258000)", "시간+날짜+데이터형 변환", 25)
    check_variable_value_by_name("SEC_TO_TIME_OUT1", "23d_10h_54m_1s_344ms", "SEC_TO_TIME_OUT1 (23d_10h_54m_1s_344ms)", "시간+날짜+데이터형 변환", 26)
    check_variable_value_by_name("TIME_TO_SEC_OUT", 1767258000, "TIME_TO_SEC_OUT (1767258000)", "시간+날짜+데이터형 변환", 27)
    check_variable_value_by_name("SEC_TO_DATE_OUT", "2026-01-01", "SEC_TO_DATE_OUT (2026-01-01)", "시간+날짜+데이터형 변환", 28)
    check_variable_value_by_name("DATE_TO_SEC_OUT", 1767258000, "DATE_TO_SEC_OUT (1767258000)", "시간+날짜+데이터형 변환", 29)
    check_variable_value_by_name("SEC_TO_TIME_OUT2", "23d_10h_54m_1s_344ms", "SEC_TO_TIME_OUT2 (23d_10h_54m_1s_344ms)", "시간+날짜+데이터형 변환", 30)
    check_variable_value_by_name("TIME_TO_NSEC_OUT", 2026441344000000, "TIME_TO_NSEC_OUT (2026441344000000)", "시간+날짜+데이터형 변환", 31)
    check_variable_value_by_name("PASS_2", "TRUE", "PASS_2 (TRUE)", "시간+날짜+데이터형 변환", 32)
    check_variable_value_by_name("ADD_LDT_LTIME_OUT", "2026-01-01-10:01:01.001001001", "ADD_LDT_LTIME_OUT (...)", "시간+날짜+데이터형 변환", 33)
    check_variable_value_by_name("SUB_LDT_LTIME_OUT", "2026-01-01-09:31:00", "SUB_LDT_LTIME_OUT (...)", "시간+날짜+데이터형 변환", 34)
    check_variable_value_by_name("ADD_LTOD_LTIME_OUT", "10:32:01.001001001", "ADD_LTOD_LTIME_OUT (...)", "시간+날짜+데이터형 변환", 35)
    check_variable_value_by_name("SUB_LTOD_LTIME_OUT", "10:02:00.000000000", "SUB_LTOD_LTIME_OUT (...)", "시간+날짜+데이터형 변환", 36)
    check_variable_value_by_name("PASS_3", "TRUE", "PASS_3 (TRUE)", "시간+날짜+데이터형 변환", 37)
    check_variable_value_by_name("CONCAT_DATE_OUT", "2026-01-01", "CONCAT_DATE_OUT (2026-01-01)", "시간+날짜+데이터형 변환", 38)
    check_variable_value_by_name("TO_LDATE_OUT", "2026-01-01", "TO_LDATE_OUT (2026-01-01)", "시간+날짜+데이터형 변환", 39)
    check_variable_value_by_name("TO_DATE_OUT", "2026-01-01", "TO_DATE_OUT (2026-01-01)", "시간+날짜+데이터형 변환", 40)
    check_variable_value_by_name("CONCAT_TOD_OUT", "12:30:30.030", "CONCAT_TOD_OUT (12:30:30.030)", "시간+날짜+데이터형 변환", 41)
    check_variable_value_by_name("TO_LTOD_OUT", "12:30:30.030000000", "TO_LTOD_OUT (...)", "시간+날짜+데이터형 변환", 42)
    check_variable_value_by_name("TO_TOD_OUT", "12:30:30.030", "TO_TOD_OUT (12:30:30.030)", "시간+날짜+데이터형 변환", 43)
    check_variable_value_by_name("CONCAT_DATE_TOD_OUT", "2026-01-01-12:30:30", "CONCAT_DATE_TOD_OUT (...)", "시간+날짜+데이터형 변환", 44)
    check_variable_value_by_name("TO_LDT_OUT", "2026-01-01-12:30:30", "TO_LDT_OUT (...)", "시간+날짜+데이터형 변환", 45)
    check_variable_value_by_name("TO_DT_OUT", "2026-01-01-12:30:30", "TO_DT_OUT (...)", "시간+날짜+데이터형 변환", 46)
    check_variable_value_by_name("PASS_4", "TRUE", "PASS_4 (TRUE)", "시간+날짜+데이터형 변환", 47)
    check_variable_value_by_name("SPLIT_DT_YEAR", 2026, "SPLIT_DT_YEAR (2026)", "시간+날짜+데이터형 변환", 48)
    check_variable_value_by_name("SPLIT_DT_MONTH", 1, "SPLIT_DT_MONTH (1)", "시간+날짜+데이터형 변환", 48)
    check_variable_value_by_name("SPLIT_DT_DAY", 1, "SPLIT_DT_DAY (1)", "시간+날짜+데이터형 변환", 48)
    check_variable_value_by_name("SPLIT_DT_HOUR", 12, "SPLIT_DT_HOUR (12)", "시간+날짜+데이터형 변환", 48)
    check_variable_value_by_name("SPLIT_DT_MIN", 30, "SPLIT_DT_MIN (30)", "시간+날짜+데이터형 변환", 48)
    check_variable_value_by_name("SPLIT_DT_SEC", 30, "SPLIT_DT_SEC (30)", "시간+날짜+데이터형 변환", 48)
    check_variable_value_by_name("CONCAT_DT_OUT", "2026-01-01-12:30:30", "CONCAT_DT_OUT (...)", "시간+날짜+데이터형 변환", 49)
    check_variable_value_by_name("SPLIT_LDT_YEAR", 2026, "SPLIT_LDT_YEAR (2026)", "시간+날짜+데이터형 변환", 50)
    check_variable_value_by_name("SPLIT_LDT_MONTH", 1, "SPLIT_LDT_MONTH (1)", "시간+날짜+데이터형 변환", 50)
    check_variable_value_by_name("SPLIT_LDT_DAY", 1, "SPLIT_LDT_DAY (1)", "시간+날짜+데이터형 변환", 50)
    check_variable_value_by_name("SPLIT_LDT_HOUR", 12, "SPLIT_LDT_HOUR (12)", "시간+날짜+데이터형 변환", 50)
    check_variable_value_by_name("SPLIT_LDT_MIN", 30, "SPLIT_LDT_MIN (30)", "시간+날짜+데이터형 변환", 50)
    check_variable_value_by_name("SPLIT_LDT_SEC", 30, "SPLIT_LDT_SEC (30)", "시간+날짜+데이터형 변환", 50)
    check_variable_value_by_name("SPLIT_LDT_MSEC", 0, "SPLIT_LDT_MSEC (0)", "시간+날짜+데이터형 변환", 50)
    check_variable_value_by_name("SPLIT_LDT_NSEC", 0, "SPLIT_LDT_NSEC (0)", "시간+날짜+데이터형 변환", 50)
    check_variable_value_by_name("CONCAT_LDT_OUT", "2026-01-01-12:30:30", "CONCAT_LDT_OUT (...)", "시간+날짜+데이터형 변환", 51)
    check_variable_value_by_name("PASS_5", "TRUE", "PASS_5 (TRUE)", "시간+날짜+데이터형 변환", 52)
    check_variable_value_by_name("SPLIT_DATE_YEAR", 2026, "SPLIT_DATE_YEAR (2026)", "시간+날짜+데이터형 변환", 53)
    check_variable_value_by_name("SPLIT_DATE_MONTH", 1, "SPLIT_DATE_MONTH (1)", "시간+날짜+데이터형 변환", 53)
    check_variable_value_by_name("SPLIT_DATE_DAY", 1, "SPLIT_DATE_DAY (1)", "시간+날짜+데이터형 변환", 53)
    check_variable_value_by_name("CONCAT_LDATE_OUT", "2026-01-01", "CONCAT_LDATE_OUT (2026-01-01)", "시간+날짜+데이터형 변환", 54)
    check_variable_value_by_name("SPLIT_TOD_HOUR", 12, "SPLIT_TOD_HOUR (12)", "시간+날짜+데이터형 변환", 55)
    check_variable_value_by_name("SPLIT_TOD_MIN", 30, "SPLIT_TOD_MIN (30)", "시간+날짜+데이터형 변환", 55)
    check_variable_value_by_name("SPLIT_TOD_SEC", 30, "SPLIT_TOD_SEC (30)", "시간+날짜+데이터형 변환", 55)
    check_variable_value_by_name("SPLIT_TOD_MSEC", 30, "SPLIT_TOD_MSEC (30)", "시간+날짜+데이터형 변환", 55)
    check_variable_value_by_name("CONCAT_LTOD_OUT", "12:30:30.030000030", "CONCAT_LTOD_OUT (...)", "시간+날짜+데이터형 변환", 56)
    check_variable_value_by_name("SPLIT_LTOD_HOUR", 12, "SPLIT_LTOD_HOUR (12)", "시간+날짜+데이터형 변환", 57)
    check_variable_value_by_name("SPLIT_LTOD_MIN", 30, "SPLIT_LTOD_MIN (30)", "시간+날짜+데이터형 변환", 57)
    check_variable_value_by_name("SPLIT_LTOD_SEC", 30, "SPLIT_LTOD_SEC (30)", "시간+날짜+데이터형 변환", 57)
    check_variable_value_by_name("SPLIT_LTOD_MSEC", 30, "SPLIT_LTOD_MSEC (30)", "시간+날짜+데이터형 변환", 57)
    check_variable_value_by_name("SPLIT_LTOD_NSEC", 30, "SPLIT_LTOD_NSEC (30)", "시간+날짜+데이터형 변환", 57)
    check_variable_value_by_name("CONCAT_DATE_LTOD_OUT", "2026-01-01-12:30:30.030000030", "CONCAT_DATE_LTOD_OUT (...)", "시간+날짜+데이터형 변환", 58)
    check_variable_value_by_name("PASS_6", "TRUE", "PASS_6 (TRUE)", "시간+날짜+데이터형 변환", 59)
    check_variable_value_by_name("SUB_DATE_DATE_OUT", "10d_0ms", "SUB_DATE_DATE_OUT (10d_0ms)", "시간+날짜+데이터형 변환", 60)
    check_variable_value_by_name("SUB_LDATE_LDATE_OUT", "10d_0ns", "SUB_LDATE_LDATE_OUT (10d_0ns)", "시간+날짜+데이터형 변환", 61)
    check_variable_value_by_name("SUB_TOD_TOD_OUT", "3h_30m_30s_30ms", "SUB_TOD_TOD_OUT (...)", "시간+날짜+데이터형 변환", 62)
    check_variable_value_by_name("SUB_LTOD_LTOD_OUT", "3h_30m_30s_30ms_0us_30ns", "SUB_LTOD_LTOD_OUT (...)", "시간+날짜+데이터형 변환", 63)
    check_variable_value_by_name("SUB_DT_DT_OUT", "10d_3h_30m_30s_0ms", "SUB_DT_DT_OUT (...)", "시간+날짜+데이터형 변환", 64)
    check_variable_value_by_name("SUB_LDT_LDT_OUT", "31d_3h_30m_30s_0ms_0us_30ns", "SUB_LDT_LDT_OUT (...)", "시간+날짜+데이터형 변환", 65)
    check_variable_value_by_name("PASS_7", "TRUE", "PASS_7 (TRUE)", "시간+날짜+데이터형 변환", 66)
    check_variable_value_by_name("DAY_OF_WEEK_OUT", 3, "DAY_OF_WEEK_OUT (3)", "시간+날짜+데이터형 변환", 67)
    check_variable_value_by_name("WEEK_OF_YEAR_OUT", 5, "WEEK_OF_YEAR_OUT (5)", "시간+날짜+데이터형 변환", 68)
    check_variable_value_by_name("DAYS_OF_MON_OUT", 28, "DAYS_OF_MON_OUT (28)", "시간+날짜+데이터형 변환", 69)
    check_variable_value_by_name("DAYS_TO_MON_OUT", 2, "DAYS_TO_MON_OUT (2)", "시간+날짜+데이터형 변환", 70)
    check_variable_value_by_name("IS_LEAP_YEAR_OUT", "TRUE", "IS_LEAP_YEAR_OUT (TRUE)", "시간+날짜+데이터형 변환", 71)
    check_variable_value_by_name("PASS_8", "TRUE", "PASS_8 (TRUE)", "시간+날짜+데이터형 변환", 72)
        
    
    # 종료
    snooze(2)
    test.log("Test 종료.")
    sendEvent("QCloseEvent", waitForObject(names.projectMainWindow))    

