# -*- coding: utf-8 -*-

import names
import mulin_utils as mulin
import builtins

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
    ### Network Qt Graphic Item을 가져옴
    ladderViewFrame = findObject(names.splitter_LadderView_MinervaD_MvLadderViewFrame)
    p = ladderViewFrame.networkCenter(0)
    
    test.log("[itemCenter] scene=(%d, %d)" % (p.x, p.y))
    mouseClick(ladderViewFrame, p.x, p.y, Qt.NoModifier, Qt.LeftButton)
    
    ### "myEn" Contact와 "myEno" Coil을 생성
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
    
    ## test
    test.log("networkItems Test Start")
    test.log(str(ladderViewFrame.networkItemsDebug(0)))
    
    ### network item 함수화 하기
    points = ladderViewFrame.networkItems(0)    
    for i in range(points.count()):
        p = points.at(i).toPoint()
        test.log("points= %d, %d" % (p.x, p.y))
        mouseClick(ladderViewFrame, p.x, p.y, Qt.NoModifier, Qt.LeftButton)
        snooze(1)
    
    test.log("networkItems Test End")
    
    snooze(10)

def smoothMove(obj, fromX, fromY, toX, toY, steps=25, duration=0.4):
    """fromX,Y에서 toX,Y까지 duration초 동안 부드럽게 이동"""
    for s in range(1, steps + 1):
        t = s / float(steps)
        t = t * t * (3 - 2 * t)   # ease-in-out: 출발·도착에서 느려짐
        x = builtins.int((fromX + (toX - fromX) * t))
        y = builtins.int(builtins.int(fromY + (toY - fromY) * t))
        mouseMove(obj, x, y)
        snooze(duration / steps)