import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from selene.support.shared import browser

FILE_PATH = os.path.abspath(__file__)
PROJECT_PATH = os.path.dirname(FILE_PATH)
RESOURCE_PATH = os.path.join(PROJECT_PATH, 'resources')


@pytest.fixture(scope="session")
def load_env():
    load_env()


@pytest.fixture(autouse=True)
def setup_browser():
    # Список всех доступных парамеров https://peter.sh/experiments/chromium-command-line-switches/

    browser.config.window_height = 1400
    browser.config.window_width = 1600
    browser_version = "100.0"
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)
    attach.add_logs(browser)

    browser.quit()
