# -*- coding: utf-8 -*-

import names
import re

def main():
    # 1. 앱 실행 및 대기
    startApplication('"MuLiN Creator"')
    waitForObject(names.muLiN_Creator_MinervaD_MvMainWindow, 15000)
    
    # 1. 3000ms(3초) 동안 복구 다이얼로그 창이 활성화되기를 기다립니다.
    try:
        # 3000ms(3초) 동안 창을 기다립니다. 찾지 못하면 에러(Exception)가 발생합니다.
        waitForObject(names.mvRecoverProjectDialog_MinervaD_MvRecoverProjectDialog, 3000)
        # 창을 찾았다면 닫기 버튼 클릭
        clickButton(waitForObject(names.mvRecoverProjectDialog_btnClose_QPushButton))
        test.log("복구 다이얼로그 닫음")
    except LookupError:
        # 3초 동안 창이 안 뜨면 에러를 무시하고 넘어갑니다.
        test.log("복구 다이얼로그가 나타나지 않아 스킵합니다.")
        
    
    # 2. 메뉴바에서 '파일' -> '프로젝트 열기' 실행
    activateItem(waitForObjectItem(names.muLiN_Creator_QMenuBar, "파일"))
    activateItem(waitForObjectItem(names.muLiN_Creator_QMenu_3, "프로젝트 열기"))
    snooze(0.5)
    
    # 3. [수정] 트리 뷰에서 프로젝트 폴더(SquishTest1)를 선택 (clickButton -> mouseClick)
    # 만약 폴더 안으로 진입해야 한다면 doubleClick(waitForObject(...)) 을 사용하세요.
    doubleClick(waitForObject(names.treeView_testProject_SquishTest3))
    snooze(0.5)
    
    # 4. [순서 변경] 폴더 내부에 있는 실제 프로젝트 파일(.mdp)을 먼저 선택합니다.
    doubleClick(waitForObject(names.treeView_SquishTest3_mdp_QModelIndex))
    # 1. 3000ms(3초) 동안 복구 다이얼로그 창이 활성화되기를 기다립니다.
    try:
        # 3000ms(3초) 동안 창을 기다립니다. 찾지 못하면 에러(Exception)가 발생합니다.
        waitForObject(names.mvRecoverProjectDialog_MinervaD_MvRecoverProjectDialog, 1000)
        # 창을 찾았다면 닫기 버튼 클릭
        clickButton(waitForObject(names.mvRecoverProjectDialog_btnClose_QPushButton))
        test.log("복구 다이얼로그 닫음")
    except LookupError:
        # 3초 동안 창이 안 뜨면 에러를 무시하고 넘어갑니다.
        test.log("복구 다이얼로그가 나타나지 않아 스킵합니다.")
    
    # 5. 파일이 선택된 상태에서 최종적으로 '열기' 버튼을 클릭합니다.
    snooze(2)

    activateItem(waitForObjectItem(names.muLiN_Creator_Documents_mdp_QMenuBar, "프로젝트"))
    activateItem(waitForObjectItem(names.muLiN_Creator_Documents_mdp_QMenu, "빌드"))
    # 빌드대기
    snooze(0.5)
    check_build_result()
    snooze(0.5)
    
    # Record기능을 이용한 커넥팅 및 다운로드
    doubleClick(waitForObject(names.o_Program1_QModelIndex))
    clickButton(waitForObject(names.o_Qtitan_ToolButton))
    clickButton(waitForObject(names.o_Qtitan_ToolButton_2))
    clickButton(waitForObject(names.mvDownloadToDeviceDialog_QPushButton))
    clickButton(waitForObject(names.o_QPushButton))
    clickButton(waitForObject(names.o_Qtitan_ToolButton_3))
    # doubleClick(waitForObject(names.o_Program1_QModelIndex))
    
    # 모니터링 값 비교
    # 1. 객체 대기 및 toolTip 속성 추출
    snooze(3)
    scrollBar = waitForObject(names.ladderView_QScrollBar)
    page_step = cast(object.properties(scrollBar)["pageStep"], int) # Network 페이지 크기만큼 int 형으로 읽어오기
    
    # scrollTo(scrollBar, page_step * 1)    # item = waitForObject(names.o_h2_b_font_color_blue_font_b_h2_b_30_b_br_QGraphicsItem)
    
    snooze(3)
    if test.imagePresent("add_result.png"):
        test.passes("add_result.png 찾음")
    else:
        test.fail("add_result.png 못 찾음")
            
def check_build_result():
    # 1. 빌드가 완료되고 UI를 찾을 때 까지 대기
    test.log("Project Build Start...")
    error_button = waitForObject(names.tabBuild_btnError_QToolButton_2, 10000)
    test.log("Project Build End")
    
    # 2. [공식문서 가이드] object.properties()를 통해 객체의 전체 속성을 딕셔너리로 추출합니다.
    button_properties = object.properties(error_button)
    
    # 3. 딕셔너리에서 "text" 속성 값을 안전하게 꺼내 문자열로 변환합니다.
    button_text = str(button_properties["text"])
    
    # 4. [검증 방식 A] 정확히 "에러 (0)" 인지 체크하는 방법
    if button_text == "에러 (0)":
        test.passes("빌드가 에러 없이 성공적으로 완료되었습니다.")
    else:
        test.fail(f"빌드 실패! {button_text}이(가) 발견되었습니다.")
