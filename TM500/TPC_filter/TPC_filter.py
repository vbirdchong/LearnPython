#!/usr/bin/env python
# coding = utf-8

import re
import csv

OFF_SET = 2
TTI_SFN_TX_PWR = []
VALUE_TX_PWR = []
DSP_TIME_TX_PWR = []


TTI_SFN_TX_ADJ = []
VALUE_TX_ADJ = []
DSP_TIME_TX_ADJ = []

# log example
# HLCLog_1.txt:   10981.841664866:   LTE DSP   4.3    LOG_UL_CTRL_SLAVE_PUCCH_PWRCTRL_BEGIN(Ue Index: -, HWI: -, Internal ID: 3, Tti: 9857, bIsClpc(0/1/T/F): 1, InitalPwer(MBm): -10000, Clpc Pwr Adjustment(MB): -300)
# HLCLog_1.txt:   10981.841666255:   LTE DSP   4.3    LOG_UL_CTRL_SLAVE_PUCCH_PWRCTRL_END(Ue Index: -, HWI: -, Internal ID: 3, Tti: 9857, Olpc Pucch Pwr (mBm): -9000, Pucch Tx Power (mBm): -9000, PucchAccLimitClamp: ULPC_LIMIT_IN_RANGE_E)

def find_pucch_pwr_adjustment(line, internal_id):
    v = "Internal ID: " + internal_id + ','
    
    if line.find(v) == -1:
        #print 'not found' + v
        return

    if  line.find('Tti') != -1 and line.find('Adjustment(MB)') != -1:
        tti_char = line[line.find('Tti'):]
        
        colon_index = tti_char.find(':')
        number_length = tti_char.find(',') - colon_index - OFF_SET
        #print number_length
        tti_sfn = int(tti_char[colon_index + OFF_SET: colon_index + OFF_SET + number_length])
    
        adjustment_char = line[line.find('Adjustment(MB)'):]
        #print adjustment_char
        colon_index = adjustment_char.find(':')
        number_length = adjustment_char.rfind(')') - colon_index - OFF_SET
        #print number_length
        adjust_value = int(adjustment_char[colon_index + OFF_SET: colon_index + OFF_SET + number_length])
        #print ("adjust:%d" % adjust_value)

        dsp_time_char = '0'
        lte_dsp_char_index = line.find('LTE DSP')
        if lte_dsp_char_index != -1:
            dsp_time_char = line[lte_dsp_char_index - 19: lte_dsp_char_index - 4]

        TTI_SFN_TX_ADJ.append(tti_sfn)
        VALUE_TX_ADJ.append(adjust_value/100)
        DSP_TIME_TX_ADJ.append(dsp_time_char)

        
        
def save_tx_adj_to_file(ue_internal_id):
    try:
        csv_file_name = 'TX_Adjustment_InternalID_' + ue_internal_id + '.csv'
        with open(csv_file_name, 'wb+') as csv_file:
            csv_write = csv.writer(csv_file)
            row_param_info = ['index', 'dsp time', 'sfn', 'Adjustment value']
            csv_write.writerow(row_param_info)
            
            for i in range(len(TTI_SFN_TX_ADJ)):
                data = []
                data.append(i)
                data.append(DSP_TIME_TX_ADJ[i])
                data.append(TTI_SFN_TX_ADJ[i])
                data.append(VALUE_TX_ADJ[i])
                csv_write.writerow(data)
            print("Save " + csv_file_name + " successful...Record number:%d" % len(TTI_SFN_TX_ADJ))
    except Exception, e:
	    raise e
    
def save_tx_pwr_to_file(ue_internal_id):
    try:
        csv_file_name = 'TX_PWR_InternalID_' + ue_internal_id + '.csv' 
        with open(csv_file_name, 'wb+') as csv_file:
            csv_write = csv.writer(csv_file)
            row_param_info = ['index', 'dsp time', 'sfn', 'TX PWR value']
            csv_write.writerow(row_param_info)

            for i in range(len(TTI_SFN_TX_PWR)):
                data = []
                data.append(i)
                data.append(DSP_TIME_TX_PWR[i])
                data.append(TTI_SFN_TX_PWR[i])
                data.append(VALUE_TX_PWR[i])
                csv_write.writerow(data)
            print("Save " + csv_file_name + " successful...Record number:%d" % len(TTI_SFN_TX_PWR))
    except Exception, e:
	    raise e


def is_sfn_same():
    if (len(TTI_SFN_TX_PWR) == len(TTI_SFN_TX_ADJ)) and (TTI_SFN_TX_PWR == TTI_SFN_TX_ADJ):
        return True
    else:
        return False


def save_to_file(ue_internal_id):
    if is_sfn_same():
        print("SFN are same for TPC adjustment and TX power, save to one file...")
        # save to one file
        try:
            csv_file_name = 'Pwr_and_Adjust_Internal_ID_' + ue_internal_id + '.csv'
            with open(csv_file_name, 'wb+') as csv_file:
                csv_write = csv.writer(csv_file)
                row_param_info = ['index', 'dsp time', 'sfn', 'TX PWR value', 'Adjustment value']
                csv_write.writerow(row_param_info)

                for i in xrange(len(TTI_SFN_TX_PWR)):
                    data = []
                    data.append(i)
                    data.append(DSP_TIME_TX_PWR[i]) # we use Pucch TX Power's dsp time to save
                    data.append(TTI_SFN_TX_PWR[i])
                    data.append(VALUE_TX_PWR[i])
                    data.append(VALUE_TX_ADJ[i])
                    csv_write.writerow(data)
                print("Save to " + csv_file_name + ' successful...Record number:%d' % len(TTI_SFN_TX_PWR))
        except Exception, e:
            raise e

    else:
        # save to two files
        print("Some SFN for TPC adjustment and TX power are not match, save to different files...")
        save_tx_adj_to_file(ue_internal_id)
        save_tx_pwr_to_file(ue_internal_id)
	
def find_pucch_tx_power(line, internal_id):
    v = "Internal ID: " + internal_id + ','
    
    if line.find(v) == -1:
        #print 'not found' + v
        return
    
    if  line.find('Tti') != -1 and line.find('Pucch Tx Power (mBm)') != -1:
        tti_char = line[line.find('Tti'):]
        colon_index = tti_char.find(':')
        number_length = tti_char.find(',') - colon_index - OFF_SET
        #print number_length
        tti_sfn = int(tti_char[colon_index + OFF_SET: colon_index + OFF_SET + number_length])
        #print tti_sfn

        tx_power_char = line[line.find('Pucch Tx Power (mBm)'):]
        colon_index = tx_power_char.find(':')
        number_length = tx_power_char.find(',') - colon_index - OFF_SET
        tx_pwr_value = int(tx_power_char[colon_index + OFF_SET: colon_index + OFF_SET + number_length])
        #print tti_sfn, tx_pwr_value

        dsp_time_char = '0'
        lte_dsp_char_index = line.find('LTE DSP')
        if lte_dsp_char_index != -1:
            dsp_time_char = line[lte_dsp_char_index - 19: lte_dsp_char_index - 4]
            

        TTI_SFN_TX_PWR.append(tti_sfn)
        VALUE_TX_PWR.append(tx_pwr_value/100)
        DSP_TIME_TX_PWR.append(dsp_time_char)


def main():
    data = raw_input("Please input the TM500 PTC data file(e.g. HLCLog.txt): ")
    ue_internal_id = raw_input("Please input the UE Internal ID: ")

    if (not (ue_internal_id.isdigit()) or (int(ue_internal_id) > 65535 or int(ue_internal_id) <= 0)):
        print"The input ue ue internal id  is invalid, ID=" + ue_internal_id
    else:
        try:
            with open(data) as data:
                for each_line in data:
                    find_pucch_tx_power(each_line, ue_internal_id)
                    find_pucch_pwr_adjustment(each_line, ue_internal_id)
                save_to_file(ue_internal_id)
        except IOError as err:
            print("Open file error: " + str(err))

if __name__ == '__main__':
	main()

    
