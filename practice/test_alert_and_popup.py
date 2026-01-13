import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

class TestAlertAndPopup:
    
    def test_handle_alerts(self, driver):

        driver.get("https://www.letskodeit.com/practice")
        driver.find_element(By.ID, "alertbtn").click()
        sleep(2)
        alert_obj = driver.switch_to.alert 
        alert_obj.accept()
        driver.find_element(By.ID, "confirmbtn").click()
        sleep(2)
        confirm_popup = driver.switch_to.alert
        confirm_popup.accept()
        sleep(5)