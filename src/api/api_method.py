import requests

def api_request(method, base_url, path, headers=None, raise_on_error=True, **kwargs):
    url = f"{base_url.rstrip('/')}{path}"
    response = requests.request(
        method, url, headers=headers, **kwargs
    )

    if not response.ok and raise_on_error:
        raise AssertionError(
            f"""
            ❌ API 요청 실패
            METHOD: {method}
            URL: {url}
            STATUS: {response.status_code}
            RESPONSE: {response.text}
            """
        )
    return response

def api_get(base_url, path, headers=None, raise_on_error=True, **kwargs):
    return api_request("GET", base_url, path, headers, raise_on_error=raise_on_error, **kwargs)


def api_post(base_url, path, headers=None, raise_on_error=True, **kwargs):
    return api_request("POST", base_url, path, headers, raise_on_error=raise_on_error, **kwargs)


def api_patch(base_url, path, headers=None, raise_on_error=True, **kwargs):
    return api_request("PATCH", base_url, path, headers, raise_on_error=raise_on_error, **kwargs)


def api_delete(base_url, path, headers=None, raise_on_error=True, **kwargs):
    return api_request("DELETE", base_url, path, headers, raise_on_error=raise_on_error, **kwargs)

