from selenium import webdriver


driver = webdriver.Firefox()
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver.get_cookies())

# Сохраняем куки с первого входа
savedCookies = driver.get_cookies()
driver2 = webdriver.Firefox()
driver2.get("http://pythonscraping.com")
# Удаляем куки 2-го входа
driver2.delete_all_cookies()
print(driver2.get_cookies())

# Записываем куки из первого входа
for cookie in savedCookies:
    driver2.add_cookie(cookie)
# driver2.get("http://pythonscraping.com")
# driver2.implicitly_wait(1)
print(driver2.get_cookies())
