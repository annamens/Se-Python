import threading
from multiprocessing import Process

def worker():
    print("Worker")

# Create a process
process = Process(target=worker)

# Start the process
process.start()
#se - 4.21.0
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("url")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
el=WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.XPATH, "pathh"))
driver.refresh()
driver.forward()
driver.switch_to.window(driver.window_handles[-1])
driver.current_window_handle
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.move_to_element("el").click().perform()
actions.double_click("el").perform()
actions.context_click("el").perform()
from selenium.webdriver.support.select import Select
select = Select("dropdown_el")
select.select_by_index(4)
select.select_by_visible_text("text")

import pymysql

with pymysql.connect(
    hostname="",
    username="",
    password="",
    DB=""
) as conn:

    cursor=conn.cursor()
    cursor.execute("sql query")

import pandas as pd

df=pd.read_excel("", sheet_name='')
for index, row in df.items():
    username=row['username']

import logging
logging.basicConfig("")
logger=logging.getLogger()
logger.setLevel()
logger.info()
logger.debug()

import configparser
config=configparser.ConfigParser()
config.read("file_name")
config.get("info",username)