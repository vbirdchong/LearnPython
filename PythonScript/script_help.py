#! python3

import os

USAGE_INFO = '''
Usage: python script_help.py'''

SCRIPT_PATH = r'D:\LearnPython\PythonScript'
QUOTATION_MARK = "\'\'\'"

def read_usage_info(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
        info_index = data.find("USAGE_INFO")
        if (info_index > 0):
            first_quotation_idx = data.find(QUOTATION_MARK, info_index)
            second_quotation_idx = data.find(QUOTATION_MARK, first_quotation_idx + len(QUOTATION_MARK))
        return data[first_quotation_idx + len(QUOTATION_MARK) : second_quotation_idx]
            
def main():
    os.chdir(SCRIPT_PATH)
    filenames = os.listdir(SCRIPT_PATH)
    name_list = [file_ for file_ in filenames if file_.endswith('.py')]
    for name_ in name_list:
        print('-'*80)
        print(name_ + read_usage_info(name_) + '\n')
        
if __name__ == '__main__':
    main()
