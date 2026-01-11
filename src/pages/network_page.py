from src.pages.base_page import BasePage
from src.utils.locator import NetworkLocator as L
import logging
logger = logging.getLogger(__name__)

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class NetworkPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        
    def click_network_menu(self):
        self.wait_clickable(L.NET_MENU).click()
        logger.info("네트워크 메뉴 클릭 완료")
        
    def click_network_interface_tab(self):
        self.wait_clickable(L.NET_NETWORK_INTERFACE_TAB).click()
        logger.info("네트워크 인터페이스 탭 클릭 완료")
        
    def click_create_btn(self):
        self.wait_clickable(L.NET_CREATE_BTN).click()
        logger.info("네트워크 인터페이스 생성 버튼 클릭 완료")
        
    def click_cancel_btn(self):
        self.wait_clickable(L.NET_CANCEL).click()
        logger.info("네트워크 인터페이스 생성 취소 버튼 클릭 완료")
        
    def click_network_virual_network_tab(self):
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_TAB).click()
        logger.info("가상 네트워크 탭 클릭 완료")
          
    def create_interface(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_NETWORK_INTERFACE_TAB).click()
        self.wait_clickable(L.NET_CREATE_BTN).click()
        self.wait_clickable(L.NET_INPUT_NAME).clear()
        self.wait_clickable(L.NET_INPUT_NAME).send_keys("team4_interface")
        self.wait_clickable(L.NET_INTERFACE_ATTACHED_SUBNET).click()
        self.wait_clickable(L.NET_ATTACHED_SUBNET).click()
        self.wait_clickable(L.NET_CREATE).click()
        logger.info("인터페이스 생성 완료")
        
    def load_created_interface(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_NETWORK_INTERFACE_TAB).click()
        self.wait_clickable(L.NET_INTERFACE_TEAM4).click()
        logger.info("생성된 인터페이스 로드 완료")
        
    def modify_interface_name(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_NETWORK_INTERFACE_TAB).click()
        self.wait_clickable(L.NET_INTERFACE_TEAM4).click()
        self.wait_clickable(L.NET_EDIT).click()
        self.wait_clickable(L.NET_INPUT_NAME).clear()
        self.wait_clickable(L.NET_INPUT_NAME).send_keys("team4_modify_interface")
        self.wait_clickable(L.NET_SAVE).click()
        logger.info("인터페이스 수정 완료")
    
    def modify_cancel(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_NETWORK_INTERFACE_TAB).click()
        self.wait_clickable(L.NET_INTERFACE_MODIFY_NAME).click()
        self.wait_clickable(L.NET_EDIT).click()
        self.wait_clickable(L.NET_CANCEL).click()
        logger.info("인터페이스 수정 취소 완료")

    def delete_interface(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_NETWORK_INTERFACE_TAB).click()
        self.wait_clickable(L.NET_INTERFACE_MODIFY_NAME).click()
        self.wait_clickable(L.NET_DELETE).click()
        self.wait_clickable(L._NET_DELETE).click()
        logger.info("인터페이스 삭제 완료")

    def click_network_subnet_tab(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_SUBNET_TAB).click()
        logger.info("서브넷 탭 클릭 완료")
        
    def create_subnet(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_SUBNET_TAB).click()
        self.wait_clickable(L.NET_CREATE_BTN).click()
        self.wait_clickable(L.NET_INPUT_NAME).clear()
        self.wait_clickable(L.NET_INPUT_NAME).send_keys("team_subnet_04")
        self.wait_clickable(L.NET_SUBNET_ATTACHED_VIRTUAL_NETWORK).click()
        self.wait_presence(L.NET_ATTACHED_VIRTUAL_NETWORK).click()
        self.wait_clickable(L.NET_CREATE).click()
        logger.info("서브넷 생성 완료")
    
    def click_created_subnet(self):
        self.wait_clickable(L.NET_SUBNET_TEAM4).click()
        logger.info("생성된 서브넷 클릭 완료")

    def modify_subnet_name(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_SUBNET_TAB).click()
        self.wait_clickable(L.NET_SUBNET_TEAM4).click()
        self.wait_clickable(L.NET_EDIT).click()
        self.wait_clickable(L.NET_INPUT_NAME).clear()
        self.wait_clickable(L.NET_INPUT_NAME).send_keys("team_subnet_modify_04")
        self.wait_clickable(L.NET_SAVE).click()
        logger.info("서브넷 이름 수정 완료")
    
    def modify_subnet_cancel(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_SUBNET_TAB).click()
        self.wait_clickable(L.NET_SUBNET_MODIFY_NAME).click()
        self.wait_clickable(L.NET_EDIT).click()
        self.wait_clickable(L.NET_CANCEL).click()
        logger.info("서브넷 이름 수정 취소 완료")
    
    def delete_subnet(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_SUBNET_TAB).click()
        self.wait_clickable(L.NET_SUBNET_MODIFY_NAME).click()
        self.wait_clickable(L.NET_DELETE).click()
        self.wait_clickable(L._NET_DELETE).click()
        logger.info("서브넷 삭제 완료")

    def click_network_virtual_network_tab(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_TAB).click()
        logger.info("가상 네트워크 탭 클릭 완료")

    def create_virtual_network(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_TAB).click()
        self.wait_clickable(L.NET_CREATE_BTN).click()
        self.wait_clickable(L.NET_INPUT_NAME).clear()
        self.wait_clickable(L.NET_INPUT_NAME).send_keys("team_virtual_network_04")
        self.wait_clickable(L.NET_CREATE).click()
        logger.info("가상 네트워크 생성 완료")

    def click_created_virtual_network(self):
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_TEAM4).click()
        logger.info("생성된 가상 네트워크 클릭 완료")
    
    def modify_virtual_network_name(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_TAB).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_TEAM4).click()
        self.wait_clickable(L.NET_EDIT).click()
        self.wait_clickable(L.NET_INPUT_NAME).clear()
        self.wait_clickable(L.NET_INPUT_NAME).send_keys("team_virtual_network_modify_04")
        self.wait_clickable(L.NET_SAVE).click()
        logger.info("가상 네트워크 이름 수정 완료")
    
    def modify_virtual_network_cancel(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_TAB).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_MODIFY_NAME).click()
        self.wait_clickable(L.NET_EDIT).click()
        self.wait_clickable(L.NET_CANCEL).click()
        logger.info("가상 네트워크 이름 수정 취소 완료")

    def virtual_network_firewall_tab(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_TAB).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_MODIFY_NAME).click()
        self.wait_clickable(L.NET_FIREWALL_ADD_BTN).click()
        logger.info("가상 네트워크 방화벽 추가 버튼 클릭 완료")

    def virtual_network_firewall_cancel(self):
        self.wait_clickable(L.NET_FIREWALL_BTN_CANCEL).click()
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_TAB).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_MODIFY_NAME).click()
        self.wait_clickable(L.NET_FIREWALL_ADD_BTN).click()
        self.wait_clickable(L.NET_FIREWALL_BTN_CANCEL).click()
        logger.info("가상 네트워크 방화벽 추가 취소 버튼 클릭 완료")

    def virtual_network_firewall_add_1(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_TAB).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_MODIFY_NAME).click()
        self.wait_clickable(L.NET_FIREWALL_ADD_BTN).click()
        self.wait_clickable(L.NET_FIREWALL_RADIO_PROTOCOL_ALL).click()
        
        # input clear 이슈 해결을 위해 Keys 활용
        self.wait_presence(L.NET_FIREWALL_RADIO_SOURCE).send_keys(Keys.CONTROL + "a")
        self.wait_presence(L.NET_FIREWALL_RADIO_SOURCE).send_keys(Keys.BACK_SPACE)
        self.wait_presence(L.NET_FIREWALL_RADIO_SOURCE).send_keys("192.168.1.1")
        
        self.wait_presence(L.NET_FIREWALL_RADIO_DESTINATION).send_keys(Keys.CONTROL + "a")
        self.wait_presence(L.NET_FIREWALL_RADIO_DESTINATION).send_keys(Keys.BACK_SPACE)
        self.wait_presence(L.NET_FIREWALL_RADIO_DESTINATION).send_keys("192.168.1.1")
        
        self.wait_clickable(L.NET_FIREWALL_BTN_ADD_RULE).click()
        logger.info("가상 네트워크 방화벽1 추가 완료")

    def virtual_network_firewall_add_2(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_TAB).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_MODIFY_NAME).click()
        self.wait_clickable(L.NET_FIREWALL_ADD_BTN_2).click()
        self.wait_clickable(L.NET_FIREWALL_RADIO_PROTOCOL_TCP).click()
        self.wait_clickable(L.NET_FIREWALL_BTN_ADD_RULE).click()
        logger.info("가상 네트워크 방화벽2 추가 완료")

    def virual_network_firewall_order_change(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_TAB).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_MODIFY_NAME).click()
        self.wait_clickable(L.NET_FIREWALL_CHANGE_ORDER).click()
        self.wait_clickable(L.NET_FIREWALL_DOWN_ORDER).click()
        self.wait_clickable(L.NET_DONE).click()
        logger.info("가상 네트워크 방화벽 순서 변경 완료")

    def delete_virtual_network(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_TAB).click()
        self.wait_clickable(L.NET_VIRTUAL_NETWORK_MODIFY_NAME).click()
        self.wait_clickable(L.NET_DELETE).click()
        self.wait_clickable(L._NET_DELETE).click()
        logger.info("가상 네트워크 삭제 완료")

    def public_ip_tab(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_PUBLIC_IP_TAB).click()
        logger.info("공인 IP 탭 클릭 완료")

    def click_create_public_ip(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_PUBLIC_IP_TAB).click()
        self.wait_clickable(L.NET_CREATE_BTN).click()
        
        logger.info("공인 IP 생성 클릭 완료")

    def click_cancel_public_ip(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_PUBLIC_IP_TAB).click()
        self.wait_clickable(L.NET_CREATE_BTN).click()
        self.wait_clickable(L.NET_CANCEL).click()
        
        logger.info("공인 IP 생성 취소 클릭 완료")

    def create_public_ip(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_PUBLIC_IP_TAB).click()
        self.wait_clickable(L.NET_CREATE_BTN).click()
        self.wait_clickable(L.NET_CREATE).click()
        logger.info("공인 IP 생성 완료")

    def modify_public_ip_interface(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_PUBLIC_IP_TAB).click()
        self.wait_clickable(L.NET_PUBLIC_IP_LAST_ITEM).click()
        self.wait_clickable(L.NET_EDIT).click()
        self.wait_clickable(L.NET_PUBLIC_IP_ATTACHED_INTERFACE).click()
        self.wait_clickable(L.NET_ATTACHED_INTERFACE).click()
        self.wait_clickable(L.NET_SAVE).click()
        logger.info("공인 IP 인터페이스 수정 완료")

    def modify_public_ip_cancel(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_PUBLIC_IP_TAB).click()
        self.wait_clickable(L.NET_PUBLIC_IP_LAST_ITEM).click()
        self.wait_clickable(L.NET_EDIT).click()
        self.wait_clickable(L.NET_CANCEL).click()
        logger.info("공인 IP 인터페이스 수정 취소 완료")

    def modify_public_ip_delete(self):
        self.wait_clickable(L.NET_MENU).click()
        self.wait_clickable(L.NET_PUBLIC_IP_TAB).click()
        self.wait_clickable(L.NET_PUBLIC_IP_LAST_ITEM).click()
        self.wait_clickable(L.NET_EDIT).click()
        ActionChains(self.driver).move_to_element(self.wait_presence(L.NET_PUBLIC_IP_ATTACHED_INTERFACE)).perform()
        self.wait_clickable(L.NET_BTN_DELETE_CHIP).click()
        self.wait_clickable(L.NET_SAVE).click()
        self.wait_clickable(L.NET_DELETE).click()
        self.wait_clickable(L._NET_DELETE).click()
        logger.info("공인 IP 인터페이스 수정 삭제 완료")