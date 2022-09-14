import os

from selenium import webdriver

from src.data.admin_page import *
from src.elements.elements import *
from src.pages.componenrs.section import Section
from src.pages.main_page import MainPage

class AdminPage(MainPage):

    _currents_page_url = ADMIN_PAGE_URL
    current_status_indicator = Label(*status_indicator)
    jms_name_l = Label(*jms_name)
    status_indicator_l = Label(*status_indicator)
    startup_btn = Button(*startup_btn)
    status_label = Label(*status_label)

    jms_section_component = {
        JMS_NAME: jms_name_l,
        STATUS_INDICATOR: status_indicator_l,
        STARTUP_BTN: startup_btn,
        STATUS_LABEL: status_label
    }
    soap_radiobutton = RadioButton(*soap_radiobutton)
    rest_json_radiobutton = RadioButton(*rest_json_radiobutton)
    rest_xml_radiobutton = RadioButton(*rest_xml_radiobutton)
    jdbc_radiobutton = RadioButton(*jdbc_radiobutton)
    data_access_mode = {
        SOAP_RADIOBUTTON: soap_radiobutton,
        REST_JSON_RADIOBUTTON: rest_json_radiobutton,
        REST_XML_RADIOBUTTON: rest_xml_radiobutton,
        JDBC_RADIOBUTTON: jdbc_radiobutton,
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
