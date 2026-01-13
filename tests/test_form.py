from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest
from time import sleep

# --- FIXTURE (Nằm ngoài class để dùng chung) ---
@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5) # Wait ngầm định cơ bản
    driver.maximize_window()
    yield driver
    driver.quit()

class TestForm:
    # URL chung cho cả class
    LOGIN_URL = "https://the-internet.herokuapp.com/login"

    def test_login_success_with_submit(self, driver):
        """
        Test case 1: Login thành công sử dụng hàm .submit()
        """
        driver.get(self.LOGIN_URL)

        # 1. Nhập Username
        driver.find_element(By.ID, "username").send_keys("tomsmith")

        # 2. Nhập Password
        pass_element = driver.find_element(By.ID, "password")
        pass_element.send_keys("SuperSecretPassword!")

        # 3. Dùng hàm .submit() thay vì click button
        # Selenium sẽ tự tìm form chứa element này và submit
        pass_element.submit()

        # 4. Sử dụng WebDriverWait (Wait tường minh) để đợi kết quả
        # Thay vì sleep(), ta đợi cho đến khi thông báo "flash" xuất hiện
        wait = WebDriverWait(driver, 10)
        flash_element = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        
        assert "You logged into a secure area!" in flash_element.text

    def test_login_fail_with_enter_key(self, driver):
        """
        Test case 2: Login thất bại sử dụng phím ENTER (Keys.ENTER)
        Để demo cách dùng thư viện Keys bạn đã import
        """
        driver.get(self.LOGIN_URL)

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        
        pass_element = driver.find_element(By.ID, "password")
        pass_element.send_keys("wrong_password")
        
        # 3. Giả lập hành động nhấn phím ENTER trên bàn phím
        pass_element.send_keys(Keys.ENTER)

        # 4. Wait và Assert lỗi
        wait = WebDriverWait(driver, 10)
        flash_element = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        
        assert "Your password is invalid!" in flash_element.text

    def test_element_not_found_demo(self, driver):
        """
        Demo cách xử lý exception NoSuchElementException bạn đã import
        """
        driver.get(self.LOGIN_URL)
        
        try:
            # Cố tình tìm một ID không tồn tại
            driver.find_element(By.ID, "nut_login_khong_ton_tai").click()
        except NoSuchElementException:
            print("\n✅ Đã bắt được lỗi: Không tìm thấy phần tử như mong đợi (Đúng kịch bản).")
            # Test case này coi như pass vì ta mong đợi nó không tìm thấy
            assert True