import inspect  # used to autocapture function name
import pytest
# from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


def get_function_name():
    return inspect.currentframe().f_back.f_code.co_name


class Test_001_Login:
    # baseURL = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"
    # created these static inputs in Configurations/config.ini file and read data using utilities/readProperties.py file
    # we call data from this file
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    print(baseURL, username, password)
    print(logger)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("**********Test_001_Login**********")  # test case id - (class name)
        self.logger.info("**********Verify home page title**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.logger.info(f"{10 * '*'}home page title test passed{10 * '*'}")
        else:
            self.driver.save_screenshot(f"Screenshots/{get_function_name()}.png")
            self.driver.close()
            self.logger.info(f"{10 * '*'}home page title test failed{10 * '*'}")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):

        self.logger.info("********** Verify Login test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            self.logger.info("********** Login test is passed **********")
            self.driver.close()
            assert True
        else:
            # self.driver.save_screenshot(r"Screenshots/test_homePageTitle.png")
            self.driver.save_screenshot(f"Screenshots/{get_function_name()}.png")
            self.logger.error("********** Login test is Failed **********")
            self.driver.close()
            assert False
