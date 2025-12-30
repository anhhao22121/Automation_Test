from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import Base_Page
import pytest
from time import sleep
class LoginPage(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        # Không dùng dấu * ở đây vì find_element của Base_Page sẽ xử lý nó
        self.find_element(self.username_input).send_keys(username)

    def enter_password(self, password):
        self.find_element(self.password_input).send_keys(password)

    def click_login_button(self):
        # Truyền tuple vào hàm click của Base_Page
        self.click(self.login_button)

    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()