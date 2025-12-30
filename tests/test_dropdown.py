from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
from time import sleep


def test_dropdown_details(driver):
    dropdown_element = driver.find_element(By.ID, "dropdown")
    select = Select(dropdown_element)
    select.select_by_visible_text("Option 1")
    current_option = select.first_selected_option.text
    print(f"Giá trị đang chọn : {current_option}")
    assert current_option == "Option 1"
    select.select_by_visible_text("Option 2")
    current_option = select.first_selected_option.text
    print(f"Giá trị đang chọn : {current_option}")
    assert current_option == "Option 2"
    all_options = [opt.text for opt in select.options]
    print(f"Tất cả các options: {all_options}")
    
