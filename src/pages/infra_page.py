from src.utils.locator import InfraLocator as L
from src.pages.base_page import BasePage
import time
import logging
logger = logging.getLogger(__name__)

class InfraPage(BasePage):
    def __init__(self, driver, timeout=30):
        super().__init__(driver, timeout)
        
    def click_infra_menu(self):
        self.wait_clickable(L.INF_MENU).click()
        logger.info("인프라 메뉴 클릭 완료")
        
    def click_infra_region_tab(self):
        self.wait_clickable(L.INF_MENU).click()
        self.wait_clickable(L.INF_REGION_TAB).click()
        logger.info("인프라 리전 탭 클릭 완료")
        
    def click_infra_zone_tab(self):
        self.wait_clickable(L.INF_MENU).click()
        self.wait_clickable(L.INF_ZONE_TAB).click()
        logger.info("인프라 영역 탭 클릭 완료")
        
    def click_infra_instance_type_tab(self):
        self.wait_clickable(L.INF_MENU).click()
        self.wait_clickable(L.INF_INSTANCE_TYPE_TAB).click()
        logger.info("인프라 인스턴스 유형 탭 클릭 완료")
        
    def click_infra_block_storage_image_tab(self):
        self.wait_clickable(L.INF_MENU).click()
        self.wait_clickable(L.INF_BLOCK_STORAGE_IMAGE_TAB).click()
        logger.info("인프라 블록스토리지 이미지 탭 클릭 완료")
        
    def click_infra_notice_tab(self):
        self.wait_clickable(L.INF_NOTICE_TAB).click()
        logger.info("인프라 공지 탭 클릭 완료")
        
    def click_resource_status_tab(self):
        self.wait_clickable(L.INF_RESOURCE_STATUS_TAB).click()
        logger.info("인프라 리소스 현황 탭 클릭 완료")
    
    def click_infra_notice_specific_page(self):
        self.wait_clickable(L.INF_MENU).click()
        self.wait_clickable(L.INF_NOTICE_TAB).click()
        self.wait_clickable(L.INF_NOTICE_SPECIFIC_PAGE).click()
        logger.info("인프라 공지 상세 페이지 클릭 완료")

    def click_refresh_btn(self):
        self.wait_clickable(L.INF_REFRESH_BTN).click()
        logger.info("인프라 리소스 현황 페이지 새로고침 버튼 클릭 완료")

    def get_last_updated_time(self):
        time.sleep(1)
        return self.wait_presence(L.INF_LAST_UPDATED_TEXT).text