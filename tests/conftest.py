import pytest
from selene import browser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

import tests.utils.attach


@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
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

    tests.utils.attach.add_screenshot(browser)
    tests.utils.attach.add_logs(browser)
    tests.utils.attach.add_html(browser)
    tests.utils.attach.add_video(browser)

    browser.quit()

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = '1920'
    browser.config.window_height = '1080'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 5
    yield
    browser.quit()
