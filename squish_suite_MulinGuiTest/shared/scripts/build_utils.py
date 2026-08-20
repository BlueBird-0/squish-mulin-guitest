# -*- coding: utf-8 -*-
"""
MuLiN 프로젝트 빌드 관련 재사용 가능한 유틸리티 함수들
"""

import names


def close_recovery_dialog(timeout=3000):
    """
    복구 다이얼로그가 나타나면 닫기
    
    Args:
        timeout (int): 다이얼로그 대기 시간 (밀리초)
    
    Returns:
        bool: 다이얼로그를 찾아 닫으면 True, 나타나지 않으면 False
    """
    try:
        waitForObject(names.mvRecoverProjectDialog_MinervaD_MvRecoverProjectDialog, timeout)
        clickButton(waitForObject(names.mvRecoverProjectDialog_btnClose_QPushButton))
        test.log("복구 다이얼로그 닫음")
        return True
    except LookupError:
        test.log("복구 다이얼로그가 나타나지 않아 스킵합니다.")
        return False


def build_project(menu_bar_name, menu_name, submenu_name, wait_time=0.5):
    """
    프로젝트 빌드 실행
    
    Args:
        menu_bar_name (str): 메뉴바 이름 (names 객체의 속성)
        menu_name (str): 메뉴 이름
        submenu_name (str): 서브메뉴 이름
        wait_time (float): 빌드 명령 후 대기 시간 (초)
    """
    try:
        activateItem(waitForObjectItem(menu_bar_name, menu_name))
        activateItem(waitForObjectItem(menu_bar_name, submenu_name))
        snooze(wait_time)
        test.log(f"프로젝트 빌드 시작: {menu_name} > {submenu_name}")
    except Exception as e:
        test.log(f"빌드 실행 중 오류: {str(e)}")
        raise


def check_build_result(error_button_name, timeout=10000, expected_error_count=0):
    """
    빌드 결과 확인 및 검증
    
    Args:
        error_button_name (str): 에러 버튼의 names 객체 속성
        timeout (int): 빌드 완료 대기 시간 (밀리초)
        expected_error_count (int): 예상 에러 개수 (기본값: 0)
    
    Returns:
        dict: 빌드 결과 {'success': bool, 'error_count': int, 'button_text': str}
    """
    test.log("프로젝트 빌드 시작...")
    error_button = waitForObject(error_button_name, timeout)
    test.log("프로젝트 빌드 완료")
    
    # 버튼 속성에서 에러 정보 추출
    button_properties = object.properties(error_button)
    button_text = str(button_properties["text"])
    
    # 버튼 텍스트에서 에러 개수 추출 (예: "에러 (0)" -> 0)
    try:
        error_count = int(button_text.split("(")[1].split(")")[0])
    except (IndexError, ValueError):
        error_count = -1  # 파싱 실패
    
    result = {
        'success': error_count == expected_error_count,
        'error_count': error_count,
        'button_text': button_text
    }
    
    # 결과 로깅 및 검증
    if result['success']:
        test.passes(f"빌드 완료: {button_text}")
    else:
        test.fail(f"빌드 실패! {button_text} (예상: 에러 ({expected_error_count}))")
    
    return result


def execute_build_with_validation(menu_bar_name, menu_name, submenu_name, 
                                   error_button_name, expected_error_count=0,
                                   recovery_timeout=3000, build_timeout=10000, 
                                   wait_after_build=0.5):
    """
    빌드 실행부터 검증까지 한 번에 처리하는 통합 함수
    
    Args:
        menu_bar_name (str): 메뉴바 이름
        menu_name (str): 메뉴 이름
        submenu_name (str): 서브메뉴 이름
        error_button_name (str): 에러 버튼의 names 객체 속성
        expected_error_count (int): 예상 에러 개수
        recovery_timeout (int): 복구 다이얼로그 대기 시간 (밀리초)
        build_timeout (int): 빌드 완료 대기 시간 (밀리초)
        wait_after_build (float): 빌드 후 대기 시간 (초)
    
    Returns:
        dict: 빌드 결과
    """
    # 복구 다이얼로그 처리
    close_recovery_dialog(recovery_timeout)
    
    # 빌드 실행
    build_project(menu_bar_name, menu_name, submenu_name, wait_after_build)
    
    # 빌드 결과 확인
    result = check_build_result(error_button_name, build_timeout, expected_error_count)
    
    return result
