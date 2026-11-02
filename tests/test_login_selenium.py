"""Selenium login tests. Start the app first:  python app.py  (or the Docker container).
Override the URL with BASE_URL=http://host:port."""
import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = os.environ.get("BASE_URL", "http://localhost:5000")


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


def login(driver, username, password):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-btn").click()


def test_login_with_valid_credentials(driver):
    login(driver, "admin", "admin123")
    welcome = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "welcome")))
    assert "/menu" in driver.current_url
    assert "Welcome, admin" in welcome.text


@pytest.mark.parametrize(
    "username, password",
    [("admin", "wrongpass"), ("nouser", "admin123"), ("", "")],
)
def test_login_with_invalid_credentials(driver, username, password):
    login(driver, username, password)
    error = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "error")))
    assert "/login" in driver.current_url
    assert error.text == "Invalid username or password"