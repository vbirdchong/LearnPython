#!/usr/bin/env python
# coding=utf-8

import re
import urllib2

# http://aqicn.org/city/hangzhou/

class AqiModule(object):
	"""docstring for AqiModule"""
	def __init__(self, city):
		super(AqiModule, self).__init__()
		self.city = city
		# self.url = 'http://aqicn.org/city/' + city + '/'
		self.url = r'http://aqicn.org/city/hangzhou/'
		

	def open_page(self):
		user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
		headers = {'User-Agent' : user_agent}

		request = urllib2.Request(self.url, headers = headers)
		response = urllib2.urlopen(request)
		print 'Content-Length:%s' % response.headers['Content-Length']
		aqi_city_page = response.read()
		print self.url

		f = open('page_string', 'w')
		f.write(aqi_city_page)
		f.close()
		
		self.get_data(aqi_city_page)

	def get_data(self, aqi_city_page):
		# aqi_pm25_match = re.search(r'<div class=\'aqivalue\'.*?>(\d+?)</div>', aqi_city_page, re.S)
		# PM25的数据格式如下
		# <td id='cur_pm25' class='tdcur' style='font-weight:bold;font-size:11px;' align=center>162</td>
		aqi_pm25_cur_match = re.search(r'<td id=\'cur_pm25\'.*?>(\d+?)</td>', aqi_city_page, re.S)
		aqi_pm25_min_match = re.search(r'<td id=\'min_pm25\'.*?>(\d+?)</td>', aqi_city_page, re.S)
		aqi_pm25_max_match = re.search(r'<td id=\'max_pm25\'.*?>(\d+?)</td>', aqi_city_page, re.S)
		if aqi_pm25_cur_match:
			# print aqi_pm25_cur_match.group(0)
			print 'cur_pm25 =' + aqi_pm25_cur_match.group(1)
		if aqi_pm25_min_match:
			# print aqi_pm25_min_match.group(0)
			print 'min_pm25 =' + aqi_pm25_min_match.group(1)
		if aqi_pm25_max_match:
			# print aqi_pm25_max_match.group(0)
			print 'max_pm25 =' + aqi_pm25_max_match.group(1)

		# AQI level : 'no data','Good','Moderate', 'Unhealthy', 'Very Unhealthy', 'Hazardous'
		# <div id=aqiwgtinfo' style='font-size:42px; text-shadow: 1px 1px 0 #ffffff; color:#cc0033'>Unhealthy
		aqi_wgt_match = re.search(r'<div id=aqiwgtinfo.*?>(\S+?)</div>', aqi_city_page, re.S)
		if aqi_wgt_match:
			# print aqi_wgt_match.group(0)
			print 'aqi_wgt_info =' + aqi_wgt_match.group(1)
		else:
			print 'aqi_wgt_match not match'

		# <script>try{checkWidgetUpdateTime(1456398000,' on Thursday, Feb 25th 2016, 20:00 pm','aqiwgtutime963130798');}catch(e){}</script>
		aqi_update_time = re.search(r'<script>try{checkWidgetUpdateTime(.*?)(on.*?), (.*?), (.*?)(\',\'.*?)</script>', aqi_city_page, re.S)
		if aqi_update_time:
			print 'update time:'
			print aqi_update_time.group(2)
			print aqi_update_time.group(3)
			print aqi_update_time.group(4)
		else:
			print 'aqi_update_time not match'



if __name__ == '__main__':
	test_module = AqiModule('hangzhou')
	test_module.open_page()