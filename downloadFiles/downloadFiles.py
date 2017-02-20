#! /usr/bin/env python
# -*- coding = utf-8 -*-

import requests

def main():
	res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
	try:
		res.raise_for_status()
	except Exception as e:
		print('There was a problem: %s' % e)

	file = open('Romeo and Juliet.txt', 'wb')
	for chunk in res.iter_content(100000):
		file.write(chunk)
	file.close()

if __name__ == '__main__':
	main()