import pytest

from src.data.admin_page import REST_XML_RADIOBUTTON, ADMIN_PAGE_URL
from src.pages.admin_page import AdminPage


class TestAdminPage:
    @pytest.fixture()
    def admin_page(self, authorization) -> AdminPage:
        authorization.webdriver.get(url=ADMIN_PAGE_URL)
        return AdminPage(webdriver=authorization.webdriver)

    def test_indicator(self, admin_page):
        status_before_click = admin_page.current_status_indicator.text
        print(admin_page.change_jms_status())
        admin_page.change_jms_status()
        status_after_click = admin_page.current_status_indicator.text
        print(admin_page.current_status_indicator.text)
        print(admin_page.click_radiobutton(REST_XML_RADIOBUTTON))
        print(admin_page.current_status_indicator.text)
        assert status_before_click != status_after_click, 'Indicator work incorrect'
