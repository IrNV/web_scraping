from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator


def is_common(ngram):
    """
    Проверка входит ли n-грамма в самые распространенные слова,
    для того что бы убрать n-граммы, по типу "to the", "to be", "in the"...
    """
    common_words = ["the", "be", "and", "of", "a", "in", "to", "have", "it",
                    "i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
                    "they", "is", "an", "at", "but", "we", "his", "from", "that", "not",
                    "by", "she", "or", "as", "what", "go", "their","can", "who", "get",
                    "if", "would", "her", "all", "my", "make", "about", "know", "will",
                    "as", "up", "one", "time", "has", "been", "there", "year", "so",
                    "think", "when", "which", "them", "some", "me", "people", "take",
                    "out", "into", "just", "see", "him", "your", "come", "could", "now",
                    "than", "like", "other", "how", "then", "its", "our", "two", "more",
                    "these", "want", "way", "look", "first", "also", "new", "because",
                    "day", "more", "use", "no", "man", "find", "here", "thing", "give",
                    "many", "well"]

    for word in ngram:
        if word in common_words:
            return True

    return False


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
        if is_common(text[i:i+n]):
            continue
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