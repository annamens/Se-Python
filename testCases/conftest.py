from selenium import webdriver
import pytest


@pytest.fixture()
def set_up(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching chrome browser...")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching firefox browser...")
    elif browser == "ie":
        driver = webdriver.Ie()
        print("Launching IE browser...")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Srinivas'

# It is hook for delete/Modify Environment info to HTML Report
@ pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
