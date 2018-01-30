#! python3

import os
import sys

# DONE: 1. file name should split correctly xx.csc.txt.a.log 
# DONE: 2. the input file is include a path, so we need get the right file name D:\LearnPython\SYSLOG.LOG
# DONE: 3. change to path then create the file
# TODO: 4. if we read file as size, we will meet the last line would not complete issue

# 1024 * 1024 Byte = 1MB
SPLITE_UNIT = 1048576
USAGE = '''
Usage: python splite_file.py src_file_path split_size
 src_file_path: file path
 split_size: the unit of size if 1MB
 e.g. python splite_file.py D:\\LOG\\SYSLOG.LOG 50'''


def get_path_and_file(path_info):
    detail = path_info.split('\\')
    file_name = detail[-1]
    path = ('\\').join(detail[0:-1])
    print("file:" + file_name)
    print("path:" + path)
    return path, file_name

def get_file_pre_post_fix(file_name):
    point_index = file_name.rfind('.')
    file_prefix = file_name[:point_index]
    file_postfix = file_name[point_index + 1:]
    return file_prefix, file_postfix

def split_log_by_size(path_info, split_size):
    path, file_name = get_path_and_file(path_info)
    file_prefix, file_postfix = get_file_pre_post_fix(file_name)
    os.chdir(path)

    with open(file_name, 'r') as input_file:
        split_file_index = 0
        while True:
            data = input_file.read(split_size * SPLITE_UNIT)
            if not data:
                break
            new_file_name = file_prefix + "_" + str(split_file_index) + "." + file_postfix
            split_file_index += 1
            print(new_file_name)
            print("size:" + str(len(data)))
            with open(new_file_name, 'w') as output_file:
                output_file.write(data)

def main():
    # TEST_FILE = r'D:\LearnPython\SYSLOG.CSV.LOG'
    print(sys.argv)
    if len(sys.argv) != 3:
        print(USAGE)
    else:
        path = sys.argv[1]
        size = int(sys.argv[2])
        split_log_by_size(path, size)

if __name__ == '__main__':
    main()