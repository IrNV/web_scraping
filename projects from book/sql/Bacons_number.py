from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import MySQLdb
conn = MySQLdb.connect(host='host', user='username, passwd="password", db=db', charset='utf8')
cur = conn.cursor()


def insert_page_if_not_exists(url):
    """
    Проверяем есть ли среди страниц данная. Если нет, то добавляем,
    если да, то возвращаем id
    """
    cur.execute("SELECT * FROM pages WHERE url = %s", (url, ))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages (url) VALUES (%s)", (url, ))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]


def insert_link(fromPageId, toPageId):
    """
    Вставляем id страниц у которых есть связь
    """
    cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s",
                (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)",
                    (int(fromPageId), int(toPageId)))
    conn.commit()

pages = set()


def get_links(page_url, recursion_level):
    """
    Получаем ссылки с страницы и добавляем в БД возможные переходы с данной страницы
    на другие
    """
    global pages
    if recursion_level > 1:
        return
    page_id = insert_page_if_not_exists(page_url)
    html = urlopen("http://en.wikipedia.org" + page_url)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        insert_link(page_id,
                    insert_page_if_not_exists(link.attrs['href']))
        if link.attrs['href'] not in pages:
            # Мы получили новую страницу, добавляем ее и ищем ссылки
            new_page = link.attrs['href']
            pages.add(new_page)
            get_links(new_page, recursion_level + 1)


get_links("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()
