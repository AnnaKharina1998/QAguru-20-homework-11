import pytest
from selene import browser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

import tests.utils.attach


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    # options = Options()
    options = webdriver.ChromeOptions()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True
        },
        "goog:loggingPrefs": {"browser": "ALL"}
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    # tests.utils.attach.add_screenshot(browser)
    # tests.utils.attach.add_logs(browser)
    # tests.utils.attach.add_html(browser)
    # tests.utils.attach.add_video(browser)

    browser.quit()