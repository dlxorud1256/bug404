import pytest
import random
from src.utils.object_utils import generate_bucket_name, wait_until_grant_activated, negative_post_cleanup
import src.api.api_method as api_method

# TC-OS-API-001
def test_dashboard_get(api_base_url, api_headers):
    params = {
        "filter_status": "activated",
        "count": 50
    }
    response = api_method.api_get(
        api_base_url, "/user/resource/storage/object_storage", 
        params=params, headers=api_headers
    )
    
    body = response.json()

    assert response.status_code == 200, f"대시보드 조회 실패: {response.status_code}"
    assert isinstance(body, list), "응답이 리스트 형태가 아님"

    for bucket in body:
        assert "id" in bucket, "'id' 키가 존재하지 않습니다"
        assert "name" in bucket, "'name' 키가 존재하지 않습니다"

# TC-OS-API-002
@pytest.mark.negative
def test_dashboard_count_error(api_base_url, api_headers):
    params = {
        "filter_status": "activated",
        "count": 101
    }

    response = api_method.api_get(
        api_base_url, "/user/resource/storage/object_storage", params=params, headers=api_headers, raise_on_error=False
    )
    assert response.status_code == 422, f"count error code: {response.status_code}"

# TC-OS-API-003
def test_bucket_list_get(api_base_url, api_headers):
    params = {
        "count": 50
    }
    
    response = api_method.api_get(api_base_url, "/user/resource/storage/object_storage", params=params, headers=api_headers)
    body = response.json()

    assert response.status_code == 200, f"전체 버킷 리스트 조회 실패: {response.status_code}"
    
    assert isinstance(body, list), "응답이 리스트 형태가 아님"

    assert len(body) <= 50, "항목 50개 초과"

    for bucket in body:
        assert "id" in bucket, "'id' 키 없음"
        assert "name" in bucket, "'name' 키 없음"

# TC-OS-API-004
def test_bucket_post(object_bucket):
    status_code, bucket = object_bucket
    assert status_code == 200, f"버킷 생성 실패: {status_code}"
    assert "id" in bucket, "'id' 키 없음"

# TC-OS-API-005
@pytest.mark.negative
def test_bucket_name_duplicated_error(api_base_url, api_headers, object_bucket, zone_id):
    _, bucket = object_bucket
    payload = {
        "name": bucket['name'],
        "zone_id": zone_id,
        "size_gib":10,
        "tags":{"description":"이름 중복 검사"}
    }
    response = api_method.api_post(
        api_base_url, "/user/resource/storage/object_storage",
        headers=api_headers,
        json = payload,
        raise_on_error=False
    ) 

    assert response.status_code == 409, f"버킷 이름 중복 생성 성공: {response.status_code}"

# TC-OS-API-006
@pytest.mark.negative
@pytest.mark.parametrize("invalid_name", [
    "한글" + generate_bucket_name(), 
    "name with space", 
    "~name!^_^", 
    "a"*257, 
    "" 
])
def test_bucket_post_validation_name(api_base_url, api_headers, invalid_name, zone_id):
    payload = {
        "name": invalid_name,
        "zone_id": zone_id,
        "size_gib":10,
        "tags":{"description":"이름 유효성 검사"}
    }

    response = negative_post_cleanup(
        api_base_url,
        "/user/resource/storage/object_storage",
        api_headers,
        payload
    )
    
    assert response.status_code == 422, f"버킷 생성 이름 유효성 검사 실패: {response.status_code}, '{invalid_name}' did not return 422"

# TC-OS-API-007
@pytest.mark.negative
def test_bucket_post_validation_size_gib(api_base_url, api_headers, zone_id):
    size = random.randint(1, 9)
    payload = {
        "name": generate_bucket_name(),
        "zone_id": zone_id,
        "size_gib":size,
        "tags":{"description":"사이즈 유효성 검사"}
    }

    response = negative_post_cleanup(
        api_base_url,
        "/user/resource/storage/object_storage",
        api_headers,
        payload
    )
    assert response.status_code == 422, f"버킷 크기 유효성 검사 실패: {response.status_code}, '{size}' did not return 422"

# TC-OS-API-008
def test_bucket_detail_get(api_base_url, api_headers, object_bucket):
    _, bucket = object_bucket
    response = api_method.api_get(
        api_base_url,
        f"/user/resource/storage/object_storage/{bucket['id']}",
        headers=api_headers
    )
    
    assert response.status_code == 200, f"버킷 상세 조회 실패 {response.status_code}"

    body = response.json()
    
    assert isinstance(body, dict), "응답이 dict 형태가 아님"

    assert body["id"] == bucket['id'], "id 값이 요청한 id와 다름"
    assert "name" in body, "'name' 키가 존재하지 않습니다"

# TC-OS-API-012
@pytest.mark.negative
@pytest.mark.parametrize("invalid_name", [
    "수정 테스트" + generate_bucket_name(),
    "with   space", 
    "=:) name!^_^", 
    "a"*257, 
    "" 
])
def test_bucket_validation_patch(api_base_url, api_headers, invalid_name, object_bucket, zone_id):
    _, bucket = object_bucket
    payload = {
        "name": invalid_name, 
        "zone_id": zone_id,
        "size_gib":10,
        "tags":{"description":"변경값"}
    }

    patch_respose = api_method.api_patch(
        api_base_url, f"/user/resource/storage/object_storage/{bucket['id']}",
        headers=api_headers,
        json=payload,
        raise_on_error=False
    )
    assert patch_respose.status_code == 422, f"버킷 이름 수정 유효성 검사: {patch_respose.status_code}, '{invalid_name}' did not return 422"

# TC-OS-API-013
def test_bucket_patch(api_base_url, api_headers, object_bucket, zone_id):
    _, bucket = object_bucket
    payload = {
        "name": generate_bucket_name(),
        "zone_id": zone_id,
        "size_gib":10,
        "tags":{"description":"버킷 수정 성공"}
    }

    patch_respose = api_method.api_patch(
        api_base_url, f"/user/resource/storage/object_storage/{bucket['id']}",
        headers=api_headers,
        json=payload
    )
    assert patch_respose.status_code == 200, f"버킷 수정 실패: {patch_respose.status_code}"

# TC-OS-API-014
def test_bucket_delete(api_base_url, api_headers, object_bucket):
    _, bucket = object_bucket
    response = api_method.api_delete(
        api_base_url,
        f"/user/resource/storage/object_storage/{bucket['id']}",
        headers=api_headers,
        raise_on_error=False
    )
    assert response.status_code == 200, f"버킷 삭제 실패: {response.status_code}"

# TC-OS-API-015 
def test_user_get(api_base_url, api_headers):
    params = {
        "count": 50
    }
    response = api_method.api_get(api_base_url, "/user/resource/storage/object_storage/user", params=params, headers=api_headers)
    
    body = response.json()

    assert response.status_code == 200, f"유저 전제 리스트 조회: {response.status_code}"
    assert isinstance(body, list), "응답이 리스트 형태가 아님"
    assert len(body) <= 50, "항목 50개 초과"

    for user in body:
        assert "id" in user, "'id' 키가 존재하지 않습니다"
        assert "name" in user, "'name' 키가 존재하지 않습니다"

# TC-OS-API-016 
def test_user_post(object_user):
    status_code, user = object_user
    assert status_code == 200, f"유저 생성 실패: {status_code}"
    assert "id" in user, "'id' 키 없음"

# TC-OS-API-017
def test_user_detail_get(api_base_url, api_headers, object_user):
    _, user = object_user
    response = api_method.api_get(
        api_base_url,
        f"/user/resource/storage/object_storage/user/{user['id']}",
        headers=api_headers
    )

    body = response.json()
    assert response.status_code == 200, f"유저 상세 조회 실패: {response.status_code}"
    assert body["id"] == user["id"], "id 값이 요청한 id와 다름"

# TC-OS-API-018
def test_user_auth_post(user_grant):
    status_code, grant = user_grant
    assert status_code == 200, f"사용자 권한 추가 실패: {status_code}"
    assert "id" in grant

# TC-OS-API-019 
def test_user_auth_patch(api_base_url, api_headers, user_grant):
    _, grant = user_grant

    assert wait_until_grant_activated(grant["id"], api_base_url, api_headers), "사용자 권한 생성 timeout"

    payload = {
        "permission":"read_write"
    }

    response = api_method.api_patch(
        api_base_url, f"/user/resource/storage/object_storage/user_grant/{grant['id']}",
        headers=api_headers,
        json = payload,
        raise_on_error = False
    )
    assert response.status_code == 200, f"사용자 권한 수정 실패: {response.status_code}"

# TC-OS-API-020
def test_user_auth_delete(api_base_url, api_headers, user_grant):
    _, grant = user_grant

    response = api_method.api_delete(
        api_base_url,
        f"/user/resource/storage/object_storage/user_grant/{grant['id']}",
        headers=api_headers,
        raise_on_error=False
    )
    assert response.status_code == 200, f"사용자 권한 삭제 실패: {response.status_code}"

# TC-OS-API-021
def test_user_patch(object_user):
    status_code, user = object_user
    assert status_code == 200, f"사용자 정보 수정 실패: {status_code}"
    assert "id" in user

# TC-OS-API-022
def test_user_delete(object_user, api_base_url, api_headers):
    _, user = object_user

    response = api_method.api_delete(
        api_base_url,
        f"/user/resource/storage/object_storage/user/{user['id']}",
        headers=api_headers,
        raise_on_error=False
    )
    assert response.status_code == 200, f"사용자 삭제 실패: {response.status_code}"

## 아래는 데이터 삭제용 코드
# def test_bucket_name_team4_delete(api_base_url, api_headers, object_bucket):
    
#     # 1. 모든 버킷 조회
#     params = {"count": 100}  # 필요한 만큼의 개수를 조회
#     response = api_method.api_get(
#         api_base_url, "/user/resource/storage/object_storage",
#         params=params, headers=api_headers
#     )
#     assert response.status_code == 200, f"버킷 리스트 조회 실패: {response.status_code}"
    
#     buckets = response.json()
    
#     # 2. 이름에 'team4'가 포함된 버킷만 필터링
#     team4_buckets = [b for b in buckets if 'team4' in b.get('name', '')]

#     # 3. 각 버킷 삭제
#     for bucket in team4_buckets:
#         del_resp = api_method.api_delete(
#             api_base_url,
#             f"/user/resource/storage/object_storage/{bucket['id']}",
#             headers=api_headers,
#             raise_on_error=False
#         )
#         assert del_resp.status_code == 200, f"버킷 삭제 실패: {bucket['name']}, 상태코드: {del_resp.status_code}"

# def test_user_name_user4_delete(api_base_url, api_headers):
#     # 1. 모든 사용자 조회
#     params = {"count": 100}  # 필요한 만큼 조회
#     response = api_method.api_get(
#         api_base_url, "/user/resource/storage/object_storage/user",
#         params=params, headers=api_headers
#     )
#     assert response.status_code == 200, f"사용자 리스트 조회 실패: {response.status_code}"

#     users = response.json()

#     # 2. 이름에 'user4'가 포함된 사용자 필터링
#     user4_users = [u for u in users if 'user4' in u.get('name', '')]

#     # 3. 각 사용자 삭제
#     for user in user4_users:
#         del_resp = api_method.api_delete(
#             api_base_url,
#             f"/user/resource/storage/object_storage/user/{user['id']}",
#             headers=api_headers,
#             raise_on_error=False
#         )
#         assert del_resp.status_code == 200, f"사용자 삭제 실패: {user['name']}, 상태코드: {del_resp.status_code}"