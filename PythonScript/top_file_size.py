#! python3

import os

ONE_MB = 1048576

def get_folder_size(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += get_folder_size(itempath)

    return total_size


def main():
    TEST_DIR = r'D:\LearnPython'

    folder_size_list = []
    folder_info = []
    for root, subdir, files in os.walk(TEST_DIR):
        for folder in subdir:
            path = os.path.join(root, folder)
            size = get_folder_size(path)
            folder_size_list.append(size)
            info = {}
            info['folder'] = path
            info['size'] = size
            folder_info.append(info)
            
            # print(path + "\tsize: " + str(get_folder_size(path)))

    folder_size_list.sort(reverse=True)
    print("TOP size:")
    print(folder_size_list[:10])


if __name__ == '__main__':
    main()
