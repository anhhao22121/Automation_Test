from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep
def test_login():
    driver=webdriver.Chrome()
    base_url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver.get(base_url)
    driver.maximize_window()
    sleep(5)
    #Enter Username and Password
    driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.NAME,"password").send_keys("admin123")
    #Click on Login Button
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    sleep(5)
    assert driver.find_element(By.CSS_SELECTOR,".oxd-text--h6").text=="Dashboard"


    