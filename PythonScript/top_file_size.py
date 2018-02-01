#! python3

import os

ONE_MB = 1048576
ONE_GB = 1073741824

def get_folder_size(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += get_folder_size(itempath)

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
        folder_size = size_sorted[i][0]
        folder_path = size_sorted[i][1]

        print_info = ''
        if folder_size > ONE_GB:
            print_info = '%10.2f GB' % (folder_size / ONE_GB) + '\t'
        else:
            print_info = '%10.2f MB' % (folder_size / ONE_MB) + '\t'

        print_info += folder_path
        top_size_folder_info.append(print_info)
    return top_size_folder_info

def main():
    TEST_DIR = r'D:\Code\LearnPython'
    info = get_top_size_folder_info(TEST_DIR, 10)
    for data in info:
        print(data)


if __name__ == '__main__':
    main()
