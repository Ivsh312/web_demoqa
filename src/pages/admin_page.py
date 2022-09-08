import os

from selenium import webdriver

from src.data.admin_page import *
from src.elements.elements import *
from src.pages.componenrs.section import Section
from src.pages.main_page import MainPage

def a(c=12345):
    ...

class ab:
    ...
class AdminPage(MainPage):

    _currents_page_url = ADMIN_PAGE_URL
    current_status_indicator = Label(*status_indicator)
    jms_section_component = {
        JMS_NAME: lambda: Label(*jms_name),
        STATUS_INDICATOR: lambda: Label(*status_indicator),
        STARTUP_BTN: lambda: Button(*startup_btn),
        STATUS_LABEL: lambda: Label(*status_label)
    }
    data_access_mode = {
        SOAP_RADIOBUTTON: lambda: RadioButton(*soap_radiobutton),
        REST_JSON_RADIOBUTTON: lambda: RadioButton(*rest_json_radiobutton),
        REST_XML_RADIOBUTTON: lambda: RadioButton(*rest_xml_radiobutton),
        JDBC_RADIOBUTTON: lambda: RadioButton(*jdbc_radiobutton),
    }


    def __init__(self, webdriver: WebDriver):
        super().__init__(webdriver)
        self.jms_service_section = Section(
            webdriver, section_locator=jms_section, inner_components=self.jms_section_component)
        self.data_access_mode_section = Section(
            webdriver, section_locator=data_access_mode, inner_components=self.data_access_mode)

    def change_jms_status(self) -> str:
        self.jms_service_section[STARTUP_BTN].click()
        return self.current_status_indicator.text

    def click_radiobutton(self, item: str) -> dict:
        self.data_access_mode_section[item].click()
        return {key: value.is_selected() for key, value in self.data_access_mode_section.items()}


if __name__ == '__main__':


    path_to_firefox = os.path.abspath('../../drivers/chromedriver.exe')
    apage = AdminPage(webdriver=webdriver.Chrome(path_to_firefox))
    apage.webdriver.get(url=ADMIN_PAGE_URL)

    print(apage.current_status_indicator.text)
    print(apage.change_jms_status())
    apage.change_jms_status()
    print(apage.current_status_indicator.text)
    print(apage.click_radiobutton(REST_XML_RADIOBUTTON))
    print(apage.current_status_indicator)

    # mpage.login(username=test_login, password=test_password)
    # mpage.button_menu.select_item(1)
    # print(mpage.is_current_page())
    # mpage.logout()
    # mpage.webdriver.quit()
    # print(mpage.is_logged_in)
