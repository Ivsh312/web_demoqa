from selenium.webdriver.remote.webdriver import WebDriver, WebElement


class BaseMenu:
    def __init__(self, webdriver: WebDriver):
        self.webdriver: WebDriver = webdriver

