# 빌드 유틸리티 사용 가이드

## 개요

`build_utils.py`는 MuLiN 프로젝트의 빌드 관련 작업을 재사용 가능하게 구성한 라이브러리입니다. 복구 다이얼로그 처리, 빌드 실행, 빌드 결과 검증 등의 기능을 제공합니다.

## 제공 함수

### 1. `close_recovery_dialog(timeout=3000)`

복구 다이얼로그가 나타나면 자동으로 닫습니다.

**파라미터:**
- `timeout` (int): 다이얼로그를 기다리는 시간 (밀리초, 기본값: 3000)

**반환값:** 
- `bool`: 다이얼로그를 찾아 닫으면 True, 나타나지 않으면 False

**사용 예시:**
```python
from build_utils import close_recovery_dialog

# 기본 타임아웃 (3초)
close_recovery_dialog()

# 커스텀 타임아웃 (1초)
close_recovery_dialog(1000)
```

---

### 2. `build_project(menu_bar_name, menu_name, submenu_name, wait_time=0.5)`

메뉴를 통해 프로젝트 빌드를 실행합니다.

**파라미터:**
- `menu_bar_name` (str): 메뉴바의 names 객체 속성
- `menu_name` (str): 메뉴 이름 (예: "프로젝트")
- `submenu_name` (str): 서브메뉴 이름 (예: "빌드")
- `wait_time` (float): 빌드 명령 후 대기 시간 (초, 기본값: 0.5)

**사용 예시:**
```python
from build_utils import build_project
import names

build_project(
    names.muLiN_Creator_Documents_mdp_QMenuBar,
    "프로젝트",
    "빌드",
    wait_time=0.5
)
```

---

### 3. `check_build_result(error_button_name, timeout=10000, expected_error_count=0)`

빌드 완료를 대기하고 결과를 검증합니다.

**파라미터:**
- `error_button_name` (str): 에러 버튼의 names 객체 속성
- `timeout` (int): 빌드 완료를 기다리는 시간 (밀리초, 기본값: 10000)
- `expected_error_count` (int): 예상되는 에러 개수 (기본값: 0)

**반환값:**
- `dict`: 빌드 결과 정보
  ```python
  {
      'success': bool,           # 성공 여부
      'error_count': int,        # 실제 에러 개수
      'button_text': str         # 버튼 텍스트 (예: "에러 (0)")
  }
  ```

**사용 예시:**
```python
from build_utils import check_build_result
import names

result = check_build_result(
    names.tabBuild_btnError_QToolButton_2,
    timeout=10000,
    expected_error_count=0
)

if result['success']:
    print(f"빌드 성공: {result['button_text']}")
else:
    print(f"빌드 실패: {result['button_text']}")
```

---

### 4. `execute_build_with_validation(menu_bar_name, menu_name, submenu_name, error_button_name, expected_error_count=0, recovery_timeout=3000, build_timeout=10000, wait_after_build=0.5)` ⭐ **권장**

빌드 실행부터 검증까지 모든 단계를 한 번에 처리합니다. **대부분의 경우 이 함수를 사용하시면 됩니다.**

**파라미터:**
- `menu_bar_name` (str): 메뉴바의 names 객체 속성
- `menu_name` (str): 메뉴 이름
- `submenu_name` (str): 서브메뉴 이름
- `error_button_name` (str): 에러 버튼의 names 객체 속성
- `expected_error_count` (int): 예상 에러 개수 (기본값: 0)
- `recovery_timeout` (int): 복구 다이얼로그 대기 시간 (밀리초, 기본값: 3000)
- `build_timeout` (int): 빌드 완료 대기 시간 (밀리초, 기본값: 10000)
- `wait_after_build` (float): 빌드 후 대기 시간 (초, 기본값: 0.5)

**반환값:** 빌드 결과 딕셔너리

**사용 예시:**
```python
from build_utils import execute_build_with_validation
import names

result = execute_build_with_validation(
    menu_bar_name=names.muLiN_Creator_Documents_mdp_QMenuBar,
    menu_name="프로젝트",
    submenu_name="빌드",
    error_button_name=names.tabBuild_btnError_QToolButton_2,
    expected_error_count=0
)
```

---

## 실제 사용 예시

### 기본 테스트 구조

```python
# -*- coding: utf-8 -*-

import sys
import os

# shared/scripts 경로 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../shared/scripts'))

import names
from build_utils import execute_build_with_validation

def main():
    # 1. 앱 시작
    startApplication('"MuLiN Creator"')
    waitForObject(names.muLiN_Creator_MinervaD_MvMainWindow, 15000)
    
    # 2. 프로젝트 열기 (기존 코드)
    activateItem(waitForObjectItem(names.muLiN_Creator_QMenuBar, "파일"))
    activateItem(waitForObjectItem(names.muLiN_Creator_QMenu_3, "프로젝트 열기"))
    
    # ... (프로젝트 로드 코드)
    
    # 3. 빌드 실행 및 검증 (한 줄로!)
    execute_build_with_validation(
        names.muLiN_Creator_Documents_mdp_QMenuBar,
        "프로젝트",
        "빌드",
        names.tabBuild_btnError_QToolButton_2,
        expected_error_count=0
    )
```

---

## 주요 개선사항

✅ **코드 중복 제거**: 복구 다이얼로그 처리 코드 중복 제거  
✅ **매직 넘버 제거**: 타임아웃 값들을 파라미터화  
✅ **가독성 향상**: 복잡한 로직을 함수로 추상화  
✅ **재사용성 증대**: 다른 테스트 케이스에서 쉽게 재사용 가능  
✅ **유지보수 용이**: 빌드 로직 수정 시 한 곳만 수정하면 됨  

---

## 다른 테스트 케이스에 적용하기

`tst_Project002_case`, `tst_Project003_case` 등 다른 테스트 디렉토리의 `test.py` 파일도 동일한 방식으로 수정하면 됩니다:

1. import 문 추가
2. `execute_build_with_validation()` 함수 호출로 변경
3. 파라미터는 각 테스트에 맞게 조정

예시 (Project002):
```python
from build_utils import execute_build_with_validation

execute_build_with_validation(
    names.muLiN_Creator_Documents_mdp_QMenuBar,
    "프로젝트",
    "빌드",
    names.tabBuild_btnError_QToolButton_2,  # 필요시 다른 이름으로 변경
    expected_error_count=0
)
```
