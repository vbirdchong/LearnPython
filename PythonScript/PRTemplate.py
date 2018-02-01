#! python3
# coding: utf-8

import sys
import pyperclip

USAGE_INFO = '''
Usage: python PRTemplate.py'''

def copyTemplate():
    strTemplate = \
    '''
    [Findings]

    [Log files]

    [Conclusion]

    [Next Steps]

    [Analysis Author]
    '''
    pyperclip.copy(strTemplate)

def main():
    copyTemplate()
    print("Template info was in clipbord, Paste it directly...")

if __name__ == '__main__':
    main()
