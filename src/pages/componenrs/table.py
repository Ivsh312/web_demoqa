from typing import Tuple

from selenium.webdriver.remote.webelement import WebElement

from src.elements.elements import Element, Cell


class Table(Element):

    def __init__(self, driver, table_locator, cell_locator):
        super().__init__(*table_locator)
        self.webdriver = driver
        self.table_locator = table_locator

        self.cell_locator = cell_locator

    def __getitem__(self, key: Tuple[int, int]) -> WebElement:
        cell = Cell(*self.cell_locator)
        cell.value = cell.value.format(row_numbe=key[0]+1, column_numbe=key[1]+1)
        return cell
    # def __len__(self):
