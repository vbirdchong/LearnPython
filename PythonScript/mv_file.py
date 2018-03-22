# -*- coding=utf-8 -*-

import os
import sys

USAGE_INFO = '''
Usage: python mv_file.py <file_postfix> <src_folder> <target_folder> <git_or_cmd>
 git: use git mv command to move the file
 cmd: use windows command to move the file
 e.g: python mv_file.py py D:\src_test D:\\target_test cmd'''

MOVE_WIN = "move "
MOVE_GIT = "git mv "
CMD = MOVE_WIN

def mv_file(file_postfix_type, src_folder, target_folder):
    if os.path.isabs(src_folder) and os.path.isabs(target_folder):
        os.chdir(src_folder)
        print(os.getcwd())

        files = os.listdir(src_folder)
        for f in files:
            if f.endswith(file_postfix_type):
                os.system(get_cmd_info(f, target_folder))
    else:
        print('Error: The src/target folder should be a absolute path!')

def get_cmd_info(file_name, target_folder):
    cmd = CMD + '\"' + file_name + '\"' " " + target_folder
    print(cmd)
    return cmd

def main():
    global CMD
    if len(sys.argv) != 5 or (sys.argv[4].lower() != r'git' and sys.argv[4].lower() != r'cmd'):
        print(USAGE_INFO)
    else:
        if sys.argv[4].lower() == r'git':
            CMD = MOVE_GIT
        else:
            CMD = MOVE_WIN

        mv_file(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == '__main__':
    main()