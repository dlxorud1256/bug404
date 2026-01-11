import os
import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

def do_login(driver):
    wait = WebDriverWait(driver, 15)

    driver.get("https://qatrack.elice.io/eci")

    user = os.getenv("ECI_ID")
    pwd = os.getenv("ECI_PASSWORD")
    if not user or not pwd:
        raise RuntimeError("ECI_ID / ECI_PASSWORD 없음")
    
    wait.until(EC.presence_of_element_located((By.NAME, "loginId"))).send_keys(user)
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(pwd)
    
    # 로그인 버튼 20번 반복
    for i in range(20):
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
            if wait.until(EC.invisibility_of_element_located((By.NAME, "loginId"))):
                break
            else:
                time.sleep(0.5)
        except Exception:
            raise 

def change_language(driver):
    driver.execute_script("window.localStorage.setItem('locale', 'ko-KR');")
    driver.refresh()

def fetch_access_token(driver): 
    wait = WebDriverWait(driver, 15)
    
    wait.until(lambda d: d.execute_script(
        "return window.localStorage.getItem('accessToken') !== null;"
    ))
    token = driver.execute_script("return window.localStorage.getItem('accessToken');")
    if not token:
        raise RuntimeError("토큰 발급 실패")
    return token

def login_and_fetch_token(driver):
    do_login(driver)
    return fetch_access_token(driver)