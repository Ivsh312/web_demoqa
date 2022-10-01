import abc
import time
from abc import ABC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver, WebElement

from exceptions.exeption import BasePageException
from src.data.constants import *
class BasePage(ABC):

    _currents_page_url = None

    def __init__(self, webdriver: WebDriver):
        self.webdriver: WebDriver = webdriver

    def is_current_page(self):
        return self.webdriver.current_url == self._currents_page_url

    @staticmethod
    def wait_until_element_param_dont_change(element: WebElement, param, current_value, time_limit=START_AWAIT_TIMEOUT):
        start_time = time.time()
        if time.time()-start_time < time_limit:
            if element.get_attribute(param) == current_value:
                time.sleep(START_SLEEP)
            else:
                return element.get_attribute(param)
        raise BasePageException("Status not changed")
