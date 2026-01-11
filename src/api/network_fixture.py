import pytest
import os
from dotenv import load_dotenv
load_dotenv()
ZONE_ID = os.getenv("ZONE_ID")

@pytest.fixture(scope="function")
def network_with_subnet(resource_manager):
    # 1. virtual network 생성
    network_code, network_body = resource_manager(
        path="/user/resource/network/virtual_network",
        json={
            "name": "test_virtual_network_04",
            "zone_id": ZONE_ID,
            "network_cidr": "192.168.0.0/16",
        }
    )

    # 2. subnet 생성
    subnet_code, subnet_body = resource_manager(
        path="/user/resource/network/subnet",
        json={
            "name": "test_subnet_04",
            "zone_id": ZONE_ID,
            "purpose": "virtual_machine",
            "network_gw": "192.168.0.1/24",
            "attached_network_id": network_body["id"],
        }
    )
    # 3. 테스트에 필요한 최소 정보만 반환
    return network_body, subnet_body

@pytest.fixture(scope="function")
def network_with_interface(resource_manager):
     # 1. virtual network 생성
    network_code, network_body = resource_manager(
        path="/user/resource/network/virtual_network",
        json={
            "name": "test_virtual_network_04",
            "zone_id": ZONE_ID,
            "network_cidr": "192.168.0.0/16",
        }
    )
    # 2. subnet 생성
    subnet_code, subnet_body = resource_manager(
        path="/user/resource/network/subnet",
        json={
            "name": "test_subnet_04",
            "zone_id": ZONE_ID,
            "purpose": "virtual_machine",
            "network_gw": "192.168.0.1/24",
            "attached_network_id": network_body["id"],
        }
    )
    # 3. network interface 생성
    interface_code, interface_body = resource_manager(
        path="/user/resource/network/network_interface",
        json={
            "name": "test_interface_04",
            "zone_id": ZONE_ID,
            "attached_subnet_id": subnet_body["id"],
            "dr": False,
        }
    )
    return interface_body

@pytest.fixture(scope="function")
def network_with_virtual_network(resource_manager):
    # 1. virtual network 생성
    network_code, network_body = resource_manager(
        path="/user/resource/network/virtual_network",
        json={
            "name": "test_virtual_network_04",
            "zone_id": ZONE_ID,
            "network_cidr": "192.168.0.0/16",
        }
    )
    return network_body

@pytest.fixture(scope="function")
def network_with_ip(resource_manager):
    # 1. public ip 생성
    ip_code, ip_body = resource_manager(
        path="/user/resource/network/public_ip",
        json={
            "zone_id": ZONE_ID,
            "dr": False
        }
    )
    return ip_body
