import logging

import pytest

from src.pages.about_page import AboutPage
from src.pages.contact_us_page import ContactUsPage
from src.pages.forum_page import ForumPage
from src.pages.locations_page import LocationsPage
from src.pages.main_page import *
from src.pages.products_page import ProductsPage
from src.pages.services import ServicesPage
from src.pages.site_map_page import SiteMapPage


class TestAdminPage:
    menu_expected_data = {
        0: lambda: MainPage,
        1: lambda: AboutPage,
        2: lambda: ServicesPage,
        3: lambda: ProductsPage,
        4: lambda: LocationsPage,
        5: lambda: ForumPage,
        6: lambda: SiteMapPage,
        7: lambda: ContactUsPage
    }

    @pytest.fixture(scope='function')
    def main_page(self, authorization) -> MainPage:
        authorization.webdriver.get(url=BASE_URL)
        return MainPage(webdriver=authorization.webdriver)

    @pytest.fixture(scope='function', params=menu_expected_data.items(), ids=[
        f"menu point: {i}" for i in menu_expected_data.keys()])
    def expected_page(self, main_page, request):
        link_number, page = request.param
        current_page = page()(main_page.webdriver)
        return current_page, link_number

    def test_url(self, main_page):
        assert not main_page.is_current_page()


    def test_navigation(self, main_page, expected_page):
        main_page.button_menu.select_item(expected_page[1])
        assert expected_page[0].is_current_page(), f'menu point {expected_page[1]}, dont lead to {type(expected_page[0])}'
