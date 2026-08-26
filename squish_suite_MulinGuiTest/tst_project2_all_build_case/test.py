# -*- coding: utf-8 -*-
"""지정한 폴더 안의 모든 MuLiN 프로젝트가 정상적으로 빌드되는지 검사하는 테스트 케이스.

동작 개요
    1. 테스트할 MuLiN 프로젝트목록을 입력받습니다.
    2. 프로젝트마다 [AUT 실행 -> 프로젝트 열기 -> 빌드 -> AUT 종료] 를 반복합니다.
    3. 마지막에 전체 성공/실패를 요약하고, 하나라도 실패하면 테스트를 실패로 판정합니다.

프로젝트마다 AUT 를 재시작하는 이유
    names.py 의 ``muLiN_Creator_QMenuBar`` 는 windowTitle 이 정확히 "MuLiN Creator" 인
    윈도우(= 아직 프로젝트를 열지 않은 상태)만 매칭합니다. 프로젝트를 열면 타이틀에 파일
    경로가 붙어 더 이상 매칭되지 않으므로, 같은 인스턴스에서 '파일 > 프로젝트 열기' 를
    두 번 호출할 수 없습니다. 따라서 프로젝트별로 AUT 를 새로 띄웁니다.
    (부수 효과로 이전 프로젝트의 상태가 다음 빌드 결과에 영향을 주지 않습니다.)

공통 동작은 shared/scripts/mulin_utils.py 를 `mulin` 이름으로 사용합니다.

참고 문서
    * https://doc.qt.io/squish/qt-convenience-api.html
    * https://doc.qt.io/squish/waitforobject-function.html  (타임아웃 시 LookupError)
    * https://doc.qt.io/squish/applicationcontext-class.html  (detach() / isRunning)
"""

import names
import mulin_utils as mulin

# ---------------------------------------------------------------------------
# 설정
# ---------------------------------------------------------------------------

MAIN_WINDOW_TIMEOUT = 15000    #: 앱 실행 후 메인 윈도우 대기(ms)
RECOVER_DIALOG_TIMEOUT = 3000  #: 복구 다이얼로그 대기(ms)
APP_EXIT_TIMEOUT_SEC = 10.0    #: AUT 종료 대기(초)


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main():
    # 1. 빌드 대상 프로젝트 목록 ('문서' 폴더에 존재해야 함.)
    projects = ["SquishTest1", "SquishTest2_math", "SquishTest3_userFc", "SquishTest4_MuLiN 명령어 테스트 케이스"]

    test.log("총 %d개 프로젝트를 빌드합니다: %s" % (len(projects), ", ".join(projects)))

    # 2. 프로젝트별로 열기 + 빌드
    succeeded = []
    failed = []
    for index, project_name in enumerate(projects, start=1):
        test.log("[%d/%d] %s" % (index, len(projects), project_name))
        if build_single_project(project_name):
            succeeded.append(project_name)
        else:
            failed.append(project_name)

    # 3. 전체 결과 요약
    report_summary(projects, succeeded, failed)


def build_single_project(project_name):
    """프로젝트 하나를 열고 빌드한 뒤 AUT 를 종료합니다.

    한 프로젝트가 실패해도 나머지 프로젝트 검사를 계속하기 위해 예외를 잡아
    실패로 기록합니다.

    :returns: 빌드가 에러 없이 성공하면 ``True``, 그 외 ``False``.
    """
    test.startSection("프로젝트 빌드: %s" % project_name)
    result = False
    try:
        # 앱 실행 및 대기
        startApplication('"MuLiN Creator"')
        waitForObject(names.muLiN_Creator_MinervaD_MvMainWindow, MAIN_WINDOW_TIMEOUT)

        # 시작 시 뜨는 복구 다이얼로그 처리
        mulin.close_recover_dialog(RECOVER_DIALOG_TIMEOUT)

        # 프로젝트 열기 ('파일' > '프로젝트 열기')
        if not mulin.open_project(project_name, 1000):
            test.fail("'%s' 프로젝트를 열지 못했습니다." % project_name)
        else:
            # 프로젝트 로딩 중 뜨는 복구 다이얼로그 처리
            mulin.close_recover_dialog(RECOVER_DIALOG_TIMEOUT)
            # 빌드 실행 및 결과 검증
            result = mulin.build_project()
    except LookupError as exc:
        # waitForObject 계열 타임아웃 (객체를 찾지 못함)
        test.fail("'%s' 빌드 중 객체를 찾지 못했습니다: %s" % (project_name, exc))
    except Exception as exc:
        test.fail("'%s' 빌드 중 예외가 발생했습니다: %s" % (project_name, exc))
    finally:
        # 다음 프로젝트를 깨끗한 상태에서 시작하기 위해 AUT 를 종료합니다.
        stop_application()
        test.endSection()
    return result


def report_summary(projects, succeeded, failed):
    """전체 빌드 결과를 요약해 로그와 최종 판정으로 남깁니다."""
    test.startSection("전체 빌드 결과 요약")
    test.log("대상 %d개 / 성공 %d개 / 실패 %d개"
             % (len(projects), len(succeeded), len(failed)))
    if succeeded:
        test.log("성공: %s" % ", ".join(succeeded))
    if failed:
        test.fail("빌드 실패 %d개: %s" % (len(failed), ", ".join(failed)))
    else:
        test.passes("모든 프로젝트(%d개)가 에러 없이 빌드되었습니다." % len(projects))
    test.endSection()

# ---------------------------------------------------------------------------
# AUT 종료
# ---------------------------------------------------------------------------

def stop_application(timeout=APP_EXIT_TIMEOUT_SEC):
    """실행 중인 MuLiN Creator 를 종료합니다.

    ``ApplicationContext.detach()`` 는 정상 종료를 시도하고, 그래도 살아있으면 강제로
    종료합니다. 따라서 저장 확인 다이얼로그가 떠 있어도 정리됩니다.

    :returns: 종료가 확인되면 ``True``, 아니면 ``False``.
    """
    try:
        ctx = currentApplicationContext()
    except Exception as exc:
        test.log("종료할 AUT 컨텍스트가 없습니다. (%s)" % exc)
        return False

    if ctx is None:
        test.log("종료할 AUT 컨텍스트가 없습니다.")
        return False

    try:
        ctx.detach()
    except Exception as exc:
        test.warning("AUT 종료 중 예외가 발생했습니다: %s" % exc)

    waited = 0.0
    while waited < timeout:
        try:
            if not ctx.isRunning:
                test.log("MuLiN Creator 종료 완료")
                return True
        except Exception:
            # detach 후 컨텍스트 접근이 불가해지면 종료된 것으로 간주합니다.
            test.log("MuLiN Creator 종료 완료")
            return True
        snooze(0.5)
        waited += 0.5

    test.warning("MuLiN Creator 가 %.1f초 내에 종료되지 않았습니다." % timeout)
    return False
