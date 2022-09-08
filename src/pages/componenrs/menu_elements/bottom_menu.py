from typing import Union

# from selenium.webdriver.remote.webdriver import WebDriver
from src.data.menu import *
from src.elements.elements import *
from src.pages.componenrs.menu_elements.menu import BaseMenu


class BottomMenu(BaseMenu):
    home_link = Link(*home_point)
    about_point = Link(*about_point)
    services_point = Link(*services_point)
    products_point = Link(*products_point)
    locations_point = Link(*locations_point)
    forum_point = Link(*forum_point)
    site_map_point = Link(*site_map_point)
    contact_us_point = Link(*contact_us_point)

    def __init__(self):
        menu_items = {
            HOME_POINT: self.home_link,
            ABOUT_POINT: self.about_point,
            SERVICES_POINT: self.services_point,
            PRODUCTS_POINT: self.products_point,
            LOCATIONS_POINT: self.locations_point,
            FORUM_POINT: self.forum_point,
            SITE_MAP_POINT: self.site_map_point,
            CONTACT_US_POINT: self.contact_us_point
        }
    def select_item(self, item: Union[str, int]) -> None:
        menu_items_by_index = dict(zip([i for i in range(len(self.menu_items))], self.menu_items.values()))
        if isinstance(item, str):
            menu_item = self.menu_items.get(item)
        elif isinstance(item, int):
            menu_item = menu_items_by_index.get(item)
        else:
            raise TypeError(f'Unsaported type of menu_item {type(item)}')
        menu_item.click()


