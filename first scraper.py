from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("We can't take a page")
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        print("We can't find a tag")
        return None

    return title

title = get_title("http://www.pythonscraping.com/exercises/exercise1.html")
if title is None:
    print("We have a problem")
else:
    print(title)
