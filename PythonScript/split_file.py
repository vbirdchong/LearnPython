#! python3

import os
import sys
import time

# DONE: 1. file name should split correctly xx.csc.txt.a.log 
# DONE: 2. the input file is include a path, so we need get the right file name D:\LearnPython\SYSLOG.LOG
# DONE: 3. change to path then create the file
# DONE: 4. if we read file as size, we will meet the last line would not complete issue

# 1024 * 1024 Byte = 1MB
SPLITE_UNIT = 1048576
USAGE_INFO = '''
Usage: python splite_file.py src_file_path split_size
 src_file_path: file path
 split_size: the unit of size if 1MB
 e.g.: python splite_file.py D:\\LOG\\SYSLOG.LOG 50'''


def get_path_and_file(path_info):
    path = os.path.dirname(path_info)
    file_name = os.path.basename(path_info)
    print("Path:" + os.path.dirname(path_info))
    print("File:" + os.path.basename(path_info))
    return path, file_name

def get_file_pre_post_fix(file_name):
    info = os.path.splitext(file_name)
    file_prefix = info[0]
    file_postfix = info[1]
    return file_prefix, file_postfix

def write_to_new_file(new_file_name, data):
    with open(new_file_name, 'w') as output_file:
        output_file.writelines(data)

def split_log_by_size(path_info, split_size):
    path, file_name = get_path_and_file(path_info)
    file_prefix, file_postfix = get_file_pre_post_fix(file_name)
    os.chdir(path)

    with open(file_name, 'r') as input_file:
        split_file_index = 0
        while True:
            data = input_file.readlines(split_size * SPLITE_UNIT)
            if not data:
                break
            new_file_name = file_prefix + "_" + str(split_file_index) + file_postfix
            split_file_index += 1
            print("Creating file: " + new_file_name + "...")
            write_to_new_file(new_file_name, data)

def main():
    print(sys.argv)
    if len(sys.argv) != 3:
        print(USAGE_INFO)
    else:
        path = sys.argv[1]
        size = int(sys.argv[2])
        time_start = time.clock()
        split_log_by_size(path, size)
        time_end = time.clock()
        print("Split done, time spent: " + str(time_end - time_start) )

if __name__ == '__main__':
    main()