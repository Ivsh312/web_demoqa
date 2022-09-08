from selenium.webdriver.common.by import By
SERVICES_PAGE_URL = "https://parabank.parasoft.com/parabank/services.htm"
table_name = ('//*[@id="rightPanel"]/span[1]', By.XPATH)
table_content = ('//*[@id="rightPanel"]/table[1]', By.XPATH)
table_cell_locator = '//*[@id="rightPanel"]/table[1]/tbody/tr[{row_numbe}]/td[{column_numbe}]'
table_cell = (table_cell_locator, By.XPATH)