import pytest

from exceptions.exeption import BasePageException
from src.data.admin_page import ADMIN_PAGE_URL
from src.pages.admin_page import AdminPage


class TestAdminPage:
    @pytest.fixture()
    def admin_page(self, authorization) -> AdminPage:
        authorization.webdriver.get(url=ADMIN_PAGE_URL)
        return AdminPage(webdriver=authorization.webdriver)

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
