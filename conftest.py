import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="Chrome",
                     help="Choose browser: Chrome, Firefox, Opera, Edge or Safari")
    parser.addoption('--selenoid',
                     action='store',
                     default='',
                     help="Selenoid")

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser_name')
    selenoid = request.config.getoption("selenoid")
    if (selenoid == 'true'):
        desiredCapabilities = {
            "browserName": "chrome",
            "version": "",
            "enableVNC": True,
            "enableVideo": False,
        }
        browser = webdriver.Remote('http://test.local.com:4444/wd/hub', desiredCapabilities)
        browser.set_window_size(1920, 1000)
    elif browser_name == "Chrome":
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif browser_name == "Firefox":
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif browser_name == "Opera":
        browser = webdriver.Opera(executable_path=OperaDriverManager().install())
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif browser_name == "Edge":
        browser = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif browser_name == "Safari":
        browser = webdriver.Safari()
        browser.maximize_window()
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError("'--browser_name' should be 'Chrome, Firefox, Opera, Edge or Safari")

    yield browser
    time.sleep(3)
    browser.quit()
