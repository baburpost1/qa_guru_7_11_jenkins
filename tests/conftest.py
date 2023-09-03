import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from utils import attach


FILE_PATH = os.path.abspath(__file__)
PROJECT_PATH = os.path.dirname(FILE_PATH)
RESOURCE_PATH = os.path.join(PROJECT_PATH, 'resources')


@pytest.fixture(scope='function')
def setup_browser(request):
    # browser_version = "114.0.5735.198"
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        # "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver))
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
