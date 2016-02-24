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
		self.url = 'http://aqicn.org/city/' + city + '/'
		

	def open_page(self):
		aqi_city_page = urllib2.urlopen(self.url).read()
		print self.url
		# print aqi_city_page
		f = open('page_string', 'w')
		f.writelines(aqi_city_page)
		f.close()
		
		# <div class="aqivalue" style=" font-size:80px; background-color: #cc0033;color:#ffffff; " title="Unhealthy">161</div>
		# <td id="cur_pm25" class="tdcur" style="font-weight:bold;font-size:11px;" align="center">161</td>
		# aqi_pm25_match = re.search(r'<div class=\'aqivalue\'.*?>(\d+?)</div>', aqi_city_page, re.S)
		aqi_pm25_cur_match = re.search(r'<td id=\'cur_pm25\'.*?>(\d+?)</td>', aqi_city_page, re.S)
		aqi_pm25_min_match = re.search(r'<td id=\'min_pm25\'.*?>(\d+?)</td>', aqi_city_page, re.S)
		aqi_pm25_max_match = re.search(r'<td id=\'max_pm25\'.*?>(\d+?)</td>', aqi_city_page, re.S)
		if aqi_pm25_cur_match:
			print aqi_pm25_cur_match.group(0)
		if aqi_pm25_min_match:
			print aqi_pm25_min_match.group(0)
		if aqi_pm25_max_match:
			print aqi_pm25_max_match.group(0)

if __name__ == '__main__':
	test_module = AqiModule('hangzhou')
	test_module.open_page()