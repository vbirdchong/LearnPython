#!/usr/bin/env python
# coding=utf-8

import shelve

db_file = r'/home/chonchen/python/tornado/pro1/methods/username.db'

def check_user(name, user_list):
	for i in range(len(user_list)):
		if user_list[i].has_key(name):
			return False

	return True

def add_user(name, password):
	try:
		file = shelve.open(db_file, writeback=True)
		if (file.has_key('userinfo') and check_user(name, file['userinfo'])):
			file['userinfo'].append({name:password})
		else:
			file['userinfo'] = [{name:password}]
	finally:
		file.close()

def del_user(name):
	retval = False
	try:
		file = shelve.open(db_file, writeback=True)
		if (file.has_key('userinfo')):
			user_number = len(file['userinfo'])
			for i in range(user_number):
				if file['userinfo'][i].has_key(name):
					del file['userinfo'][i]
					retval = True
					break
	finally:
		file.close()

	return retval

def get_user(name):
	ret_data = {}
	try:
		file = shelve.open(db_file)
		if (file.has_key('userinfo')):
			user_number = len(file['userinfo'])
			for i in range(user_number):
				if file['userinfo'][i].has_key(name):
					ret_data = file['userinfo'][i]
					break
	finally:
		file.close()

	return ret_data



def print_user():
	try:
		file = shelve.open(db_file)
		print "Open success!"
		if (file.has_key('userinfo')):
			user_number = len(file['userinfo'])
			for i in range(user_number):
				print file['userinfo'][i]
	finally:
		file.close()


# if __name__ == '__main__':
# 	print_user()
	
# 	add_user('chen1', '111')
# 	add_user('chen2', '222')
# 	add_user('chen3', '333')
# 	print_user()

# 	user = get_user('chen1')
# 	print user

# 	del_user('chen3')
# 	print_user()
	
	
	
	