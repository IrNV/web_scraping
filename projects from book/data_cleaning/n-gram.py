from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string


def clean_input(text):
    """
    Очистка данных
    """
    text = re.sub('\n+', " ", text)  # Замена символов переноса строки на пробел
    text = re.sub('\[[0-9]*\]', "", text)  # Замена ссылок на пустую строку
    text = re.sub(' +', " ", text)  # Замена нескольких пробелов на один
    text = bytes(text, "UTF-8")
    text = text.decode("ascii", "ignore")
    clean_text = []
    text = text.split(' ')
    for item in text:
        item = item.strip(string.punctuation)  # Удаляем знаки препинания
        # Берем слова длинна которых больше 1 или это слова "a" и "i"
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            clean_text.append(item)
    return clean_text


def ngrams(text, n):
    input = clean_input(text)
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i + n])
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngrams = ngrams(content, 2)

print(ngrams)
print("2-grams count is: " + str(len(ngrams)))

