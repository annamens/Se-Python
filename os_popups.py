import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.file.io/')
el = driver.find_element(By.XPATH, "//label[@for='upload-button']").click()
time.sleep(2)
file = r'C:\Users\shrin\Downloads\console.txt'
pyautogui.write(file)
pyautogui.press('enter')
time.sleep(10)
driver.quit()
