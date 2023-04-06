from src.config.config import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = config.get("GITHUB_LOGIN")

def test_github_login_page_title():
    driver.get(url)
    driver.maximize_window()
    act_title = driver.title
    assert act_title == "Sign in to GitHub · GitHub"

def test_github_failed_login_page():
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.ID, "login_field").send_keys("HorbachovVL")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[11]').click()
    driver.implicitly_wait(5)
    error_message = driver.find_element(By.XPATH, '//*[@id="js-flash-container"]/div/div/div').text
    assert error_message == "Incorrect username or password."