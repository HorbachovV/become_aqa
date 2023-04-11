# from src.config.config import config
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# class GitHubUi:

#     # def __init__(self):
#     #     pass
#     def user_login(self, element, message):
#         self.driver.find_element(By.ID, element).send_keys(message)

#     def user_password(self, element, message):
#         self.driver.find_element(By.ID, element).send_keys(message)
    
#     def confirm_login(self, element):
#         self.driver.find_element(By.XPATH, element)

#     def error_message(self, element):
#         driver.find_element(By.XPATH, element)

from src.config.config import config
from selenium.webdriver.common.by import By

url = config.get("GITHUB_LOGIN")

class GitHubUi:
    def __init__(self, driver):
        self.driver = driver
        self.url = config.get("GITHUB_LOGIN") #"https://github.com/login"

    def load(self):
        self.driver.get(self.url)

    def maximize_window(self):
        self.driver.maximize_window()

    def get_title(self):
        return self.driver.title

    def enter_username(self, username):
        self.driver.find_element(By.ID, "login_field").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.NAME, "commit").click()

    def get_error_message(self):
        return self.driver.find_element(By.ID, "flash").text