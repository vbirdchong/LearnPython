#!usr/bin/env ptyhon
# coding=utf-8

import csv
from itertools import islice

dl_key_value = {
	'crnti': 'ETtiTraceDlParUe_crnti',
	'time': 'Time',
	'sfn': 'ETtiTraceDlParCell_sfn',
	'esfn': 'ETtiTraceDlParCell_esfn',
	'interval': 'interval',
	'ackNack': 'EHarqParDl_ackNackDtxCw1',
	'tbSize': 'ETtiTraceDlParUe_tbSizeDrb3',
	'qci': 'ETtiTraceDlParUe_qci_DRB3'
}

ul_key_value = {
	'crnti': 'ETtiTraceUlParUe_crnti',
	'time': 'Time',
	'sfn': 'ETtiTraceUlParCell_sfn',
	'esfn': 'ETtiTraceUlParCell_esfn',
	'interval': 'interval'
}


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
		self.list_index_param = {}
		self.ttitrace_key_index = {}
		self.ttitrace_record_data = {}

	def get_ttitrace_key_index(self, param_list):
		self.ttitrace_key_index['time'] = param_list.index(self.list_index_param['time'])
		self.ttitrace_key_index['crnti'] = param_list.index(self.list_index_param['crnti'])
		self.ttitrace_key_index['sfn'] = param_list.index(self.list_index_param['sfn'])
		self.ttitrace_key_index['esfn'] = param_list.index(self.list_index_param['esfn'])
		self.ttitrace_key_index['ackNack'] = param_list.index(self.list_index_param['ackNack'])
		# print self.ttitrace_key_index

	def get_data_by_crnti(self, row_data):
		if (row_data[self.ttitrace_key_index['crnti']].isdigit() and self.crnti == int(row_data[self.ttitrace_key_index['crnti']])):
			self.ttitrace_record_data['crnti'].append(row_data[self.ttitrace_key_index['crnti']])
			self.ttitrace_record_data['time'].append(row_data[self.ttitrace_key_index['time']])
			self.ttitrace_record_data['sfn'].append(row_data[self.ttitrace_key_index['sfn']])
			self.ttitrace_record_data['esfn'].append(row_data[self.ttitrace_key_index['esfn']])
			self.ttitrace_record_data['ackNack'].append(row_data[self.ttitrace_key_index['ackNack']])


	def filter_by_crnti(self):
		self.check_file()
		try:
			with open(self.file_name, 'rb') as csv_file:
				csv_read = csv.reader(csv_file)
				for row in islice(csv_read, 1, 2):
					self.get_ttitrace_key_index(row)

				for row_data in csv_read:
					self.get_data_by_crnti(row_data)
			# print self.ttitrace_record_data
		except IOError, e:
			raise e
		self.save_to_file()

	def save_to_file(self):
		try:
			with open('volte_interval_crnti_'+str(self.crnti)+'.csv', 'wb+') as csv_file:
				csv_write = csv.writer(csv_file)
				
				# write the list param info
				row_param_name = [self.list_index_param['crnti'],
									self.list_index_param['time'],
									self.list_index_param['sfn'],
									self.list_index_param['esfn'],
									self.list_index_param['interval'],
									self.list_index_param['ackNack']]
				
				csv_write.writerow(row_param_name)
				print row_param_name
				# write the data info 
				for row_line in range(len(self.ttitrace_record_data['crnti'])):
					row_data = [self.ttitrace_record_data['crnti'][row_line],
								self.ttitrace_record_data['time'][row_line],
								self.ttitrace_record_data['sfn'][row_line],
								self.ttitrace_record_data['esfn'][row_line]]
					# calculate the diff for sfn
					sfn_diff = 65535
					if row_line == 0:
						sfn_diff = 65535
					elif row_line <= len(self.ttitrace_record_data['crnti']) and row_line > 0:
						sfn_diff = (int(self.ttitrace_record_data['sfn'][row_line]) * 10 + int(self.ttitrace_record_data['esfn'][row_line])) - \
									(int(self.ttitrace_record_data['sfn'][row_line-1]) * 10 + int(self.ttitrace_record_data['esfn'][row_line-1]))
					row_data.append(sfn_diff)

					row_data.append(self.ttitrace_record_data['ackNack'][row_line])
					csv_write.writerow(row_data)	
		except Exception, e:
			raise e

	def init_param(self, key_value={}):
		self.list_index_param = key_value
		for key in key_value.keys():
			self.ttitrace_record_data[key] = []


	def check_file(self):
		if self.file_name.upper().find('DL') > -1:
			self.init_param(dl_key_value)
		elif self.file_name.upper().find('UL') > -1:
			self.init_param(ul_key_value)
		else:
			raise "file name need contain the key value 'dl' or 'ul'"


def main():
	# input_crnti = raw_input("Please enter the crnti: ")

	input_crnti = '5631'
	if (not (input_crnti.isdigit()) or (int(input_crnti) > 65535 or int(input_crnti) <= 0)):
		print"The input value is invalid, crnti=" + input_crnti
	else:
		# test_file = 'ttiTrace_20160314141705_1232_dl_0013_ffff.csv'
		test_file = 'ttiTrace_20160314141705_1232_dl_0013.csv'
		test = volte_interval(test_file, int(input_crnti))
		test.filter_by_crnti()
		# filter_by_crnti(int(input_crnti))


if __name__ == '__main__':
	main()