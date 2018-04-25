from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver.get_cookies())
