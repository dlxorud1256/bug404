from src.api.api_method import api_get, api_post, api_patch, api_delete
from src.api.compute_fixture import vm_post, cluster_post
from src.api.network_fixture import network_with_interface
from src.api.block_storage_fixture import post_block_storage
  
def test_vm_list_get(api_base_url, api_headers):
    resp = api_get(
        api_base_url,
        "/user/resource/compute/virtual_machine?sort_by=created_desc&count=100",
        headers=api_headers,
    )
    assert resp.status_code == 200

def test_vm_post(api_base_url, api_headers, vm_post):
    vm_post_resp_status = vm_post["vm_status_code"]
    assert vm_post_resp_status == 200
    vm_post_resp_body = vm_post["vm_body"]
    assert vm_post_resp_body is not None

def test_vm_get(api_base_url, api_headers, vm_post):
    vm_id = vm_post["vm_id"]
    vm_get_resp = api_get(
        api_base_url,
        f"/user/resource/compute/virtual_machine/{vm_id}",
        headers=api_headers,
    )
    assert vm_get_resp.status_code == 200
    vm_get_body = vm_get_resp.json()
    assert vm_get_body is not None

def test_vm_patch(api_base_url, api_headers, vm_post):
    vm_id = vm_post["vm_id"]
    
    patch_resp = api_patch(
        api_base_url,
        f"/user/resource/compute/virtual_machine/{vm_id}",
        headers=api_headers,
        json={"name": "team4-patch"},
    )
    assert patch_resp.status_code == 200

def test_vm_delete(api_base_url, api_headers, vm_post):
    vm_id = vm_post["vm_id"]
    nic_id = vm_post["nic_id"]
    bs_id = vm_post["storage_id"]
    
    api_patch(api_base_url, f"/user/resource/storage/block_storage/{bs_id}",
              headers=api_headers, raise_on_error=False, json={"attached_machine_id": None})
    api_patch(api_base_url, f"/user/resource/network/network_interface/{nic_id}",
              headers=api_headers, raise_on_error=False, json={"attached_machine_id": None})

    api_delete(
        api_base_url,
        f"/user/resource/storage/block_storage/{bs_id}",
        headers=api_headers,
    )
    api_delete(
        api_base_url,
        f"/user/resource/network/network_interface/{nic_id}",
        headers=api_headers,
    )
    delete_resp = api_delete(
        api_base_url,
        f"/user/resource/compute/virtual_machine/{vm_id}",
        headers=api_headers,
    )
    assert delete_resp.status_code in (200, 202, 204)
    assert delete_resp.json()["status"] == "deleted"

def test_vm_get_invalid_token_returns_403(api_base_url, api_headers):
    bad_headers = dict(api_headers)
    bad_headers["Authorization"] = "Bearer INVALID_TOKEN_123"

    resp = api_get(
        api_base_url,
        "/user/resource/compute/virtual_machine?sort_by=created_desc&count=100",
        headers=bad_headers,
        raise_on_error=False,
    )

    assert resp.status_code in (401, 403), f"예상 외 응답: {resp.status_code}, {resp.text}"
    assert resp.json().get("code") == "wrong_token_format"

def test_vm_post_missing_name_returns_422(api_base_url, api_headers):
    payload = {
        "zone_id": "0a89d6fa-8588-4994-a6d6-a7c3dc5d5ad0",
        "instance_type_id": "abb0fa6a-dcdf-459d-9313-0f51e35e7632",
        "always_on": False,
        "dr": False,
        "username": "user1",
        "password": "securepass9#",
        "on_init_script": "",
    }

    resp = api_post(
        api_base_url,
        "/user/resource/compute/virtual_machine",
        headers=api_headers,
        json=payload,
        raise_on_error=False,
    )

    assert resp.status_code == 422, f"예상 외 응답: {resp.status_code}, {resp.text}"

def test_vm_post_invalid_username_returns_422(api_base_url, api_headers):
    payload = {
        "name": "test-vm-invalid-username",
        "zone_id": "0a89d6fa-8588-4994-a6d6-a7c3dc5d5ad0",
        "instance_type_id": "abb0fa6a-dcdf-459d-9313-0f51e35e7632",
        "always_on": False,
        "dr": False,
        "username": "invalid username!",  # 공백 및 특수문자 포함
        "password": "securepass9#",
        "on_init_script": "",
    }

    resp = api_post(
        api_base_url,
        "/user/resource/compute/virtual_machine",
        headers=api_headers,
        json=payload,
        raise_on_error=False,
    )

    assert resp.status_code == 422, f"예상 외 응답: {resp.status_code}, {resp.text}"

def test_vm_post_weak_password_returns_409(api_base_url, api_headers):
    payload = {
        "name": "test-vm-weak-password",
        "zone_id": "0a89d6fa-8588-4994-a6d6-a7c3dc5d5ad0",
        "instance_type_id": "abb0fa6a-dcdf-459d-9313-0f51e35e7632",
        "always_on": False,
        "dr": False,
        "username": "user1",
        "password": "123",  # 너무 약한 비밀번호
        "on_init_script": "",
    }

    resp = api_post(
        api_base_url,
        "/user/resource/compute/virtual_machine",
        headers=api_headers,
        json=payload,
        raise_on_error=False,
    )

    assert resp.status_code == 409, f"예상 외 응답: {resp.status_code}, {resp.text}"
    
def test_vm_allocation_post_and_delete(api_base_url, api_headers, vm_post):
    vm_id = vm_post["vm_id"]
    
    # VM 실행 POST
    alloc_resp = api_post(
        api_base_url,
        "/user/resource/compute/virtual_machine_allocation",
        headers=api_headers,
        json={"machine_id": vm_id, "zone_id": "0a89d6fa-8588-4994-a6d6-a7c3dc5d5ad0"},
    )
    assert alloc_resp.status_code in (200, 201, 202, 204)

    alloc_body = alloc_resp.json()
    alloc_id = alloc_body.get("id")
    assert alloc_id, f"할당 응답에서 id를 못 찾음: {alloc_body}"

    # VM 실행 중지 DELETE
    alloc_del_resp = api_delete(
        api_base_url,
        f"/user/resource/compute/virtual_machine_allocation/{alloc_id}",
        headers=api_headers,
    )
    assert alloc_del_resp.status_code in (200, 202, 204)
    alloc_del_body = alloc_del_resp.json()
    assert alloc_del_body is not None

def test_cluster_list_get(api_base_url, api_headers):
    resp = api_get(
        api_base_url,
        "/user/resource/compute/virtual_cluster?sort_by=created_desc&count=100",
        headers=api_headers,
    )
    assert resp.status_code == 200

def test_cluster_post(api_base_url, api_headers, cluster_post):
    cluster_post_resp_status = cluster_post["cluster_post_resp_status"]
    assert cluster_post_resp_status == 200
    cluster_post_resp_body = cluster_post["cluster_post_resp_body"]
    assert cluster_post_resp_body is not None

def test_cluster_get(api_base_url, api_headers, cluster_post):
    cluster_id = cluster_post["cluster_id"]
    cluster_get_resp = api_get(
        api_base_url,
        f"/user/resource/compute/virtual_cluster/{cluster_id}",
        headers=api_headers,
    )
    assert cluster_get_resp.status_code == 200
    cluster_get_body = cluster_get_resp.json()
    assert cluster_get_body is not None

def test_cluster_patch(api_base_url, api_headers, cluster_post):
    cluster_id = cluster_post["cluster_id"]
    
    patch_resp = api_patch(
        api_base_url,
        f"/user/resource/compute/virtual_cluster/{cluster_id}",
        headers=api_headers,
        json={"name": "team4-cluster-patch"},
    )
    assert patch_resp.status_code == 200

def test_cluster_delete(api_base_url, api_headers, cluster_post):
    cluster_id = cluster_post["cluster_id"]
    
    delete_resp = api_delete(
        api_base_url,
        f"/user/resource/compute/virtual_cluster/{cluster_id}",
        headers=api_headers,
    )
    assert delete_resp.status_code in (200, 202, 204)
    assert delete_resp.json()["status"] == "deleted"


