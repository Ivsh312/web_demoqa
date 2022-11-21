import pytest

from exceptions.exeption import BasePageException
from src.data.admin_page import REST_XML_RADIOBUTTON, ADMIN_PAGE_URL
from src.pages.admin_page import AdminPage


class TestAdminPage:
    @pytest.fixture()
    def admin_page(self, authorization) -> AdminPage:
        authorization.webdriver.get(url=ADMIN_PAGE_URL)
        return AdminPage(webdriver=authorization.webdriver)

    def test_indicator(self, admin_page):
        status_before_click = admin_page.current_status_indicator.text
        admin_page.startup_btn.click()
        print(status_before_click)
        try:
            admin_page.wait_until_element_param_dont_change(admin_page.status_label, 'text', status_before_click)
            print(admin_page.current_status_indicator.text)
            assert True
        except BasePageException:
            assert False, "indicator dont changed status after click switcher"