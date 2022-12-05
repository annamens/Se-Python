import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import addCustomer
from pageObjects.searchCustomer import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getAppUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, set_up):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver = set_up
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = addCustomer(self.driver)
        self.addcust.clickCustomerBtn()
        self.addcust.clickCustomerMenuItem()

        self.logger.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
