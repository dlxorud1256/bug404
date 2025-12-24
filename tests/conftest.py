import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from scripts.get_token import get_valid_token

BASE_URL = "https://portal.gov.elice.cloud/api"


@pytest.fixture(scope="session")
def driver():
    options = Options()
    # options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def api_headers(driver):
    token = get_valid_token(driver)
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Host": "portal.gov.elice.cloud",
    }

@pytest.fixture(scope="session")
def api_base_url():
    return BASE_URL
