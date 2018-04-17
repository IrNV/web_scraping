from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

# Поиск дочерних элементов
for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)

# Поиск одноуровневых тегов за исключением первого
for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

# Находим картинку первого товара и ищем цену
print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"
                         }).parent.previous_sibling.get_text())
