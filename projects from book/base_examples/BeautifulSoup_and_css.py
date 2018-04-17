from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

nameList = bsObj.findAll("span", {"class": "green"})
headers = bsObj.findAll({"h1", "h2", "h3"})  # {} group of tags which we want to find

for header in headers:
    print(header.get_text())
print("\n")
for name in nameList:
    print(name.get_text())
