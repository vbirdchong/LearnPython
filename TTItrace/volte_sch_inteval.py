#!usr/bin/env ptyhon
# coding=utf-8

import csv
import sys
from itertools import islice

UL = 1
DL = 2

dl_key_value = {
	'crnti': 'ETtiTraceDlParUe_crnti',
	'time': 'Time',
	'sfn': 'ETtiTraceDlParCell_sfn',
	'esfn': 'ETtiTraceDlParCell_esfn',
	'interval': 'interval',
	'trNum': 'ETtiTraceDlParUe_trNumCW1',
	'ackNack': 'EHarqParDl_ackNackDtxCw1',
	'tbSize': 'ETtiTraceDlParUe_tbSizeDrb3',
	'qci': 'ETtiTraceDlParUe_qci_DRB3'
}

ul_key_value = {
	'crnti': 'ETtiTraceUlParUe_crnti',
	'time': 'Time',
	'sfn': 'ETtiTraceUlParCell_sfn',
	'esfn': 'ETtiTraceUlParCell_esfn',
	'interval': 'interval',
	'trNum': 'ETtiTraceUlParUe_trNumCw1',
	'ackNack': 'EHarqParUl_ackNackDtxCw1',
	'fdNum': 'ETtiTraceUlParCell_numUesFd',
	'lcg1Status': 'ETtiTraceUlParUe_Lcg1Status',
	'lcg2Status': 'ETtiTraceUlParUe_Lcg2Status',
	'lcg3Status': 'ETtiTraceUlParUe_Lcg3Status',
	'bitsInLcg1': 'ETtiTraceUlParUe_bitsInLcg1',
	'bitsInLcg2': 'ETtiTraceUlParUe_bitsInLcg2',
	'bitsInLcg3': 'ETtiTraceUlParUe_bitsInLcg3',
	'brsReport': 'ETtiTraceUlParUe_bsrReported',
	'requiredTbsSrbGbr': 'ETtiTraceUlParUe_rrmRequiredTbsSrbGbr'
}


class volte_interval(object):

	"""
	docstring for volte_interval
	"""
	def __init__(self, file_name, crnti=0):
		'''
		param: crnti must be integer
		'''
		super(volte_interval, self).__init__()
		self.crnti = crnti
		self.file_name = file_name
		self.ul_or_dl = 0	# ul=1, dl=2, default=0
		self.list_index_param = {}
		self.ttitrace_key_index = {}
		self.ttitrace_record_data = {}
		self.qci1_lcg_channel = 0

	def get_ttitrace_key_index(self, param_list):
		self.ttitrace_key_index['time'] = param_list.index(self.list_index_param['time'])
		self.ttitrace_key_index['crnti'] = param_list.index(self.list_index_param['crnti'])
		self.ttitrace_key_index['sfn'] = param_list.index(self.list_index_param['sfn'])
		self.ttitrace_key_index['esfn'] = param_list.index(self.list_index_param['esfn'])
		self.ttitrace_key_index['trNum'] = param_list.index(self.list_index_param['trNum'])
		self.ttitrace_key_index['ackNack'] = param_list.index(self.list_index_param['ackNack'])

		if (self.ul_or_dl == DL):
			self.ttitrace_key_index['tbSize'] = param_list.index(self.list_index_param['tbSize'])
			self.ttitrace_key_index['qci'] = param_list.index(self.list_index_param['qci'])
		elif (self.ul_or_dl == UL):
			self.ttitrace_key_index['fdNum'] = param_list.index(self.list_index_param['fdNum'])
			self.ttitrace_key_index['lcg1Status'] = param_list.index(self.list_index_param['lcg1Status'])
			self.ttitrace_key_index['lcg2Status'] = param_list.index(self.list_index_param['lcg2Status'])
			self.ttitrace_key_index['lcg3Status'] = param_list.index(self.list_index_param['lcg3Status'])
			self.ttitrace_key_index['bitsInLcg1'] = param_list.index(self.list_index_param['bitsInLcg1'])
			self.ttitrace_key_index['bitsInLcg2'] = param_list.index(self.list_index_param['bitsInLcg2'])
			self.ttitrace_key_index['bitsInLcg3'] = param_list.index(self.list_index_param['bitsInLcg3'])
			self.ttitrace_key_index['brsReport'] = param_list.index(self.list_index_param['brsReport'])
			self.ttitrace_key_index['requiredTbsSrbGbr'] = param_list.index(self.list_index_param['requiredTbsSrbGbr'])
		# print self.ttitrace_key_index

	def get_qci1_lcg_channel(self, row_data):
		'''
		Logical channel group 1 status bit map
		bit 0: Is only have Gbr bear 
		bit 1: Is only have Qci1 bear
		bit 2: Has Qci1 bear or not
		bit 3: Has Qci234 bear or not
		bit 4: Has NoGbr bear or not
		bit 5: Is Deprioritized
		'''
		qci1_lcg_channel = 0
		lcg_status = []
		lcg_status.append(row_data[self.ttitrace_key_index['lcg1Status']])
		lcg_status.append(row_data[self.ttitrace_key_index['lcg2Status']])
		lcg_status.append(row_data[self.ttitrace_key_index['lcg3Status']])
		
		for qci1_lcg_channel in range(0, 3):
			if ((len(lcg_status[qci1_lcg_channel]) == 6 and ((int(lcg_status[qci1_lcg_channel])/100)%1000 == 1))
				or ((len(lcg_status[qci1_lcg_channel]) == 5) and ((int(lcg_status[qci1_lcg_channel])/100)%100 == 1))
				or ((len(lcg_status[qci1_lcg_channel]) == 4) and ((int(lcg_status[qci1_lcg_channel])/100)%10 == 1))
				or ((len(lcg_status[qci1_lcg_channel]) == 3) and ((int(lcg_status[qci1_lcg_channel])/100) == 1))
				):
				# logic channel from 1 to 3
				qci1_lcg_channel += 1
				break
		self.qci1_lcg_channel = qci1_lcg_channel
		return qci1_lcg_channel

	def get_qic1_lcg_bits(self, row_data):
		self.get_qci1_lcg_channel(row_data)
		if(self.qci1_lcg_channel == 0):
			return False

		ret, bitsInLcgX = self.get_qci1_lcg_str()
		if (ret):
			self.ttitrace_record_data[bitsInLcgX].append(row_data[self.ttitrace_key_index[bitsInLcgX]])

	def get_qci1_lcg_str(self):
		bitsInLcgX = ''
		if self.qci1_lcg_channel == 1:
			bitsInLcgX = 'bitsInLcg1'
		elif qci1_lcg_channel == 2:
			bitsInLcgX = 'bitsInLcg2'
		elif qci1_lcg_channel == 3:
			bitsInLcgX = 'bitsInLcg3'
		else:
			return False

		return True, bitsInLcgX

	def get_data_by_crnti(self, row_data):
		if (len(row_data) > self.ttitrace_key_index['crnti'] and row_data[self.ttitrace_key_index['crnti']].isdigit() and self.crnti == int(row_data[self.ttitrace_key_index['crnti']])):
			self.ttitrace_record_data['crnti'].append(row_data[self.ttitrace_key_index['crnti']])
			self.ttitrace_record_data['time'].append(row_data[self.ttitrace_key_index['time']])
			self.ttitrace_record_data['sfn'].append(row_data[self.ttitrace_key_index['sfn']])
			self.ttitrace_record_data['esfn'].append(row_data[self.ttitrace_key_index['esfn']])
			self.ttitrace_record_data['trNum'].append(row_data[self.ttitrace_key_index['trNum']])
			self.ttitrace_record_data['ackNack'].append(row_data[self.ttitrace_key_index['ackNack']])
			
			if (self.ul_or_dl == DL):
				self.ttitrace_record_data['tbSize'].append(row_data[self.ttitrace_key_index['tbSize']])
				self.ttitrace_record_data['qci'].append(row_data[self.ttitrace_key_index['qci']])
			elif (self.ul_or_dl == UL):
				self.ttitrace_record_data['fdNum'].append(row_data[self.ttitrace_key_index['fdNum']])
				self.ttitrace_record_data['brsReport'].append(row_data[self.ttitrace_key_index['brsReport']])
				self.ttitrace_record_data['requiredTbsSrbGbr'].append(row_data[self.ttitrace_key_index['requiredTbsSrbGbr']])
				self.get_qic1_lcg_bits(row_data)
		# print self.ttitrace_record_data

	def filter_by_crnti(self):
		self.check_file()
		try:
			with open(self.file_name, 'rb') as csv_file:
				csv_read = csv.reader(csv_file)
				for row in islice(csv_read, 1, 2):
					self.get_ttitrace_key_index(row)

				for row_data in csv_read:
					self.get_data_by_crnti(row_data)
		except IOError, e:
			raise e
		self.save_to_file()

	def write_row_param_name(self):
		list_param = [self.list_index_param['crnti'],
						self.list_index_param['time'],
						self.list_index_param['sfn'],
						self.list_index_param['esfn'],
						self.list_index_param['interval'],
						self.list_index_param['trNum'],
						self.list_index_param['ackNack']]
				
		if (self.ul_or_dl == DL):
			list_param.append(self.list_index_param['tbSize'])
			list_param.append(self.list_index_param['qci'])
		elif (self.ul_or_dl == UL):
			list_param.append(self.list_index_param['fdNum'])
			list_param.append(self.list_index_param['brsReport'])
			list_param.append(self.list_index_param['requiredTbsSrbGbr'])
			ret, bitsInLcgX = self.get_qci1_lcg_str()
			if (ret):
				list_param.append(self.list_index_param[bitsInLcgX])

		return list_param

	def write_row_data(self, row_line):
		row_data = [self.ttitrace_record_data['crnti'][row_line],
					self.ttitrace_record_data['time'][row_line],
					self.ttitrace_record_data['sfn'][row_line],
					self.ttitrace_record_data['esfn'][row_line]]
					
		# calculate the diff for sfn
		sfn_diff = 0
		if row_line == 0:
			sfn_diff = 0
		elif row_line <= len(self.ttitrace_record_data['crnti']) and row_line > 0:
			sfn_diff = (int(self.ttitrace_record_data['sfn'][row_line]) * 10 + int(self.ttitrace_record_data['esfn'][row_line])) - \
						(int(self.ttitrace_record_data['sfn'][row_line-1]) * 10 + int(self.ttitrace_record_data['esfn'][row_line-1]))
			if sfn_diff < 0:
				sfn_diff += 10240
		sfn_diff *= 10
		row_data.append(sfn_diff)

		row_data.append(self.ttitrace_record_data['trNum'][row_line])
		row_data.append(self.ttitrace_record_data['ackNack'][row_line])

		if (self.ul_or_dl == DL):
			row_data.append(self.ttitrace_record_data['tbSize'][row_line])
			row_data.append(self.ttitrace_record_data['qci'][row_line])
		elif (self.ul_or_dl == UL):
			row_data.append(self.ttitrace_record_data['fdNum'][row_line])
			row_data.append(self.ttitrace_record_data['brsReport'][row_line])
			row_data.append(self.ttitrace_record_data['requiredTbsSrbGbr'][row_line])
			ret, bitsInLcgX = self.get_qci1_lcg_str()
			if (ret):
				row_data.append(self.ttitrace_record_data[bitsInLcgX][row_line])
		return row_data

	def save_to_file(self):
		try:
			with open(self.file_name+'_crnti_'+str(self.crnti)+'.csv', 'wb+') as csv_file:
				csv_write = csv.writer(csv_file)
				# write the list param info
				row_param_name = self.write_row_param_name()
				csv_write.writerow(row_param_name)

				print row_param_name
				# write the data info 
				for row_line in range(len(self.ttitrace_record_data['crnti'])):
					row_data = self.write_row_data(row_line)
					csv_write.writerow(row_data)
					
		except Exception, e:
			raise e

	def init_param(self, key_value={}):
		self.list_index_param = key_value
		for key in key_value.keys():
			self.ttitrace_record_data[key] = []


	def check_file(self):
		if self.file_name.upper().find('DL') > -1:
			self.ul_or_dl = DL
			self.init_param(dl_key_value)
		elif self.file_name.upper().find('UL') > -1:
			self.ul_or_dl = UL
			self.init_param(ul_key_value)
		else:
			raise "file name need contain the key value 'dl' or 'ul'"


def main():

	test_file = raw_input("Please enter the UL or DL csv file:\n")
	input_crnti = raw_input("Please enter the crnti:\n")
	# for i in range(1, len(sys.argv)):
	# 	print 'arg:%d' % i, sys.argv[i]

	# test_file = sys.argv[1]
	# input_crnti = sys.argv[2]

	# test_file = 'ttiTrace_20160328104952_1233_ul_0008.csv'
	# input_crnti = '15416'

	if (not (input_crnti.isdigit()) or (int(input_crnti) > 65535 or int(input_crnti) <= 0)):
		print"The input value is invalid, crnti=" + input_crnti
	else:
		test = volte_interval(test_file, int(input_crnti))
		test.filter_by_crnti()


if __name__ == '__main__':
	main()
	raw_input('Enter enter key to exit...')