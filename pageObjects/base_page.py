import self
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
class base_page():


    def __init__(self, driver):
        self.driver = driver

    actions = ActionChains(self.driver)

    def click_by_xpath(self, el):
        el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, el))
        el.click()

    def click_by_css(self, el):
        el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, el))
        el.click()

    def clear_xpath(self, el):
        self.driver.find_element(By.XPATH, el).clear()

    def set_text(self, el, text):
        self.driver.find_element(By.XPATH, el).send_keys(text)

    def hover(self,el):
         actions.move_to_element(el).perform()
    def drag_and_drop(self,source, target):
        actions.drag_and_drop(source, target)

    def select_dropdown_by_value(self,el, option_value):
        element = self.driver.find_element(By.XPATH,el)
        select = Select(element)
        select.select_by_value(option_value)

    def select_dropdown_by_text(self,el, text):
        select = Select(self.driver.find_element(By.XPATH,el))
        select.select_by_visible_text(text)

    def refresh(self):
        self.driver.refresh()
    def navigate_to_tab(self,index ):
        self.driver.switch_to.window(self.driver.window_handles[index])
    def open_new_empty_tab(self):
        self.driver.switch_to.new_window('tab')

    def open_new_window(self):
        self.driver.switch_to.new_window('window')

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()