#! /usr/bin/env python
# -*- coding = utf-8 -*-

# Usage: get douban's book data


import bs4
import requests

WEB_SITE = 'https://book.douban.com/'
FIRST_PAGE_TAG = 'tag/%E7%BC%96%E7%A8%8B'

# 'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B'


def save_to_file(bookList):
    recordFile = open('bookList.txt', 'wb')
    for book in bookList:
        recordFile.write(book + '\r\n')

    recordFile.close()


def main():
    page_tag = FIRST_PAGE_TAG

    while True:
        res = requests.get(WEB_SITE + page_tag)
        try:
            res.raise_for_status()
        except Exception as e:
            print('There is an error ' + str(e))

        htmlSoup = bs4.BeautifulSoup(res.text)

        bookList = []
        # print(type(htmlSoup.select('a')))

        for elemt in htmlSoup.select('a'):
            if elemt.attrs.has_key('title'):
                book = elemt.attrs.get('title')
                try:
                    print(book)
                    # for chinese, we need encode the data to 'gb2312',
                    # then we can save to file correctly
                    bookList.append(book.encode('gbk'))
                except UnicodeEncodeError as e:
                    print('Can not decode the book name...')

        # save_to_file(bookList)

        # pageInfo = htmlSoup.select('div [class="paginator"]')
        pageInfo = htmlSoup.select('.next a')

        print(pageInfo)
        print(pageInfo[0].attrs)
        print(pageInfo[0].get('href'))
        page_tag = pageInfo[0].get('href')

        # need add break condition


if __name__ == '__main__':
    main()
