# -*- coding=utf-8 -*-

import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_absolute_url(base_url, source):
    if source.startswith("http://wwww."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = "http://" + source[4:]
    else:
        url = base_url + "/" + source
    return url

def get_download_path(base_url, absoulte_url, download_directory, path_dufault=True):
    path = absoulte_url.replace("www.", "")

    if path_dufault:
        path = path.replace(base_url, "").split('/')
        path = download_directory + '/' + path[-1]
    else:
        path = path.replace(base_url, "")
        path = download_directory + path

    print("Path: " + path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

def main():
    download_directory = "downloaded_img"
    base_url = "http://pythonscraping.com"

    html = urlopen("http://pythonscraping.com")
    bs_obj = BeautifulSoup(html, "lxml")
    download_list = bs_obj.findAll("img")

    for download in download_list:
        file_url = get_absolute_url(base_url, download['src'])
        if file_url is not None:
            print(file_url)
            urlretrieve(file_url, get_download_path(base_url, file_url, download_directory, path_dufault=True))

if __name__ == '__main__':
    main()