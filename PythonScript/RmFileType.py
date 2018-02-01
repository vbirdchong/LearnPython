#! python3

import sys
import os
import send2trash
from git import Repo

USAGE_INFO = '''
Usage: python RmFileType.py <file_name> <file_path> <git_or_cmd>
 git: use git rm command to delete the file
 cmd: use windows command to delete the file and send to trash
 e.g: python RmFileType.py a.exe D:\ cmd'''

def deleteFile(file_name, file_path, command):
    repo = Repo(file_path)
    git_index = repo.index

    for folder_name, subfolders, file_names in os.walk(file_path):
        # print('The current folder is ' + folder_name)
        for files in file_names:
            if files == file_name:
                delete_file = folder_name + '\\' + files
                # if we want use git command to remove file
                # else use windows cmd to delete the file
                if (command == r'git') :
                    git_index.remove([delete_file])
                else:
                    send2trash.send2trash(delete_file)
                print('Deleting ' + delete_file + '...')

def main():
    if len(sys.argv) != 4:
        print(USAGE_INFO)
    else:
        command = sys.argv[3]
        if (command != 'git' and command != 'cmd') :
            print(USAGE_INFO)
        else :
            file_name = sys.argv[1]
            file_path = sys.argv[2]
            print("File Name: " + file_name + '\n' + 'File Path: ' + file_path + '\n')
            deleteFile(file_name, file_path, command)

if __name__ == '__main__':
    main()
