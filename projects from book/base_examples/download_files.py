import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"


def get_absolute_u_r_l(base_url, source):
    # Заменяем начало источника картинки
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = "http://" + source[4:]
    else:
        url = base_url + "/" + source
    if base_url not in url:
        return None

    # В данном случае проверяем расширение картинки jpg
    if source[-3:] != "jpg":
        return None

    return url


def get_download_path(base_url, absolute_url, download_directory):
    # С помощью модуля os создаем папку и сохраняем туда картинку
    path = absolute_url.replace("www.", "")
    path = path.replace(base_url, "")
    path += download_directory
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path


html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = get_absolute_u_r_l(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl, get_download_path(baseUrl, fileUrl, downloadDirectory))