from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep

def test_hidden(driver):
    hide_button = driver.find_element(By.ID, "hide-textbox")
    hide_button.click()
    sleep(5)
  
    display_textbox = driver.find_element(By.ID, "displayed-text")
    driver.execute_script("arguments[0].value='Hello World!'", display_textbox)

    show_button = driver.find_element(By.ID,"show-textbox")
    show_button.click()
    sleep(5)
    
    hide_button.screenshot("tnduyen.png")
    sleep(5)
