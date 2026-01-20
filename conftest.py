
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
   
    options = Options()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    base_url = "https://the-internet.herokuapp.com/dropdown"
    driver.get(base_url)
    yield driver
    driver.quit()
