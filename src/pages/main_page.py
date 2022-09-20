from src.data.main_page import *
from src.elements.elements import *
from src.pages.base_page import BasePage
from src.pages.componenrs.menu_elements.bottom_menu import BottomMenu


class MainPage(BasePage):

    _currents_page_url = BASE_URL
    login_input = InputField(*login_input_fild)
    password_input = InputField(*password_input_fild)
    login_btn = Button(*login_btn)
    logout_btn = Button(*logout_link)

    def __init__(self, webdriver: WebDriver):
        super().__init__(webdriver)
        self.button_menu = BottomMenu(webdriver=webdriver)

    def is_current_page(self):
        return self.webdriver.current_url == self._currents_page_url

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




