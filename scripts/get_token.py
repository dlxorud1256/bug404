import os
import time
import jwt

from src.pages.login_page import login_and_fetch_token

TOKEN_FILE = "token.txt"

def is_token_valid(token: str) -> bool:
    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        exp = decoded.get("exp")
        return exp and exp > time.time()
    except Exception:
        return False

def read_token():
    if not os.path.exists(TOKEN_FILE):
        return None
    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()

def save_token(token: str):
    with open(TOKEN_FILE, "w", encoding="utf-8") as f:
        f.write(token)

def get_valid_token(driver) -> str:
    token = read_token()

    if token and is_token_valid(token):
        return token

    token = login_and_fetch_token(driver)
    save_token(token)
    return token
