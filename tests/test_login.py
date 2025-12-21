from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep
from pages.login_page import LoginPage
class TestLogin:
    def test_login_pass(self, driver):
        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login_button()
        sleep(5)
        assert driver.find_element(By.CSS_SELECTOR,".oxd-text--h6").text=="Dashboard"

    def test_login_fail(self, driver):
        login_page = LoginPage(driver)
        login_page.enter_username("Admin111")
        login_page.enter_password("wrongpassword")
        login_page.click_login_button()
        sleep(5)
        assert driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p']").text=="Invalid credentials"
