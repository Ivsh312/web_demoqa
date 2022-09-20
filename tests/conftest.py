import configparser

import pytest
from selenium import webdriver

from src.data.main_page import BASE_URL
import src.pages.main_page as main_page
from .data.constants import *


@pytest.fixture(scope='session')
def credentials() -> tuple:
    config = configparser.ConfigParser()
    config.read(cred_path)
    username = config[BASE_CREDENTIALS_SECTION_NAME][USERNAME_WORD]
    password = config[BASE_CREDENTIALS_SECTION_NAME][PASSWORD_WORD]
    return username, password


@pytest.fixture(scope='session')
def driver(app_type=CHROM_TYPE_APP) -> webdriver:
    webdriver_instance = None
    if app_type == CHROM_TYPE_APP:
        webdriver_instance = webdriver.Chrome()
        yield webdriver_instance
    if webdriver_instance is not None:
        webdriver_instance.close()


@pytest.fixture(scope='module')
def start_page(driver) -> webdriver:
    start_page = main_page.MainPage(webdriver=driver)
    start_page.webdriver.get(BASE_URL)
    return start_page


@pytest.fixture(scope='module')
def authorization(start_page, credentials) -> webdriver:
    start_page.login(*credentials)
    return start_page
