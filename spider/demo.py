#!/usr/bin/env python
# coding:utf-8

import urllib
import urllib2
import re
import time
import thread

class SpiderModel(object):
	"""docstring for SpiderModel"""
	def __init__(self):
		super(SpiderModel, self).__init__()
		self.page = 1
		self.pages = []
		self.enable = False
		
	# 获取页面中的所有的段子，添加到返回列表中
	def get_page(self, page_num):
		print "获取第%s页..." % page_num
		url = 'http://www.qiushibaike.com/hot/page/' + page_num
		user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
		headers = {'User-Agent' : user_agent}

		request = urllib2.Request(url, headers = headers)
		response = urllib2.urlopen(request)
		
		# 获取到页面
		page = response.read()
		# print page
		# 网上教程这里需要对页面做转换，目前可以直接使用页面中的编码
		# unicode_page = page#.decode("utf-8")

		# 百科中的段子如下格式
		# <div class="content">
		# 今天接亲，新娘家人不高兴了，说我们接亲的十辆婚车双闪闪得不整齐
		# <!--1455775450-->
		# </div>

		# 找出所有 class="content" 的div标记
		my_items = re.findall('<div.*?class="content">(.*?)<!--', page, re.S | re.M)
		items = []
		for item in my_items:
			items.append(item.replace('<br/>', '\n'))
		
		return items

	def load_page(self):
		# 如果用户没有输入quit，则程序一直运行
		while self.enable:
			print 'aaaaaaaa\n'
			if len(self.pages) < 2:
				try:
					# 获取新页面中的段子
					print 'page:%d' % self.page
					my_page = self.get_page(str(self.page))
					self.page += 1
					self.pages.append(my_page)
				except Exception, e:
					print 'except:', e
					print '无法连接糗事百科\n'
			else:
				print 'bbb'
				time.sleep(1)

	def show_page(self, now_page, page_num):
		for items in now_page:
			print '\n 第%d页' % page_num, items
			user_input = raw_input()
			if (user_input == 'quit'):
				self.enable = False
				break

	def start_model(self):
		self.enable = True
		page = self.page

		thread.start_new_thread(self.load_page, ())

		while self.enable:
			if self.pages:
				current_page = self.pages[0]
				del self.pages[0]
				self.show_page(current_page, page)
				page += 1
				print page





#----------- 程序的入口处 -----------
print """
---------------------------------------
   程序：糗百爬虫
   版本：0.3
   作者：why
   日期：2014-06-03
   语言：Python 2.7
   操作：输入quit退出阅读糗事百科
   功能：按下回车依次浏览今日的糗百热点
---------------------------------------
   原文地址(源代码):http://blog.csdn.net/pleasecallmewhy/article/details/8932310
   修改内容:网址和正则表达式部分
   修改者:Ryan
   修改日期:2015-09-19
   测试通过版本:Python 2.7.10
---------------------------------------
"""

test_model = SpiderModel()
test_model.start_model()


# now_page = test_model.get_page(1)
# for item in now_page:
# 	print item