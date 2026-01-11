import time
import uuid
import pytest
from src.api.network_fixture import network_with_interface
from src.api.block_storage_fixture import post_block_storage
from src.api.api_method import api_get, api_post, api_patch, api_delete
from tests.conftest import api_headers, api_base_url

ZONE_ID = "0a89d6fa-8588-4994-a6d6-a7c3dc5d5ad0"
INSTANCE_TYPE_ID = "abb0fa6a-dcdf-459d-9313-0f51e35e7632"
CLUSTER_INSTANCE_TYPE_ID = "e97bf9b9-9724-48e3-9653-5fc5a28f684e"

def wait_block_storage_prepared(api_base_url, api_headers, bs_id, timeout=120, interval=3):
    """block_storage 상태가 prepared 될 때까지 대기"""
    end = time.time() + timeout

    last = None
    while time.time() < end:
        res = api_get(api_base_url, f"/user/resource/storage/block_storage/{bs_id}", headers=api_headers)
        data = res.json()
        last = data.get("status")
        if last == "prepared":
            return data
        time.sleep(interval)

    raise AssertionError(f"block_storage가 prepared가 안 됨. last_status={last}, bs_id={bs_id}")

@pytest.fixture
def vm_post(resource_manager, api_base_url, api_headers, network_with_interface, post_block_storage):
    suffix = uuid.uuid4().hex[:8]
    vm_name = f"vm-fixture-{suffix}"

    vm_status, vm_body = resource_manager(
        "/user/resource/compute/virtual_machine",
        json={
            "name": vm_name,
            "zone_id": ZONE_ID,
            "instance_type_id": INSTANCE_TYPE_ID,
            "always_on": False,
            "dr": False,
            "username": "user1",
            "password": "securepass9#",
            "on_init_script": "",
        },
    )
    vm_status_code = vm_status
    nic_id = network_with_interface["id"]
    bs_status, bs_id, bs_name = post_block_storage
    vm_id = vm_body["id"]

    # attach
    api_patch(api_base_url, f"/user/resource/network/network_interface/{nic_id}",
              headers=api_headers, json={"attached_machine_id": vm_id})
    
    # ✅ block storage prepared 대기 (이게 없어서 409)
    wait_block_storage_prepared(api_base_url, api_headers, bs_id, timeout=180, interval=3)

    api_patch(api_base_url, f"/user/resource/storage/block_storage/{bs_id}",
              headers=api_headers, json={"attached_machine_id": vm_id})

    # ✅ 여기서 테스트에 넘겨줌
    yield {"vm_id": vm_id, "nic_id": nic_id, "storage_id": bs_id, "vm_body": vm_body, "vm_status_code": vm_status_code}

    # ✅ teardown: detach 먼저 (API가 지원할 때!)
    # 보통 attached_machine_id를 null로 보내거나 detach 전용 endpoint가 있음
    api_patch(api_base_url, f"/user/resource/storage/block_storage/{bs_id}",
              headers=api_headers, raise_on_error=False, json={"attached_machine_id": None})
    api_patch(api_base_url, f"/user/resource/network/network_interface/{nic_id}",
              headers=api_headers, raise_on_error=False, json={"attached_machine_id": None})

@pytest.fixture
def cluster_post(resource_manager):
    """
    resource_manager로 Cluster 생성 → 자동 정리(DELETE)는 resource_manager가 처리
    반환: {"cluster_id":..., "cluster_name":..., "cluster": <응답json>}
    """
    suffix = uuid.uuid4().hex[:8]
    cluster_name = f"cluster-fixture-{suffix}"

    cluster_post_resp_status, cluster_post_resp_body = resource_manager(
        "/user/resource/compute/virtual_cluster",
        json={
            "name": cluster_name,
            "zone_id": ZONE_ID,
            "instance_type_id": CLUSTER_INSTANCE_TYPE_ID,
        },
    )

    cluster_id = cluster_post_resp_body.get("id") if isinstance(cluster_post_resp_body, dict) else None
    assert cluster_id, f"Cluster 생성 응답에서 id 못 찾음: {cluster_post_resp_body}"

    return {"cluster_post_resp_status": cluster_post_resp_status, "cluster_post_resp_body": cluster_post_resp_body, "cluster_id": cluster_id}
