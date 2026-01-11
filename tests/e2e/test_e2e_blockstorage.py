from src.pages.block_storage_page import BlockStoragePage
from src.utils.locator import BlockStorageLocator as BSL
import pytest
import uuid

@pytest.fixture
def create_page_ready(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_block_storage_tab()
    page.click_block_storage_create()
    return page

@pytest.fixture
def edit_page_ready(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_block_storage_tab()
    page.click_non_first_row()
    page.click_edit_button()
    return page

random_name = f"{uuid.uuid8().hex[:8]}"

def test_block_storage_menu_click(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    
    assert page.wait_visibility_element(BSL.BS_BLOCKSTORAGE_TAB, timeout=60)
    assert page.wait_visibility_element(BSL.BS_SNAPSHOT_TAB, timeout=60)
    assert page.wait_visibility_element(BSL.BS_SCHEDULER_TAB, timeout=60)
    
def test_block_storage_list_check(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_block_storage_tab()
    
    assert page.check_block_storage_list_page_element()
    
def test_block_storage_create_check(create_page_ready):
    page = create_page_ready
    assert page.check_block_storage_create_element()
    
def test_block_storage_create(create_page_ready):
    page = create_page_ready
    target_name = page.get_name_input_value()
    page.update_size_value("30")
    page.click_create_button()
    
    assert page.response_create_block_storage(target_name), f"목록에서 {target_name}을 찾을 수 없습니다."

def test_block_storage_img_create(create_page_ready):
    page = create_page_ready
    target_name = page.get_name_input_value()
    page.select_disk_type_image()
    page.click_create_button()
    
    assert page.response_create_block_storage(target_name), f"목록에서 {target_name}을 찾을 수 없습니다."
    
def test_block_storage_snapshot_create(create_page_ready):
    page = create_page_ready
    target_name = page.get_name_input_value()
    page.select_disk_type_snapshot()
    page.click_create_button()
    
    assert page.response_create_block_storage(target_name), f"목록에서 {target_name}을 찾을 수 없습니다."

def test_block_storage_duplicate_name(create_page_ready):
    page = create_page_ready
    page.update_name_value("team4-blockstorage")
    page.click_create_button()
    
    assert not page.response_create_block_storage("team4-blockstorage"), "중복 이름으로 생성 되었습니다."
    
def test_missing_block_storage_field(create_page_ready):
    page = create_page_ready
    page.update_name_value("")
    
    assert page.check_create_button_disabled(), "이름을 입력하지 않았는데 생성 버튼이 클릭 가능한 상태입니다."
    
def test_missing_block_storage_field(create_page_ready):
    page = create_page_ready
    page.update_name_value("")
    
    assert page.check_create_button_disabled(), "이름을 입력하지 않았는데 생성 버튼이 클릭 가능한 상태입니다."
    
def test_block_storage_create_cancel(create_page_ready):
    page = create_page_ready
    page.click_cancel_button()
    
    assert "new" not in page.current_url(), f"취소 후에도 생성페이지에 있습니다: {page.current_url}"
    
def test_block_storage_edit_cancel(edit_page_ready):
    page = edit_page_ready
    page.click_cancel_button()
    
    assert "edit" not in page.current_url(), f"취소 후에도 수정페이지에 있습니다: {page.current_url}"
    
def test_block_storage_delete_cancel(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_block_storage_tab()
    page.click_non_first_row()
    before_url = e2e_driver.current_url
    page.click_delete_button()
    page.click_cancel_button()
    after_url = e2e_driver.current_url
    assert before_url == after_url, f"URL이 변경되었습니다. 이전: {before_url}, 이후: {after_url}"
    
def test_block_storage_detail_page_check(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_block_storage_tab()
    page.click_first_row()

    assert page.check_block_storage_detail_page_element(), "삭제, 수정, 스냅샷 생성버튼 노출되지 않음"
    
def test_block_storage_chain_snapshot(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_block_storage_tab()
    page.click_first_row()
    
    id = page.get_first_snapshot_id()
    page.click_first_row()
    
    assert id in page.current_url(), f"url에 id가 포함되어있지 않습니다: {page.current_url}"
    
def test_block_storage_chain_vm(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_block_storage_tab()
    page.click_first_row()
    
    href = page.get_vm_id()
    page.click_vm_link()
    
    assert href in page.current_url(), f"url에 href 내용이 포함되어있지 않습니다: {page.current_url}"
    
def test_block_storage_detail_page_snapshot_create(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_block_storage_tab()
    page.click_first_row()

    page.click_snapshot_create()
    name = page.get_snapshot_name_input_value()
    page.click_create_button()
    assert page.table_list(name)
    
def test_block_storage_edit_element_check(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_block_storage_tab()
    page.click_first_row()
    page.click_edit_button()

    assert page.check_block_storage_edit_element()
    
def test_block_storage_edit(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_block_storage_tab()
    page.click_non_first_row()
    page.click_edit_button()
    name = page.update_name_value(random_name)
    page.click_edit_save_button()
    actual_name = page.get_name_input_value()
    # page.select_first_block_storage()
    assert actual_name == name, f"수정시 입력한 이름과 불일치합니다. 기대값: {name}, 실제값: {actual_name}"
    
def test_block_storage_delete(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_block_storage_tab()
    page.click_non_first_row()
    name = page.get_detail_name_text()
    page.click_delete_button()
    page.click_modal_delete_button()
    alert_msg = page.get_alert_message()
    
    if alert_msg:
        assert "연결된 가상머신이 있습니다" in alert_msg
    else:
        assert page.table_list(name) != name, f"삭제 알럿도 없고 목록에 {name}이 남아있습니다."

#스냅샷
def test_snapshot_list_check(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_snapshot_tab()
    
    assert page.check_snapshot_list_page_element()
    
def test_snapshot_create_check(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_snapshot_tab()
    page.click_snapshot_create()
    
    assert page.check_snapshot_create_element()
    
def test_snapshot_create(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_snapshot_tab()
    page.click_snapshot_create()
    
    target_name = page.get_name_input_value()
    page.select_first_block_storage()
    page.click_create_button()
    
    assert page.response_create_block_storage(target_name), f"목록에서 {target_name}을 찾을 수 없습니다."
    
def test_snapshot_duplicate_name(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_snapshot_tab()
    page.click_snapshot_create()

    page.update_name_value("snapshot-a03411")
    page.select_first_block_storage()
    page.click_create_button()
    
    assert not page.response_create_block_storage("snapshot-a03411"), "중복 이름으로 생성 되었습니다."
    
def test_missing_snapshot_field(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_snapshot_tab()
    page.click_snapshot_create()

    page.update_name_value("")
    
    assert page.wait_url_contains("snapshot/new"), "생성 페이지에 머물러야 합니다."
    
def test_snapshot_create_cancel(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_snapshot_tab()
    page.click_snapshot_create()

    page.click_cancel_button()
    assert "new" not in page.current_url(), f"취소 후에도 생성페이지에 있습니다: {page.current_url}"

def test_snapshot_edit_cancel(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_snapshot_tab()
    page.click_non_first_row()
    page.click_edit_button()
    page.click_cancel_button()
    assert "edit" not in page.current_url(), f"취소 후에도 수정페이지에 있습니다: {page.current_url}"

def test_snapshot_delete_cancel(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_snapshot_tab()
    page.click_non_first_row()
    before_url = e2e_driver.current_url
    page.click_delete_button()
    page.click_cancel_button()
    after_url = e2e_driver.current_url
    assert before_url == after_url, f"URL이 변경되었습니다. 이전: {before_url}, 이후: {after_url}"
    
def test_snapshot_detail_page_check(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_snapshot_tab()
    page.click_first_row()

    assert page.check_detail_page_element(), "삭제, 수정버튼 노출되지 않음"
    
def test_snapshot_chain_block_storage(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_snapshot_tab()
    page.click_first_row()
    
    href = page.get_target_href()
    page.click_link_element()
    
    assert href in page.current_url(), f"url에 href 내용이 포함되어있지 않습니다: {page.current_url}"

def test_snapshot_edit_element_check(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_snapshot_tab()
    page.click_first_row()
    page.click_edit_button()

    assert page.check_snapshot_edit_element()
    
def test_snapshot_edit(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_snapshot_tab()
    page.click_non_first_row()
    page.click_edit_button()
    name = page.update_name_value(random_name)
    page.click_edit_save_button()
    actual_name = page.get_name_input_value()
    assert actual_name == name, f"수정시 입력한 이름과 불일치합니다. 기대값: {name}, 실제값: {actual_name}"
    
def test_snapshot_delete(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_snapshot_tab()
    page.click_non_first_row()
    name = page.get_detail_name_text()
    page.click_delete_button()
    page.click_modal_delete_button()
    
    assert page.table_list(name) != name, "삭제 실패하였습니다."
    
#스케줄러
def test_scheduler_list_check(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_scheduler_tab()
    
    assert page.check_scheduler_list_page_element()
    
def test_scheduler_create_check(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_scheduler_tab()
    page.click_scheduler_create()
    
    assert page.check_scheduler_create_element()
    
def test_scheduler_create(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_scheduler_tab()
    page.click_scheduler_create()
    
    target_name = page.get_name_input_value()
    page.select_first_block_storage()
    page.click_create_button()
    
    assert page.response_create_block_storage(target_name), f"목록에서 {target_name}을 찾을 수 없습니다."

def test_scheduler_duplicate_name(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_scheduler_tab()
    page.click_scheduler_create()
    
    page.update_name_value("team4-scheduler")
    page.select_first_block_storage()
    page.click_create_button()
    
    assert not page.response_create_block_storage("team4-scheduler"), "중복 이름으로 생성 되었습니다."
    
def test_missing_scheduler_field(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_scheduler_tab()
    page.click_scheduler_create()

    page.update_name_value("")
    page.click_create_button()
    
    assert page.wait_url_contains("snapshot-scheduler/new"), "생성 페이지에 머물러야 합니다."
    
def test_scheduler_cron(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_scheduler_tab()
    page.click_scheduler_create()
    
    page.select_first_block_storage()
    page.update_cron_value()
    page.click_create_button()
    
    expected_msg = "유효하지 않은 Cron 표현식입니다"
    actual_msg = page.get_cron_error_text()
    
    assert expected_msg in actual_msg, f"에러 문구가 일치하지 않습니다. 실제 문구: {actual_msg}"

def test_scheduler_create_cancel(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_scheduler_tab()
    page.click_scheduler_create()

    page.click_cancel_button()
    assert "new" not in page.current_url(), f"취소 후에도 생성페이지에 있습니다: {page.current_url}"

def test_scheduler_edit_cancel(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_scheduler_tab()
    page.click_non_first_row()
    page.click_edit_button()
    page.click_cancel_button()
    assert "edit" not in page.current_url(), f"취소 후에도 수정페이지에 있습니다: {page.current_url}"
    
def test_snapshot_detail_page_check(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_scheduler_tab()
    page.click_first_row()

    assert page.check_detail_page_element(), "삭제, 수정버튼 노출되지 않음"
    
def test_scheduler_chain_block_storage(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_scheduler_tab()
    page.click_first_row()
    
    href = page.get_target_href()
    page.click_link_element()
    
    assert href in page.current_url(), f"url에 href 내용이 포함되어있지 않습니다: {page.current_url}"
    
def test_scheduler_edit_element_check(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_scheduler_tab()
    page.click_first_row()
    page.click_edit_button()

    assert page.check_scheduler_edit_element()
    
def test_scheduler_edit(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_scheduler_tab()
    page.click_non_first_row()
    page.click_edit_button()
    name = page.update_name_value(random_name)
    max_snapshot = page.update_snapshot_value("10")
    page.click_edit_save_button()
    actual_name = page.get_name_input_value()
    actual_max_snapshot = page.get_max_snapshot_input_value()
    assert actual_name == name and actual_max_snapshot == max_snapshot, f"수정시 입력한 이름과 불일치합니다. 기대값: {name}, 실제값: {actual_name}"
    
def test_scheduler_delete(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_scheduler_tab()
    page.click_non_first_row()
    name = page.get_detail_name_text()
    page.click_delete_button()
    page.click_modal_delete_button()
    
    assert page.wait_table_not_contains(name, timeout=30), f"삭제 실패: 목록에 {name}이 여전히 존재합니다."

def test_scheduler_delete_cancel(e2e_driver):
    page = BlockStoragePage(e2e_driver)
    page.click_block_storage_menu()
    page.click_scheduler_tab()
    page.click_non_first_row()
    before_url = e2e_driver.current_url
    page.click_delete_button()
    page.click_cancel_button()
    after_url = e2e_driver.current_url
    assert before_url == after_url, f"URL이 변경되었습니다. 이전: {before_url}, 이후: {after_url}"
