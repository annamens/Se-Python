from selenium.common import TimeoutException
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from utilities.custom_logger import exception_logger, test_logger, error_logger


class base_page():

    def __init__(self, driver):
        self.driver = driver

    def click(self,locator):
        self.find_element(locator).clear()
        self.find_element(locator).click()
    def click_by_xpath(self, el):
        el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, el))
        el.click()

    def click_by_css(self, el):
        self.wait_until_element_present(self, el).click()
        # el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, el))
        # el.click()

    def clear_xpath(self, el):
        self.driver.find_element(By.XPATH, el).clear()

    def set_text(self, el, text):
        self.driver.find_element(By.XPATH, el).send_keys(text)

    def hover(self, el):
        actions = ActionChains(self.driver)
        actions.move_to_element(el).perform()

    def drag_and_drop(self, source, target):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target)

    def select_dropdown_by_value(self, el, option_value):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, el)
        select = Select(element)
        select.select_by_value(option_value)

    def select_dropdown_by_text(self, el, text):
        select = Select(self.driver.find_element(By.XPATH, el))
        select.select_by_visible_text(text)

    def refresh(self):
        self.driver.refresh()

    def navigate_to_tab(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def open_new_empty_tab(self):
        self.driver.switch_to.new_window('tab')

    def open_new_window(self):
        self.driver.switch_to.new_window('window')

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def wait_until_element_visible(self, *locator):
        try:
            el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*locator))
            print((el, ' element is visible'))
            return el
        except TimeoutException:
            try:
                print('Giving another try for element visibility...')
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*locator))
                return element
            except TimeoutException:
                print(el, ' cannot be found')
    def find_element(self, locator):
        self.wait_until_element_visible(self,locator)

    def wait_until_element_present(self, *locator):
        try:
            el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(*locator))
            print((el, ' element is visible'))
            return el
        except TimeoutException:
            try:
                print('Giving another try for element visibility...')
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(*locator))
                return element
            except TimeoutException as e:
                exception_logger.error(str(e))
                print(el, ' cannot be found')

    def identify_selector(selector):
        # Define patterns for XPath and CSS selectors
        xpath_pattern = r'^//'
        css_pattern = r'^[a-zA-Z#.[\]*=:]+'
        # Check if the selector matches XPath pattern
        if re.match(xpath_pattern, selector):
            return "XPath"
        # Check if the selector matches CSS selector pattern
        elif re.match(css_pattern, selector):
            return "CSS Selector"
