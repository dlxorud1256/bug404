import requests

def test_vm_get(api_base_url, api_headers):
    r = requests.get(
        f"{api_base_url}/user/resource/compute/virtual_machine?sort_by=created_desc&count=100",
        headers=api_headers,
    )
    assert r.status_code == 200

