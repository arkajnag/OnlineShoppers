import os
import sys

import allure
import pytest

#sys.path.append("../")
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Pages.LaunchPage import launchPage

@allure.epic("Regression Test - Online Shoppers")
@allure.feature("Online Shoppers - Launch Page Testing Scope")
@pytest.mark.usefixtures('setup')
class Test_launchPage:

    @allure.description("Perform a basic Search of Item from Online Shopping Launch Page")
    @allure.severity(severity_level=allure.severity_level.NORMAL)
    def test_fnc_searchNewItemFromLaunchPage(self):
        driver = self.driver
        lnchPage = launchPage(driver)
        lnchPage.fnc_searchNewItemFromLaunchPage('Dress')
        currentUrl = driver.current_url
        try:
            assert 'Dress' in currentUrl
        finally:
            if AssertionError:
                allure.attach(driver.get_screenshot_as_png(), name="LaucnhPage_SearchItem_Failure",
                              attachment_type=allure.attachment_type.PNG)
