from selenium.webdriver.common.by import By

BASE_URL = "https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC"
LOGIN_PAGE_URL = "https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC"

login_input_fild = ('//*[@id="loginPanel"]/form/div[1]/input', By.XPATH)
password_input_fild = ('//*[@id="loginPanel"]/form/div[2]/input', By.XPATH)

login_btn = ('//*[@id="loginPanel"]/form/div[3]/input', By.XPATH)

test_password = 'test'
test_login = 'test'

logout_link = ('//*[@id="leftPanel"]/ul/li[8]/a', By.XPATH)