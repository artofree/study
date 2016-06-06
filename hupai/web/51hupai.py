from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sikuli import *

driver =webdriver.Ie()
driver.get("http://test.alltobid.com/")


assert "No results found."
