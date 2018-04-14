import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")
# Получаем данные с первой таблице на странице
table = bsObj.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")
csvFile = open("C:/Users/1/PycharmProjects/web_scraping/projects from book/editors.csv",
               'wt', encoding="utf-8")
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
