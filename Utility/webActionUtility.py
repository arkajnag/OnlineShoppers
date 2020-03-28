import sys
import traceback

from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.select import Select


class webActionUtility(object):

    @staticmethod
    def set_value_in_element(WebElement, Value):
        try:
            WebElement.send_keys(Value)
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    @staticmethod
    def click_on_element(WebElement):
        try:
            WebElement.click()
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    @staticmethod
    def get_txt_value_from_element(WebElement):
        try:
            return WebElement.text
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    @staticmethod
    def get_value_as_attribute(WebElement, attributeName):
        try:
            return WebElement.get_attribute(attributeName)
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    @staticmethod
    def select_dropdown_by_index(WebElement, indexValue):
        try:
            Select(WebElement).select_by_index(indexValue)
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    @staticmethod
    def select_dropdown_by_value(WebElement, attributeValue):
        try:
            Select(WebElement).select_by_value(attributeValue)
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    @staticmethod
    def select_dropdown_by_visibleText(WebElement, visibleText):
        try:
            Select(WebElement).select_by_visible_text(visibleText)
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    @staticmethod
    def move_to_element(WebElement, driver):
        try:
            AC(driver).move_to_element(WebElement).perform()
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    @staticmethod
    def switch_to_childWindow(driver):
        try:
            parent_Window_Name = driver.current_window_handle()
            list_of_windows = driver.window_handles()
            for eachWindow in list_of_windows:
                child_Window_name = eachWindow
                if child_Window_name is not parent_Window_Name:
                    webActionUtility.switch_window(driver, child_Window_name)
                    break
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

    @staticmethod
    def switch_window(driver, windowName):
        try:
            driver.switch_to.window(windowName)
        except Exception:
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)