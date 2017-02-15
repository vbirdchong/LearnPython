#! /usr/bin/env python
# coding = utf-8

import re

upperCase = re.compile(r'[A-Z]+')
lowerCase = re.compile(r'[a-z]+')
digital = re.compile(r'\d+')
minPasswordLen = 8

def password_check(password):
	if len(password) > minPasswordLen:
		if (upperCase.search(password) != None 
			and lowerCase.search(password) != None
			and digital.search(password) != None):
			return True
	else:
		return False

def main():
	password = raw_input('Please input the password to check:')
	if password_check(password) is True:
		print('password is ok...')
	else:
		print('password is not avalilable...')

if __name__ == '__main__':
	main()