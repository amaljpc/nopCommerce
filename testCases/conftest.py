import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest

"""
pytest xdist is package used to run file parallel
use this command on console, to run tests on desired browser
pytest -s -v testCases/test_Login.py --browser chrome
pytest -s -v testCases/test_Login.py --browser firefox
"""
"""
use this command on console, to run parallel tests on desired browser
pytest -s -v -n=2 testCases/test_Login.py --browser chrome
pytest -v --browser=firefox
or
pytest -s -v -n=2 testCases/test_Login.py --browser firefox
"""


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


"""
pytest -s -v -n=3 --html=Reports/report.html testCases/test_Login.py --browser chrome
pytest -v -n=3 --html=Reports/report.html testCases/test_Login.py --browser chrome

############ METHOD FOR GENERATE PYTEST HTML REPORT ############
"""


# This is hook for adding  env info to html reort
def pytest_configure(config):
    config._metadata = { 'Project Name': 'nop Commerce',
                         'Module Name' : 'Customers',
                         'Tester' : 'Amal'}
    """below format is not supported anymore"""
    # config._metadata['Project Name'] = 'nop Commerce'
    # config._metadata['Module Name'] = 'Customers'
    # config._metadata['Tester'] = 'Amal'

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
