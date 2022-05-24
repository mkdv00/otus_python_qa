import pytest

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Miximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    
    driver = None
    
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser_name == "opera":
        driver = webdriver.Opera(executable_path=OperaDriverManager().install(), options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(GeckoDriverManager().install(), options=options)
        
    if maximized:
        driver.maximize_window()
        
    def tear_down():
        driver.quit()
        
    request.addfinalizer(tear_down)
    
    return driver
