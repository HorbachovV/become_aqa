from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()