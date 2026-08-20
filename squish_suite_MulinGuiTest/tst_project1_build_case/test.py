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
    mulin.open_project("SquishTest1")
    
    # 4. 3000ms(3초) 동안 복구 다이얼로그 창이 활성화되기를 기다립니다.
    mulin.close_recover_dialog(3000)

    # 5. 프로젝트를 빌드합니다
    mulin.build_project()
