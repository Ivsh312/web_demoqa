import abc
from abc import ABC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver, WebElement

class BasePage(ABC):

    _currents_page_url = None

    def __init__(self, webdriver: WebDriver):
        self.webdriver: WebDriver = webdriver

    def is_current_page(self):
        return self.webdriver.current_url == self._currents_page_url
