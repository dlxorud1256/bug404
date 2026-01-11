import csv
import requests
import time


BASE_URL = "https://portal.gov.elice.cloud/api"
ZONE_ID = "0a89d6fa-8588-4994-a6d6-a7c3dc5d5ad0"
HEADERS = {
    "Authorization": f"Bearer {open('token.txt').read().strip()}",
    "Content-Type": "application/json",
    "Host": "portal.gov.elice.cloud"
}

def wait_until_disk_ready(block_id, timeout=300, interval=3):
    end = time.time() + timeout
    last = None

    while time.time() < end:
        res = requests.get(
            f"{BASE_URL}/user/resource/storage/block_storage/{block_id}",
            headers=HEADERS
        )
        res.raise_for_status()
        data = res.json()
        last = data.get("status")
    
        if last in ("prepared"):
            return data

        if last in ("ERROR", "FAILED"):
            raise AssertionError(f"block_storage 생성 실패: {data}")

        time.sleep(interval)

    raise AssertionError(
        f"block_storage가 준비 상태가 안 됨. last_status={last}, bs_id={block_id}"
    )



network = requests.post(
    f"{BASE_URL}/user/resource/network/virtual_network",
    headers=HEADERS,
    json={
        "name": "perf-network-04",
        "zone_id": ZONE_ID,
        "network_cidr": "192.168.0.0/16",
    }
).json()

NETWORK_ID = network["id"]

subnet = requests.post(
    f"{BASE_URL}/user/resource/network/subnet",
    headers=HEADERS,
    json={
        "name": "perf-subnet-04",
        "zone_id": ZONE_ID,
        "purpose": "virtual_machine",
        "network_gw": "192.168.0.1/24",
        "attached_network_id": NETWORK_ID,
    }
).json()
SUBNET_ID = subnet["id"]

VM_COUNT = 3
rows = []

for i in range(VM_COUNT):
    # 인터페이스 생성
    interface_res = requests.post(
        f"{BASE_URL}/user/resource/network/network_interface",
        headers=HEADERS,
        json={
            "name": f"team-4-interface-{i}",
            "zone_id": ZONE_ID,
            "attached_subnet_id": SUBNET_ID,
            "dr": False
        }
    ).json()

    # 블록 스토리지 생성    
    block_storage_res = requests.post(
        f"{BASE_URL}/user/resource/storage/block_storage",
        headers=HEADERS,
        json={
            "dr": False,
            "name": f"team-4-block_storage-{i}",
            "image_id": "9e6454a3-8e45-4f8c-89e7-2b156b239898",
            "size_gib": 30,
            "snapshot_id": None,
            "zone_id": ZONE_ID,
    }
    ).json()
    
    wait_until_disk_ready(block_storage_res["id"],timeout=180, interval=3)

    rows.append({
        "interface_id": interface_res["id"],
        "block_storage_id": block_storage_res["id"]
    })

with open("vm_resources.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["interface_id", "block_storage_id"])
    writer.writeheader()
    writer.writerows(rows)

