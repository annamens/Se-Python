import self
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


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

    def hover(el):
         actions.move_to_element(el).perform()
    def drag_and_drop(source, target):
        actions.drag_and_drop(source, target)

