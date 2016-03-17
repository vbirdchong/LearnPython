#!usr/bin/env ptyhon
# coding=utf-8

import csv
from itertools import islice

time = []
sfn = []
esfn = []

dl_key_value = {
	'time': 'Time',
	'sfn': 'ETtiTraceDlParCell_sfn',
	'esfn': 'ETtiTraceDlParCell_esfn',
	'crnti': 'ETtiTraceDlParUe_crnti'
}

ul_key_value = {
	'time': 'Time',
	'sfn': 'ETtiTraceUlParCell_sfn',
	'esfn': 'ETtiTraceUlParCell_esfn',
	'crnti': 'ETtiTraceUlParUe_crnti'
}

dl_ttitrace_key = ['ETtiTraceDlParUe_crnti', 'Time', 'ETtiTraceDlParCell_sfn', 'ETtiTraceDlParCell_esfn', ]

# record_data = {
# 	'time':[],
# 	'sfn':[],
# 	'esfn':[]
# }

class volte_interval(object):
	"""
	docstring for volte_interval
	"""
	def __init__(self, file_name, crnti=0):
		'''
		param: ul_or_dl [ul:0, dl:1], crnti must be integer
		'''
		super(volte_interval, self).__init__()
		self.crnti = crnti
		self.file_name = file_name
		self.time = []
		self.sfn = []
		self.esfn = []
		self.list_index_param = {}
		self.ttitrace_key = []
		self.ttitrace_key_index = []
		self.record_data = []


	def filter_by_crnti(self):
		self.check_file()
		try:
			with open(self.file_name, 'rb') as csv_file:
				csv_read = csv.reader(csv_file)
				# get the crnti list's index
				'''
				for row in islice(csv_read, 1, 2):
					crnti_list_index = row.index(self.list_index_param['crnti'])
					time_list_index = row.index(self.list_index_param['time'])
					sfn_list_index = row.index(self.list_index_param['sfn'])
					esfn_list_index = row.index(self.list_index_param['esfn'])
					print crnti_list_index, time_list_index, sfn_list_index, esfn_list_index

				for row_data in csv_read:
					# print row_data[crnti_list_index]
					if self.crnti == int(row_data[crnti_list_index]):
						# print row_data
						# print row_data[time_list_index]
						self.time.append(row_data[time_list_index])
						self.sfn.append(int(row_data[sfn_list_index]))
						self.esfn.append(int(row_data[esfn_list_index]))

				print self.time
				print self.sfn
				print self.esfn
				'''

				'''
				不同方式实现
				'''
				for row in islice(csv_read, 1, 2):
					for i in range(len(self.ttitrace_key)):
						self.ttitrace_key_index.append(row.index(self.ttitrace_key[i]))

				for row_data in csv_read:
					# ttitrace_key_index[0] = crnti's index
					# find the same crnti's info
					if self.crnti == int(row_data[self.ttitrace_key_index[0]]):
						for i in range(len(self.ttitrace_key_index)):
							self.record_data[i].append(row_data[self.ttitrace_key_index[i]])
						
		except IOError, e:
			raise e

		'''
		row_name = [self.list_index_param['time'],
					self.list_index_param['sfn'],
					self.list_index_param['esfn']]
		self.save_to_file(row_name)
		'''

		'''
		不同方式实现
		'''
		print self.ttitrace_key_index
		print self.record_data
		self.save_to_file()

	def save_to_file(self, row_name=[]):
		try:
			with open('volte_interval_crnti_'+str(self.crnti)+'.csv', 'wb+') as csv_file:
				csv_write = csv.writer(csv_file)
				'''
				csv_write.writerow(row_name)

				for row_line in range(len(self.time)):
					row = [self.time[row_line], self.sfn[row_line], self.esfn[row_line]]
					csv_write.writerow(row)
				'''

				'''
				不同的实现方式
				'''
				csv_write.writerow(self.ttitrace_key)
				for row in range(len(self.record_data[0])):
					data = []
					sfn_diff = 0
					if (row + 1) != len(self.record_data[0]):
						sfn_diff = (int(self.record_data[2][row+1]) * 10 + int(self.record_data[3][row+1])) - (int(self.record_data[2][row]) * 10 + int(self.record_data[3][row]))
						if (sfn_diff < 0):
							sfn_diff += 10240

					for column in range(len(self.record_data)):
						data.append(self.record_data[column][row])
					data.append(sfn_diff)
					csv_write.writerow(data)
		except Exception, e:
			raise e

	def check_file(self):
		'''
		if self.file_name.upper().find('DL') > -1:
			self.list_index_param = dl_key_value
		elif self.file_name.upper().find('UL') > -1:
			self.list_index_param = ul_key_value
		else:
			raise "file name need contain the key value 'dl' or 'ul'"
		print self.list_index_param		
		'''

		'''
		不同的实现方式
		'''
		if self.file_name.upper().find('DL') > -1:
			self.ttitrace_key = dl_ttitrace_key
			# 根据ttitrace key值得不同，来创建不同的record data list表
			for i in range(len(self.ttitrace_key)):
				self.record_data.append([])
		else:
			raise "file name need contain the key value 'dl' or 'ul'"
		print self.ttitrace_key	

# def filter_by_crnti(crnti):
# 	try:
# 		with open('test.csv', 'rb') as csv_file:
# 			csv_read = csv.reader(csv_file)
# 			# get the crnti list's index
# 			for row in islice(csv_read, 1, 2):
# 				crnti_list_index = row.index('ETtiTraceDlParUe_crnti')
# 				time_list_index = row.index('Time')
# 				sfn_list_index = row.index('ETtiTraceDlParCell_sfn')
# 				esfn_list_index = row.index('ETtiTraceDlParCell_esfn')
# 				print crnti_list_index, time_list_index, sfn_list_index, esfn_list_index

			
# 			for row_data in csv_read:
# 				# print row_data[crnti_list_index]
# 				if crnti == int(row_data[crnti_list_index]):
# 					# print row_data
# 					# print row_data[time_list_index]
# 					time.append(row_data[time_list_index])
# 					sfn.append(row_data[sfn_list_index])
# 					esfn.append(row_data[esfn_list_index])

# 			print time
# 			print sfn
# 			print esfn
# 	except IOError, e:
# 		raise e

def main():
	# input_crnti = raw_input("Please enter the crnti: ")

	input_crnti = '5631'
	if (not (input_crnti.isdigit()) or (int(input_crnti) > 65535 or int(input_crnti) <= 0)):
		print"The input value is invalid, crnti=" + input_crnti
	else:
		test_file = 'test_dl.csv'
		test = volte_interval(test_file, int(input_crnti))
		test.filter_by_crnti()
		# filter_by_crnti(int(input_crnti))


if __name__ == '__main__':
	main()