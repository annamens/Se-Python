import random
import string
import time

import pytest
import self
from selenium.webdriver.common.by import By

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import addCustomer


class Test_001_AddCustomer:
    baseurl = ReadConfig.getAppUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    @pytest.mark.regression
    def test_addCustomer(self, set_up):
        self.logger.info("*********** test_addCustomer ***********")
        self.driver = set_up
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")
        self.logger.info("******* Starting Add Customer Test **********")
        self.ac = addCustomer(self.driver)
        self.ac.clickCustomerBtn()
        self.ac.clickCustomerMenuItem()
        self.ac.clickAddNew()
        self.email = random_generator() + "@gmail.com"
        self.ac.enterEmail(self.email)
        self.ac.enterPassword("test123")
        self.ac.enterFirstName("Srinivas")
        self.ac.enterLastName("Annameni")
        self.ac.selectGender("Male")
        self.ac.enterDateOfBith("7/05/1985")
        self.ac.enterCompanyName("Persistent")
        #self.ac.selectNewsLetter("Test store 2")
        self.ac.setManagerOfVendor("Vendor 2")
        self.ac.setCustomerRoles("Guests")
        self.ac.setAdminContent("This is for testing...")
        self.ac.clickOnSave()

        self.logger.info("************* Saving customer info **********")
        self.logger.info("********* Add customer validation started *****************")


        print(self.ac.getSuccessText())
        if 'The new customer has been added successfully.' in self.ac.getSuccessText():
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            assert False
            self.logger.info("********* Add customer Test Failed *********")

        self.driver.close()

        self.logger.info("******* Ending Add customer test *********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
