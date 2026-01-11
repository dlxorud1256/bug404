import pytest
import random
from src.utils.object_utils import *
import src.api.api_method as api_method

# TC-INFRA-API-001
def test_region_get(api_base_url, api_headers):
    params = {
        "count": 50
    }
    response = api_method.api_get(
        api_base_url,
        "/user/region", 
        params=params,
        headers=api_headers
    )
    assert response.status_code == 200, f"리전 정보 조회 실패: {response.status_code}"

# TC-INFRA-API-002
def test_zone_get(api_base_url, api_headers):
    params = {
        "count": 50
    }
    response = api_method.api_get(
        api_base_url,
        "/user/infra/zone", 
        params=params,
        headers=api_headers
    )
    assert response.status_code == 200, f"영역 정보 조회 실패: {response.status_code}"

# TC-INFRA-API-003
def test_instance_type_get(api_base_url, api_headers):
    params = {
        "count": 100
    }
    response = api_method.api_get(
        api_base_url,
        "/user/infra/instance_type", 
        params=params,
        headers=api_headers
    )
    assert response.status_code == 200, f"인스턴스 유형 정보 조회 실패: {response.status_code}"

# TC-INFRA-API-004
def test_block_storage_get(api_base_url, api_headers):
    params = {
        "count": 50
    }
    response = api_method.api_get(
        api_base_url,
        "/user/infra/block_storage_image", 
        params=params,
        headers=api_headers
    )
    assert response.status_code == 200, f"블록 스토리지 이미지 조회 실패: {response.status_code}"

# TC-INFRA-API-005
def test_notice_get(api_base_url, api_headers):
    params = {
        "count": 100
    }
    response = api_method.api_get(
        api_base_url,
        "/user/notice", 
        params=params,
        headers=api_headers
    )

    body = response.json()

    assert response.status_code == 200, f"공지 전체 조회 실패: {response.status_code}"
    assert isinstance(body, list), "공지 목록 응답이 list가 아닙니다"
    assert len(body) > 0, "공지 목록 없음"

# TC-INFRA-API-006
def test_notice_detail_get(api_base_url, api_headers):
    # 1. 공지 목록 조회
    list_response = api_method.api_get(
        api_base_url,
        "/user/notice",
        params={"count": 100},
        headers=api_headers
    )

    assert list_response.status_code == 200, "공지 목록 조회 실패"
    notices = list_response.json()

    random_notice = random.choice(notices)
    notice_id = random_notice["id"]

    detail_response = api_method.api_get(
        api_base_url,
        f"/user/notice{notice_id}",
        headers=api_headers
    )
    assert detail_response.status_code == 200, f"공지 상세 조회 실패: {detail_response.status_code}"

# TC-INFRA-API-007
def test_resource_get(api_base_url, api_headers):
    response = api_method.api_get(
        api_base_url,
        "/user/organization", 
        headers=api_headers
    )
    assert response.status_code == 200, f"리소스 현황 조회 실패: {response.status_code}"