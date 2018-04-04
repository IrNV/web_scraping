from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

images = bsObj.findAll("img",
                       {"src": re.compile("\.\./img/gifts/img.*\.jpg")})

# Находим цену всех продуктов используя функцию нахождения родителя и
# предыдущего одноуровневого тега
for image in images:
    print("Image src:", image["src"])
    print("Price", bsObj.find("img", {"src": image["src"]
                                      }).parent.previous_sibling.get_text())
