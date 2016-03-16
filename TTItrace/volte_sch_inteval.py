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

class volte_interval(object):
	"""
	docstring for volte_interval
	"""
	def __init__(self, file_name, crnti):
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


	def filter_by_crnti(self):
		self.check_file()
		try:
			with open(self.file_name, 'rb') as csv_file:
				csv_read = csv.reader(csv_file)
				# get the crnti list's index
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
						self.sfn.append(row_data[sfn_list_index])
						self.esfn.append(row_data[esfn_list_index])

				print self.time
				print self.sfn
				print self.esfn
		except IOError, e:
			raise e


	def check_file(self):
		if self.file_name.upper().find('DL') > -1:
			self.list_index_param = dl_key_value
		elif self.file_name.upper().find('UL') > -1:
			self.list_index_param = ul_key_value
		else:
			raise "file name need contain the key value 'dl' or 'ul'"
		print self.list_index_param		


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