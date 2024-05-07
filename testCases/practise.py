from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.forward()
driver.back()
driver.refresh()
driver.implicitly_wait(10)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.XPATH, "el"))
from selenium.common import ElementNotVisibleException

wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException])
el = wait.until(EC.visibility_of_element_located(By.XPATH, ""))
import time

time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "el").click()
driver.find_element(By.ID, "el").send_keys("txt")
# action_chains
from selenium.webdriver.common.action_chains import ActionChains

actionchains = ActionChains(driver)
actionchains.move_to_element("el").click().perform()
actionchains.context_click("el").perform()
actionchains.drag_and_drop("src", "trgt").perform()
actionchains.click_and_hold("el").perform()
actionchains.release("el").perform()
# alerts
alerts = driver.switch_to.alert
alerts.accept()
alerts.text()
alerts.send_keys("")
alerts.dismiss()

from selenium.webdriver.support.select import Select

dropdown = Select("dropdown_el")
dropdown.select_by_index(3)
dropdown.select_by_visible_text("text")
# window
window = driver.switch_to.window(driver.window_handles[-1])
current_win = driver.current_window_handle()
driver.switch_to.window(current_win)

driver.switch_to.frame("")
driver.switch_to.default_content()
driver.save_screenshot("path")

import pymysql

connection = pymysql.connect(
    Hostname="",
    DB="",
    username=""
)
cursor = connection.cursor()
cursor.execute("select * ")

import pandas as pd

data = pd.read_excel("file", sheet_name="sheet1")

for index, row in data.iterrows():
    username = data["username"]
    password = data["password"]
    driver.find_element(By.XPATH, "").send_keys(username)
    driver.find_element(By.XPATH, "").send_keys(password)
    driver.find_element(By.XPATH, "").click()

import pytest


@pytest.mark.regression
def test_case_1():
    pass


@pytest.fixture()
def test_case_2():
    pass
    yield


@pytest.mark.skip("test is not implemented yet")
def test_skip():
    pass


@pytest.mark.xfail("expected failure")
def test_exp_fail():
    assert 1 / 0 == 1


@pytest.mark.skipif(
    webdriver.Chrome() not in webdriver.__dict__.values(), reason=""
)
def test_skip_chrome():
    pass


@pytest.mark.parametrize('url',
                         ["google.com", "amazon.com", "youtube.com"])
def test_param():
    pass
