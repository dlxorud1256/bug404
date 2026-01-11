import os
import pytest
from pathlib import Path
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from src.pages.login_page import do_login

E2E_HOME_URL = "https://qatrack.elice.io/eci"

def _chrome_options():
    options = Options()
    options.add_argument("--lang=ko-KR")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_experimental_option('prefs', {"intl.accept_languages": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"})
    return options

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="module")
def e2e_driver():
    service = None
    
    # 3. Chromedriver 경로 설정 (Docker 환경변수)
    if os.environ.get("CHROME_DRIVER"):
        service = Service(executable_path=os.environ.get("CHROME_DRIVER"))
        
    drv = webdriver.Chrome(service=service, options=_chrome_options())
    drv.execute_cdp_cmd("Emulation.setLocaleOverride", {"locale": "ko-KR"})
    drv.execute_cdp_cmd("Emulation.setTimezoneOverride", {"timezoneId": "Asia/Seoul"})
    try:
        do_login(drv)
        yield drv
    finally:
        drv.quit()

@pytest.fixture(scope="function", autouse=True)
def fail_screenshot(request, e2e_driver):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        out_dir = Path("/app/reports/screenshots")
        out_dir.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = "".join(c if c.isalnum() or c in "._-" else "_" for c in request.node.name)
        e2e_driver.save_screenshot(str(out_dir / f"{safe_name}_{ts}.png"))