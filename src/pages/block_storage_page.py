from src.pages.base_page import BasePage
import time
from src.utils.locator import BlockStorageLocator as L
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import logging
logger = logging.getLogger(__name__)

class BlockStoragePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    # 공통 예외 처리
    def handle_exception(self, e, action_desc):
        error_type = type(e).__name__          # 예: TimeoutException
        original_msg = str(e)                  # 원래 에러 메시지
        self.driver.save_screenshot(f"fail_{action_desc}.png") # 화면 캡처 추가

        raise Exception(
            f"[FAIL] {action_desc} 실패 | "
            f"원인: {error_type} | "
            f"원본 메시지: {original_msg}"
        ) from e
        
    def current_url(self):
        return self.driver.current_url
        
    def click_block_storage_menu(self):
        self.wait_clickable(L.BS_MENU).click()
        logger.info("블록스토리지 메뉴 클릭 완료")
    
    def click_block_storage_tab(self):
        self.wait_clickable(L.BS_BLOCKSTORAGE_TAB).click()
        logger.info("블록스토리지 탭 클릭 완료")
            
    def check_block_storage_list_page_element(self):
        try:
            self.wait_visibility_element(L.BS_NAME_COLUMN)
            self.wait_visibility_element(L.BS_STATUS_COLUMN)
            self.wait_visibility_element(L.BS_SIZE_COLUMN)
            self.wait_visibility_element(L.BS_DR_COLUMN)
            self.wait_visibility_element(L.BS_CREATED_AT_COLUMN)
            self.wait_visibility_element(L.BS_CREATE_BUTTON)
            return True
        except Exception as e:
            self.handle_exception(e, "블록스토리지 목록 화면 요소 체크")
            return False
        
    def click_block_storage_create(self):
        self.wait_clickable(L.BS_CREATE_BUTTON).click()
        logger.info("블록스토리지 생성 클릭 완료")
        
    def click_edit_button(self):
        self.wait_clickable(L.EDIT_BUTTON).click()
        logger.info("블록스토리지 수정 클릭 완료")
        
    def click_edit_save_button(self):
        self.wait_clickable(L.EDIT_BUTTON_SAVE).click()
        logger.info("수정 저장 클릭 완료")
        
    def click_delete_button(self):
        self.wait_clickable(L.DELETE_BUTTON).click()
        logger.info("삭제 클릭 완료")
        
    def click_modal_delete_button(self):
        self.wait_clickable(L.MODAL_DELETE_BUTTON).click()
        logger.info("삭제 클릭 완료")
        
    def check_block_storage_create_element(self):
        try:
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("이름"))
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("영역 ID"))
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("디스크 타입"))
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("크기 (GiB)"))
            self.wait_visibility_element(L.BS_DR_SWITCH)
            
            return True
        except Exception as e:
                self.handle_exception(e, "블록스토리지 생성 폼 요소 체크")
                return False
            
    def check_block_storage_edit_element(self):
        try:
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("이름"))
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("연결된 머신 ID"))
            return True
        except Exception as e:
                self.handle_exception(e, "블록스토리지 수정 폼 요소 체크")
                return False
            
    def check_block_storage_detail_page_element(self):
        try:
            self.wait_visibility_element(L.DELETE_BUTTON)
            self.wait_visibility_element(L.EDIT_BUTTON)
            self.wait_visibility_element(L.BS_SNAPSHOT_CREATE_BUTTON)
            return True
        except Exception as e:
            self.handle_exception(e, "블록스토리지 상세페이지 화면 요소 체크")
            return False
            
    def click_create_button(self):
        btn = self.wait_clickable(L.CREATE_BUTTON)
        btn.click()
        logger.info("생성버튼 클릭 완료")
        
    def click_cancel_button(self):
        btn = self.wait_clickable(L.CANCEL_BUTTON)
        btn.click()
        logger.info("취소버튼 클릭 완료")
    
    def update_size_value(self, new_size):
        size_field = self.wait_visibility_element(L.SIZE_INPUT)
        #트리플 클릭으로 전체 선택
        actions = ActionChains(self.driver)
        actions.click(size_field).click(size_field).click(size_field).perform()
        
        size_field.send_keys(Keys.BACKSPACE)
        size_field.send_keys(str(new_size))
        
        logger.info(f"사이즈 {new_size} 입력 완료")
        
    def update_name_value(self, name):
        size_field = self.wait_visibility_element(L.NAME_INPUT)
        
        #트리플 클릭으로 전체 선택
        actions = ActionChains(self.driver)
        actions.click(size_field).click(size_field).click(size_field).perform()
        
        size_field.send_keys(Keys.BACKSPACE)
        size_field.send_keys(str(name))
        
        logger.info(f"이름 {name} 입력 완료")
        
        return name
    
    def update_snapshot_value(self, max):
        size_field = self.wait_visibility_element(L.MAX_SNAPSHOT_INPUT)
        
        #트리플 클릭으로 전체 선택
        actions = ActionChains(self.driver)
        actions.click(size_field).click(size_field).click(size_field).perform()
        
        size_field.send_keys(Keys.BACKSPACE)
        size_field.send_keys(str(max))
        
        logger.info(f"최대 스냅샷 수 {max} 입력 완료")
        
        return max
        
    def update_cron_value(self):
        size_field = self.wait_visibility_element(L.CRON_INPUT)
        actions = ActionChains(self.driver)
        actions.click(size_field).click(size_field).click(size_field).perform()
        size_field.send_keys(Keys.BACKSPACE)
        size_field.send_keys("2 24 * * * * * *")
        
    def verify_size_error(self, expected_msg):
        el = self.wait_visibility_element(L.HELPER_TEXT)
        assert expected_msg in el.text, f"메시지 불일치! 실제: {el.text}"
        
    def update_disk_type_value(self, new_size):
        size_field = self.wait_visibility_element(L.SIZE_INPUT)
        # 2. OS에 맞는 Modifier Key 가져오기 (Command 또는 Control)
        select_key = self.select_all_key()
        size_field.send_keys(select_key + "a")
        size_field.send_keys(Keys.BACK_SPACE)
        size_field.send_keys(str(new_size))
        
    def get_name_input_value(self):
        element = self.wait_presence(L.NAME_INPUT)
        current_value = element.get_attribute("value")
        return current_value
    
    def get_max_snapshot_input_value(self):
        element = self.wait_presence(L.MAX_SNAPSHOT_INPUT)
        current_value = element.get_attribute("value")
        return current_value
    
    def get_detail_name_text(self):
        #상세 페이지의 이름 텍스트
        element = self.wait_visibility_element(L.DETAIL_NAME_VALUE)
        return element.text.strip()
    
    def select_disk_type_image(self):
            self.wait_clickable(L.DISK_TYPE_SELECT).click()
            self.wait_visibility_element(L.IMAGE_OPTION).click()
            
            logger.info("디스크 타입 변경 완료: data-value='image'")
            
    def select_disk_type_snapshot(self):
            self.wait_clickable(L.DISK_TYPE_SELECT).click()
            self.wait_visibility_element(L.SNAPSHOT_OPTION).click()
            logger.info("디스크 타입 변경 완료: data-value='snapshot'")
    
    def response_create_block_storage(self, expected_name):
        self.wait_url_contains("/block-storage")
        
        while True:
            # 현재 페이지에 생성한 블록스토리지와 동일한 이름이 있는지 확인
            rows = self.wait_all_presence(L.TABLE_ROWS)
            if any(expected_name in row.text for row in rows):
                return True
            
            # 다음 버튼
            next_btn = self.wait_presence(L.NEXT_PAGE_BUTTON)
            
            # 마지막 페이지면 종료, 아니면 클릭
            if next_btn.get_attribute("disabled") or "Mui-disabled" in next_btn.get_attribute("class"):
                break
            next_btn.click()
            time.sleep(1)
        return False
    
    def table_list(self, expected_name):
        while True:
            rows = self.wait_all_presence(L.TABLE_ROWS)
            if any(expected_name in row.text for row in rows):
                return True
            
    def wait_table_not_contains(self, expected_name: str, timeout: int = 20) -> bool:
        def _cond(d):
            try:
                rows = d.find_elements(*L.TABLE_ROWS)
                # 테이블이 아직 안그려졌을 수도 있으니 rows가 0이면 계속 기다림
                if not rows:
                    return False
                return all(expected_name not in r.text for r in rows)
            except StaleElementReferenceException:
                return False  # 리렌더 중이니 계속 대기

        WebDriverWait(self.driver, timeout).until(_cond)
        return True
    
    def check_create_button_disabled(self):
        btn = self.wait_presence(L.CREATE_BUTTON)
        # disabled 속성이 존재하거나 is_enabled가 False인 경우 True 반환
        return btn.get_attribute("disabled") is not None or not btn.is_enabled()
    
    def verify_size_helper_text(self, expected_text):
        try:
            el = self.wait_visibility_element(L.HELPER_TEXT)
            actual_text = el.text.strip()
    
            logger.info(f"유효성 메시지 확인 - 실제: '{actual_text}', 기대: '{expected_text}'")
        
            return expected_text in actual_text
        except Exception as e:
            self.handle_exception(e, "유효성 메세지 확인")
            return False
        
    def get_cron_error_text(self):
        el = self.wait_visibility_element(L.HELPER_TEXT)
        return el.text.strip()
        
    def click_first_row(self):
        td = self.wait_visibility_element(L.FIRST_ROW)
        actions = ActionChains(self.driver)
        actions.move_to_element(td).click().perform()
        logger.info("좌표 계산을 통한 물리적 클릭 완료")
        
    def click_non_first_row(self):
        td = self.wait_visibility_element(L.NON_FIRST_ROW)
        actions = ActionChains(self.driver)
        actions.move_to_element(td).click().perform()
        logger.info("좌표 계산을 통한 물리적 클릭 완료")
        
    def get_alert_message(self):
        # 에러 알럿 메시지가 나타나면 그 텍스트를 가져옵기
        # 알럿이 나타나지 않으면(정상 삭제 시) None을 반환
        try:
            element = self.wait_visibility_element(L.VM_CONNECTION_ALERT)
            
            if element:
                alert_text = element.text.strip()
                logger.info(f"에러 알럿 감지: {alert_text}")
                return alert_text
        except Exception:
            # 타임아웃 발생 시 알럿이 없는 것으로 간주
            pass
        
        return None
        
#스냅샷    
    def click_snapshot_tab(self):
        self.wait_clickable(L.BS_SNAPSHOT_TAB).click()
        logger.info("스냅샷 탭 클릭 완료")
        
    def check_snapshot_list_page_element(self):
        try:
            self.wait_visibility_element(L.BS_NAME_COLUMN)
            self.wait_visibility_element(L.BS_STATUS_COLUMN)
            self.wait_visibility_element(L.BS_SIZE_COLUMN)
            self.wait_visibility_element(L.BS_DR_COLUMN)
            self.wait_visibility_element(L.BS_CREATED_AT_COLUMN)
            self.wait_visibility_element(L.BS_SNAPSHOT_CREATE_BUTTON)
            return True
        except Exception as e:
            self.handle_exception(e, "스냅샷 목록 화면 요소 체크")
            return False
        
    def click_snapshot_create(self):
        self.wait_clickable(L.BS_SNAPSHOT_CREATE_BUTTON).click()
        logger.info("스냅샷 생성 클릭 완료")
        
        
    def check_snapshot_create_element(self):
        try:
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("이름"))
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("영역 ID"))
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("블록 스토리지"))
            return True
        except Exception as e:
            self.handle_exception(e, "스냅샷 생성 폼 요소 체크")
            return False
    
    def select_first_block_storage(self):
        self.wait_clickable(L.BLOCK_STORAGE_OPEN_BTN).click()
        self.wait_clickable(L.FIRST_OPTION).click()
        self.wait_invisibility_element(L.FIRST_OPTION)
        logger.info("첫 번째 블록 스토리지 선택 완료")
        
    def check_detail_page_element(self):
        try:
            self.wait_visibility_element(L.DELETE_BUTTON)
            self.wait_visibility_element(L.EDIT_BUTTON)
            return True
        except Exception as e:
            self.handle_exception(e, "블록스토리지 상세페이지 화면 요소 체크")
            return False
        
    def get_first_snapshot_id(self):
        try:
            # 요소가 보일 때까지 대기 후 텍스트 추출
            element = self.wait_presence(L.SNAPSHOT_ID_SPAN)
            snapshot_id = element.text.strip()
            logger.info(f"가져온 스냅샷 ID: {snapshot_id}")
            return snapshot_id
        except Exception as e:
            self.handle_exception(e, "스냅샷 ID 텍스트 가져오기 실패")
            return None
        
    def get_vm_id(self):
        id_element = self.wait_visibility_element(L.VM_ID_TEXT)
        target_id = id_element.text.strip()
        logger.info(f"추출된 VM ID: {target_id}")
        return target_id
    
    def click_vm_link(self):
        self.wait_clickable(L.VM_LINK).click()
        logger.info("VM 상세 링크 클릭 완료")
        
    def get_target_href(self):
        element = self.wait_presence(L.BLOCKSTORAGE_LINK)
        href_value = element.get_attribute("href")
        logger.info(f"추출된 href 값: {href_value}")
        return href_value

    def click_link_element(self):
        self.wait_clickable(L.BLOCKSTORAGE_LINK).click()
        logger.info("링크 클릭 완료")
        
    def get_snapshot_name_input_value(self):
        element = self.wait_visibility_element(L.NAME_FIELD)
        input_value = element.get_attribute("value")
        
        logger.info(f"추출된 입력값: {input_value}")
        return input_value
    
    def check_snapshot_edit_element(self):
        self.wait_visibility_element(L.ELEMENT_BY_LABEL("이름"))
        return True
        
            
#스케줄러
    def click_scheduler_tab(self):
        self.wait_clickable(L.BS_SCHEDULER_TAB).click()
        logger.info("스케줄러 탭 클릭 완료")
        
    def check_scheduler_list_page_element(self):
        try:
            self.wait_presence(L.BS_NAME_COLUMN)
            self.wait_presence(L.BS_BS_COLUMN)
            self.wait_presence(L.BS_SCHEDULE_COLUMN)
            self.wait_presence(L.BS_STATUS_COLUMN)
            self.wait_presence(L.BS_MAX_SNAPSHOT_COLUMN)
            self.wait_presence(L.BS_LAST_AT_COLUMN)
            self.wait_presence(L.BS_NEXT_AT_COLUMN)
            self.wait_presence(L.BS_CREATED_AT_COLUMN)
            self.wait_presence(L.BS_SCHEDULER_CREATE_BUTTON)
            return True
        except Exception as e:
            self.handle_exception(e, "스케줄러 목록 화면 요소 체크")
            return False
        
    def click_scheduler_create(self):
        self.wait_clickable(L.BS_SCHEDULER_CREATE_BUTTON).click()
        logger.info("스케줄러 탭 클릭 완료")
        
    def check_scheduler_create_element(self):
        try:
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("이름"))
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("영역 ID"))
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("대상 블록 스토리지"))
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("Cron 표현식"))
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("최대 스냅샷 수"))
            return True
        except Exception as e:
            self.handle_exception(e, "스케줄러 생성 폼 요소 체크")
            return False
        
    def check_scheduler_edit_element(self):
        try:
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("이름"))
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("Cron 표현식"))
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("대상 블록 스토리지"))
            self.wait_visibility_element(L.ELEMENT_BY_LABEL("최대 스냅샷 수"))
            return True
        except Exception as e:
            self.handle_exception(e, "스케줄러 수정 폼 요소 체크")
            return False