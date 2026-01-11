import uuid
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.keys import Keys
from src.pages.base_page import BasePage
from src.utils.locator import ComputeLocator, ClusterLocator

def _rand(prefix="ui-cluster"):
    return f"{prefix}-{uuid.uuid4().hex[:6]}"

class ClusterPage(BasePage):
    def go_cluster_list(self):
        # 사이드바 > 컴퓨트 > 가상 클러스터
        self.wait_clickable(ComputeLocator.COMPUTE_MENU).click()
        self.wait_clickable(ComputeLocator.VIRTUAL_CLUSTER_TAB).click()

        # 목록 페이지 진입 확인
        self.wait_visibility_element(ClusterLocator.CLUSTER_LIST_TITLE)
        return self

    def open_create(self):
        self.wait_clickable(ClusterLocator.BTN_CREATE_CLUSTER).click()
        self.wait_visibility_element(ClusterLocator.INPUT_NAME)
        return self

    # ----------------------------
    # 상태 확인 / 대기(Assert-friendly)
    # ----------------------------
    def is_name_visible(self, name: str) -> bool:
        return name in self.driver.page_source

    def is_name_not_in_list(self, name: str) -> bool:
        return name not in self.driver.page_source

    def wait_name_visible(self, name: str, timeout: int = 30) -> bool:
        try:
            self._get_wait_object(timeout).until(lambda d: name in d.page_source)
            return True
        except TimeoutException:
            return False

    def wait_name_disappear(self, name: str, timeout: int = 30) -> bool:
        try:
            self._get_wait_object(timeout).until(lambda d: name not in d.page_source)
            return True
        except TimeoutException:
            return False

    # ----------------------------
    # 액션
    # ----------------------------
    def create_cluster(self, name: str):
        self.open_create()
        inp = self.wait_visibility_element(ClusterLocator.INPUT_NAME)

        inp.click()
        inp.send_keys(self.select_all_key(), "a")
        inp.send_keys(Keys.BACKSPACE)
        inp.send_keys(name)

        self.wait_clickable(ClusterLocator.BTN_SUBMIT_CREATE).click()
        self.wait_name_visible(name, timeout=40)
        return self

    def rename_cluster(self, new_name: str):
        self.wait_clickable(ClusterLocator.BTN_EDIT).click()
        inp = self.wait_visibility_element(ClusterLocator.INPUT_NAME)

        inp.click()
        inp.send_keys(self.select_all_key(), "a")
        inp.send_keys(Keys.BACKSPACE)
        inp.send_keys(new_name)

        self.wait_clickable(ClusterLocator.BTN_SAVE).click()
        self.wait_name_visible(new_name, timeout=40)
        return self

    def delete_cluster(self):
        self.wait_clickable(ClusterLocator.BTN_DELETE).click()

        # dialog 뜰 때까지
        self.wait_visibility_element(ClusterLocator.DELETE_DIALOG)

        # checkbox 컨테이너 클릭 (stale/overlay 대비 재시도)
        for _ in range(3):
            try:
                cb = self.wait_clickable(ClusterLocator.DELETE_CONFIRM_CHECKBOX, timeout=20)
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", cb)
                try:
                    cb.click()
                except ElementClickInterceptedException:
                    self.driver.execute_script("arguments[0].click();", cb)
                break
            except StaleElementReferenceException:
                continue

        self.wait_clickable(ClusterLocator.DELETE_CONFIRM_BTN, timeout=30).click()

        # 목록 복귀 확인
        self.wait_visibility_element(ClusterLocator.CLUSTER_LIST_TITLE, timeout=40)
        return self
