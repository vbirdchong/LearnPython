#! /usr/bin/env python
# -*- coding = utf-8 -*-

# findLargeFiles.py - Find the files which exceed 'requiredSize(unti: 1MB)' in the path of 'requiredFilePath'
# python findLargeFiles.py <size> <abspath>

import os
import sys

# MB_SIZE = 2
MB_SIZE = (1024 * 1024)

def find_files(size, path):
	for root, dirs, files in os.walk(path):
		for file in files:
			file = os.path.join(root,file)
			# print(file)
			if os.path.isfile(file):
				fileSize = os.path.getsize(file) / MB_SIZE
				if (fileSize) >= size:
					print(file + ' size: ' + str(fileSize) + 'MB')

def main():
	if len(sys.argv) == 3:
		find_files(int(sys.argv[1]), sys.argv[2])
	else:
		print('Usage: python findLargeFiles.py <requiredSize MB> <requiredFilePath>')

if __name__ == '__main__':
	main()