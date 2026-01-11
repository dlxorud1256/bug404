import requests
import src.utils.object_utils as random
import src.api.api_method as api
from src.api.block_storage_fixture import *

#TC-BS-API-001
def test_block_storage_get_all(api_base_url, api_headers):
    items = get_all_with_pagination(
        api_base_url,
        api_headers,
        path="/user/resource/storage/block_storage",
    )
    assert isinstance(items, list)

#TC-BS-API-002
def test_block_storage_post(post_block_storage):
    status, block_id, _ = post_block_storage
    assert block_id and status == 200, f"블록 스토리지 생성 실패:{status}"

#TC-BS-API-003
def test_block_storage_missing_required_fields(api_base_url, api_headers, zone_id):
    payload = {
        "dr": False,
        "name": "",
        "image_id": None,
        "size_gib": "",
        "snapshot_id": None,
        "zone_id": zone_id,
    }
    
    response = api.api_post(
        base_url=api_base_url,
        path="/user/resource/storage/block_storage",
        headers=api_headers,
        json=payload,
        raise_on_error=False,
    )
    assert response.status_code == 422, f"블록 스토리지 필수 입력 누락 유효성 검사 실패: {response.status_code}"

#TC-BS-API-004
def test_block_storage_range_value(api_base_url, api_headers, zone_id):
    payload = {
        "dr": False,
        "name": random._random_suffix(),
        "image_id": None,
        "size_gib": 9,
        "snapshot_id": None,
        "zone_id": zone_id,
    }
    
    response=api.api_post(
        base_url=api_base_url,
        path="/user/resource/storage/block_storage",
        headers=api_headers,
        json=payload,
        raise_on_error=False,
    )
    assert response.status_code == 422, f"블록 스토리지 범위값 유효성 검사 실패: {response.status_code}"

#TC-BS-API-005
def test_block_storage_duplicate_name(post_block_storage, api_base_url, api_headers, zone_id):
    status, block_id, name = post_block_storage
    assert status == 200 and block_id, f"블록 스토리지 생성 실패:{status}"
    
    payload = {
        "dr": False,
        "name": name,
        "image_id": None,
        "size_gib": 10,
        "snapshot_id": None,
        "zone_id": zone_id,
    }
    
    response = api.api_post(
        base_url=api_base_url,
        path="/user/resource/storage/block_storage",
        headers=api_headers,
        json=payload,
        raise_on_error=False
    )
    assert response.status_code != 200, f"블록 스토리지 중복 이름 생성 테스트 실패:{response.status_code}"

#TC-BS-API-006
def test_block_storage_detail_get(post_block_storage, api_base_url, api_headers):
    status, block_id, _ = post_block_storage
    assert block_id and status == 200, f"블록 스토리지 생성 실패:{status}"
    
    response = api.api_get(
        base_url=api_base_url,
        path=f"/user/resource/storage/block_storage/{block_id}",
        headers=api_headers,
    )
    assert response.status_code == 200, f"블록 스토리지 상세페이지 조회 실패:{response.status_code}"

#TC-BS-API-007
def test_block_storage_patch(post_block_storage, api_base_url, api_headers):
    status, block_id, _ = post_block_storage
    assert block_id and status == 200, f"블록 스토리지 생성 실패:{status}"
    
    payload = {
        "name": "변경된 이름",
    }
    
    response = api.api_patch(
        base_url=api_base_url,
        path=f"/user/resource/storage/block_storage/{block_id}",
        headers=api_headers,
        json=payload,
    )
    assert response.status_code == 200, f"블록 스토리지 수정 실패:{response.status_code}"

#TC-BS-API-008
def test_block_storage_delete(post_block_storage, api_base_url, api_headers):
    status, block_id, _ = post_block_storage
    assert block_id and status == 200, f"블록 스토리지 생성 실패:{status}"

    response = api.api_delete(
        base_url=api_base_url,
        path=f"/user/resource/storage/block_storage/{block_id}",
        headers=api_headers,
    )
    assert response.status_code == 200, f"블록 스토리지 삭제 실패:{response.status_code}"

#TC-BS-API-009
def test_snapshot_get_all(api_base_url, api_headers):
    items = get_all_with_pagination(
        api_base_url,
        api_headers,
        path="/user/resource/storage/block_storage/snapshot",
    )
    assert isinstance(items, list)

#TC-BS-API-010
def test_snapshot_post(post_snapshot):
    status, snapshot_id, _ = post_snapshot
    assert snapshot_id and status == 200, f"스냅샷 생성 실패:{status}"

#TC-BS-API-011
def test_snapshot_missing_required_fields(api_base_url, api_headers, zone_id):
    payload = {
        "block_storage_id": "",
        "name": "",
        "zone_id": zone_id,
    }
    
    response = api.api_post(
        base_url=api_base_url,
        path="/user/resource/storage/block_storage/snapshot",
        headers=api_headers,
        json=payload,
        raise_on_error=False,
    )
    assert response.status_code == 422, f"스냅샷 필수 입력 누락 유효성 검사 실패: {response.status_code}"

#TC-BS-API-012
def test_snapshot_duplicate_name(post_snapshot, api_base_url, api_headers, zone_id):
    status, snapshot_id, name = post_snapshot
    assert status == 200 and snapshot_id, f"스냅샷 생성 실패:{status}"
    
    payload = {
        "block_storage_id": "4df3452d-07e8-4bfe-a874-2df672212d61",
        "name": name,
        "zone_id": zone_id,
    }
    
    response = api.api_post(
        base_url=api_base_url,
        path="/user/resource/storage/block_storage/snapshot",
        headers=api_headers,
        json=payload,
        raise_on_error=False,
    )
    assert response.status_code != 200, f"스냅샷 중복 이름 생성 테스트 실패:{response.status_code}"

#TC-BS-API-013
def test_snapshot_detail_get(post_snapshot, api_base_url, api_headers):
    status, snapshot_id, _ = post_snapshot
    assert snapshot_id and status == 200, f"스냅샷 생성 실패:{status}"
    
    response = api.api_get(
        base_url=api_base_url,
        path=f"/user/resource/storage/block_storage/snapshot/{snapshot_id}",
        headers=api_headers,
    )
    assert response.status_code == 200, f"스냅샷 상세페이지 조회 실패:{response.status_code}"

#TC-BS-API-014
def test_snapshot_patch(post_snapshot, api_base_url, api_headers):
    status, snapshot_id, _ = post_snapshot
    assert snapshot_id and status == 200, f"스냅샷 생성 실패:{status}"
    
    payload = {
        "name": "변경된 이름",
    }
    
    response = api.api_patch(
        base_url=api_base_url,
        path=f"/user/resource/storage/block_storage/snapshot/{snapshot_id}",
        headers=api_headers,
        json=payload,
    )
    assert response.status_code == 200, f"스냅샷 수정 실패:{response.status_code}"

#TC-BS-API-015
def test_snapshot_delete(post_snapshot, api_base_url, api_headers):
    status, snapshot_id, _ = post_snapshot
    assert snapshot_id and status == 200, f"스냅샷 생성 실패:{status}"

    response = api.api_delete(
        base_url=api_base_url,
        path=f"/user/resource/storage/block_storage/snapshot/{snapshot_id}",
        headers=api_headers,
    )
    assert response.status_code == 200, f"스냅샷 삭제 실패:{response.status_code}"

#TC-BS-API-016
def test_snapshot_scheduler_get_all(api_base_url, api_headers):
    items = get_all_with_pagination(
        api_base_url,
        api_headers,
        path="/user/resource/storage/block_storage/snapshot_scheduler",
    )
    assert isinstance(items, list)

#TC-BS-API-017
def test_snapshot_scheduler_post(post_snapshot_scheduler):
    status, snapshot_scheduler_id, _ = post_snapshot_scheduler
    assert snapshot_scheduler_id and status == 200, f"스냅샷 스케줄러 생성 실패:{status}"

#TC-BS-API-018
def test_snapshot_scheduler_missing_required_fields(api_base_url, api_headers, zone_id):
    payload = {
        "zone_id":zone_id,
        "name":"",
        "block_storage_id":"",
        "cron_expression":"",
        "max_snapshots":"",
        "tags":{}
    }
    
    response = api.api_post(
        base_url=api_base_url,
        path="/user/resource/storage/block_storage/snapshot_scheduler",
        headers=api_headers,
        json=payload,
        raise_on_error=False,
    )
    assert response.status_code == 422, f"스냅샷 스케줄러 필수 입력 누락 유효성 검사 실패: {response.status_code}"

#TC-BS-API-019
def test_snapshot_scheduler_cron(api_base_url, api_headers, zone_id):
    payload = {
        "zone_id":zone_id,
        "name":random._random_suffix(),
        "block_storage_id":"4df3452d-07e8-4bfe-a874-2df672212d61",
        "cron_expression":"2 1000 * * * * * * *",
        "max_snapshots":7,
        "tags":{}
    }    
        
    response=api.api_post(
        base_url=api_base_url,
        path="/user/resource/storage/block_storage/snapshot_scheduler",
        headers=api_headers,
        json=payload,
        raise_on_error=False,
    )
    assert response.status_code == 409, f"스냅샷 스케줄러 cron 표현식 유효성 검사 실패: {response.status_code}"

#TC-BS-API-020
def test_snapshot_scheduler_duplicate_name(post_snapshot_scheduler, api_base_url, api_headers, zone_id):
    status, snapshot_scheduler_id, name = post_snapshot_scheduler
    assert status == 200 and snapshot_scheduler_id, f"스냅샷 스케줄러 생성 실패:{status}"
    
    payload = {
        "zone_id":zone_id,
        "name":name,
        "block_storage_id":"4df3452d-07e8-4bfe-a874-2df672212d61",
        "cron_expression":"2 4 * * *",
        "max_snapshots":7,
        "tags":{}
    }
    
    response = api.api_post(
        base_url=api_base_url,
        path="/user/resource/storage/block_storage/snapshot_scheduler",
        headers=api_headers,
        json=payload,
        raise_on_error=False
    )
    assert response.status_code == 422, f"스냅샷 스케줄러 중복 이름 생성 테스트 실패:{response.status_code}"
    
#TC-BS-API-021
def test_snapshot_scheduler_detail_get(post_snapshot_scheduler, api_base_url, api_headers):
    status, snapshot_scheduler_id, _ = post_snapshot_scheduler
    assert snapshot_scheduler_id and status == 200, f"블록 스토리지 생성 실패:{status}"
    
    response = api.api_get(
        base_url=api_base_url,
        path="/user/resource/storage/block_storage/snapshot_scheduler",
        headers=api_headers,
    )
    assert response.status_code == 200, f"스냅샷 스케줄러 상세페이지 조회 실패:{response.status_code}"

#TC-BS-API-022
def test_snapshot_scheduler_patch(post_snapshot_scheduler, api_base_url, api_headers):
    status, snapshot_scheduler_id, _ = post_snapshot_scheduler
    assert snapshot_scheduler_id and status == 200, f"스냅샷 스케줄러 생성 실패:{status}"
    
    payload = {
        "name": "변경된 이름",
    }
    
    response = api.api_patch(
        base_url=api_base_url,
        path=f"/user/resource/storage/block_storage/snapshot_scheduler/{snapshot_scheduler_id}",
        headers=api_headers,
        json=payload,
    )
    assert response.status_code == 200, f"스냅샷 스케줄러 수정 실패:{response.status_code}"

#TC-BS-API-023
def test_snapshot_scheduler_delete(post_snapshot_scheduler, api_base_url, api_headers):
    status, snapshot_scheduler_id, _ = post_snapshot_scheduler
    assert snapshot_scheduler_id and status == 200, f"스냅샷 스케줄러 생성 실패:{status}"

    response = api.api_delete(
        base_url=api_base_url,
        path=f"/user/resource/storage/block_storage/snapshot_scheduler/{snapshot_scheduler_id}",
        headers=api_headers,
    )
    assert response.status_code == 200, f"스냅샷 스케줄러 삭제 실패:{response.status_code}"