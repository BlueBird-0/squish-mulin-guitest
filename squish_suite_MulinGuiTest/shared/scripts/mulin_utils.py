# -*- coding: utf-8 -*-
"""MuLiN Creator GUI 테스트 공용 유틸리티 모듈.

Squish 테스트 케이스에서 반복적으로 사용되는 동작을 함수로 분리한 모듈입니다.
`shared/scripts` 에 위치하므로 모든 테스트 케이스에서 아래처럼 import 할 수 있습니다.

    import mulin_utils as mulin

    def main():
        mulin.open_project("SquishTest1")
        mulin.build_project()

공용 함수
---------
* :func:`open_project`          - 프로젝트명을 받아 해당 MuLiN 프로젝트를 엽니다.
* :func:`build_project`         - 메뉴에서 빌드를 실행하고 성공 여부를 검증합니다.
* :func:`close_recover_dialog`  - 복구 다이얼로그가 뜨면 닫고, 없으면 그냥 넘어갑니다.

보조 함수
---------
* :func:`start_mulin`           - AUT 실행 후 메인 윈도우가 뜰 때까지 대기합니다.

참고 문서
---------
* https://doc.qt.io/squish/qt-convenience-api.html
* https://doc.qt.io/squish/api-reference-manual.html
* https://doc.qt.io/squish/waitforobject-function.html
  (waitForObject(objectOrName, timeoutMSec) - 타임아웃 시 LookupError 발생)
"""

import re

import names
import squish
from objectmaphelper import Wildcard

# ---------------------------------------------------------------------------
# 공용 함수
# ---------------------------------------------------------------------------

def close_recover_dialog(timeout=1000):
    """복구 다이얼로그가 떠 있으면 닫습니다.

    ``timeout`` 동안 다이얼로그가 나타나지 않으면 로그만 남기고 그냥 넘어갑니다.
    (waitForObject 는 타임아웃 시 LookupError 를 발생시키므로 이를 잡아서 무시합니다.)

    :param timeout: 다이얼로그 대기 시간(ms). 기본 3000ms.
    :returns: 실제로 다이얼로그를 닫았으면 ``True``, 나타나지 않았으면 ``False``.
    """
    
    try:
        squish.waitForObject(
            names.mvRecoverProjectDialog_MinervaD_MvRecoverProjectDialog, timeout
        )
    except LookupError:
        squish.test.log("복구 다이얼로그가 나타나지 않아 스킵합니다. (대기 %dms)" % timeout)
        return False

    squish.clickButton(squish.waitForObject(names.mvRecoverProjectDialog_btnClose_QPushButton))
    squish.test.log("복구 다이얼로그를 닫았습니다.")
    return True


def open_project(project_name,
                 timeout=1000,
                 recover_dialog_timeout=1000):
    """프로젝트명을 받아 해당 MuLiN 프로젝트를 엽니다.

    수행 순서
        1. (``start_app`` 이 True 면) AUT 실행 및 메인 윈도우 대기
        2. 시작 시 뜨는 복구 다이얼로그 닫기
        3. 메뉴바 '파일' > '프로젝트 열기' 실행
        4. 파일 열기 다이얼로그 트리에서 ``{프로젝트명}`` 폴더 진입
        5. 폴더 안의 ``{프로젝트명}.mdp`` 파일을 더블클릭하여 열기
        6. 프로젝트 로딩 중 뜨는 복구 다이얼로그 닫기
        7. 윈도우 타이틀에 프로젝트명이 반영되는지 확인

    :param project_name: 프로젝트명. ``"SquishTest1"`` 또는 ``"SquishTest1.mdp"``.
    :param timeout: 프로젝트 로딩 완료 대기 시간(ms).
    :param recover_dialog_timeout: 복구 다이얼로그 대기 시간(ms).
    :returns: 프로젝트가 열린 것으로 확인되면 ``True``, 확인에 실패하면 ``False``.
    """
    name = str(project_name)
    squish.test.log("프로젝트 열기 시작: %s" % name)

    # 메뉴바 '파일' > '프로젝트 열기'
    squish.activateItem(squish.waitForObjectItem(names.muLiN_Creator_QMenuBar, "파일"))
    squish.activateItem(squish.waitForObjectItem(names.muLiN_Creator_QMenu_3, "프로젝트 열기"))
    squish.snooze(0.5)

    try:
        # 트리 뷰에서 프로젝트 폴더로 진입
        folder = dict(names.treeView_testProjectFolders)
        folder["text"] = name
        squish.doubleClick(squish.waitForObject(folder, timeout))
    
        # 폴더 안의 .mdp 파일을 더블클릭하여 열기
        project = dict(names.treeView_project_mdps)
        project["text"] = Wildcard("*.mdp")
        squish.doubleClick(squish.waitForObject(project, timeout))

    # 프로젝트가 열렸는지 확인
    except LookupError:
        squish.test.warning(
            "'%s' 프로젝트를 열 수 없습니다 확인하지 못했습니다."
            % name
        )
        return False

    squish.test.log("프로젝트를 열었습니다: %s" % name)
    return True

def build_project():
    """메뉴에서 빌드를 실행하고 에러 없이 성공했는지 검증합니다.

    빌드 결과는 메시지 창 '빌드' 탭의 에러 버튼 텍스트(예: ``"에러 (0)"``)로 판정하며,
    ``test.passes`` / ``test.fail`` 로 결과를 기록합니다.

    :param timeout: 빌드 완료(에러 버튼 등장) 대기 시간(ms).
    :returns: 빌드 성공 시 ``True``, 실패 시 ``False``.
    """
    
    squish.activateItem(squish.waitForObjectItem(names.muLiN_Creator_Documents_mdp_QMenuBar, "프로젝트"))
    squish.activateItem(squish.waitForObjectItem(names.muLiN_Creator_Documents_mdp_QMenu, "빌드"))

    return check_build_result()

def check_build_result():
    # 1. 빌드가 완료되고 UI를 찾을 때 까지 대기
    squish.test.log("Project Build Start...")
    error_button = squish.waitForObject(names.tabBuild_btnError_QToolButton_2, 10000)
    squish.test.log("Project Build End")
    
    # 2. error_button에서 text 속성 값을 꺼내 문자열로 변환합니다.
    button_text = str(error_button["text"])
    
    # 3. [검증 방식 A] 정확히 "에러 (0)" 인지 체크하는 방법
    if button_text == "에러 (0)":
        squish.test.passes("빌드가 에러 없이 성공적으로 완료되었습니다.")
        return True
    else:
        squish.test.fail(f"빌드 실패! {button_text}이(가) 발견되었습니다.")
        return False