from src.api.api_method import *
from src.api.network_fixture import *

def test_networkinterface_get(api_base_url, api_headers):
    response = api_get(api_base_url, "/user/resource/network/network_interface", headers=api_headers, raise_on_error=False)
    assert response.status_code == 200, f"네트워크 인터페이스 불러오기 실패, 상태코드: {response.status_code}"

def test_networkinterface_post(resource_manager, network_with_subnet, zone_id):
    network_body, subnet_body = network_with_subnet
    
    interface_code, interface_body = resource_manager(
        path="/user/resource/network/network_interface",
        json={
            "name":"test_interface_04",
            "zone_id":zone_id,
            "attached_subnet_id":subnet_body["id"],
            "dr":False}
    )
    assert interface_code == 200, f"네트워크 인터페이스 생성 실패, 상태코드: {interface_code}"
    
def test_networkinterface_specific_get(network_with_interface, api_base_url, api_headers):
    interface_body = network_with_interface

    response = api_get(
        api_base_url,
        f"/user/resource/network/network_interface/{interface_body['id']}",
        headers=api_headers,     
    )
    assert response.status_code == 200, f"네트워크 인터페이스 특정 조회 실패, 상태코드: {response.status_code}"

def test_networkinterface_specific_patch(network_with_interface, api_base_url, api_headers):
    interface_body = network_with_interface

    response = api_patch(
        api_base_url,
        f"/user/resource/network/network_interface/{interface_body['id']}",
        headers=api_headers,
        json={"name": "test_04_modified"}
    )
    assert response.status_code == 200, f"네트워크 인터페이스 특정 수정 실패, 상태코드: {response.status_code}"
    
def test_networkinterface_delete(network_with_interface, api_base_url, api_headers):
    interface_body = network_with_interface

    response = api_delete(
        api_base_url,
        f"/user/resource/network/network_interface/{interface_body['id']}",
        headers=api_headers
    )
    assert response.status_code == 200, f"네트워크 인터페이스 삭제 실패, 상태코드: {response.status_code}"
    
def test_networksubnet_get(api_base_url, api_headers):
    response = api_get(
        api_base_url,
        "/user/resource/network/subnet",
        headers=api_headers
    )
    assert response.status_code == 200, f"네트워크 서브넷 불러오기 실패, 상태코드: {response.status_code}"

def test_networksubnet_post(network_with_virtual_network, resource_manager, zone_id):
    network_body = network_with_virtual_network
    
    subnet_code, subnet_body = resource_manager(
        path="/user/resource/network/subnet",
        json={
            "name": "test_subnet_04",
            "zone_id": zone_id,
            "purpose": "virtual_machine",
            "network_gw": "192.168.0.1/24",
            "attached_network_id": network_body["id"],
        }
    )
    assert subnet_code == 200, f"네트워크 서브넷 생성 실패, 상태코드: {subnet_code}"

def test_networksubnet_specific_get(api_base_url, api_headers, network_with_subnet):
    network_body, subnet_body = network_with_subnet
        
    response = api_get(
        api_base_url,
        f"/user/resource/network/subnet/{subnet_body['id']}",
        headers=api_headers
    )
    assert response.status_code == 200, f"네트워크 서브넷 특정 조회 실패, 상태코드: {response.status_code}"

def test_networksubnet_specific_patch(api_base_url, api_headers, network_with_subnet):
    network_body, subnet_body = network_with_subnet
    response = api_patch(
        api_base_url,
        f"/user/resource/network/subnet/{subnet_body['id']}",
        headers=api_headers,
        json={"name": "test_network_subnet_04_modified"}
    )
    assert response.status_code == 200, f"네트워크 서브넷 특정 수정 실패, 상태코드: {response.status_code}"

def test_networksubnet_specific_delete(api_base_url, api_headers, network_with_subnet):
    network_body, subnet_body = network_with_subnet

    response = api_delete(
        api_base_url,
        f"/user/resource/network/subnet/{subnet_body['id']}",
        headers=api_headers
    )
    assert response.status_code == 200, f"네트워크 서브넷 특정 삭제 실패, 상태코드: {response.status_code}"

def test_virtualnetwork_get(api_base_url, api_headers):
    get = api_get(
        api_base_url,
        "/user/resource/network/virtual_network",
        headers=api_headers
    )
    assert get.status_code == 200, f"네트워크 가상 네트워크 불러오기 실패, 상태코드: {get.status_code}"
    
def test_virtualnetwork_post(resource_manager, zone_id):
    virtual_code, virtual_body = resource_manager(
        path="/user/resource/network/virtual_network",
        json={
            "name":"virtual_network_test_04",
            "zone_id":zone_id,
            "network_cidr":"192.168.0.0/16"}
    )
    assert virtual_code == 200, f"네트워크 가상 네트워크 생성 실패, 상태코드: {virtual_code}"

def test_virtualnetwork_specific_get(api_base_url, api_headers, network_with_virtual_network):
    network_body = network_with_virtual_network
    
    response = api_get(
        api_base_url,
        f"/user/resource/network/virtual_network/{network_body['id']}",
        headers=api_headers
    )
    assert response.status_code == 200, f"네트워크 가상 네트워크 특정 조회 실패, 상태코드: {response.status_code}"

def test_virtualnetwork_specific_patch(api_base_url, api_headers, network_with_virtual_network):
    network_body = network_with_virtual_network

    response = api_patch(
        api_base_url,
        f"/user/resource/network/virtual_network/{network_body['id']}",
        headers=api_headers,
        json={"name": "virtual_network_test_04_modified"}
    )
    assert response.status_code == 200, f"네트워크 가상 네트워크 특정 수정 실패, 상태코드: {response.status_code}"
    
def test_virtualnetwork_delete(api_base_url, api_headers, network_with_virtual_network):
    network_body = network_with_virtual_network

    response = api_delete(
        api_base_url,
        f"/user/resource/network/virtual_network/{network_body['id']}",
        headers=api_headers
    )
    assert response.status_code == 200, f"네트워크 가상 네트워크 특정 삭제 실패, 상태코드: {response.status_code}"

def test_ip_get(api_base_url, api_headers):
    response = api_get(
        api_base_url,
        "/user/resource/network/public_ip",
        headers=api_headers
    )
    assert response.status_code == 200, f"네트워크 IP 불러오기 실패, 상태코드: {response.status_code}"

def test_ip_post(resource_manager, zone_id):
    ip_code, ip_body = resource_manager(
        path="/user/resource/network/public_ip",
        json={
            "zone_id": zone_id,
            "dr": False
        }
    )
    assert ip_code == 200, f"네트워크 IP 생성 실패, 상태코드: {ip_code}"

def test_ip_specific_get(network_with_ip, api_base_url, api_headers):
    ip_body = network_with_ip
    response = api_get(
        api_base_url,
        f"/user/resource/network/public_ip/{ip_body['id']}",
        headers=api_headers
    )
    assert response.status_code == 200, f"네트워크 IP 특정 조회 실패, 상태코드: {response.status_code}"

def test_ip_specific_patch(network_with_ip, api_base_url, api_headers, network_with_interface):
    interface_body = network_with_interface
    ip_body = network_with_ip
    
    response = api_patch(
        api_base_url,
        f"/user/resource/network/public_ip/{ip_body['id']}",
        headers=api_headers,
        json={"attached_network_interface_id": interface_body['id']}
    )
    assert response.status_code == 200, f"네트워크 IP 특정 수정 실패, 상태코드: {response.status_code}"
    
    disconnect_response = api_patch(
        api_base_url,
        f"/user/resource/network/public_ip/{ip_body['id']}",
        headers=api_headers,
        json={"attached_network_interface_id": None} # 원상복구
    )   
    assert disconnect_response.status_code == 200, f"네트워크 IP 원상 복구 실패, 상태코드: {disconnect_response.status_code}"

def test_ip_specific_delete(network_with_ip, api_base_url, api_headers):
    ip_body = network_with_ip

    response = api_delete(
        api_base_url,
        f"/user/resource/network/public_ip/{ip_body['id']}",
        headers=api_headers
    )
    assert response.status_code == 200, f"네트워크 IP 특정 삭제 실패, 상태코드: {response.status_code}"

def test_no_header(api_base_url):
    response = api_get(
        api_base_url,
        "/user/resource/network/network_interface",
        raise_on_error=False
    )
    assert response.status_code == 401, f"헤더 없이 성공 치명적 문제 발생, 상태코드: {response.status_code}"

def test_wrong_jsonformat(resource_manager, network_with_subnet, zone_id):
    network_body, subnet_body = network_with_subnet
    
    interface_code, interface_body = resource_manager(
        path="/user/resource/network/network_interface",
        json={
            "name":"test_interface_04",
            "zone_id": f"{zone_id}.",
            "attached_subnet_id":subnet_body["id"],
            "dr":False},
        raise_on_error=False
    )
    
    assert interface_code == 422, f"잘못된 JSON 형식 실패, 상태코드: {interface_code}"
    
def test_missing_required_field(resource_manager, zone_id):
    
    interface_code, interface_body = resource_manager(
        path="/user/resource/network/network_interface",    
        json={
            "name":"test_interface_04",
            "zone_id": zone_id,
            "attached_subnet_id":"", # 필수 요소 누락
            "dr":False},
        raise_on_error=False
    )
    assert interface_code == 422, f"필수 필드 누락 확인 필요, 상태코드: {interface_code}"
    
def test_duplicate_name(resource_manager, network_with_subnet, zone_id):
    
    network_body, subnet_body = network_with_subnet
    
    response1_code, response1_body = resource_manager(
        path="/user/resource/network/network_interface",
        json={
            "name":"test_04_duplicate", #이름 중복
            "zone_id": zone_id,
            "attached_subnet_id": subnet_body["id"],
            "dr":False}
    ) 
    assert response1_code == 200, f"네트워크 인터페이스 생성 실패, 상태코드: {response1_code}"
    
    response2_code, response2_body = resource_manager(
        path="/user/resource/network/network_interface",    
        json={
            "name":"test_04_duplicate", #이름 중복
            "zone_id": zone_id,
            "attached_subnet_id": subnet_body["id"],
            "dr":False},
        raise_on_error=False
    )
    assert response2_code == 409, f"네트워크 인터페이스 중복 생성 확인 필요, 상태코드: {response2_code}"

def test_ip_format(resource_manager, network_with_subnet, zone_id):
    network_body, subnet_body = network_with_subnet
    
    ip_code, ip_body = resource_manager(
        path="/user/resource/network/network_interface",
        json={
            "name":"test_ip_format_04",
            "zone_id": zone_id,
            "attached_subnet_id": subnet_body["id"],
            "ip":"999.999.999.999", # ip format 이상한 거 기입
            "dr": False
            },
        raise_on_error=False
    )
    assert ip_code == 422, f"IP 형식 오류 확인 필요, 상태코드: {ip_code}"
    
def test_unnecessary_field(resource_manager, network_with_subnet, zone_id):
    network_body, subnet_body = network_with_subnet
    
    interface_code, interface_body = resource_manager(
        path="/user/resource/network/network_interface",
        json={
            "name":"test_interface_04",
            "zone_id": zone_id,
            "attached_subnet_id":subnet_body["id"],
            "dr":False,
            "unknown_field": "value"  # 불필요한 필드 추가
        },
        raise_on_error=False
    )
    assert interface_code == 400, f"불필요한 필드 추가 확인 필요, 상태코드: {interface_code}"
     
def test_xss_attack_check(api_base_url, api_headers, resource_manager, network_with_subnet, zone_id):
    network_body, subnet_body = network_with_subnet

    interface_code, interface_body = resource_manager(
        path="/user/resource/network/network_interface",
        json={
            "name":"<script>alert('XSS')</script>", # XSS 공격 시도
            "zone_id": zone_id,
            "attached_subnet_id":subnet_body["id"],
            "dr":False}
    )
    assert interface_code == 200, f"네트워크 인터페이스 생성 실패, 상태코드: {interface_code}"
    
    response = api_get(
        api_base_url,
        f"/user/resource/network/network_interface/{interface_body['id']}",
        headers=api_headers,     
    )
    assert response.status_code == 200
    body = response.json()
    assert "<script>alert('XSS')</script>" not in body["name"], "XSS 취약점 존재" #그대로 이름으로 바꾸면 xss 공격에 취약함
    
def test_virtual_network_firewall(network_with_virtual_network, api_base_url, api_headers):
    network_body = network_with_virtual_network
    response = api_patch(
        api_base_url,
        f"/user/resource/network/virtual_network/{network_body['id']}",
        headers=api_headers,
        json={"firewall_rules":[{"proto":"TCP","source":"192.168.0.0/16","destination":"192.168.0.0/16","action":"ACCEPT"}]} #방화벽 설정 추가 (patch로만 가능)
    )
    assert response.status_code == 200, f"방화벽 규칙 설정 실패, 상태코드: {response.status_code}"
    get = api_get(
        api_base_url,
        f"/user/resource/network/virtual_network/{network_body['id']}",
        headers=api_headers
    ) # get으로 추가된 방화벽 설정 확인
    body = get.json() 
    rule = body["firewall_rules"][0]
    
    assert rule["proto"] == "TCP", f"방화벽 규칙이 올바르게 설정되지 않음"
    
def test_virtual_network_firewall_sequence(network_with_virtual_network, api_base_url, api_headers):
    network_body = network_with_virtual_network

    rule_a = {
        "proto": "ALL",
        "source": "192.168.0.0/16",
        "destination": "192.168.0.0/16",
        "action": "ACCEPT"
    }

    rule_b = {
        "proto": "TCP",
        "source": "192.168.0.0/16",
        "destination": "192.168.0.0/16",
        "port": None,
        "port_end": None,
        "action": "ACCEPT",
        "comment": ""
    }

    #A → B 순서로 설정
    res1 = api_patch(
        api_base_url,
        f"/user/resource/network/virtual_network/{network_body['id']}",
        headers=api_headers,
        json={"firewall_rules": [rule_a, rule_b]}
    )
    assert res1.status_code == 200, f"방화벽 설정 실패 {res1.status_code}"

    #GET → A, B 확인
    get1 = api_get(
        api_base_url,
        f"/user/resource/network/virtual_network/{network_body['id']}",
        headers=api_headers
    )
    rules1 = get1.json()["firewall_rules"]

    assert rules1[0]["proto"] == "ALL"
    assert rules1[1]["proto"] == "TCP"

    #B → A 순서로 변경
    res2 = api_patch(
        api_base_url,
        f"/user/resource/network/virtual_network/{network_body['id']}",
        headers=api_headers,
        json={"firewall_rules": [rule_b, rule_a]}
    )
    assert res2.status_code == 200, f"방화벽 설정 실패 {res2.status_code}"

    # GET → B, A 확인
    get2 = api_get(
        api_base_url,
        f"/user/resource/network/virtual_network/{network_body['id']}",
        headers=api_headers
    )
    rules2 = get2.json()["firewall_rules"]

    assert rules2[0]["proto"] == "TCP"
    assert rules2[1]["proto"] == "ALL"
    
def test_virtual_network_firewall_delete(network_with_virtual_network, api_base_url, api_headers):
    network_body = network_with_virtual_network
    
    response1 = api_patch(
        api_base_url,
        f"/user/resource/network/virtual_network/{network_body['id']}",
        headers=api_headers,
        json={"firewall_rules":[{"proto":"ALL","source":"192.168.0.0/16","destination":"192.168.0.0/16","action":"ACCEPT"},{"proto":"TCP","source":"192.168.0.0/16","destination":"192.168.0.0/16","port": None,"port_end": None,"action":"ACCEPT","comment":""}]}
    ) # 방화벽 규칙 설정
    assert response1.status_code ==200, f"방화벽 규칙 생성 실패, 상태코드: {response1.status_code}"
    
    response1 = api_patch(
        api_base_url,
        f"/user/resource/network/virtual_network/{network_body['id']}",
        headers=api_headers,
        json={"firewall_rules": []}
    ) # 방화벽 규칙 삭제
    assert response1.status_code ==200, f"방화벽 규칙 삭제 실패, 상태코드: {response1.status_code}"
    