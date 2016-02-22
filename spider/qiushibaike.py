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
		print "获取第%d页..." % page_num
		url = 'http://www.qiushibaike.com/hot/page/' + str(page_num)
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
		print "load_page self.pages:%d" % len(self.pages)
		while self.enable:
			if len(self.pages) < 2:
				try:
					# 获取新页面中的段子
					my_page = self.get_page(self.page)
					self.page += 1
					self.pages.append(my_page)
				except Exception, e:
					print 'except:', e
					print '无法连接糗事百科\n'
			else:
				time.sleep(1)


	def show_page(self, now_page, page_num):
		print '\n显示第%d页 共%d条:' % (page_num, len(now_page))
		i = 0
		for items in now_page:
			print "第%d条" % i, items
			i += 1
			user_input = raw_input()
			if user_input == 'quit':
				self.enable = False
				break

	def start_model(self):
		self.enable = True
		page = self.page

		print "start_model enable:%d" % self.enable
		
		# 新建一个线程在后台加载段子并存储
		# 纯粹是为了用下线程
		thread.start_new_thread(self.load_page,())
		while self.enable:
			# self.load_page()
			if self.pages:
				current_page = self.pages[0]
				del self.pages[0]
				self.show_page(current_page, page)
				page += 1
				print 'page number:' + str(page)



if __name__ == '__main__':
	print "start program........."

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
		程序如果使用IDLE，raw_input可以正常使用
		如果使用python xx.py 来运行，raw_input 会有问题，如不能运行起来
	"""

	print "please input in interger"
	test_model = SpiderModel()
	test_model.start_model()
