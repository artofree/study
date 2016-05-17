from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome()
driver.get("http://www.google.com")

elem = driver.find_element_by_id("lst-ib")
elem.send_keys("123")
elem.send_keys(Keys.RETURN)
assert "No results found."
driver.close()