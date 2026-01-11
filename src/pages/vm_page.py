import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.pages.base_page import BasePage
from src.utils.locator import ComputeVmLocator as C, VmLocator as L

def _rand(prefix="ui-vm"):
    return f"{prefix}-{uuid.uuid4().hex[:6]}"

class VmPage(BasePage):

    def _js_click(self, el):
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        try:
            el.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", el)

    def select_mui_autocomplete_by_typing(
        self,
        input_locator,            # input[@role=combobox]
        listbox_locator,          # ul[role=listbox]
        option_text: str,
    ):
        """
        (옵션이 많거나 가상화면일 때 더 안정) input에 타이핑 → 필터 → 옵션 클릭
        """
        inp = self.wait_clickable(input_locator, timeout=15)
        self._js_click(inp)
        inp.send_keys(Keys.CONTROL, "a")
        inp.send_keys(option_text)

        self.wait_visibility_element(listbox_locator, timeout=10)
        opt = (By.XPATH, f"//ul[@role='listbox']//li[@role='option'][contains(., '{option_text}')]")
        el = self.wait_clickable(opt, timeout=15)
        self._js_click(el)
        return True
    
    # ---------- Navigation ----------
    def go_vm_list(self):
        # 컴퓨트 > 가상머신
        self.wait_clickable(C.COMPUTE_MENU).click()
        self.wait_clickable(C.VM_TAB).click()
        # VM 생성 버튼이 보이면 VM 목록으로 간 걸로 판단
        self.wait_visibility_element(L.BTN_CREATE_VM, timeout=20)
        return self

    # ---------- Autocomplete helpers ----------
    def _select_from_listbox(self, text: str | None = None):
        """
        listbox가 뜬 상태에서:
        - text가 있으면 그 텍스트 포함하는 option 클릭
        - 없으면 첫 번째 옵션 클릭
        """
        ul = self.wait_visibility_element(L.LISTBOX, timeout=10)
        if text:
            opt = self.wait_clickable((By.XPATH, f"//ul[@role='listbox']//li[contains(., '{text}')]"), timeout=10)
        else:
            opt = self.wait_clickable((By.XPATH, "(//ul[@role='listbox']//li)[1]"), timeout=10)

        try:
            opt.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", opt)

    # ---------- Create flow ----------
    def open_create_vm(self):
        self.wait_clickable(L.BTN_CREATE_VM, timeout=20).click()
        self.wait_visibility_element(L.INPUT_VM_NAME, timeout=20)
        return self

    def fill_basic_info(self, vm_name: str, username: str, password: str):
        name_el = self.wait_visibility_element(L.INPUT_VM_NAME, timeout=20)
        name_el.click()
        name_el.send_keys(self.select_all_key(), "a")
        name_el.send_keys(Keys.BACKSPACE)
        name_el.send_keys(vm_name)
        self.wait_visibility_element(L.INPUT_USERNAME).send_keys(username)
        self.wait_visibility_element(L.INPUT_PASSWORD).send_keys(password)
        self.wait_visibility_element(L.INPUT_CONFIRM_PASSWORD).send_keys(password)
        return self

    def fill_networking(self, nic_name: str, subnet_text: str | None = None):
        # 1) 네트워킹 탭 클릭
        self.wait_clickable(L.TAB_NETWORKING, timeout=15).click()

        # 2) 탭 패널이 실제로 바뀌었는지(= NIC input이 보일 때까지)
        nic_el = self.wait_visibility_element(L.INPUT_NIC_NAME, timeout=20)
        nic_el.click()
        nic_el.send_keys(self.select_all_key(), "a")
        nic_el.send_keys(Keys.BACKSPACE)
        nic_el.send_keys(nic_name)

        # 3) ✅ 서브넷 드롭다운 열기: clickable 말고 presence로 잡아서 JS 클릭
        open_btn = self.wait_presence(L.SUBNET_OPEN, timeout=20)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", open_btn)
        self.driver.execute_script("arguments[0].click();", open_btn)

        # 4) listbox 대기 후 옵션 선택
        self.wait_visibility_element(L.LISTBOX, timeout=15)

        if subnet_text:
            opt = (By.XPATH, f"//ul[@role='listbox']//li[@role='option'][contains(., '{subnet_text}')]")
        else:
            opt = (By.XPATH, "(//ul[@role='listbox']//li[@role='option'])[1]")

        el = self.wait_presence(opt, timeout=20)
        self.driver.execute_script("arguments[0].click();", el)
        return self

    def fill_storage(self, block_storage_text: str | None = None):
        # 1) 스토리지 탭
        self.wait_clickable(L.TAB_STORAGE, timeout=15).click()

        # 2) 탭 패널 활성화 확인(= input이 보일 때까지)
        self.wait_presence(L.BLOCK_STORAGE_INPUT, timeout=20)

        # 3) 드롭다운 열기: presence로 잡아서 JS click
        open_btn = self.wait_presence(L.BLOCK_STORAGE_OPEN, timeout=20)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", open_btn)
        self.driver.execute_script("arguments[0].click();", open_btn)

        # 4) listbox 대기 후 옵션 선택
        self.wait_visibility_element(L.LISTBOX, timeout=15)

        if block_storage_text:
            opt = (By.XPATH, f"//ul[@role='listbox']//li[@role='option'][contains(., '{block_storage_text}')]")
        else:
            opt = (By.XPATH, "(//ul[@role='listbox']//li[@role='option'])[1]")

        el = self.wait_presence(opt, timeout=20)
        self.driver.execute_script("arguments[0].click();", el)
        return self

    def review_and_create(self):
        self.wait_clickable(L.TAB_REVIEW_CREATE).click()
        self.wait_clickable(L.BTN_CREATE_SUBMIT, timeout=20).click()

        # 생성 후 상세 페이지로 왔다고 가정: 수정/삭제 버튼이 보여야 함
        self.wait_visibility_element(L.BTN_EDIT, timeout=60)
        self.wait_visibility_element(L.BTN_DELETE, timeout=60)
        return self

    # ---------- Edit flow ----------
    def edit_name_and_save(self, new_name: str):
        self.wait_clickable(L.BTN_EDIT, timeout=20).click()

        inp = self.wait_visibility_element(L.INPUT_EDIT_NAME_FALLBACK, timeout=20)
        inp.click()
        inp.send_keys(self.select_all_key(), "a")
        inp.send_keys(Keys.BACKSPACE)
        inp.send_keys(new_name)

        self.wait_clickable(L.BTN_SAVE, timeout=20).click()

        # ✅ 저장 후 상세 이름(h5)이 새 이름으로 바뀌는지 대기
        self.wait_text_in_element(L.VM_DETAIL_NAME, new_name, timeout=40)

        return new_name

    # ---------- Delete flow ----------
    def delete_vm(self):
        self.wait_clickable(L.BTN_DELETE, timeout=20).click()

        # 네트워크 인터페이스 삭제 체크
        chk = self.wait_presence(L.CHK_DELETE_NIC, timeout=30)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", chk)
        self.driver.execute_script("arguments[0].click();", chk)

        
        # label/span 컨테이너 클릭 fallback
        consent_box = self.wait_clickable(
            (By.XPATH, "//label[.//span[contains(normalize-space(.),'본인은 이 가상 머신')]]"),
            timeout=20
        )
        self.driver.execute_script("arguments[0].click();", consent_box)

        # 최종 삭제
        self.wait_clickable(L.BTN_DELETE_CONFIRM, timeout=20).click()

        # 삭제 후 VM 목록/상위 화면으로 돌아오는 신호(생성 버튼 다시 보이기)
        self.wait_visibility_element(L.BTN_CREATE_VM, timeout=60)
        return self

    # ---------- Assertions ----------
    def assert_on_detail(self):
        self.wait_visibility_element(L.BTN_EDIT, timeout=20)
        self.wait_visibility_element(L.BTN_DELETE, timeout=20)
        return True
