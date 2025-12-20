import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    base_url="https://en.wikipedia.org"
    driver.get(base_url)
    yield driver
    driver.quit()