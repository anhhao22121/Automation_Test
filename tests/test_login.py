# ...existing code...
from selenium.webdriver.common.by import By
import pytest
from time import sleep
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader

class TestLogin:
    def test_login_pass(self, driver):
        login_page = LoginPage(driver)
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())
        sleep(3)
        el = driver.find_element(By.CSS_SELECTOR, ".oxd-text--h6")
        assert el.text.strip() == "Dashboard"
        sleep(1)

    def test_login_fail(self, driver):
        login_page = LoginPage(driver)
        # use the correct username and an incorrect password derived from config
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password() + "x")
        sleep(3)
        err_el = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]")
        assert err_el.text.strip() == "Invalid credentials"
        sleep(1)