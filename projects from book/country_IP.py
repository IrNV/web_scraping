from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json
import datetime
import random
import re

random.seed(datetime.datetime.now())


def get_links(article_url):
    html = urlopen("http://en.wikipedia.org" + article_url)
    bs_obj = BeautifulSoup(html, "html.parser")
    return bs_obj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


def get_history_ips(page_url):
    # Format of history pages is: http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    page_url = page_url.replace("/wiki/", "")
    history_url = "http://en.wikipedia.org/w/index.php?title=" + page_url + "&action=history"
    print("history url is: "+history_url)
    html = urlopen(history_url)
    bs_obj = BeautifulSoup(html)
    # finds only the links with class "mw-anonuserlink" which has IP addresses instead of usernames
    ip_addresses = bs_obj.findAll("a", {"class": "mw-anonuserlink"})
    address_list = set()
    for ipAddress in ip_addresses:
        address_list.add(ipAddress.get_text())
    return address_list


def get_country(ip_address):
    try:
        response = urlopen("http://freegeoip.net/json/" + ip_address).read().decode('utf-8')
    except HTTPError:
        return None
    response_json = json.loads(response)
    return response_json.get("country_code")

links = get_links("/wiki/Python_(programming_language)")

while len(links) > 0:
    for link in links:
        print("-------------------")
        historyIPs = get_history_ips(link.attrs["href"])
        for historyIP in historyIPs:
            country = get_country(historyIP)
            if country is not None:
                print(historyIP+" is from "+country)

    newLink = links[random.randint(0, len(links)-1)].attrs["href"]
    links = get_links(newLink)
