#!/usr/bin/env python
# coding:utf-8

# 西游记之大圣归来吧
# http://tieba.baidu.com/p/4366773707?see_lz=1#

import re
import urllib2
import string

class HTML_Tool(object):
	"""docstring for HTML_Tool"""
	
	# 匹配以下各标签与符号，然后替换之
	BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")
	EndCharToNoneRex = re.compile("<.*?>")

	BngPartRex = re.compile("<p.*?>")
	CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
	CharToNextTabRex = re.compile("<td>")

	replaceTab = [("<","<"), (">",">"), ("&", "&"), ("&", "\""), (" ", " ")]

	def Replace_Char(self, x):
		x = self.BgnCharToNoneRex.sub("", x)
		x = self.BngPartRex.sub("\n 	", x)
		x = self.CharToNewLineRex.sub("\n", x)
		x = self.CharToNextTabRex.sub("\t", x)
		x = self.EndCharToNoneRex.sub("", x)

		for t in self.replaceTab:
			x = x.replace(t[0], t[1])
		return x

		

class BaiduSpider(object):
	"""docstring for BaiduSpider"""
	def __init__(self, url):
		super(BaiduSpider, self).__init__()
		self.myUrl = url + '?see_lz=1'
		self.datas = []
		self.myTool = HTML_Tool()
		

	def baidu_tieba(self):
		# myPage = urllib2.urlopen(self.myUrl).read().decode("gbk")
		myPage = urllib2.urlopen(self.myUrl).read()
		endPage = self.page_counter(myPage)
		title = self.find_title(myPage)
		print "文章名称: " + title

		self.save_data(self.myUrl, title, endPage)

	def find_title(self, myPage):
		myMatch = re.search(r'<h1.*?>(.*?)</h1>', myPage, re.S)
		title = "暂无标题"

		if myMatch:
			title = myMatch.group(1)
		else:
			print "无法加载标题"
		# 文件名不能包含以下字符:  \ / : * ? " > < |
		title = title.replace('\\', '').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','')
		return title

	def page_counter(self, myPage):
		# 匹配 "共有<span class="red">12</span>页" 来获取一共有多少页
		myMatch = re.search(r'class="red">(\d+?)</span>', myPage, re.S)
		if myMatch:
			endPage = int(myMatch.group(1))
			print "爬虫报告：发现楼主共有%d页原创内容" % endPage
		else:
			endPage = 0
			print "爬虫报告：无法计算楼主发布内容页数"

		return endPage

	def save_data(self, url, title, endPage):
		self.get_data(url, endPage)
		print 'save_data title:' + title
		print 'type(title)=', type(title)
		f = open(title.decode('utf-8').encode('cp936')+'.txt', 'w')
		f.writelines(self.datas)
		f.close()
		print "爬虫报告：文件已经下载到本地并打包成txt文件"
		print "请按任意键退出"
		raw_input()

	def get_data(self, url, endPage):
		url = url + '&pn='
		for i in range(1, endPage+1):
			print "爬虫报告：爬虫%d号正在加载中..." % i
			myPage = urllib2.urlopen(url + str(i)).read()
			# self.deal_data(myPage.decode('gbk'))
			self.deal_data(myPage)


	def deal_data(self, myPage):
		myItems = re.findall('id="post_content.*?>(.*?)</div>', myPage, re.S)
		for item in myItems:
			# data = self.myTool.Replace_Char(item.replace("\n","").encode('gbk'))
			data = self.myTool.Replace_Char(item.replace("\n",""))
			self.datas.append(data+'\n')


if __name__ == '__main__':
	print "请输入贴吧地址最后的数字串"
	# bdurl = 'http://tieba.baidu.com/p/' + str(raw_input('http://tieba.baidu.com/p/'))
	bdurl = 'http://tieba.baidu.com/p/4366773707'
	print bdurl

	mySpider = BaiduSpider(bdurl)
	mySpider.baidu_tieba()