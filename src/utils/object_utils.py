import random
import string
import time
from src.api import api_method

def _random_suffix(length=4):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_bucket_name(prefix="team4-bucket"):
    return f"{prefix}-{_random_suffix()}"

def generate_user_name(prefix="user4"):
    return f"{prefix}-{_random_suffix()}"

def wait_for_user_activation(user_id, api_base_url, api_headers, timeout=30):
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        response = api_method.api_get(
            api_base_url,
            f"/user/resource/storage/object_storage/user/{user_id}",
            headers=api_headers,
            raise_on_error=False
        )
        user_data = response.json()
        
        if user_data.get("status") == "activated":
            return True
        
        time.sleep(2)
    
    return False

def wait_until_grant_activated(grant_id, api_base_url, api_headers, timeout=20):
    import time
    start = time.time()
    while time.time() - start < timeout:
        res = api_method.api_get(
            api_base_url,
            f"/user/resource/storage/object_storage/user_grant/{grant_id}",
            headers=api_headers,
            raise_on_error=False
        )
        if res.status_code == 200:
            body = res.json()
            if body.get("status") == "activated":
                return True
        time.sleep(1)
    return False

def negative_post_cleanup(api_base_url, path, api_headers, json_data):
    # POST 요청
    response = api_method.api_post(
        api_base_url, 
        path, 
        headers=api_headers, 
        json=json_data, 
        raise_on_error=False
    )
    
    # 만약 200 OK (네거티브 테스트인데 성공해버린 경우)
    if response.status_code == 200:
        try:
            resource_id = response.json().get("id")
            if resource_id:
                api_method.api_delete(
                    api_base_url, 
                    f"{path}/{resource_id}", 
                    headers=api_headers, 
                    raise_on_error=False
                )
        except Exception as e:
            print(f"\n[Cleanup Error] 삭제 중 오류 발생: {e}")
            
    return response