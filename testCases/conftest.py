import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import service as ChromeService
from selenium.webdriver.edge.service import service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def set_up(browser):
    browser = ReadConfig.getBrowser()
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching chrome browser...")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching firefox browser...")
    elif browser == "edge":
        driver = webdriver.Ie()
        print("Launching IE browser...")
    else:
        driver = webdriver.Chrome()
    return driver


@pytest.fixture()
def set_up1():
    browser = ReadConfig.getBrowser()
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

    if driver is not None:
        driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Srinivas'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
