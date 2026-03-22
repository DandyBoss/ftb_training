import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver(request):
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")
    firefox_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Firefox(options=firefox_options)
    driver.implicitly_wait(18)
    driver.maximize_window()
    yield driver
    driver.quit()