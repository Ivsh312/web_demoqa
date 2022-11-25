import configparser
import os
import time
from datetime import datetime
from random import random

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

import src.pages.main_page as main_page
from src.data.main_page import BASE_URL
from .data.constants import *
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import FirefoxOptions

screen_shoot_node = 'test_screen_shoot\\'
screen_shoot_extenuation = '.png'

@pytest.fixture(scope='session')
def credentials() -> tuple:
    config = configparser.ConfigParser()
    config.read(cred_path)
    username = config[BASE_CREDENTIALS_SECTION_NAME][USERNAME_WORD]
    password = config[BASE_CREDENTIALS_SECTION_NAME][PASSWORD_WORD]
    return username, password



# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


    # driver.save_screenshot(file_name)

# @pytest.fixture(scope="function", autouse=True)
# def something(request, driver):
#     yield
#     print(12)
#     if request.node.rep_setup.failed:
#         print("setting up a test failed!", request.node.nodeid)
#         time.sleep(1)
#         file_name = f'{request.node.nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/",
#                                                                                           "_").replace(
#             "::", "__")
#         driver.save_screenshot(file_name)

@pytest.fixture(scope='session', params=supported_browsers)
def driver(request) -> webdriver:
    webdriver_instance = None
    if request.param == FIREFOX_TYPE_APP:
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        webdriver_instance = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                               options=opts)

        yield webdriver_instance
    if webdriver_instance is not None:
        webdriver_instance.close()


# make a screenshot with a date and time
def take_screenshot(driver, nodeid):
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot",
                  attachment_type=AttachmentType.PNG)
    # file_name = f'{nodeid}_'.replace("/", "_").replace("::", "__").replace('.', '_')
    # print(file_name)
    # save_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), screen_shoot_node, file_name+screen_shoot_extenuation)
    # # print(save_path)
    # print(driver.save_screenshot(save_path))


# check if a test has failed
@pytest.fixture(scope="function", autouse=True)
def failed_check(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['driver']
            take_screenshot(driver, request.node.nodeid)



@pytest.fixture(scope='module')
def start_page(driver) -> webdriver:
    start_page = main_page.MainPage(webdriver=driver)
    start_page.webdriver.get(BASE_URL)
    return start_page


@pytest.fixture(scope='module')
def authorization(start_page, credentials) -> webdriver:
    start_page.login(*credentials)
    return start_page
