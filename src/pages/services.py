import os

from selenium import webdriver

from src.data.main_page import BASE_URL
from src.pages.base_page import BasePage
from src.elements.elements import *
from src.data.services import *
from src.pages.componenrs.table import Table


class ServicesPage(BasePage):

    _currents_page_url = SERVICES_PAGE_URL

    def __init__(self, webdriver: WebDriver):
        super().__init__(webdriver)
        self.table = Table(
            cell_locator=table_cell,
            table_locator=table_content,
            driver=self.webdriver
        )
    table_name = Label(*table_name)


if __name__ == '__main__':
    path_to_firefox = os.path.abspath('../../drivers/chromedriver.exe')
    spage = ServicesPage(webdriver=webdriver.Chrome(path_to_firefox))
    spage.webdriver.get(url=SERVICES_PAGE_URL)
    print(spage.table_name.text)
    print(spage.table[(1, 1)].text)
    print(spage.table.text)

