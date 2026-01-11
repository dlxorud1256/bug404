import pytest
import src.utils.object_utils as random
import src.api.api_method as api
import pytest

@pytest.fixture(scope="function")
def post_block_storage(resource_manager, zone_id):
    payload = {
        "dr": False,
        "name": random._random_suffix(),
        "image_id": "9e6454a3-8e45-4f8c-89e7-2b156b239898",
        "size_gib": 30,
        "snapshot_id": None,
        "zone_id": zone_id,
    }

    status_code, body = resource_manager(
        "/user/resource/storage/block_storage",
        json=payload,
    )
    name = payload["name"] 
    return status_code, body["id"], name

@pytest.fixture(scope="function")
def post_snapshot(resource_manager, zone_id):
    payload = {
        "block_storage_id": "4df3452d-07e8-4bfe-a874-2df672212d61",
        "name": "테스트 스냅샷",
        "zone_id": zone_id,
    }

    status_code, body = resource_manager(
        "/user/resource/storage/block_storage/snapshot",
        json=payload,
    )
    name = payload["name"]
    return status_code, body["id"], name

@pytest.fixture(scope="function")
def post_snapshot_scheduler(resource_manager, zone_id):
    payload = {
        "zone_id":zone_id,
        "name":random._random_suffix(),
        "block_storage_id":"4df3452d-07e8-4bfe-a874-2df672212d61",
        "cron_expression":"2 4 * * *",
        "max_snapshots":7,
        "tags":{}
    }

    status_code, body = resource_manager(
        "/user/resource/storage/block_storage/snapshot_scheduler",
        json=payload,
    )
    name = payload["name"] 
    return status_code, body["id"], name

def get_all_with_pagination(api_base_url, api_headers, path, count=20):
    all_items = []
    skip = 0

    while True:
        response = api.api_get(
            base_url=api_base_url,
            path=path,
            headers=api_headers,
            params={
                "skip": skip,
                "count": count,
            },
        )

        assert response.status_code == 200, f"조회 실패: {response.status_code}"

        items = response.json()

        if not items:
            break

        all_items.extend(items)

        if len(items) < count:
            break

        skip += count
        
    return all_items