#! python3
# coding: utf-8

import sys
import pyperclip

def copyTemplate():
    strTemplate = \
    '''
    [Findings]

    [Logs]

    [Next Step]

    [Conclusion]

    [Author]
    '''
    pyperclip.copy(strTemplate)

def main():
    copyTemplate()

if __name__ == '__main__':
    main()
