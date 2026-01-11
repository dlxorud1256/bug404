import pytest
from src.utils.object_utils import generate_bucket_name, generate_user_name
from src.pages.base_page import BasePage
from src.pages.object_page import DashPage, BucketPage, UserPage
from src.utils.locator import OSLocator as OSL

# TC-OS-E2E-001
def test_object_storage_menu_click(e2e_driver):
    page = BasePage(e2e_driver)
    page.click_stale_safe(OSL.OS_MENU)
    assert page.wait_visibility_element(OSL.OS_DASHBOARD_TAB), "오브젝트 스토리지 메뉴 클릭 실패"

# TC-OS-E2E-002
def test_dashboard_menu_click(e2e_driver):
    DashPage(e2e_driver).go_dashbord()
    page = BasePage(e2e_driver)
    assert page.wait_visibility_element(OSL.OS_DASH_TITLE_OVERVIEW), "대시보드 메뉴 클릭 실패"

# TC-OS-E2E-003
def test_dashboard_fast(e2e_driver):
    DashPage(e2e_driver).go_dashbord()
    page = BasePage(e2e_driver)

    page.wait_clickable(OSL.OS_DASH_BTN_CREATE).click()
    assert page.wait_visibility_element(OSL.OS_BUCKET_CREATE_TITLE), "대시보드: 생성 버튼 클릭 실패"
    e2e_driver.back()
    
    page.wait_clickable(OSL.OS_DASH_BTN_BUCKET_MANAGE).click()
    assert page.wait_visibility_element(OSL.OS_BUCKET_TITLE), "대시보드: 버킷 관리 버튼 클릭 실패"
    e2e_driver.back()
    
    page.wait_clickable(OSL.OS_DASH_BTN_USER_MANAGE).click()
    assert page.wait_visibility_element(OSL.OS_USERS_TITLE), "대시보드: 사용자 관리 버튼 클릭 실패"
    e2e_driver.back()

# TC-OS-E2E-004
def test_dashboard_resource(e2e_driver):
    page = BasePage(e2e_driver)

    page.wait_clickable(OSL.LABEL_ACTIVE_BUCKET).click()
    assert page.wait_visibility_element(OSL.OS_BUCKET_TITLE), "대시보드: 활성버킷 클릭 실패"
    e2e_driver.back()
    
    page.wait_clickable(OSL.LABEL_USER).click()
    assert page.wait_visibility_element(OSL.OS_USERS_TITLE), "대시보드: 사용자 클릭 실패"
    e2e_driver.back()
    
    page.wait_clickable(OSL.LABEL_TOTAL_USAGE).click()
    assert page.wait_visibility_element(OSL.OS_BUCKET_TITLE), "대시보드: 총 사용량 클릭 실패"
    e2e_driver.back()

# TC-OS-E2E-005
def test_bucket_menu_click(e2e_driver):
    page = BasePage(e2e_driver)

    page.click_stale_safe(OSL.OS_MENU)
    page.click_stale_safe(OSL.OS_BUCKET_TAB)

    assert page.wait_visibility_element(OSL.OS_BUCKET_TITLE), "버킷 메뉴 클릭 실패"

# TC-OS-E2E-006, TC-OS-E2E-007
def test_bucket_create_cancel(e2e_driver):
    page = BucketPage(e2e_driver).create_wait_loaded()
    page.click_cancel()
    assert page.wait_visibility_element(OSL.OS_BUCKET_TITLE), "버킷 생성 취소 실패"

# TC-OS-E2E-008
@pytest.mark.parametrize(
    "bucket_name, expected_msg_substr",
    [
        ("한글버킷", "소문자"),
        ("ABC", "소문자"),
        ("abc_", "하이픈"),
    ],
    ids=["korean", "uppercase", "underscore"],
)
def test_bucket_name_validation_parametrize(e2e_driver, bucket_name, expected_msg_substr):
    page = BucketPage(e2e_driver).create_wait_loaded()

    page.set_bucket_name(bucket_name)
    page.set_zone_first_valid()
    page.set_size_gib(10)

    created = page.submit_or_cancel_if_failed(timeout=6, cancel_on_fail=False)

    assert created is False, "버킷 생성 유효성 검사: invalid 생성 성공하면 안됨"

    page.wait_bucket_name_invalid(timeout=5)
    msg = page.get_bucket_name_helper_text()
    assert msg, "에러 helperText가 비어있음"
    assert expected_msg_substr in msg, f"에러 문구 불일치: {msg}"

    page.click_cancel()
    assert page.wait_visibility_element(OSL.OS_BUCKET_TITLE), "실패 후 리스트 복귀 실패"

# TC-OS-E2E-009
def test_bucket_create(e2e_driver):
    bucket_name = "e2e-" + generate_bucket_name()
    page = BucketPage(e2e_driver).create_wait_loaded()
    page.bucket_create_form(
        name=bucket_name,
        description="팀4 e2e 자동화 테스트 버킷",
    )
    page.click_submit()

    detail = BucketPage(e2e_driver).detail_wait_loaded()
    assert detail.get_title_bucket_name() == bucket_name, "생성한 버킷과 동일한 이름이 아님"

# TC-OS-E2E-011
def test_bucket_id_name_copy(e2e_driver):
    page = BucketPage(e2e_driver)

    page.wait_clickable(OSL.BUCKET_BTN_COPY_ID).click()
    toast = page.wait_visibility_element(OSL.COPIED_TOAST)
    assert "복사되었습니다" in toast.text, "버킷 id 복사 실패"

    page.wait_clickable(OSL.BUCKET_BTN_COPY_BUCKETNAME).click()
    toast = page.wait_visibility_element(OSL.COPIED_TOAST)
    assert "복사되었습니다" in toast.text, "버킷 name 복사 실패"

# TC-OS-E2E-012
def test_grant_create_cancel(e2e_driver):
    page = BucketPage(e2e_driver)
    page.click_add_permission()
    page.wait_clickable(OSL.DIALOG_BTN_CANCEL).click()
    assert page.wait_invisibility_element(OSL.DIALOG_BTN_CANCEL), "권한 생성 취소 실패"

# TC-OS-E2E-013
def test_grant_create(e2e_driver):
    page = BucketPage(e2e_driver)
    page.click_add_permission()
    page.select_first_user_in_dialog()
    page.wait_dialog_create_enabled()
    page.click_dialog_create()
    msg = page.wait_visibility_element(OSL.SNACKBAR_MESSAGE).text
    assert msg, "권한 생성 후 생성 안내 메시지 미제공"

# TC-OS-E2E-014
def test_grant_access_key_copy(e2e_driver):
    page = BucketPage(e2e_driver)
    page.click_stale_safe(OSL.GRANT_ACCESS_KEY_BTN)
    
    page.wait_clickable(OSL.ACCESS_KEY_COPY).click()
    toast = page.wait_visibility_element(OSL.COPIED_TOAST)
    assert toast, "액세스 키 복사 토스트 미노출"

    page.wait_clickable(OSL.SECRET_KEY_COPY).click()
    toast = page.wait_visibility_element(OSL.COPIED_TOAST)
    assert toast, "시크릿 키 복사 토스트 미노출"

    page.wait_clickable(OSL.SECRET_KEY_CLOSE).click()
    assert page.wait_invisibility_element(OSL.SECRET_KEY_CLOSE), "액세스 키 다이얼로그 닫기 실패"

# TC-OS-E2E-015
def test_grant_delete_cancel(e2e_driver):
    page = BucketPage(e2e_driver)
    page.click_stale_safe(OSL.GRANT_DELETE_BTN)
    page.wait_clickable(OSL.GRANT_DELETE_DIALOG_CANCEL_BTN).click()
    assert page.wait_visibility_element(OSL.GRANT_DELETE_BTN), "버킷 권한 삭제 취소 실패"

# TC-OS-E2E-016
def test_grant_delete(e2e_driver):
    page = BucketPage(e2e_driver)
    page.click_stale_safe(OSL.GRANT_DELETE_BTN)
    page.wait_clickable(OSL.GRANT_DELETE_DIALOG_DELETE_BTN).click()
    assert page.wait_visibility_element(OSL.GRANT_DELETE_BTN), "버킷 사용자 권한 삭제 실패"

# TC-OS-E2E-017, TC-OS-E2E-018
def test_bucket_edit_cancel(e2e_driver):
    page = BucketPage(e2e_driver)
    page.click_edit()
    page.click_stale_safe(OSL.BUCKET_EDIT_BTN_CANCEL)
    assert page.wait_visibility_element(OSL.OS_BUCKET_DETAIL_BTN_EDIT), "버킷 수정 취소 실패"

# TC-OS-E2E-019
def test_bucket_edit(e2e_driver):
    page = BucketPage(e2e_driver)
    page.click_edit()
    
    edit_bucket_name = "e2e-edit" + generate_bucket_name()
    page.edit_set_name(edit_bucket_name)
    assert page.edit_save_enabled(), "버킷 수정 > 이름 편집 후 저장 버튼 활성화되지 않음"

    page.edit_click_save()
    title = page.get_title_bucket_name()
    assert title == edit_bucket_name, f"저장 후 상세 타이틀 불일치: {title} != {edit_bucket_name}"

# TC-OS-E2E-020
def test_bucket_delete_cancel(e2e_driver):
    page = BucketPage(e2e_driver)
    page.click_stale_safe(OSL.OS_BUCKET_DETAIL_BTN_DELETE)
    page.wait_clickable(OSL.BUCKET_DELETE_CANCEL_BTN).click()
    assert page.wait_visibility_element(OSL.BUCKET_DELETE_DELETE_BTN), "버킷 삭제 레이어 닫기 실패"

# TC-OS-E2E-021
def test_bucket_delete(e2e_driver):
    page = BucketPage(e2e_driver)
    page.click_stale_safe(OSL.OS_BUCKET_DETAIL_BTN_DELETE)
    ok = page.confirm_bucket_delete_with_retry(retries=2, list_timeout=6)
    assert ok, "버킷 삭제 실패"

# TC-OS-E2E-022
def test_user_menu_click(e2e_driver):
    page = UserPage(e2e_driver)
    page.user_menu_click()
    assert page.wait_visibility_element(OSL.OS_USERS_TITLE), "사용자 메뉴 클릭 실패"

# TC-OS-E2E-023, TC-OS-E2E-024
def test_user_create_cancel(e2e_driver):
    page = UserPage(e2e_driver).user_create_wait_loaded()
    page.wait_clickable(OSL.CREATE_USER_CANCEL_BTN).click()
    assert page.wait_visibility_element(OSL.CREATE_USER_BTN), "사용자 생성 취소 후 '사용자 생성' 버튼 미노출"
    assert page.wait_visibility_element(OSL.USERS_TABLE), "사용자 생성 취소 후 사용자 테이블 미노출"

# TC-OS-E2E-026
def test_user_create(e2e_driver):
    user_name = "e2e-" + generate_user_name()
    page = UserPage(e2e_driver)
    page.wait_clickable(OSL.OS_USER_TAB).click()
    page.user_create_wait_loaded()

    page.user_create_form(
        name=user_name,
        tags={'{"team":"team4"}'}
    )
    page.wait_clickable(OSL.CREATE_USER_CREATE_BTN).click()

    assert page.wait_visibility_element(OSL.CREATE_USER_BTN), "사용자 생성 후 리스트 화면 미제공"

# TC-OS-E2E-027, TC-OS-E2E-028
def test_user_grant_create_cancel(e2e_driver):
    page = UserPage(e2e_driver)
    page.open_latest_user_detail_by_keyword("user4")
    page.user_grant_click_add()
    page.wait_clickable(OSL.USER_PERMISSION_CANCEL_BTN).click()
    assert page.wait_invisibility_element(OSL.DIALOG_BTN_CANCEL), "사용자 권한 생성 취소 실패"

# TC-OS-E2E-029
def test_user_grant_create(e2e_driver):
    page = UserPage(e2e_driver)
    page.user_grant_click_add()
    page.select_first_object_storage_and_permission()
    page.user_grant_submit_with_retry()
    assert page.wait_visibility_element(OSL.GRANT_DELETE_BTN), "사용자 권한 생성 실패"

# TC-OS-E2E-030
def test_user_grant_edit_cancel(e2e_driver):
    page = UserPage(e2e_driver)
    page.wait_clickable(OSL.USER_GRANT_EDIT_BTN).click()
    page.wait_clickable(OSL.USER_PERMISSION_CANCEL_BTN).click()
    assert page.wait_invisibility_element(OSL.DIALOG_BTN_CANCEL), "사용자 권한 수정 취소 실패"

# TC-OS-E2E-031
def test_user_grant_edit(e2e_driver):
    page = UserPage(e2e_driver)
    page.wait_clickable(OSL.USER_GRANT_EDIT_BTN).click()
    page.user_grant_edit_change_permission_to_second()
    assert page.wait_invisibility_element(OSL.GRANT_DIALOG), "사용자 권한 수정 실패"

# TC-OS-E2E-032
def test_user_grant_delete_cancel(e2e_driver):
    page = UserPage(e2e_driver)
    page.click_stale_safe(OSL.GRANT_DELETE_BTN)
    page.wait_clickable(OSL.GRANT_DELETE_DIALOG_CANCEL_BTN).click()
    assert page.wait_visibility_element(OSL.GRANT_DELETE_BTN), "사용자 권한 삭제 취소 실패"

# TC-OS-E2E-033
def test_user_grant_delete(e2e_driver):
    page = UserPage(e2e_driver)
    page.click_stale_safe(OSL.GRANT_DELETE_BTN)
    page.wait_clickable(OSL.GRANT_DELETE_DIALOG_DELETE_BTN).click()
    assert page.wait_visibility_element(OSL.GRANT_DELETE_BTN), "사용자 권한 삭제 실패"

# TC-OS-E2E-034, TC-OS-E2E-035
def test_user_edit_cancel(e2e_driver):
    page = UserPage(e2e_driver)
    page.user_edit_click()
    page.wait_clickable(OSL.USER_EDIT_CANCEL_BTN).click()
    assert page.wait_visibility_element(OSL.USER_DETAIL_BTN_EDIT), "사용자 수정 취소 실패"

# TC-OS-E2E-036
def test_user_edit(e2e_driver):
    user_edit_name = "e2e-edit-" + generate_user_name()
    page = UserPage(e2e_driver)
    page.user_edit_click()
    page.set_user_name(user_edit_name)
    page.wait_clickable(OSL.BUCKET_EDIT_BTN_SAVE).click()
    assert page.wait_invisibility_element(OSL.USER_EDIT_CANCEL_BTN), "사용자 수정 저장 실패"

# TC-OS-E2E-037
def test_user_delete_cancel(e2e_driver):
    page = UserPage(e2e_driver)
    page.wait_clickable(OSL.USER_DETAIL_BTN_DELETE).click()
    page.wait_clickable(OSL.USER_PERMISSION_CANCEL_BTN).click()
    assert page.wait_invisibility_element(OSL.USER_PERMISSION_CANCEL_BTN), "사용자 삭제 취소 실패"

# TC-OS-E2E-038
def test_user_delete(e2e_driver):
    page = UserPage(e2e_driver)
    page.wait_clickable(OSL.USER_DETAIL_BTN_DELETE).click()
    page.wait_clickable(OSL.USER_DELETE_DELETE_BTN).click()
    assert page.wait_invisibility_element(OSL.USER_DELETE_DELETE_BTN), "사용자 삭제 실패"
