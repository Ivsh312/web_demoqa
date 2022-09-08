# ---------------------------------------------------------------------------------------------------------------------
# button
# ---------------------------------------------------------------------------------------------------------------------
from selenium.webdriver.common.by import By

HOME_POINT = 'Home'
ABOUT_POINT = 'About Us'
SERVICES_POINT = 'Services'
PRODUCTS_POINT = 'Products'
LOCATIONS_POINT = 'Locations'
FORUM_POINT = 'Forum'
SITE_MAP_POINT = 'Site Map'
CONTACT_US_POINT = 'Contact Us'

home_point = ('//*[@id="footerPanel"]/ul[1]/li[1]', By.XPATH)
about_point = ('//*[@id="footerPanel"]/ul[1]/li[2]', By.XPATH)
services_point = ('//*[@id="footerPanel"]/ul[1]/li[3]', By.XPATH)
products_point = ('//*[@id="footerPanel"]/ul[1]/li[4]', By.XPATH)
locations_point = ('//*[@id="footerPanel"]/ul[1]/li[5]', By.XPATH)
forum_point = ('//*[@id="footerPanel"]/ul[1]/li[6]', By.XPATH)
site_map_point = ('//*[@id="footerPanel"]/ul[1]/li[7]', By.XPATH)
contact_us_point = ('//*[@id="footerPanel"]/ul[1]/li[8]', By.XPATH)






