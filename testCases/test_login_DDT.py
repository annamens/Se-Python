import time
import os
import pytest
import softest
from pageObjects.LoginPage import login_page
from testCases.conftest import set_up1
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from ddt import data, unpack, ddt
from utilities.custom_logger import test_logger


@pytest.mark.usefixtures('set_up1')
@ddt
class Test_002_DDT_Login(softest.TestCase):
    baseURL = ReadConfig.getAppUrl()
    logger = LogGen.logGen()  # Logger
    path = os.getcwd()
    excel_path = os.path.join(path, 'LoginData.xlsx')
    sheet_no = 'Sheet1'
    driver = set_up1

    @pytest.fixture(autouse=True)
    def class_set_up(self):
        self.lp = login_page(self.driver)

    @data(*XLUtils.read_excel_data(excel_path, sheet_no))
    @unpack
    def test_ddt_test(self,username, password, exp):
        self.driver = self.set_up1
        self.lp.load_url(self.baseURL)
        self.lp.setUserName(username)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        time.sleep(5)
        lst_status = []
        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerce administration"
        if act_title == exp_title:
            if exp == 'Pass':
                self.logger.info("**** passed ****")
                self.lp.clickLogout()
                lst_status.append("Pass")
            elif exp == 'Fail':
                test_logger.info(f'failed with {username}')
                self.logger.info("**** failed ****")
                self.lp.clickLogout()
                lst_status.append("Fail")

# @pytest.mark.regression
# def test_login_ddt(self, set_up1):
#     self.logger.info("******* Starting Test_002_DDT_Login Test **********")
#     self.logger.info("******* Starting Login DDT Test **********")
#     self.driver = set_up1
#     self.driver.get(self.baseURL)
#     self.driver.maximize_window()
#     self.lp = LoginPage(self.driver)
#
#     self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
#     print('Number of rows...', self.rows)
#     lst_status = []
#
#     for r in range(2, self.rows + 1):
#         self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
#         self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
#         self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
#
#         self.lp.setUserName(self.user)
#         self.lp.setPassword(self.password)
#         self.lp.clickLogin()
#         time.sleep(5)
#
#         act_title = self.driver.title
#         exp_title = "Dashboard / nopCommerce administration"
#
#         if act_title == exp_title:
#             if self.exp == 'Pass':
#                 self.logger.info("**** passed ****")
#                 self.lp.clickLogout()
#                 lst_status.append("Pass")
#             elif self.exp == 'Fail':
#                 self.logger.info("**** failed ****")
#                 self.lp.clickLogout()
#                 lst_status.append("Fail")
#
#         elif act_title != exp_title:
#             if self.exp == 'Pass':
#                 self.logger.info("**** failed ****")
#                 lst_status.append("Fail")
#             elif self.exp == 'Fail':
#                 self.logger.info("**** passed ****")
#                 lst_status.append("Pass")
#         print(lst_status)
#     if "Fail" not in lst_status:
#         self.logger.info("******* DDT Login test passed **********")
#         self.driver.close()
#         assert True
#     else:
#         self.logger.error("******* DDT Login test failed **********")
#         self.driver.close()
#         assert False
#
#     self.logger.info("******* End of Login DDT Test **********")
#     self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")
