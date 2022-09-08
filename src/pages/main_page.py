import os

from selenium import webdriver
from src.data.main_page import *
from src.elements.elements import *
from src.pages.base_page import BasePage
from src.pages.componenrs.menu_elements.bottom_menu import BottomMenu


class MainPage(BasePage):


    login_input = InputField(*login_input_fild)
    password_input = InputField(*password_input_fild)
    login_btn = Button(*login_btn)
    logout_btn = Button(*logout_link)

    def __init__(self, webdriver: WebDriver):
        super().__init__(webdriver)
        self.button_menu = BottomMenu(webdriver=self.webdriver)

    def is_current_page(self):
        return self.webdriver.current_url == LOGIN_PAGE_URL

    def login(self, username: str, password: str) -> 'MainPage':
        self.login_input = username
        self.password_input = password
        self.login_btn.click()
        return self

    def logout(self) -> None:
        self.logout_btn.click()

    @property
    def is_logged_in(self):
        return bool(self.login_btn is not None)




if __name__ == '__main__':
    path_to_firefox = os.path.abspath('../../drivers/chromedriver.exe')
    mpage = MainPage(webdriver=webdriver.Chrome(path_to_firefox))
    mpage.webdriver.get(url=BASE_URL)

    mpage.login(username=test_login, password=test_password)
    mpage.button_menu.select_item(1)
    print(mpage.is_current_page())
    # mpage.logout()
    # mpage.webdriver.quit()
    # print(mpage.is_logged_in)