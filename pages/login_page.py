from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep
class LoginPage:
    def __init__(self, driver):
        self.driver1 = driver

    def enter_username(self, username):
        self.driver1.find_element(By.NAME, "username").send_keys(username)

    def enter_password(self, password):
        self.driver1.find_element(By.NAME, "password").send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()