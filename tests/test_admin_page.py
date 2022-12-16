import pytest

from exceptions.exeption import BasePageException
from src.data.admin_page import ADMIN_PAGE_URL
from src.data.main_page import BASE_URL
from src.pages.admin_page import AdminPage
from src.pages.main_page import MainPage


class TestAdminPage:

    @pytest.fixture(scope='class')
    def admin_page_settings(self, authorization) -> AdminPage:
        try:
            authorization.webdriver.get(url=ADMIN_PAGE_URL)
            yield AdminPage(webdriver=authorization.webdriver)
        finally:
            authorization.webdriver.get(url=BASE_URL)

    @pytest.fixture()
    def admin_page(self, admin_page_settings) -> AdminPage:
        try:
            yield AdminPage(webdriver=admin_page_settings.webdriver)
        finally:
            admin_page_settings.webdriver.get(url=ADMIN_PAGE_URL)

    def test_indicator(self, admin_page):
        status_before_click = admin_page.current_status_indicator.text
        admin_page.startup_btn.click()
        try:
            admin_page.wait_until_element_param_dont_change(admin_page.status_label, 'text', status_before_click)
            assert True
        except BasePageException:
            assert False, "indicator dont changed status after click switcher"

    def test_for_test(self, driver):
        assert False
