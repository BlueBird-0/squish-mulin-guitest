# -*- coding: utf-8 -*-

import names
import mulin_utils as mulin

def main():
    # 1. 앱 실행 및 대기
    startApplication('"MuLiN Creator"')
    waitForObject(names.muLiN_Creator_MinervaD_MvMainWindow, 15000)
    
    # 2. 3000ms(3초) 동안 복구 다이얼로그 창이 활성화되기를 기다립니다.
    mulin.close_recover_dialog(3000)
    
    # 3. 메뉴바에서 '파일' -> '프로젝트 열기' 실행
    mulin.open_project("UserFcTest")
    
    # 4. 3000ms(3초) 동안 복구 다이얼로그 창이 활성화되기를 기다립니다.
    mulin.close_recover_dialog(3000)
    
    # 5 OpenPage
    mulin.open_page("Function1")
    
    # 6. UserFC를 생성합니다. 
    ladderViewFrame = findObject(names.MinervaD_MvLadderViewFrame)
    
    x, y = mulin.network_center(0)    
    test.log("[network Center] point=(%d, %d)" % (x, y))
    mouseClick(ladderViewFrame, x, y, Qt.NoModifier, Qt.LeftButton)
    
    # "myEn" Contact와 "myEno" Coil을 생성
    clickButton(waitForObject(names.mvNetworkControlFrame_btnContact_MinervaD_MvDragablePushButton))
    snooze(0.5)
    nativeType("enEn")
    snooze(0.5)
    nativeType("<Return>")
    snooze(0.5)
    nativeType("<Return>")
    snooze(0.5)
    nativeType("<Return>")
    snooze(0.5)
    
    nativeType("<Right>")
    snooze(0.5)

    clickButton(waitForObject(names.mvNetworkControlFrame_btnCoil_MinervaD_MvDragablePushButton))
    snooze(0.5)
    nativeType("myEno")
    snooze(0.5)
    nativeType("<Return>")
    snooze(0.5)
    nativeType("<Return>")
    snooze(0.5)
    nativeType("<Return>")
    snooze(0.5)
    
    ### network item 함수화 하기
    for x, y in mulin.network_items_centers(0):
        test.log("[network Item Center] point=(%d, %d)" % (x, y))
        mouseClick(ladderViewFrame, x, y, Qt.NoModifier, Qt.LeftButton)
        snooze(2)
        
    # 7. 여기까지 잘 오고, Build가 된다면 userFC 프로젝트가 성공된 것으로 판정합니다.
    mulin.build_project()
    
    snooze(10)
    