# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup
import random

WIKI_URL = 'https://en.wikipedia.org'
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'}
PROXY = {'https': 'http://10.144.1.10:8080'}

pages = set()
def get_soup_from_link(url):
    req = requests.get(url, headers=HEADERS, proxies=PROXY, timeout=5)
    return BeautifulSoup(req.text)

def get_link(article_url):
    global pages
    url = WIKI_URL + article_url
    print(url)
    bs_obj = get_soup_from_link(url)
    
    try:
        print(bs_obj.h1.get_text())
        print(bs_obj.find("div", {"id":"mw-content-text"}).findAll("p")[0])
        print(bs_obj.find("span", {"class":"wb-langlinks-edit wb-langlinks-link"}).find("a").attrs["href"])
    except AttributeError:
        print("Lose some attribute")
    except IndexError:
        print("Out of the index")
        exit()

    for link in bs_obj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                new_page = link.attrs['href']
                print('--------------\n' + new_page)
                pages.add(new_page)
                get_link(new_page)

def main():
    get_link('')

if __name__ == '__main__':
    main()