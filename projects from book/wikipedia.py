from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")

# Собераем все ссылки, которые ведут на статьи, а не на обсуждения или интсрументарий
for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a",
                                                             href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
