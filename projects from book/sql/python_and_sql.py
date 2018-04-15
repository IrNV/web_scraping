import MySQLdb
from bs4 import BeautifulSoup
import datetime
import random
from urllib.request import urlopen
import re

conn = MySQLdb.connect('localhost', 'user', 'password', 'db', charset='utf8')
cur = conn.cursor()
cur.execute("USE scraping")
random.seed(datetime.datetime.now())


def store(title, content):
    # Сохраняем титулку и контент в БД
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")", (title, content))
    cur.connection.commit()


def get_links(article_url):
    """
    Получаем название статьи, короткий контент после сохраняем в БД.
    Возвращаем все ссылки на странице, которые ведут нас на другие статьи.
    """
    html = urlopen("http://en.wikipedia.org" + article_url)
    bsObj = BeautifulSoup(html, "html.parser")
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div", {"id": "mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = get_links("/wiki/Kevin_Bacon")
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)
        links = get_links(newArticle)
finally:
    cur.close()
    conn.close()
