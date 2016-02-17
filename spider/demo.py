#!/usr/bin/env python
# coding:utf-8

import urllib
import urllib2

# url = 'http://www.baidu.com'
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# print response.read()


url = 'http://www.zhihu.com/#signin'
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
# referer = 'http://www.zhihu.com/'
values = {'username' : 'cc.chong.chen@gmail.com', 'password' : 'l6o2v0e806love'}
# headers = {'User-Agent' : user_agent, 'Referer' : referer}

data = urllib.urlencode(values)
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)

page = response.read()

print page
