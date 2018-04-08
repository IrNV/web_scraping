from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def get_links(page_url):
    global pages
    html = urlopen("http://en.wikipedia.org" + page_url)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # Мы получили новую страницу
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                get_links(newPage)
            else:
                print("Страница:", link.attrs["href"], " уже есть в нашем списке")

get_links("")
