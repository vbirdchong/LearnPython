#! /usr/bin/env python
# -*- coding=utf-8 -*-


import requests
import bs4
import re
import sys
import urllib


reload(sys)
sys.setdefaultencoding('utf8')


def dou_ban_book_search(bookTagLists):
    bookLists = []
    for bookTag in bookTagLists:
        print(bookTag.decode())
        bookList = book_search(bookTag)

    return bookLists


def book_search(bookTag):
    bookList = []
    pageIdx = 49

    while True:
        url = 'https://book.douban.com/tag/' + urllib.quote(bookTag) \
                + '?start=' + str(pageIdx * 20) + '&type=T'
        print(url)

        res = requests.get(url)
        try:
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text)
            # print(soup)
        except Exception as e:
            print('There was an error for get url...')
            raise e

        subjectListSoup = soup.select('div[id="subject_list"]')
        subjectItem = subjectListSoup[0].select('li[class="subject-item"]')
        if len(subjectItem) == 0:
            print('We reached the last page.')
            break
        else:
            for bookSubjectItem in subjectItem:
                bookList.append(get_book_info(bookSubjectItem))

        pageIdx += 1
        print('Geting book info on Page: %d' % (pageIdx))
    return bookList


def get_book_info(bookSubjectItem):
    bookTitle = bookSubjectItem.select('a[title]')[0].get('title') # maybe we will use encode()
    # print(bookTitle)
    bookUrl = bookSubjectItem.select('a[href]')[0].get('href')
    # print(bookUrl)
    authorInfo, pressInfo = get_book_base_info(bookSubjectItem)

    try:
        ratingNum = bookSubjectItem.select('span[class="rating_nums"]')[0].get_text()
    except Exception as e:
        ratingNum = '0.0'
    # print(ratingNum)

    print(bookTitle)
    print(authorInfo)
    print(pressInfo)
    print(ratingNum)
    return [bookTitle, authorInfo, pressInfo, ratingNum]


def get_book_base_info(bookSubjectItem):
    bookPublic = bookSubjectItem.select('div[class="pub"]')[0].get_text().strip()
    infoList = bookPublic.split('/')
    try:
        authorInfo = 'Author/Translator: ' + '/'.join(infoList[0:-3])
    except:
        authorInfo = 'Author/Translatro: ' + 'None'

    try:
        pressInfo = 'Press: ' + '/'.join(infoList[-3:])
    except:
        pressInfo = 'Press:' + 'None'

    return authorInfo, pressInfo


def main():
    bookTagLists = ['编程', '科学']
    bookList = dou_ban_book_search(bookTagLists)


if __name__ == '__main__':
    main()
