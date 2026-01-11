import platform
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def select_all_key(self):
        return Keys.COMMAND if platform.system() == "Darwin" else Keys.CONTROL
    
    def _get_wait_object(self, timeout):
        return WebDriverWait(self.driver, timeout) if timeout else self.wait
    
    # 요소 찾기 (화면에 안보여도 요소가 DOM에 존재하기만 하면 됨)
    def wait_presence(self, by_locator, timeout=None):
        wait = self._get_wait_object(timeout)
        return wait.until(EC.presence_of_element_located(by_locator))

    def wait_all_presence(self, by_locator, timeout=None):
        wait = self._get_wait_object(timeout)
        return wait.until(EC.presence_of_all_elements_located(by_locator))

    def wait_clickable(self, by_locator, timeout=None):
        wait = self._get_wait_object(timeout)
        return wait.until(EC.element_to_be_clickable(by_locator))

    def wait_visibility_element(self, by_locator, timeout=None):
        wait = self._get_wait_object(timeout)
        try:
            return wait.until(EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            return False

    def wait_visibility_all_element(self, by_locator, timeout=None):
        wait = self._get_wait_object(timeout)
        return wait.until(EC.visibility_of_all_elements_located(by_locator))
    
    # 특정 요소의 attribute 안에 특정 값이 포함될 때까지 대기 ex) class에 "active"가 들어갈 때 까지
    def wait_attrb_include(self, by_locator, attribute: str, timeout=None):
        wait = self._get_wait_object(timeout)
        return wait.until(EC.element_attribute_to_include(by_locator, attribute))
    
    # 특정 attribute 값 안에 특정 텍스트가 포함될 때까지 대기 ex) <input value="완료됨"> → value 안에 "완료" 포함될 때
    def wait_text_in_attribute(self, by_locator, attribute1: str, attribute2: str, timeout=None):
        wait = self._get_wait_object(timeout)
        return wait.until(EC.text_to_be_present_in_element_attribute(by_locator, attribute1, attribute2))
    
    # iframe 이 로드되면 자동으로 해당 frame 으로 switch
    def wait_frame_and_switch(self, by_frame, timeout=None):
        wait = self._get_wait_object(timeout)
        return wait.until(EC.frame_to_be_available_and_switch_to_it(by_frame))

    def wait_alert(self, timeout=None):
        wait = self._get_wait_object(timeout)
        return wait.until(EC.alert_is_present())
    
    # 요소의 텍스트 안에 특정 문자열이 포함될 때까지 대기 예: 로딩 완료 메시지, 상태 텍스트 확인
    def wait_text_in_element(self, by_locator, text: str, timeout=None):
        wait = self._get_wait_object(timeout)
        return wait.until(EC.text_to_be_present_in_element(by_locator, text))
    
    #현재 URL 에 특정 문자열이 포함될 때까지 대기. 페이지 이동 검증용
    def wait_url_contains(self, by_url: str, timeout=None):
        wait = self._get_wait_object(timeout)
        return wait.until(EC.url_contains(by_url))
    
    # 요소가 사라질 때까지 대기
    def wait_invisibility_element(self, by_locator, timeout=None):
        wait = self._get_wait_object(timeout)
        return wait.until(EC.invisibility_of_element_located(by_locator))
    
    # input / textarea 의 value 값에 특정 텍스트가 들어갈 때까지 대기
    def wait_text_in_element_value(self, by_locator, value_: str, timeout=None):
        wait = self._get_wait_object(timeout)
        return wait.until(EC.text_to_be_present_in_element_value(by_locator, value_))
    
    def find_element(self, by_locator):
        return self.driver.find_element(*by_locator)
    
    def find_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)
    
    def wait_dom_stable(self, timeout=3, interval=0.1):
        wait = WebDriverWait(self.driver, timeout, poll_frequency=interval)

        wait.until(lambda d: d.execute_script(
            "return document.readyState") == "complete")

        last = None
        for _ in range(5):
            current = self.driver.execute_script(
                "return document.body.innerHTML.length")

            if last is not None and current == last:
                return True

            last = current
            wait.until(lambda d: True)  # interval만큼 대기

        return True

    def click_stale_safe(self, by_locator, attempts=3):
        for i in range(attempts):
            try:
                self.wait_dom_stable()
                element = self.wait_visibility_element(by_locator)
                try:
                    element.click()
                except:
                    self.driver.execute_script("arguments[0].click();", element)
                return True 
            except StaleElementReferenceException:
                if i == attempts - 1:
                    raise
                continue

