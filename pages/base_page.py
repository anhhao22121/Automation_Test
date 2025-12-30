from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest
from time import sleep
class Base_Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        # Locator ở đây là một tuple (By.ID, "value")
        return self.driver.find_element(*locator)

    def click(self, locator):
        # Truyền locator (tuple) vào hàm wait
        element = self.wait_for_element_clickable(locator)
        element.click()

    def wait_for_element_clickable(self, locator, timeout=10):
        # Thêm giá trị mặc định cho timeout (ví dụ: 10 giây)
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator)) # Không dùng * ở đây vì EC nhận tuple