#! python3

import sys
import os
import send2trash

def deleteFile(file_name, file_path):
    for folder_name, subfolders, file_names in os.walk(file_path):
        # print('The current folder is ' + folder_name)
        for files in file_names:
            if files == file_name:
                delete_file = folder_name + '\\' + files
                print('Deleting ' + delete_file + '...')
                send2trash.send2trash(delete_file)

def main():
    if len(sys.argv) != 3:
        print('Usage:\n python RmFileType.py <file_name> <file_path>')
    else:
        file_name = sys.argv[1]
        file_path = sys.argv[2]
        print("File Name: " + file_name + '\n' + 'File Path: ' + file_path + '\n')
        # os.chdir(file_path)
        deleteFile(file_name, file_path)

if __name__ == '__main__':
    main()
