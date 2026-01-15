import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains 

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

class Test_drag_drop:
    def test_drag_5000_to_debit_amount(self, driver):
        # 1. Go to page
        driver.get("https://demo.guru99.com/test/drag_drop.html")
        
        # Đợi trang load ổn định (có thể thay bằng WebDriverWait nếu muốn chuẩn hơn)
        sleep(2) 

        # 2. Xác định các Element
        # Block 5000 thường có id là "fourth" trên trang demo này
        source_element = driver.find_element(By.ID, "fourth")
        
        # Ô Amount bên phía Debit thường có id là "amt7"
        target_element = driver.find_element(By.ID, "amt7")

        # 3. Thực hiện hành động Drag and Drop
        actions = ActionChains(driver)
        actions.drag_and_drop(source_element, target_element).perform()

        # 4. (Tùy chọn) Assert để kiểm tra kết quả
        # Kiểm tra xem ô đích đã chứa element hay chưa
        assert "5000" in target_element.text
        
        # Dừng 1 chút để bạn kịp nhìn thấy kết quả khi chạy
        sleep(5)