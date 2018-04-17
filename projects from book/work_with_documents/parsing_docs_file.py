from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

# Считываем файл
wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
# Считываем как обьект бинарного файла
wordFile = BytesIO(wordFile)
# Разархивируем docx файл, т.к. по-умолчанию это архив
document = ZipFile(wordFile)
# Считываем как XML-файл
xml_content = document.read('word/document.xml')
# Дальше производим парсинг XML-файла
wordObj = BeautifulSoup(xml_content.decode('utf-8'), "xml")
textStrings = wordObj.findAll("w:t")
for textElem in textStrings:
    print(textElem.text)
