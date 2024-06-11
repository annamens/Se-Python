import random
import string
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import login_page
from pageObjects.AddCustomer import addCustomer
from utilities.custom_logger import test_logger

class Test_001_AddCustomer:
    baseurl = ReadConfig.getAppUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    @pytest.mark.smoke
    @pytest.mark.order(1)
    @pytest.mark.regression
    def test_add_customer(self, set_up1):
        self.logger.info("*********** test_addCustomer ***********")
        self.driver = set_up1
        self.driver.get(self.baseurl)

        self.lp = login_page(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        test_logger.info('Login successful')
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
        # self.ac.selectNewsLetter("Test store 2")
        self.ac.setManagerOfVendor("Vendor 2")
        self.ac.setCustomerRoles("Guests")
        self.ac.setAdminContent("This is for testing...")
        self.ac.clickOnSave()
        test_logger.info('Saved customer info')
        self.logger.info("************* Saving customer info **********")
        self.logger.info("********* Add customer validation started *****************")

        print(self.ac.getSuccessText())
        if 'The new customer has been added successfully.' in self.ac.getSuccessText():
            assert True
            test_logger.info(' Add customer test passed')
            self.logger.info("********* Add customer Test Passed *********")
        else:
            assert False
            test_logger.info('add customer test failed')
            self.logger.info("********* Add customer Test Failed *********")

        self.driver.close()

        self.logger.info("******* Ending Add customer test *********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
