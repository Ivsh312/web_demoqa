from selenium.webdriver.common.by import By

ADMIN_PAGE_URL = 'https://parabank.parasoft.com/parabank/admin.htm'

database_section = ('//*[@id="rightPanel"]/table/tbody/tr/td[1]', By.XPATH)
database_section_name = ('//*[@id="rightPanel"]/table/tbody/tr/td[1]/h3', By.XPATH)
initialize_btn = ('//*[@id="rightPanel"]/table/tbody/tr/td[1]/form/table/tbody/tr/td[1]/button', By.XPATH)
clean_btn = ('//*[@id="rightPanel"]/table/tbody/tr/td[1]/form/table/tbody/tr/td[2]/button', By.XPATH)


jms_section = ('//*[@id="rightPanel"]/table/tbody/tr/td[2]/form', By.XPATH)
jms_name = ('//*[@id="rightPanel"]/table/tbody/tr/td[2]/h3', By.XPATH)
startup_btn = ('//*[@id="rightPanel"]/table/tbody/tr/td[2]/form/table/tbody/tr/td[3]/input', By.XPATH)
status_label = ('//*[@id="rightPanel"]/table/tbody/tr/td[2]/form/table/tbody/tr/td[1]/b', By.XPATH)
status_indicator = ('//*[@id="rightPanel"]/table/tbody/tr/td[2]/form/table/tbody/tr/td[2]', By.XPATH)

JMS_NAME = 'jms_name'
STARTUP_BTN = 'startup_btn'
STATUS_LABEL = 'status_label'
STATUS_INDICATOR = 'status_indicator'

data_access_mode = ('//*[@id="adminForm"]/table[1]', By.XPATH)
soap_radiobutton = ('//*[@id="accessMode1"]', By.XPATH)
rest_json_radiobutton = ('//*[@id="accessMode3"]', By.XPATH)
rest_xml_radiobutton = ('//*[@id="accessMode2"]', By.XPATH)
jdbc_radiobutton = ('//*[@id="accessMode4"]', By.XPATH)

SOAP_RADIOBUTTON = 'jdbc_radiobutton'
REST_JSON_RADIOBUTTON = 'rest_json_radiobutton'
REST_XML_RADIOBUTTON = 'rest_xml_radiobutton'
JDBC_RADIOBUTTON = 'jdbc_radiobutton'
