# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup
import datetime
import random


WIKI_URL = 'https://en.wikipedia.org'
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'}
PROXY = {'https': 'http://10.144.1.10:8080'}


def get_soup_from_link(url):
    req = requests.get(url, headers=HEADERS, proxies=PROXY, timeout=5)
    return BeautifulSoup(req.text)

def get_link(article_url):
    url = WIKI_URL + article_url
    print(url)
    bs_obj = get_soup_from_link(url)
    # not include ':'
    return bs_obj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def main():
    random.seed(datetime.datetime.now())
    start_artical_url = '/wiki/Kevin_Bacon'
    links = get_link(start_artical_url)

    count = 0
    while(len(links) > 0):
        new_artical = links[random.randint(0, len(links)-1)].attrs['href']
        print(new_artical)
        links = get_link(new_artical)
        count += 1
        if count > 1000:
            break

if __name__ == '__main__':
    main()

