import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains 

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

class TestActionChains:
    
    def test_hover_menu(self, driver):
        driver.get("https://demoqa.com/menu")
        driver.implicitly_wait(20)
        actions = ActionChains(driver)
        main_item_2 = driver.find_element(By.LINK_TEXT, "Main Item 2")
        print("Đang hover vào Main Item 2...")
        actions.move_to_element(main_item_2).perform()
        sleep(2)
        sub_sub_list = driver.find_element(By.LINK_TEXT, "SUB SUB LIST »")
        print("Đang hover vào SUB SUB LIST...")
        actions.move_to_element(sub_sub_list).perform()
        sub_sub_item_1 = driver.find_element(By.LINK_TEXT, "Sub Sub Item 1")
        actions.move_to_element(sub_sub_item_1).perform()
        sleep(2) 
        print("Đã hover thành công!")