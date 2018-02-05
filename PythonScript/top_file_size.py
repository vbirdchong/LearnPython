#! python3

import os
import sys
import time
import ctypes

USAGE_INFO = '''
Usage: python top_file_size.py path top_number
 e.g.: list the top 10 folders in D:\code
        python top_file_size.py D:\code 10'''

ONE_MB = 1048576
ONE_GB = 1073741824
SKIP_FOLDER = ['System Volume Information', 'Office365_Update']

def run_as_admin(argv=None, debug=False):
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True

    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        # Support pyinstaller wrapped program.
        arguments = map(unicode, argv[1:])
    else:
        arguments = map(unicode, argv)
    argument_line = u' '.join(arguments)
    executable = unicode(sys.executable)
    if debug:
        print 'Command line: ', executable, argument_line
    ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
    if int(ret) <= 32:
        return False
    return None

def get_folder_size(folder):
    print('Checking ' + folder + ' ...')
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

def is_need_skip(folder_name):
    ret = False
    if (folder_name.startswith('.')) or (folder_name in SKIP_FOLDER):
        ret = True
    return ret

def get_top_size_folder_info(directory, top_number):
    folder_info = {}
    for root, subdir, files in os.walk(directory):
        for folder in subdir:
            if is_need_skip(folder):
                continue
            else:
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
        elif folder_size > ONE_MB:
            print_info = '%10.2f MB' % (folder_size / ONE_MB) + '\t'
        else:
            print_info = '%10.2f KB' % folder_size + '\t'

        print_info += folder_path
        top_size_folder_info.append(print_info)
    return top_size_folder_info

def write_to_report_file(path, info):
    os.chdir(path)
    with open('Top_file_size_report.log', 'wt') as f:
        for data in info:
            f.write(data + '\n')

def main():
    if len(sys.argv) == 3:
        start_time = time.clock()
        info = get_top_size_folder_info(sys.argv[1], int(sys.argv[2]))
        write_to_report_file(sys.argv[1], info)
        end_time = time.clock()
        for data in info:
            print(data)
        print("Done, time spent: " + str(end_time - start_time))
    else:
        print(USAGE_INFO)

if __name__ == '__main__':
    main()
