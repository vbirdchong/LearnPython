#!/usr/bin/env python
# coding=utf-8

import re
import urllib2
import csv

# http://aqicn.org/city/hangzhou/

class AqiModule(object):
	"""docstring for AqiModule"""
	def __init__(self, city):
		super(AqiModule, self).__init__()
		self.city = city
		# self.url = 'http://aqicn.org/city/' + city + '/'
		self.url = r'http://aqicn.org/city/hangzhou/'
		self.cur_pm25 = 0
		self.min_pm25 = 0
		self.max_pm25 = 0
		self.aqi_wgt_info = 'no data'
		self.update_time = '2016/02/04 hh:mm'
		self.week = None
		
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
		
		self.get_data_pm25(aqi_city_page)
		self.get_update_time(aqi_city_page)

		# AQI level : 'no data','Good','Moderate', 'Unhealthy', 'Very Unhealthy', 'Hazardous'
		# <div id=aqiwgtinfo' style='font-size:42px; text-shadow: 1px 1px 0 #ffffff; color:#cc0033'>Unhealthy
		aqi_wgt_match = re.search(r'<div id=aqiwgtinfo.*?>(\S+?)</div>', aqi_city_page, re.S)
		if aqi_wgt_match:
			# print aqi_wgt_match.group(0)
			print 'aqi_wgt_info =' + aqi_wgt_match.group(1)
		else:
			print 'aqi_wgt_match not match'

		
	def get_update_time(self, aqi_city_page):
		# <script>try{checkWidgetUpdateTime(1456398000,' on Thursday, Feb 25th 2016, 20:00 pm','aqiwgtutime963130798');}catch(e){}</script>
		aqi_update_time = re.search(r'<script>try{checkWidgetUpdateTime(.*?)on (.*?), (.*?), (.*?)(\',\'.*?)</script>', aqi_city_page, re.S)
		if aqi_update_time:
			print 'update time:'
			print aqi_update_time.group(2)
			print aqi_update_time.group(3)
			print aqi_update_time.group(4)
			
			self.week = aqi_update_time.group(2)
			# 把日期转换成 '2016 Feb 25' 这种格式，方便存到CSV之后进行数据统计，
			# -4 : '2016'
			# -1 : ' '
			# -2 : 'th', 'rd', 'st', 'nd'
			self.data = aqi_update_time.group(3)[-4:] + ' ' + aqi_update_time.group(3)[:len(aqi_update_time.group(3)) - 4 - 1 - 2]
			self.time = aqi_update_time.group(4)
		else:
			print 'aqi_update_time not match'


	def get_data_pm25(self, aqi_city_page):
		# aqi_pm25_match = re.search(r'<div class=\'aqivalue\'.*?>(\d+?)</div>', aqi_city_page, re.S)
		# PM25的数据格式如下
		# <td id='cur_pm25' class='tdcur' style='font-weight:bold;font-size:11px;' align=center>162</td>
		aqi_pm25_cur_match = re.search(r'<td id=\'cur_pm25\'.*?>(\d+?)</td>', aqi_city_page, re.S)
		aqi_pm25_min_match = re.search(r'<td id=\'min_pm25\'.*?>(\d+?)</td>', aqi_city_page, re.S)
		aqi_pm25_max_match = re.search(r'<td id=\'max_pm25\'.*?>(\d+?)</td>', aqi_city_page, re.S)
		if aqi_pm25_cur_match:
			# print aqi_pm25_cur_match.group(0)
			print 'cur_pm25 =' + aqi_pm25_cur_match.group(1)
			self.cur_pm25 = int(aqi_pm25_cur_match.group(1))
		if aqi_pm25_min_match:
			# print aqi_pm25_min_match.group(0)
			print 'min_pm25 =' + aqi_pm25_min_match.group(1)
			self.min_pm25 = int(aqi_pm25_min_match.group(1))
		if aqi_pm25_max_match:
			# print aqi_pm25_max_match.group(0)
			print 'max_pm25 =' + aqi_pm25_max_match.group(1)
			self.max_pm25 = int(aqi_pm25_max_match.group(1))


	def detect_csv_header(self, file_name):
		has_header = True
		try:
			with open(file_name, 'r') as csv_file:
				csv_read = csv.reader(csv_file)
				for row in csv_read:
					print 'row'
					print row
					# 这里还有一点bug, 文件已经存在，但里面的内容是空的，这样的写入的时候会多出一行空行
					if row == []:
						has_header = False
						print 'The file not exist, will be creat later...'
					break
		except IOError as e:
			print 'The file not exist, will be creat later...'
			has_header = False

		return has_header
		

	def save_data(self, file_name='aqi_record.csv'):
		has_header = self.detect_csv_header(file_name)
		with open(file_name, 'ab+') as csv_file:
			csv_writer = csv.writer(csv_file)
			# 如果之前没有数据写入过，则需要将标识信息写上
			if has_header == False:
				csv_writer.writerow(['Data', 'Week', 'Time', 'Curren PM25', 'Min PM25', 'Max PM25'])

			# 将数据追加记录
			data = [self.data, self.week, self.time, self.cur_pm25, self.min_pm25, self.max_pm25]
			csv_writer.writerow(data)




if __name__ == '__main__':
	test_module = AqiModule('hangzhou')
	test_module.open_page()
	test_module.save_data()