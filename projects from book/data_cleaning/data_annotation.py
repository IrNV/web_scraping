from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator


def clean_input(text):
    """
    Очистка данных
    """
    text = re.sub('\n+', " ", text).lower()  # Замена символов переноса строки на пробел
    text = re.sub('\[[0-9]*\]', "", text)  # Замена ссылок на пустую строку
    text = re.sub(' +', " ", text)  # Замена нескольких пробелов на один
    text = bytes(text, "UTF-8")
    text = text.decode("ascii", "ignore")
    clean_text = []
    text = text.split(' ')
    for item in text:
        item = item.strip(string.punctuation) # Удаляем знаки препинания
        # Берем слова длинна которых больше 1 или это слова "a" и "i"
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            clean_text.append(item)
    return clean_text


def ngrams(text, n):
    text = clean_input(text)
    output = {}
    for i in range(len(text) - n + 1):
        ngram_temp = " ".join(text[i:i + n])
        if ngram_temp not in output:
            output[ngram_temp] = 0
        output[ngram_temp] += 1
    return output

html = urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.get_text()
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(sortedNGrams)
