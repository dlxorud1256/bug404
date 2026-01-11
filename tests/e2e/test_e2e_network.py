from src.utils.locator import NetworkLocator as L
from src.pages.network_page import NetworkPage

def test_network_menu_loaded(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.click_network_menu()
    
    assert network_page.wait_presence(L.NET_VIRTUAL_NETWORK_TAB), "가상 네트워크 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_SUBNET_TAB), "서브넷 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_NETWORK_INTERFACE_TAB), "네트워크 인터페이스 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_PUBLIC_IP_TAB), "공용 IP 탭이 표시되지 않음"
    
def test_network_interface_tab_loaded(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.click_network_menu()
    network_page.click_network_interface_tab()
    
    assert network_page.wait_presence(L.NET_NAME_TH ), "네트워크 인터페이스 이름 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_STATUS_TH), "네트워크 인터페이스 상태 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_IP_ADDRESS_TH), "네트워크 인터페이스 IP 주소 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_MAC_ADDRESS_TH), "네트워크 인터페이스 MAC 주소 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_DR_TH), "네트워크 인터페이스 재해 복구 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_CREATED_AT_TH), "네트워크 인터페이스 생성일 탭이 표시되지 않음"
    
def test_network_interface_create_loaded(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.click_network_menu()
    network_page.click_network_interface_tab()
    network_page.click_create_btn()
    
    assert network_page.wait_presence(L.NET_CREATE ), "네트워크 인터페이스 생성 탭이 표시되지 않음"
    
def test_network_interface_create_cancel(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.click_network_menu()
    network_page.click_network_interface_tab()
    network_page.click_create_btn()
    network_page.click_cancel_btn()
    
    assert network_page.wait_presence(L.NET_NAME_TH ), "네트워크 인터페이스 이름 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_STATUS_TH), "네트워크 인터페이스 상태 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_IP_ADDRESS_TH), "네트워크 인터페이스 IP 주소 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_MAC_ADDRESS_TH), "네트워크 인터페이스 MAC 주소 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_DR_TH), "네트워크 인터페이스 재해 복구 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_CREATED_AT_TH), "네트워크 인터페이스 생성일 탭이 표시되지 않음"
    
def test_network_interface_create(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.create_interface()
    
    assert network_page.wait_presence(L.NET_INTERFACE_TEAM4), "team4 interface가 생성되지않음"
    
def test_created_interface_load(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.load_created_interface()
    
    assert network_page.wait_presence(L.NET_CHECK_TEAM4_INTERFACE).text == "team4_interface", "이름과 내용이 일치하지않습니다"
    assert network_page.wait_presence(L.NET_CHECK_TEAM4_SUBNET).text == "team4_subnet", "서브넷과 내용이 일치하지않습니다"

def test_modify_interface_name(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.modify_interface_name()
    
    assert network_page.wait_presence(L.NET_INTERFACE_TEAM4_MODIFY).text == "team4_modify_interface", "이름과 내용이 일치하지않습니다"


def test_modify_cancel(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.modify_cancel()
    
    assert network_page.wait_presence(L.NET_INTERFACE_TEAM4_MODIFY).text == "team4_modify_interface", "이름과 내용이 일치하지않습니다"

def test_delete_interface(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.delete_interface()
    
    assert network_page.wait_invisibility_element(L.NET_INTERFACE_MODIFY_NAME), "삭제되지않음"

def test_subnet_load(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.click_network_subnet_tab()
    
    assert network_page.wait_presence(L.NET_NAME_TH ), "네트워크 인터페이스 이름 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_PURPOSE_TH), "네트워크 인터페이스 목적 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_GATEWAY_TH), "네트워크 인터페이스 게이트웨이 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_CREATED_AT_TH), "네트워크 인터페이스 생성일 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_STATUS_TH), "네트워크 인터페이스 상태 탭이 표시되지 않음"

def test_subnet_create(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.create_subnet()
    
    assert network_page.wait_presence(L.NET_SUBNET_TEAM4).text == "team_subnet_04", "이름과 내용이 일치하지않습니다"

def test_created_subnet_load(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.click_network_subnet_tab()
    network_page.click_created_subnet()

    assert network_page.wait_presence(L.NET_CHECK_CREATED_SUBNET).text == "team_subnet_04", "이름과 내용이 일치하지않습니다"

    
def test_subnet_modify_name(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.modify_subnet_name()
    
    assert network_page.wait_presence(L.NET_SUBNET_TEAM4_MODIFY).text == "team_subnet_modify_04", "이름과 내용이 일치하지않습니다"

def test_subnet_modify_cancel(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.modify_subnet_cancel()
    
    assert network_page.wait_presence(L.NET_SUBNET_TEAM4_MODIFY).text == "team_subnet_modify_04", "이름과 내용이 일치하지않습니다"

def test_subnet_delete(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.delete_subnet()
    
    assert network_page.wait_invisibility_element(L.NET_SUBNET_MODIFY_NAME), "삭제되지않음"

def test_virtual_network_load(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.click_network_virtual_network_tab()
    
    assert network_page.wait_presence(L.NET_NAME_TH ), "네트워크 인터페이스 이름 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_CREATED_AT_TH), "네트워크 인터페이스 생성일 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_STATUS_TH), "네트워크 인터페이스 상태 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_NET_CIDR_TH), "네트워크 인터페이스 네트워크 CIDR 탭이 표시되지 않음"
    assert network_page.wait_presence(L.NET_VXLAN_VNI_TH), "네트워크 인터페이스 VXLAN VNI 탭이 표시되지 않음"

def test_virtual_network_create(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.create_virtual_network()
    
    assert network_page.wait_presence(L.NET_VIRTUAL_NETWORK_TEAM4).text == "team_virtual_network_04", "이름과 내용이 일치하지않습니다"

def test_created_virtual_network_load(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.click_network_virtual_network_tab()
    network_page.click_created_virtual_network()
    
    assert network_page.wait_presence(L.NET_CHECK_CREATED_VIRTUAL_NETWORK).text == "team_virtual_network_04", "이름과 내용이 일치하지않습니다"

def test_virtual_network_modify_name(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.modify_virtual_network_name()
    
    assert network_page.wait_presence(L.NET_VIRTUAL_NETWORK_MODIFY).text == "team_virtual_network_modify_04", "이름과 내용이 일치하지않습니다"

def test_virtual_network_firewall_check(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.virtual_network_firewall_tab()
    
    # "규칙 추가" 모달의 주요 텍스트들이 보이는지 검증
    assert network_page.wait_presence(L.NET_FIREWALL_LABEL_PROTOCOL), "프로토콜 라벨이 보이지 않음"
    assert network_page.wait_presence(L.NET_FIREWALL_LABEL_SOURCE), "소스 라벨이 보이지 않음"
    assert network_page.wait_presence(L.NET_FIREWALL_LABEL_DESTINATION), "대상 라벨이 보이지 않음"
    assert network_page.wait_presence(L.NET_FIREWALL_LABEL_PORT), "포트 라벨이 보이지 않음"
    assert network_page.wait_presence(L.NET_FIREWALL_LABEL_ACTION), "액션 라벨이 보이지 않음"
    assert network_page.wait_presence(L.NET_FIREWALL_LABEL_DESCRIPTION), "설명 라벨이 보이지 않음"

def test_virtual_network_firewall_cancel(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.virtual_network_firewall_cancel()
    
    assert network_page.wait_presence(L.NET_VIRTUAL_NETWORK_MODIFY).text == "team_virtual_network_modify_04", "이름과 내용이 일치하지않습니다"

def test_virtual_network_modify_cancel(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.modify_virtual_network_cancel()
    
    assert network_page.wait_presence(L.NET_VIRTUAL_NETWORK_MODIFY).text == "team_virtual_network_modify_04", "이름과 내용이 일치하지않습니다"

def test_virtual_network_firewall_add(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.virtual_network_firewall_add_1()
    
    assert network_page.wait_presence(L.NET_FIREWALL_CHANGE_ORDER), "순서 변경 버튼이 보이지 않음"

def test_virtual_network_firewall_order_change(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.virtual_network_firewall_add_2()
    network_page.virual_network_firewall_order_change()
    
    assert network_page.wait_presence(L.NET_FIREWALL_ROW_1_PROTOCOL).text == "TCP", "순서 변경 버튼이 보이지 않음"

def test_virtual_network_delete(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.delete_virtual_network()
    
    assert network_page.wait_invisibility_element(L.NET_VIRTUAL_NETWORK_MODIFY_NAME), "삭제되지않음"

def test_public_ip_load(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.public_ip_tab()
    
    assert network_page.wait_presence(L.NET_PUBLIC_IP_TH), "공인 IP 탭이 보이지 않음"
    assert network_page.wait_presence(L.NET_DDOS_PROTECTION_TH), "DDOS 방어 탭이 보이지 않음"
    assert network_page.wait_presence(L.NET_STATUS_TH), "상태 탭이 보이지 않음"
    assert network_page.wait_presence(L.NET_DR_TH), "재해 복구 탭이 보이지 않음"
    assert network_page.wait_presence(L.NET_CREATED_AT_TH), "생성일 탭이 보이지 않음"

def test_public_ip_create_click(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.click_create_public_ip()
    
    assert network_page.wait_visibility_element(L.NET_CREATE), "생성 버튼이 보이지 않음"
    assert network_page.wait_visibility_element(L.NET_CANCEL), "취소 버튼이 보이지 않음"

def test_public_ip_create_cancel(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.click_cancel_public_ip()
    
    assert network_page.wait_invisibility_element(L.NET_CREATE), "생성 버튼이 보이지 않음"
    assert network_page.wait_invisibility_element(L.NET_CANCEL), "취소 버튼이 보이지 않음"  

def test_public_ip_create(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.create_public_ip()
    
    assert network_page.wait_invisibility_element(L.NET_CREATE), "생성 버튼이 보이지 않음"
    assert network_page.wait_invisibility_element(L.NET_CANCEL), "취소 버튼이 보이지 않음"
     

def test_public_ip_modify_interface(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.modify_public_ip_interface()
    
    assert network_page.wait_presence(L.NET_PUBLIC_IP_INTERFACE).text == "team04-vm-nic", "이름과 내용이 일치하지않습니다"

def test_public_ip_modify_cancel(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.modify_public_ip_cancel()
    
    assert network_page.wait_presence(L.NET_PUBLIC_IP_INTERFACE).text == "team04-vm-nic", "이름과 내용이 일치하지않습니다"

def test_public_ip_delete(e2e_driver):
    network_page = NetworkPage(e2e_driver)
    network_page.modify_public_ip_delete()
    
    assert network_page.wait_presence(L.NET_PUBLIC_IP_TH), "삭제되지않음"