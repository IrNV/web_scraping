import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver


#   Создаем новый драйвер Selenium
driver = webdriver.Firefox()
driver.get("https://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200#reader_1427030200")
time.sleep(2)

imageList = set()

#   Пока кнопка со стрелкой вправо кликабельна, переворачиваем страницу
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    # Ищем URL-адреса изображений на всех загруженных страницах (могут загрузиться
    # сразу несколько страниц, но дупликаты не будут добавлены в набор)
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)
driver.quit()

#   Начинаем обработку изображений, собранных с URL-адресов, с помощью Tesseract
for image in sorted(imageList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open("page.txt", "r")
    print(f.read())
