import pytest
from utils.api_helper import APIHelper 

# Tag API tests as regression so they can be run in CI selectively
pytestmark = pytest.mark.regression

class TestJsonPlaceholderAPI:
    
    def test_get_user_id_1(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
        }
        base_url = "https://jsonplaceholder.typicode.com/users/1" 
        response = APIHelper.get_request(base_url, headers=headers)
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
        json_data = response.json()
        for key, value in json_data.items():
            print("\n"f"{key}: {value}")
        actual_email = json_data["email"]
        assert actual_email == "Sincere@april.biz"
        print(f"Email kiểm tra: {actual_email}")
        
    