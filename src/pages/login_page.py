import os
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


def login_and_fetch_token(driver) -> str:
    """driver를 받아서 로그인 후 accessToken 반환"""
    wait = WebDriverWait(driver, 10)

    driver.get("https://qatrack.elice.io/eci")

    user = os.getenv("ECI_ID")
    pwd = os.getenv("ECI_PASSWORD")
    if not user or not pwd:
        raise RuntimeError("ECI_ID / ECI_PASSWORD 없음")

    wait.until(EC.presence_of_element_located((By.NAME, "loginId"))).send_keys(user)
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(pwd)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    wait.until(EC.url_contains("home"))

    token = driver.execute_script(
        "return window.localStorage.getItem('accessToken');"
    )
    if not token:
        raise RuntimeError("토큰 발급 실패")

    return token
