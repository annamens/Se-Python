import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    @pytest.mark.regression
    def test_homePageTitle(self, set_up1):
        self.logger.info("************** Test_001_Login *****************")
        self.logger.info("************** verifying home page title *****************")
        self.driver = set_up1
        self.driver.get(self.baseURL)
        time.sleep(1)
        act_title = self.driver.title

        if act_title == 'Your store. Login':
            assert True
            self.driver.close()
            self.logger.info("************** Home page title passed *****************")

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle.png")
            assert False
            self.driver.close()
            self.logger.error("************** Home page title failed *****************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, set_up1):
        self.logger.info("************** test_login *****************")
        self.logger.info("************** verify Login test  *****************")
        self.driver = set_up1
        self.driver.get(self.baseURL)
        time.sleep(1)
        self.lp = LoginPage(self.driver)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
            self.logger.info("************** Login test passed *****************")

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            assert False
            self.driver.close()
            self.logger.error("************** Login test failed *****************")
