from typing import Tuple

from selenium.webdriver.remote.webelement import WebElement

from src.elements.elements import Element, Cell


class Section(Element, dict):

    def __init__(self, driver, section_locator, inner_components: dict):
        super().__init__(*section_locator)
        self.webdriver = driver
        self.inner_components = inner_components

    def __getitem__(self, key: str) -> WebElement:
        return self.inner_components.get(key).__get__(instance=self, owner=self)

    def values(self):
        return [i.__get__(instance=self, owner=self) for i in self.inner_components.values()]

    def items(self):
        return [
            (key, value.__get__(instance=self, owner=self))
            for key, value in self.inner_components.items()
        ]
