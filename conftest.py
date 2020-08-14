import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en or ru")


@pytest.fixture()
def browser(request):
    user_language = request.config.getoption("language")
    driver_name = request.config.getoption("browser_name")
    browser = None
    if driver_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome("driver/chromedriver.exe", options=options)
    elif driver_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(executable_path="driver/geckodriver.exe", firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox or edge")
    browser.maximize_window()
    yield browser
    browser.quit()

