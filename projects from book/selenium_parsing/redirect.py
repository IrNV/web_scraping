from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException


def wait_for_load(driver):
    """
    Ожидаем пока перейдем на конечную страницу, каждые 0.5 с. в течении 20с опрашивая DOM
    """
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return

driver = webdriver.Firefox()
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
wait_for_load(driver)
print(driver.page_source)
