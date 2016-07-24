#!/usr/bin/env python
# coding = utf-8

import sys
import os
import csv
from itertools import islice

UL_KEY_VALUE ={
    'time' : 'Time',
    'crnti' : 'ETtiTraceUlParUe_crnti',
    'cw1_acknack': 'EHarqParUl_ackNackDtxCw1'
}

DL_KEY_VALUE ={
    'time': 'Time',
    'crnti': 'ETtiTraceDlParUe_crnti',
    'cw_acknack': 'EHarqParDl_ackNackDtxCw1'
}

KEY_VALUE = [
    UL_KEY_VALUE,
    DL_KEY_VALUE
]

LINK_TYPE_UNKNOW = -1
LINK_TYPE_UL = 0
LINK_TYPE_DL = 1

SUMMARY_KEY = {
    'file_name': 'log file',
    'enb_tag': 'ENB',
    'ul_dl': 'UL/DL',
    'start_time': 'Time(start)',
    'end_time': 'Time(end)',
    'crnti': 'CRNTI',
    'cw1_ack': 'CW1_ACK',
    'cw1_nack': 'CW1_NACK',
    'cw1_dtx': 'CW1_DTX'
}


TEST_FILE = 'ttiTrace_20160715144234_1233_ul_0002.csv'



class CTtiSummary(object):
    def __init__(self):
        super(CTtiSummary, self).__init__()
        self.link_type = LINK_TYPE_UNKNOW
        self.ue_info_list = []
        self.ue_list = []

    def open_csv_file(self):
        file_list = os.listdir(os.getcwd())
        for file in file_list:
            if(file.find('csv')):
                # print file
                if file == TEST_FILE:
                    self.read_file(file)

        self.save_to_summary_file()
        

    def save_to_summary_file(self):
        try:
            with open('ue_summary'+'.csv', 'wb+') as csv_file:
                csv_write = csv.writer(csv_file)
                # write the list param info
                row_param_name = [SUMMARY_KEY['file_name'],
                                    SUMMARY_KEY['enb_tag'],
                                    SUMMARY_KEY['ul_dl'],
                                    SUMMARY_KEY['start_time'],
                                    SUMMARY_KEY['end_time'],
                                    SUMMARY_KEY['crnti'],
                                    SUMMARY_KEY['cw1_ack'],
                                    SUMMARY_KEY['cw1_nack'],
                                    SUMMARY_KEY['cw1_dtx']]
                csv_write.writerow(row_param_name)

                print row_param_name
                # write the data info 
                for ue_info in self.ue_info_list:
                    row_data = [ue_info['file_name'],
                                ue_info['enb_tag'],
                                ue_info['ul_dl'],
                                ue_info['start_time'],
                                ue_info['end_time'],
                                ue_info['crnti'],
                                ue_info['cw1_ack'],
                                ue_info['cw1_nack'],
                                ue_info['cw1_dtx']]
                    csv_write.writerow(row_data)
                    
        except Exception, e:
            raise e

    def get_file_base_info(self, info):
        '''
         find the enb version and UL/DL link
        '''
        # print info
        file_info = {'ul_dl': 'unknow', 'enb_tag': '0000'}
        file_useful = False
        if len(info) == 6:
            if info[4].upper().find('UL') != -1:
                file_info['ul_dl'] = 'UL'
                self.link_type = LINK_TYPE_UL
                file_useful = True
            elif info[4].upper().find('DL') != -1:
                file_info['ul_dl'] = 'DL'
                self.link_type = LINK_TYPE_DL
                file_useful = True
            else:
                file_info['ul_dl'] = 'unknow'
                self.link_type = LINK_TYPE_UNKNOW
                file_useful = False

            file_info['enb_tag'] = info[5]
        return file_useful, file_info


    def get_key_info_index(self, key_info):
        key_info_index = {}
        key_info_index['time'] = key_info.index(KEY_VALUE[self.link_type]['time'])
        key_info_index['crnti'] = key_info.index(KEY_VALUE[self.link_type]['crnti'])
        key_info_index['cw1_acknack'] = key_info.index(KEY_VALUE[self.link_type]['cw1_acknack'])
        return key_info_index

    def get_row_data(self, row_data, key_info_index, curren_file_info, file_name):
        time = row_data[key_info_index['time']]
        crnti = row_data[key_info_index['crnti']]
        ack_nack_dtx = row_data[key_info_index['cw1_acknack']]

        ack = 0
        nack = 0
        dtx = 0
        if ack_nack_dtx == 'ACK':
            ack = 1
        elif ack_nack_dtx == 'NACK':
            nack = 1
        elif ack_nack_dtx == 'DTX':
            dtx = 1
        else:
            pass
            # print ('other info in "ackNackDtxCw1" = %s' % ack_nack_dtx)
        # print crnti, type(crnti)
        # print row_data

        # we need to skip the '-' symble
        if crnti.isdigit():
            ue_info = {
                'crnti': crnti,
                'start_time': time,
                'end_time': time,
                'cw1_ack': ack,
                'cw1_nack': nack,
                'cw1_dtx': dtx,
                'file_name': file_name,
                'ul_dl': curren_file_info['ul_dl'],
                'enb_tag': curren_file_info['enb_tag']
            }
            self.record_ue_info(ue_info)


    def record_ue_info(self, ue_info):
        # just only update the 'end_time/ack,nack,dtx counter' info
        if self.ue_list.count(int(ue_info['crnti'])) != 0:
            self.ue_info_list[self.ue_list.index(int(ue_info['crnti']))]['end_time'] = ue_info['end_time']
            self.ue_info_list[self.ue_list.index(int(ue_info['crnti']))]['cw1_ack'] += ue_info['cw1_ack']
            self.ue_info_list[self.ue_list.index(int(ue_info['crnti']))]['cw1_nack'] += ue_info['cw1_nack']
            self.ue_info_list[self.ue_list.index(int(ue_info['crnti']))]['cw1_dtx'] += ue_info['cw1_dtx']
        else:
            # 'ue_list' and 'ue_info_list' have the same index for one ue's crnti
            self.ue_list.append(int(ue_info['crnti']))
            self.ue_info_list.append(ue_info)

    def read_file(self, file_name):
        try:
            with open(file_name, 'rb') as csv_file:
                csv_read = csv.reader(csv_file)
                curren_file_info = {}
                curren_file_useful = False
                key_info_index = {}
                
                for info in islice(csv_read, 0, 1):
                    curren_file_useful, curren_file_info = self.get_file_base_info(info)
                # print curren_file_useful, curren_file_info

                if curren_file_useful:
                    print curren_file_useful, curren_file_info
                    for key_info in islice(csv_read, 0, 1):
                        key_info_index = self.get_key_info_index(key_info)

                    for row_data in csv_read:
                        self.get_row_data(row_data, key_info_index, curren_file_info, file_name)

                # print self.ue_info_list, len(self.ue_info_list)
                # print self.ue_list, len(self.ue_list)

        except IOError, e:
            raise e

def main():
    test = CTtiSummary()
    test.open_csv_file()


if __name__ == '__main__':
    main()