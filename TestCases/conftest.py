import os
import sys
import traceback

import pytest
from selenium import webdriver

#sys.path.append("../")
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Utility.CommonUtility import commonUtility


@pytest.fixture(scope="class")
def setup(request):
    try:
        driver = webdriver.Firefox(executable_path='../Resources/geckodriver.exe')
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.set_page_load_timeout(20)
        driver.delete_all_cookies()
        driver.get(commonUtility.read_config_file()['baseURL'])
        request.cls.driver = driver
        yield driver
        driver.quit()
    except Exception:
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)
