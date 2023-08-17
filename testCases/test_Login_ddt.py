import inspect  # used to autocapture function name
import pytest
# from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtiils as XLUtils


def get_function_name():
    return inspect.currentframe().f_back.f_code.co_name


class Test_002_ddt_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_Login_ddt(self, setup):
        self.logger.info("********** test002_Login_ddt **********")
        self.logger.info("********** Verify Login test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)

        print(self.path)
        self.rows = XLUtils.getRowCount(self.path, 'LoginData')
        print("Number of Rows in excel", self.rows)
        status_list = []
        for r in range(2, self.rows+1):
            self.username = XLUtils.readData(self.path, 'LoginData', r, 1)
            self.password = XLUtils.readData(self.path, 'LoginData', r, 2)
            self.exp = XLUtils.readData(self.path, 'LoginData', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            actual_title = self.driver.title
            if actual_title == "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("********** Login test is passed **********")
                    self.lp.clickLogout()
                    status_list.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("********** Login test is failed **********")
                    self.lp.clickLogout()
                    status_list.append("Fail")
            else:
                if self.exp == "Pass":
                    self.logger.info("********** Login test is Failed **********")
                    status_list.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("********** Login test is Passed **********")
                    status_list.append("Pass")

        if "Fail" not in status_list:
            self.logger.info("********** Login DTT test Passed ****** ")
            self.driver.close()
            assert True
        else:
            self.logger.info("********** Login DTT test Failed ****** ")
            self.driver.close()
            assert False
