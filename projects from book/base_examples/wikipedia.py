from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())


def get_links(article_url):
    html = urlopen("http://en.wikipedia.org" + article_url)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a",
                                                            href=re.compile("^(/wiki/)((?!:).)*$"))

links = get_links("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = get_links(newArticle)
