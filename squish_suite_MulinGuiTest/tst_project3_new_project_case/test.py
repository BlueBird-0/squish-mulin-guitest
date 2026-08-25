# -*- coding: utf-8 -*-

import names
import mulin_utils as mulin

def main():
    # 1. 앱 실행 및 대기
    startApplication('"MuLiN Creator"')
    waitForObject(names.muLiN_Creator_MinervaD_MvMainWindow, 15000)
    
    # 2. 3000ms(3초) 동안 복구 다이얼로그 창이 활성화되기를 기다립니다.
    mulin.close_recover_dialog(3000)
    
    # 3. 프로젝트를 생성합니다.
    mulin.new_project("new_project_test")
    snooze(10)
