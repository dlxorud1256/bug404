from src.pages.base_page import BasePage
from src.utils.locator import ComputeDashboardLocator as L

class ComputeDashboardPage(BasePage):
    def go_dashboard(self):
        # 사이드바: 컴퓨트 > 대시보드
        self.wait_clickable(L.COMPUTE_MENU).click()
        self.wait_clickable(L.DASHBOARD_TAB).click()
        return self

    def assert_default_gpu_tab(self):
        # 대시보드 진입 시 기본으로 GPU 탭(평균 GPU 사용률 카드)이 떠야 함
        self.wait_visibility_element(L.GPU_AVG_CONTAINER, timeout=20)
        return True

    def click_tab_and_assert_container(self, tab_locator, container_locator):
        # 탭 클릭
        self.wait_clickable(tab_locator, timeout=15).click()

        # 해당 컨테이너(그래프 카드) 표시 확인
        self.wait_visibility_element(container_locator, timeout=20)
        return True

    
