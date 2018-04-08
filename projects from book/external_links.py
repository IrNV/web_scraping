from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random


pages = set()
random.seed(datetime.datetime.now())


def get_internal_links(bsObj, include_url):
    internal_links = []
    # Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+include_url+")")):
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in internal_links:
                    internal_links.append(link.attrs['href'])
    return internal_links


# Извлекает список всех внешних ссылок, найденных на странице
def get_external_links(bsObj, exclude_url):
    external_links = []
    # Находит все ссылки, которые начинаются с "http" или "www"
    # не содержат текущий URL-адрес
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+exclude_url+").)*""$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in external_links:
                external_links.append(link.attrs['href'])

    return external_links


def split_address(address):
    address_parts = address.replace("http://", "").split("/")
    return address_parts


def get_random_external_link(starting_page):
    html = urlopen(starting_page)
    bsObj = BeautifulSoup(html)
    external_links = get_external_links(bsObj, split_address(starting_page)[0])
    if len(external_links) == 0:
        internal_links = get_internal_links(starting_page)
        return get_random_external_link(internal_links[random.randint(0, len(internal_links) - 1)])
    else:
        return external_links[random.randint(0, len(external_links) - 1)]


def follow_external_only(starting_site):
    external_link = get_random_external_link(starting_site)
    print("Random external link is: " + external_link)
    follow_external_only(external_link)

follow_external_only("http://oreilly.com")