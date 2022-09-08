from typing import Dict, Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BaseElement:
    AWAIT_TIMEOUT = 10

    def __init__(self, value, by=By.CSS_SELECTOR):
        self.by = by
        self.value = value
        self._descriptor_name = None

    def __set_name__(self, owner, name):
        self._descriptor_name = name

    def __get__(self, instance, owner) -> WebElement:
        webdriver: WebDriver = instance.webdriver
        element = WebDriverWait(webdriver, self.AWAIT_TIMEOUT).until(
            ec.presence_of_element_located((self.by, self.value)))
        return element

    def __set__(self, instance, value):
        element: WebElement = getattr(instance, self._descriptor_name)
        element.clear()
        element.send_keys(value)


class Element(BaseElement):
    ...


class InputField(Element):
    ...


class SelectButton(Element):
    ...


class Button(Element):
    ...


class Link(Element):
    ...


class Label(Element):
    ...


class Cell(Element):
    ...


class RadioButton(Button):
    ...


    # def __get__(self, instance,owner):
    #
    #     return super().__get__(instance,owner)

