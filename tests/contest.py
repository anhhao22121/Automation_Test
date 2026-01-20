
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """Create a Chrome webdriver configured for Ubuntu CI runners.

    - Uses webdriver_manager to install a matching chromedriver.
    - Runs headless when GITHUB_ACTIONS is set or when HEADLESS=1.
    - Adds common flags required on Linux containers: --no-sandbox, --disable-dev-shm-usage.
    """
    options = Options()

    # Determine headless mode: CI (GitHub Actions) or explicit env var HEADLESS=1
    is_ci = os.getenv("GITHUB_ACTIONS", "false").lower() == "true"
    headless_env = os.getenv("HEADLESS", "1")
    headless = is_ci or headless_env in ("1", "true", "yes")

    if headless:
        # Use the newer headless mode when available, fall back to classic headless
        try:
            options.add_argument("--headless=new")
        except Exception:
            options.add_argument("--headless")

    # Flags recommended for running Chrome in Linux CI/container environments
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    base_url = "https://the-internet.herokuapp.com/dropdown"
    driver.get(base_url)
    yield driver
    driver.quit()
