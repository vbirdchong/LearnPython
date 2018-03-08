#! python3
# coding:utf-8

import sys
import pyperclip

USAGE_INFO = '''
Usage: python knife_path.py'''

def main():
    knife_path = r'\\eseefsn50.emea.nsn-net.net\rotta4internal\BB\Hangzhou\chenchong'
    pyperclip.copy(knife_path)
    print('knife path was in clipbord, Paste it directly')

if __name__ == '__main__':
    main()