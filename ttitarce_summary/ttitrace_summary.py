#!/usr/bin/env python
# coding = utf-8

import sys
import os
import csv
import time
from itertools import islice


UL_KEY_VALUE ={
    'time' : 'Time',
    'crnti' : 'ETtiTraceUlParUe_crnti',
    'ueIndex' : 'ETtiTraceUlParUe_ueIndex',
    'cw1_acknack': 'EHarqParUl_ackNackDtxCw1',
    'rssi_pusch': 'ETtiTraceUlParUe_rssiPusch',
    'sinr_pusch': 'ETtiTraceUlParUe_sinrPusch'
}

DL_KEY_VALUE ={
    'time': 'Time',
    'crnti': 'ETtiTraceDlParUe_crnti',
    'ueIndex' : 'ETtiTraceDlParUe_ueIndex',
    'cw1_acknack': 'EHarqParDl_ackNackDtxCw1',
    'cw0_wbcqi': 'ETtiTraceDlParUe_wbCqiCw0'
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
    'ueIndex': 'ueIndex',
    'cw1_ack': 'CW1_ACK',
    'cw1_nack': 'CW1_NACK',
    'cw1_nack_ratio': 'CW1_NACK_Ratio',
    'cw1_dtx': 'CW1_DTX',
    'cw1_dtx_ratio': 'CW1_DTX_Ratio',
    'rssi_pusch': 'rssi_pusch',
    'sinr_pusch': 'sinr_pusch',
    'cw0_wbcqi': 'cw0_wbcqi'
}


class CTtiSummary(object):
    def __init__(self):
        super(CTtiSummary, self).__init__()
        self.link_type = LINK_TYPE_UNKNOW
        self.ue_info_list = []
        self.ue_list = []
        self.file_list = []

    def clean_ue_info(self):
        self.ue_list = []
        self.ue_info_list = []
        self.link_type = LINK_TYPE_UNKNOW

    def open_csv_file(self):
        pro_start_time = time.clock()
        file_name_list = os.listdir(os.getcwd())
        for file in file_name_list:
            if(file.find('csv') != -1):
                self.read_file(file)
                self.clean_ue_info()

        self.save_to_summary_file()
        pro_end_time = time.clock()
        print("Time spend: %d" % (pro_end_time - pro_start_time))
        
    def summary_key_info(self):
        return [SUMMARY_KEY['file_name'],
                SUMMARY_KEY['enb_tag'],
                SUMMARY_KEY['ul_dl'],
                SUMMARY_KEY['start_time'],
                SUMMARY_KEY['end_time'],
                SUMMARY_KEY['crnti'],
                SUMMARY_KEY['ueIndex'],
                SUMMARY_KEY['cw1_ack'],
                SUMMARY_KEY['cw1_nack'],
                SUMMARY_KEY['cw1_nack_ratio'],
                SUMMARY_KEY['cw1_dtx'],
                SUMMARY_KEY['cw1_dtx_ratio'],
                SUMMARY_KEY['rssi_pusch'],
                SUMMARY_KEY['sinr_pusch'],
                SUMMARY_KEY['cw0_wbcqi']]

    def summary_ue_info_data(self, ue_info):
        rssi_val = '-'
        rssi_num_record = len(ue_info['rssi_pusch']) - 1
        if rssi_num_record > 0:
            rssi_val = sum(ue_info['rssi_pusch']) / rssi_num_record

        sinr_val = '-'
        sinr_num_record = len(ue_info['sinr_pusch']) - 1
        if sinr_num_record > 0:
            sinr_val = sum(ue_info['sinr_pusch']) / sinr_num_record
        
        cw0_wbcqi_val = '-'
        cw0_wbcqi_record = len(ue_info['cw0_wbcqi']) - 1
        if cw0_wbcqi_record > 0:
            cw0_wbcqi_val = sum(ue_info['cw0_wbcqi']) / cw0_wbcqi_record
            # print(ue_info['crnti'], sum(ue_info['cw0_wbcqi']), cw0_wbcqi_record)

        # calculate the percent ratio for NACK/DTX
        ack_nack_sum_value =  ue_info['cw1_ack'] + ue_info['cw1_nack'] + ue_info['cw1_dtx']
        cw1_nack_ratio = (ue_info['cw1_nack'] * 100.0 / ack_nack_sum_value) if ack_nack_sum_value != 0 else 0
        cw1_dtx_ratio = (ue_info['cw1_dtx'] * 100.0 / ack_nack_sum_value) if ack_nack_sum_value != 0 else 0
        # print("crnti:{0}, ack:{1}, nack:{2}, dtx:{3}, sum:{4}, nack_ratio:{5}".format(ue_info['crnti'], 
        #                         ue_info['cw1_ack'], ue_info['cw1_nack'], ue_info['cw1_dtx'], ack_nack_sum_value, round(cw1_nack_ratio,3)))


        ret = [ue_info['file_name'],
                ue_info['enb_tag'],
                ue_info['ul_dl'],
                ue_info['start_time'],
                ue_info['end_time'],
                ue_info['crnti'],
                ue_info['ueIndex'],
                ue_info['cw1_ack'],
                ue_info['cw1_nack'],
                round(cw1_nack_ratio, 3),
                ue_info['cw1_dtx'],
                round(cw1_dtx_ratio, 3),
                rssi_val,
                sinr_val,
                cw0_wbcqi_val]  # we need to reduce 1, because the ue_info['rssi_pusch'][0] = 0.0
        return ret

    def save_to_summary_file(self):
        try:
            with open('ue_summary'+'.csv', 'wb+') as csv_file:
                csv_write = csv.writer(csv_file)
                # write the list param info
                row_param_name = self.summary_key_info()
                csv_write.writerow(row_param_name)
                print row_param_name

                # write the data info 
                for file in self.file_list:
                    for ue_info in file:
                        row_data = self.summary_ue_info_data(ue_info)
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
        key_info_index['ueIndex'] = key_info.index(KEY_VALUE[self.link_type]['ueIndex'])
        key_info_index['cw1_acknack'] = key_info.index(KEY_VALUE[self.link_type]['cw1_acknack'])
        
        if self.link_type == LINK_TYPE_UL:
            key_info_index['rssi_pusch'] = key_info.index(KEY_VALUE[self.link_type]['rssi_pusch'])
            key_info_index['sinr_pusch'] = key_info.index(KEY_VALUE[self.link_type]['sinr_pusch'])

        if self.link_type == LINK_TYPE_DL:
            key_info_index['cw0_wbcqi'] = key_info.index(KEY_VALUE[self.link_type]['cw0_wbcqi'])

        return key_info_index

    def get_ack_nack(self, ack_nack_dtx):
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
        return ack, nack, dtx
        

    def get_row_data(self, row_data, key_info_index, curren_file_info, file_name):
        time = row_data[key_info_index['time']]
        crnti = row_data[key_info_index['crnti']]
        ueIndex = row_data[key_info_index['ueIndex']]
        ack,nack,dtx = self.get_ack_nack(row_data[key_info_index['cw1_acknack']])
        
        g = lambda x: 0.0 if x == '-' else eval(x)
        rssi_pusch = []
        sinr_pusch = []
        if self.link_type == LINK_TYPE_UL:
            rssi_pusch.append(g(row_data[key_info_index['rssi_pusch']]))
            sinr_pusch.append(g(row_data[key_info_index['sinr_pusch']]))

        cw0_wbcqi = []
        if self.link_type == LINK_TYPE_DL:
            cw0_wbcqi.append(g(row_data[key_info_index['cw0_wbcqi']]))

        # we need to check the crnti is digit, else skip the '-' symble
        if crnti.isdigit():
            ue_info = {
                'crnti': int(crnti),
                'ueIndex': ueIndex,
                'start_time': time,
                'end_time': time,
                'cw1_ack': ack,
                'cw1_nack': nack,
                'cw1_dtx': dtx,
                'file_name': file_name,
                'ul_dl': curren_file_info['ul_dl'],
                'enb_tag': curren_file_info['enb_tag'],
                'rssi_pusch': rssi_pusch,
                'sinr_pusch': sinr_pusch,
                'cw0_wbcqi': cw0_wbcqi
            }
            self.record_ue_info(ue_info)


    def record_ue_info(self, ue_info):
        # just only update the 'end_time/ack,nack,dtx counter' info
        if self.ue_list.count(ue_info['crnti']) != 0:
            self.ue_info_list[self.ue_list.index(ue_info['crnti'])]['end_time'] = ue_info['end_time']
            self.ue_info_list[self.ue_list.index(ue_info['crnti'])]['cw1_ack'] += ue_info['cw1_ack']
            self.ue_info_list[self.ue_list.index(ue_info['crnti'])]['cw1_nack'] += ue_info['cw1_nack']
            self.ue_info_list[self.ue_list.index(ue_info['crnti'])]['cw1_dtx'] += ue_info['cw1_dtx']
            # print('rssi_pusch: %f' % ue_info['rssi_pusch'][0])
            if len(ue_info['rssi_pusch']) != 0 and ue_info['rssi_pusch'][0] != 0.0:
                self.ue_info_list[self.ue_list.index(ue_info['crnti'])]['rssi_pusch'].append(ue_info['rssi_pusch'][0])
            if len(ue_info['sinr_pusch']) != 0 and ue_info['sinr_pusch'][0] != 0.0:
                self.ue_info_list[self.ue_list.index(ue_info['crnti'])]['sinr_pusch'].append(ue_info['sinr_pusch'][0])
            if len(ue_info['cw0_wbcqi']) != 0 and ue_info['cw0_wbcqi'][0] != 0.0:
                self.ue_info_list[self.ue_list.index(ue_info['crnti'])]['cw0_wbcqi'].append(ue_info['cw0_wbcqi'][0])
        else:
            # 'ue_list' and 'ue_info_list' have the same index for one ue's crnti
            self.ue_list.append(ue_info['crnti'])
            self.ue_info_list.append(ue_info)

    def read_file(self, file_name):
        try:
            with open(file_name, 'rb') as csv_file:
                csv_read = csv.reader(csv_file)
                curren_file_info = {}
                curren_file_useful = False
                
                for info in islice(csv_read, 0, 1):
                    curren_file_useful, curren_file_info = self.get_file_base_info(info)

                if curren_file_useful:
                    print (file_name, curren_file_useful, curren_file_info)
                    key_info_index = {}
                    for key_info in islice(csv_read, 0, 1):
                        key_info_index = self.get_key_info_index(key_info)

                    for row_data in csv_read:
                        self.get_row_data(row_data, key_info_index, curren_file_info, file_name)

                    # save all ue's info into one file list, 'file_list[i]' contant all ue in the file
                    self.file_list.append(self.ue_info_list)
                else:
                    return

        except IOError, e:
            raise e

def main():
    test = CTtiSummary()
    test.open_csv_file()


if __name__ == '__main__':
    main()
