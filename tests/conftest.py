import os
import time
import logging
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.api.api_method import api_post, api_delete
from src.auth.get_token import get_valid_token
from src.api.object_fixture import *

logger = logging.getLogger(__name__)
load_dotenv()

def _chrome_options():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--lang=ko-KR")
    options.add_argument("--window-size=1920,1080")
    return options

@pytest.fixture(scope="session")
def api_base_url():
    base_url = os.getenv("API_BASE_URL")
    if not base_url:
        raise RuntimeError("API_BASE_URL이 .env에 없습니다.")
    return base_url

@pytest.fixture(scope="session")
def zone_id():
    zid = os.getenv("ZONE_ID")
    if not zid:
        raise RuntimeError("ZONE_ID가 .env에 없습니다.")
    return zid

@pytest.fixture(scope="session")
def api_driver():
    """토큰 발급 전용 드라이버 (E2E driver와 이름 분리!)"""
    driver = webdriver.Chrome(options=_chrome_options())
    try:
        yield driver
    finally:
        driver.quit()

@pytest.fixture(scope="session")
def api_headers(api_driver):
    token = get_valid_token(api_driver)
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Host": "portal.gov.elice.cloud",
    }

@pytest.fixture(scope="function")
def resource_manager(api_base_url, api_headers):
    created_resources = []

    def create(path, json=None, params=None, raise_on_error=True):
        res = api_post(
            api_base_url, path,
            headers=api_headers,
            json=json, params=params,
            raise_on_error=False
        )
        status_code = res.status_code
        try:
            body = res.json()
        except Exception:
            body = {}

        if status_code == 200 and isinstance(body, dict) and "id" in body:
            created_resources.append((path, body))

        if raise_on_error and status_code != 200:
            raise AssertionError(f"리소스 생성 실패: {res.text}")
        return status_code, body

    yield create

    for path, resource in reversed(created_resources):
        max_retries = 3
        retry_count = 0

        while retry_count < max_retries:
            res = api_delete(
                api_base_url,
                f"{path}/{resource['id']}",
                headers=api_headers,
                raise_on_error=False
            )

            if res.status_code in (200, 204, 404):
                break
            elif res.status_code == 409:
                retry_count += 1
                time.sleep(1)
            else:
                logger.error(f"Cleanup failed for {path}/{resource['id']}: {res.status_code}")
                break