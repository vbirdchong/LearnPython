#! python3

import os
import sys
import time

USAGE_INFO = '''
Usage: python top_file_size.py path top_number
 e.g.: list the top 10 folders in D:\code
        python top_file_size.py D:\code 10'''

ONE_MB = 1048576
ONE_GB = 1073741824

def get_folder_size(folder):
    print('Checking ' + folder + '...')
    total_size = os.path.getsize(folder)
    try:
        for item in os.listdir(folder):
            itempath = os.path.join(folder, item)
            if os.path.isfile(itempath):
                total_size += os.path.getsize(itempath)
            elif os.path.isdir(itempath):
                total_size += get_folder_size(itempath)
    except IOError:
        print('Error upon either deleting or creating the directory or files.\t' + folder)

    return total_size

def get_top_size_folder_info(directory, top_number):
    folder_info = {}
    for root, subdir, files in os.walk(directory):
        for folder in subdir:
            path = os.path.join(root, folder)
            size = get_folder_size(path)
            folder_info[path] = size

    size_sorted = sorted(zip(folder_info.values(), folder_info.keys()), reverse=True)
    top_size_folder_info = []
    for i in range(top_number):
        folder_size, folder_path = size_sorted[i]

        print_info = ''
        if folder_size > ONE_GB:
            print_info = '%10.2f GB' % (folder_size / ONE_GB) + '\t'
        else:
            print_info = '%10.2f MB' % (folder_size / ONE_MB) + '\t'

        print_info += folder_path
        top_size_folder_info.append(print_info)
    return top_size_folder_info

def main():
    if len(sys.argv) == 3:
        start_time = time.clock()
        info = get_top_size_folder_info(sys.argv[1], int(sys.argv[2]))
        end_time = time.clock()
        for data in info:
            print(data)
        print("Done, time spent: " + str(end_time - start_time))
    else:
        print(USAGE_INFO)

if __name__ == '__main__':
    main()
