from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import re
from datetime import datetime
from src.pages.base_page import BasePage
from src.utils.locator import OSLocator as OSL

class DashPage(BasePage):
    def go_dashbord(self):
        self.click_stale_safe(OSL.OS_MENU)
        self.click_stale_safe(OSL.OS_DASHBOARD_TAB)
        self.wait_visibility_element(OSL.OS_DASH_TITLE_OVERVIEW)
        return self
    
class BucketPage(BasePage):
    def create_wait_loaded(self):
        self.wait_clickable(OSL.OS_BUCKET_BTN_CREATE).click()
        self.wait_visibility_element(OSL.OS_BUCKET_CREATE_INPUT_NAME)
        return self

    def set_bucket_name(self, name: str):
        el = self.wait_visibility_element(OSL.OS_BUCKET_CREATE_INPUT_NAME)
        el.click()
        el.clear()
        el.send_keys(name)
        return self

    def set_description(self, text: str):
        el = self.wait_visibility_element(OSL.OS_BUCKET_CREATE_TEXTAREA_DESC)
        el.click()
        el.clear()
        el.send_keys(text)
        return self

    def click_submit(self):
        btn = self.wait_clickable(OSL.OS_BUCKET_CREATE_BTN_SUBMIT)
        btn.click()
        return self

    def click_cancel(self):
        btn = self.wait_clickable(OSL.OS_BUCKET_CREATE_BTN_CANCEL)
        btn.click()
        return self

    def bucket_create_form(self, name: str, description: str | None = None):
        self.set_bucket_name(name)
        if description is not None:
            self.set_description(description)
        return self
    
    def detail_wait_loaded(self):
        self.wait_visibility_element(OSL.OS_BUCKET_DETAIL_BTN_EDIT)
        self.wait_visibility_element(OSL.OS_BUCKET_DETAIL_BTN_DELETE)
        return self

    def get_title_bucket_name(self):
        return self.wait_visibility_element(OSL.OS_BUCKET_DETAIL_TITLE).text.strip()
    
    def get_bucket_name_helper_text(self) -> str:
        inp = self.wait_visibility_element(OSL.OS_BUCKET_CREATE_INPUT_NAME)
        helper_id = inp.get_attribute("aria-describedby")
        if not helper_id:
            return ""
        try:
            return self.wait_visibility_element((By.ID, helper_id), timeout=2).text.strip()
        except Exception:
            return ""

    def is_bucket_name_invalid(self) -> bool:
        inp = self.wait_visibility_element(OSL.OS_BUCKET_CREATE_INPUT_NAME)
        return (inp.get_attribute("aria-invalid") or "").lower() == "true"

    def wait_bucket_name_invalid(self, timeout=5):
        wait = self._get_wait_object(timeout)
        wait.until(lambda _d: self.is_bucket_name_invalid())
        return self
    
    def set_zone_first_valid(self):
        el = self.wait_visibility_element(OSL.OS_BUCKET_CREATE_SELECT_ZONE)
        sel = Select(el)
        for opt in sel.options:
            v = (opt.get_attribute("value") or "").strip()
            if v:
                sel.select_by_value(v)
                break
        return self

    def set_size_gib(self, size: int):
        el = self.wait_visibility_element(OSL.OS_BUCKET_CREATE_INPUT_SIZE)
        el.click()
        el.clear()
        el.send_keys(str(size))
        return self

    def is_bucket_create_success(self, timeout: int = 2) -> bool:
        return bool(self.wait_visibility_element(OSL.OS_BUCKET_DETAIL_BTN_EDIT, timeout=timeout))

    def submit_or_cancel_if_failed(self, timeout: int = 6, cancel_on_fail: bool = True) -> bool:
        self.click_stale_safe(OSL.OS_BUCKET_CREATE_BTN_SUBMIT)

        wait = self._get_wait_object(timeout)

        def _done(_driver):
            return self.is_bucket_create_success(timeout=1) or self.is_bucket_name_invalid()

        try:
            wait.until(_done)
        except TimeoutException:
            pass

        if self.is_bucket_create_success(timeout=1):
            return True

        if cancel_on_fail:
            self.click_stale_safe(OSL.OS_BUCKET_CREATE_BTN_CANCEL)
            self.wait_visibility_element(OSL.OS_BUCKET_TITLE, timeout=timeout)
        return False
    
    def click_edit(self):
        self.wait_clickable(OSL.OS_BUCKET_DETAIL_BTN_EDIT).click()
        self.wait_visibility_element(OSL.OS_BUCKET_EDIT_TITLE)
        self.wait_visibility_element(OSL.BUCKET_EDIT_INPUT_NAME)
        return self

    def edit_set_name(self, name: str):
        el = self.wait_visibility_element(OSL.BUCKET_EDIT_INPUT_NAME)
        el.click()
        el.clear()
        el.send_keys(name)
        return self

    def edit_save_enabled(self) -> bool:
        return self.wait_presence(OSL.BUCKET_EDIT_BTN_SAVE).is_enabled()

    def edit_click_save(self):
        self.wait_clickable(OSL.BUCKET_EDIT_BTN_SAVE).click()
        self.wait_visibility_element(OSL.OS_BUCKET_DETAIL_BTN_EDIT)
        return self

    def click_add_permission(self):
        self.wait_clickable(OSL.OS_BUCKET_PERMISSION_BTN_CREATE).click()
        self.wait_visibility_element(OSL.DIALOG_PERMISSION_TITLE)
        return self
    
    def select_first_user_in_dialog(self):
        self.wait_clickable(OSL.DIALOG_USER_DROPDOWN_BTN).click()

        self.wait_visibility_element(OSL.DIALOG_USER_LISTBOX)
        self.wait_clickable(OSL.DIALOG_USER_FIRST_OPTION).click()
        return self

    def wait_dialog_create_enabled(self, timeout: int = 10):
        self._get_wait_object(timeout).until(
            lambda d: d.find_element(*OSL.DIALOG_BTN_CREATE).is_enabled()
        )
        return self

    def click_dialog_create(self, retries: int = 2, snackbar_timeout: int = 3):
        for _ in range(retries + 1):
            try:
                self.wait_dialog_create_enabled(timeout=5)
            except Exception:
                try:
                    self.select_first_user_in_dialog()
                    self.wait_dialog_create_enabled(timeout=5)
                except Exception:
                    pass

            self.click_stale_safe(OSL.DIALOG_BTN_CREATE)

            snackbar = self.wait_visibility_element(OSL.SNACKBAR_MESSAGE, timeout=snackbar_timeout)
            if snackbar:
                return self
            
        return self
    
    def confirm_bucket_delete_with_retry(self, retries: int = 2, list_timeout: int = 5, dialog_timeout: int = 3):
        for _ in range(retries + 1):
            try:
                self.click_stale_safe(OSL.OS_BUCKET_DETAIL_BTN_DELETE)
                self.click_stale_safe(OSL.BUCKET_DELETE_DELETE_BTN)
                if self.wait_visibility_element(OSL.OS_BUCKET_TITLE, timeout=list_timeout):
                    return True
            except Exception:
                pass

            try:
                self.click_stale_safe(OSL.BUCKET_DELETE_CANCEL_BTN)
                self.wait_invisibility_element(OSL.BUCKET_DELETE_CANCEL_BTN, timeout=dialog_timeout)
            except Exception:
                pass

        return False

class UserPage(BasePage):
    def user_menu_click(self):
        self.wait_clickable(OSL.OS_MENU).click()
        self.wait_clickable(OSL.OS_USER_TAB).click()
        self.wait_visibility_element(OSL.OS_USERS_TITLE)
        return self

    def user_create_wait_loaded(self):
        self.wait_clickable(OSL.CREATE_USER_BTN).click()
        self.wait_visibility_element(OSL.CREATE_USER_NAME_INPUT)
        return self

    def set_user_name(self, name: str):
        el = self.wait_visibility_element(OSL.CREATE_USER_NAME_INPUT)
        el.click()
        el.clear()
        el.send_keys(name)
        return self

    def set_tags(self, tags: str):
        el = self.wait_visibility_element(OSL.CREATE_USER_TAGS_TEXTAREA)
        el.click()
        el.clear()
        el.send_keys(tags)
        return self
    
    def user_create_form(self, name: str, tags: str | None = None):
        self.set_user_name(name)
        if tags is not None:
            self.set_tags(tags)
        return self
    
    def _wait_rows_visible(self):
        self.wait.until(lambda d: len(d.find_elements(*OSL.TABLE_ROWS)) > 0)

    def _parse_korean_datetime(self, text: str) -> datetime:
        # ex. '2026. 1. 5. 오전 10:37:26', '2026. 1. 2. 오후 3:25:33'
        t = text.strip()

        m = re.search(
            r"(\d{4})\.\s*(\d{1,2})\.\s*(\d{1,2})\.\s*(오전|오후)\s*(\d{1,2}):(\d{2}):(\d{2})",
            t
        )
        if not m:
            raise ValueError(f"생성일 파싱 실패: '{text}'")

        year = int(m.group(1))
        month = int(m.group(2))
        day = int(m.group(3))
        ampm = m.group(4)
        hour = int(m.group(5))
        minute = int(m.group(6))
        second = int(m.group(7))

        # 오전/오후 -> 24시간 변환
        if ampm == "오후" and hour != 12:
            hour += 12
        if ampm == "오전" and hour == 12:
            hour = 0

        return datetime(year, month, day, hour, minute, second)

    def open_latest_user_detail_by_keyword(self, keyword: str):
        self._wait_rows_visible()

        rows = self.find_elements(OSL.TABLE_ROWS)

        candidates = []
        for row in rows:
            try:
                username_el = row.find_element(*OSL.USERNAME_IN_ROW)
                created_el = row.find_element(*OSL.CREATED_AT_IN_ROW)
            except Exception:
                # 구조 다르면 스킵
                continue

            username = (username_el.text or "").strip()
            created_text = (created_el.text or "").strip()

            if keyword not in username:
                continue

            created_dt = self._parse_korean_datetime(created_text)
            candidates.append((created_dt, username_el))

        if not candidates:
            raise AssertionError(f"'{keyword}' 포함 사용자 행을 찾지 못했습니다.")

        candidates.sort(key=lambda x: x[0])
        _, latest_username_el = candidates[-1]
        self.wait_clickable(latest_username_el)
        latest_username_el.click()

    def get_title_user_name(self) -> str:
        return self.wait_visibility_element(OSL.USER_DETAIL_TITLE).text.strip()
    
    def user_grant_click_add(self):
        self.wait_clickable(OSL.USER_PERMISSION_BTN_ADD).click()
        self.wait_visibility_element(OSL.USER_OBJECT_STORAGE_SELECT)
        return self

    def _click(self, locator):
        el = self.wait_clickable(locator)
        el.click()
        return el

    def _open_select_and_choose_first(self, select_locator):
        self._click(select_locator)
        self.wait_presence(OSL.ACTIVE_LIST)
        self._click(OSL.FIRST_ENABLED_OPTION)

        try:
            self.wait_invisibility_element(OSL.ACTIVE_LIST)
        except Exception:
            pass

    def select_first_object_storage_and_permission(self):
        self._open_select_and_choose_first(OSL.USER_OBJECT_STORAGE_SELECT)
        self._open_select_and_choose_first(OSL.USER_PERMISSION_SELECT)
        return self
    
    def user_grant_submit_with_retry(self, attempts: int = 3):
        for _ in range(attempts):
            btn = self.wait_presence(OSL.USER_PERMISSION_SUBMIT_BTN)
            if not btn.is_enabled():
                self.select_first_object_storage_and_permission()
                self._get_wait_object(5).until(
                    lambda d: d.find_element(*OSL.USER_PERMISSION_SUBMIT_BTN).is_enabled()
                )

            self.click_stale_safe(OSL.USER_PERMISSION_SUBMIT_BTN)

            if self.wait_visibility_element(OSL.GRANT_DELETE_BTN, timeout=5):
                return self

            try:
                self.wait_invisibility_element(OSL.GRANT_DIALOG, timeout=3)
                self.wait_visibility_element(OSL.GRANT_DELETE_BTN, timeout=10)
                return self
            except Exception:
                pass

        raise AssertionError("사용자 권한 생성: 생성 버튼 클릭/처리 재시도 실패")

    def user_grant_edit_change_permission_to_second(self):
        self.wait_clickable(OSL.USER_GRANT_EDIT_PERMISSION_SELECT).click()
        self.wait_clickable(OSL.USER_GRANT_EDIT_PERMISSION_SECOND_OPTION).click()
        self.wait_clickable(OSL.USER_GRANT_EDIT_SAVE_BTN).click()
        self.wait_invisibility_element(OSL.GRANT_DIALOG)
        return self
    
    def user_edit_click(self):
        self.click_stale_safe(OSL.USER_DETAIL_BTN_EDIT)
        self.wait_visibility_element(OSL.USER_EDIT_CANCEL_BTN)
        return self