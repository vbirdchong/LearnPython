#! /usr/bin/env python
# -*- coding=utf-8 -*-

# usage: python rmaexe.py <d:\\AlgoCode>

import os
import sys
import send2trash


def findExeFile(path):
    for folderName, subfolders, fileNames in os.walk(path):
        for file in fileNames:
            if file == 'a.exe':
                filePath = os.path.join(folderName,file) 
                print(filePath)
                # delete the file to trash
                # we can recover the file from trash
                send2trash.send2trash(filePath)


def main():
    if len(sys.argv) == 2:
        findExeFile(sys.argv[1])
    else:
        print("Usage: python rmaexe.py <abspath>")


if __name__ == '__main__':
    main()