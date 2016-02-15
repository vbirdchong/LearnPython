#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.shelve_db as db
# from methods.shelve_db import get_user

class IndexHandler(tornado.web.RequestHandler):
	"""docstring for IndexHandler"""
	def get(self):
		self.render("index.html")

	def post(self):
		username = self.get_argument("username")
		password = self.get_argument("password")
		userinfo = db.get_user(username)
		if userinfo:
			if password == userinfo[username]:
				self.write('welcome you: ' + username)
			else:
				self.write('Your password is not correct!')
		else:
			self.write('Sorry. There is no this user!')

		