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
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

class TestSwitchWindow:
    
    def test_switch_to_window(self, driver):
        driver.get("https://www.letskodeit.com/practice")
        
        # Lưu ID cửa sổ cha
        parent_handle = driver.current_window_handle
        
        # Mở cửa sổ mới
        driver.find_element(By.ID, "openwindow").click()
        sleep(2) # Chờ cửa sổ bật lên
        
        # Tìm và switch sang cửa sổ mới
        for handle in driver.window_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                break
        
        # Phóng to cửa sổ mới và kiểm tra
        driver.maximize_window()
        assert "All Courses" in driver.title
        
        # Đóng cửa sổ con và quay về cửa sổ cha
        driver.close()
        driver.switch_to.window(parent_handle)
        
        # Kiểm tra đã về lại trang gốc
        assert "Practice" in driver.title