from urllib.request import urlopen
from bs4 import BeautifulSoup


def ngrams(text, n):
    text = text.split(' ')
    output = []
    for i in range(len(text) - n + 1):
        output.append(text[i:i + n])
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngrams = ngrams(content, 2)

print(ngrams)
print("2-grams count is: " + str(len(ngrams)))

