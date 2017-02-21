#! /usr/bin/env python
# -*- coding = utf-8 -*-

# Usage: get douban's book data


import bs4
import requests


def save_to_file(bookList):
	recordFile = open('bookList.txt', 'wb')
	for book in bookList:
		recordFile.write(book + '\r\n')

	recordFile.close()


def main():
	res = requests.get('https://book.douban.com/tag/%E7%BC%96%E7%A8%8B')
	try:
		res.raise_for_status()
	except Exception as e:
		print('There is an error ' + str(e))

	htmlSoup = bs4.BeautifulSoup(res.text)

	bookList = []
	for elemt in htmlSoup.select('a'):
		if elemt.attrs.has_key('title'):
			print(elemt.attrs.get('title'))
			# for chinese, we need encode the data to 'gb2312', then we can save to file correctly
			bookList.append(elemt.attrs.get('title').encode('gb2312'))
	
	# save_to_file(bookList)
	
	pageInfo = htmlSoup.select('div [class="paginator"]')
	print(pageInfo)
	print(type(pageInfo))
	print(len(pageInfo))

if __name__ == '__main__':
	main()