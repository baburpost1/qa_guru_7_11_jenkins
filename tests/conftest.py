import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from utils import attach
from selene.support.shared import browser

FILE_PATH = os.path.abspath(__file__)
PROJECT_PATH = os.path.dirname(FILE_PATH)
RESOURCE_PATH = os.path.join(PROJECT_PATH, 'resources')
#
#
# @pytest.fixture(autouse=True)
# def setup_browser():
#     browser_version = "100.0"
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": browser_version,
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     }
#     options.capabilities.update(selenoid_capabilities)
#     driver = webdriver.Remote(
#         command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
#         options=options
#     )
#
#     browser = Browser(Config(driver))
#     yield browser
#
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_html(browser)
#     attach.add_video(browser)
#
#     browser.quit()
@pytest.fixture(autouse=True)
def setup_browser():
    browser.config.base_url = 'https://demoqa.com'
    # driver_options = browser.config.driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless')
    # driver_options.add_argument('--disable-notifications')
    # browser.config.driver_options = driver_options
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
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()