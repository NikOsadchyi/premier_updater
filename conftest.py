import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="module")
def driver():
    service = Service(executable_path=ChromeDriverManager().install())

    # set up the Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.headless = True

    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    driver.quit()
