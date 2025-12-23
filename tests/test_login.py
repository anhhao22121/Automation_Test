from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep
from pages.login_page import LoginPage
class TestLogin:
    def test_login_pass(self, driver):
        login_page = LoginPage(driver)
        login_page.do_login("Admin", "admin123")
        sleep(5)
        assert driver.find_element(By.CSS_SELECTOR,".oxd-text--h6").text=="Dashboard"
        sleep(5)

    def test_login_fail(self, driver):
        login_page = LoginPage(driver)
        login_page.do_login("Admin", "admin12") 
        sleep(5)
        assert driver.find_element(By.CLASS_NAME,"oxd-text oxd-text--p oxd-alert-content-text").text=="Invalid credentials"
        sleep(5)
