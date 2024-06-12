#download the allure bin file in the directory and set the env path
import allure

import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import login_page
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.custom_logger import exception_logger, error_logger, test_logger

@allure.severity(allure.severity_level.NORMAL)
class Test_allure:
    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    @all
    @pytest.mark.regression
    def test_homePageTitle(self, set_up1):
        self.logger.info("************** Test_001_Login *****************")
        self.logger.info("************** verifying home page title *****************")
        self.driver = set_up1
        self.driver.get(self.baseURL)
        time.sleep(1)
        act_title = self.driver.title

        if act_title == 'Your store. Login-':
            assert True
            self.driver.close()
            test_logger.info('Home page title asserted.')
            self.logger.info("************** Home page title passed *****************")

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle.png")
            allure.attach(self.driver.get_screenshot_as_png(),name='allure_demo')
            assert False
            self.driver.close()
            self.logger.error("************** Home page title failed *****************")

#run the below command
#python -m pytest -v -s testCases/allure_reports.py --alluredir=allure-results
#once the report is generated run the below command
#allure serve allure-results
