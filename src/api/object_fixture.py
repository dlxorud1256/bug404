import pytest
from src.utils.object_utils import generate_bucket_name, generate_user_name, wait_for_user_activation

@pytest.fixture(scope="function")
def object_bucket(resource_manager, zone_id):
    bucket_name = generate_bucket_name()
    status, bucket = resource_manager(
        path = "/user/resource/storage/object_storage",
        json = {
            "name": bucket_name,
            "zone_id": zone_id,
            "size_gib": 10,
            "tags": {"description": "4팀 bucket"}
        }
    )
    bucket["name"] = bucket_name
    return status, bucket

@pytest.fixture(scope="function")
def object_user(resource_manager, api_base_url, api_headers, zone_id):
    status, user = resource_manager(
        path = "/user/resource/storage/object_storage/user",
        json = {
            "zone_id": zone_id,
            "name": generate_user_name(),
            "tags": {"team": "user-4team4"}
        }
    )
    activated = wait_for_user_activation(user['id'], api_base_url, api_headers)
    assert activated, "아직 유저 활성화 안됨"
    return status, user

@pytest.fixture(scope="function")
def user_grant(resource_manager, api_base_url, api_headers, zone_id):
    bucket_name = generate_bucket_name()
    _, bucket = resource_manager(
        path = "/user/resource/storage/object_storage",
        json = {
            "name": bucket_name,
            "zone_id": zone_id,
            "size_gib": 10,
            "tags": {"description": "team4 bucket"}
        }
    )

    _, user = resource_manager(
        path = "/user/resource/storage/object_storage/user",
        json = {
            "zone_id": zone_id,
            "name": generate_user_name() + "user2",
            "tags": {"team": "user-4team4"}
        }
    )
    activated = wait_for_user_activation(user["id"], api_base_url, api_headers)
    assert activated, "아직 유저 활성화 안됨"

    status, grant = resource_manager(
        path = "/user/resource/storage/object_storage/user_grant",
        json = {
        "zone_id": zone_id,
        "object_storage_user_id": user["id"],
        "object_storage_id": bucket["id"],
        "permission": "read_only"
        }
    )
    return status, grant
