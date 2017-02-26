#! /usr/bin/env python
# -*- coding=utf-8 -*-

# Usage: get douban's book data


import bs4
import requests
import re


WEB_SITE = 'https://book.douban.com/'
FIRST_PAGE_TAG = 'tag/%E7%BC%96%E7%A8%8B?start=0&type=T'
# FIRST_PAGE_TAG = 'tag/%E7%BC%96%E7%A8%8B?start=980&type=T'
TOP_BOOK_NUM = 50

def save_to_file(bookList, ratingNumList):
    recordFile = open('bookList.txt', 'wb')
    for i in range(len(bookList)):
        recordFile.write(str(i + 1) + '. ' + bookList[i] \
                            + ' :' + ratingNumList[i] + '\r\n')
    recordFile.close()


def save_top_book_to_file(topBookList):
    topBookFile = open('topBookList.txt', 'wb')
    for i in range(len(topBookList)):
        topBookFile.write(str(i + 1) + '. ' + topBookList[i][0] \
                            + ' :' +  topBookList[i][1] + '\r\n')
    topBookFile.close()


def get_top_book(bookList, ratingNumList, topNum):
    sortedRatingNumlist = sorted(ratingNumList, reverse=True)
    topBookList = []
    for i in range(topNum):
        bookRateIndex = ratingNumList.index(sortedRatingNumlist[i])
        topBookList.append((bookList[bookRateIndex], ratingNumList[bookRateIndex]))
        ratingNumList[bookRateIndex] = '0.0'

    return topBookList


def get_next_page_link(soup):
    nextPageInfo = soup.select('.next a')
    return nextPageInfo[0].get('href')


def get_rating_num(subjectItemInfo):
    ratingInfo = subjectItemInfo.select('[class="rating_nums"]')
    if len(ratingInfo) != 0:
        # this is a unicode type
        return ratingInfo[0].get_text()
    else:
        return '0.0'


def get_book_info(soup, bookList, ratingNumList, pageIndex):
    print('Searching page:' + str(pageIndex / 20 + 1))
    for subjectItem in soup.select('[class="subject-item"]'):
        for itemInfo in subjectItem.select('a[title]'):
            bookName = itemInfo.get('title')
            try:
                bookList.append(bookName.encode('gbk'))
                ratingNum = get_rating_num(subjectItem)
                ratingNumList.append(ratingNum.encode('utf-8'))
            except UnicodeError:
                print('''Can not decode the book name in page:''' \
                    + str(pageIndex / 20 + 1))


def get_soup_from_link(pageLink):
    res = requests.get(WEB_SITE + pageLink)
    try:
        res.raise_for_status()
    except Exception as e:
        raise('There is an error' + str(e))

    return bs4.BeautifulSoup(res.text)


def is_reached_the_last_page(soup):
    if len(soup.select('div [class="paginator"]')) == 0:
        return True
    else:
        return False


def main():
    pageLink = FIRST_PAGE_TAG
    bookList = []
    ratingNumList = []
    pageIndexRegex = re.compile(r'start=(\d+)', flags=0)

    while True:
        soup = get_soup_from_link(pageLink)
        if is_reached_the_last_page(soup):
            print('We reached the last page, ' \
                    'got book number:%d' % (len(bookList)))
            break

        pageIndex = int(pageIndexRegex.search(pageLink).group(1))
        get_book_info(soup, bookList, ratingNumList, pageIndex)
        pageLink = get_next_page_link(soup)

    save_to_file(bookList, ratingNumList)
    save_top_book_to_file(get_top_book(bookList, ratingNumList, TOP_BOOK_NUM))


if __name__ == '__main__':
    main()
