from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

from Locators.Locators import Locators
from Utility.webActionUtility import webActionUtility


class launchPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(self.driver, 10)
        self.txt_searchItem_By_ID = self.driver.find_element(By.ID, Locators.txt_searchItem_By_ID)
        self.btn_searchButton_By_CSS = self.driver.find_element(By.CSS_SELECTOR, Locators.btn_searchButton_By_CSS)

    def fnc_searchNewItemFromLaunchPage(self, searchItemName):
        webActionUtility.set_value_in_element(self.txt_searchItem_By_ID, searchItemName)
        webActionUtility.click_on_element(self.btn_searchButton_By_CSS)
