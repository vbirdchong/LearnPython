#! /usr/bin/env python
# -*- coding = utf-8 -*-

# renameDates.py - Rename filenames with American MM-DD-YYYY date format to European DD-MM-YYYY

import os
import re
import shutil

datePattern = re.compile(r'''^(.*?) # all text before the date
	((0|1)?\d)-						# one or two digits for the month
	((0|1|2|3)?\d)-					# one or two digits for the day
	((19|20)\d\d)					# four digits for the year
	(.*?)$							# all text after the date
	''', re.VERBOSE)


def rename_files():
	for amerFilename in os.listdir('.'):
		matchedFile = datePattern.search(amerFilename)
		if matchedFile != None:
			beforePart 	= matchedFile.group(1)
			monthPart 	= matchedFile.group(2)
			dayPart		= matchedFile.group(4)
			yearPart	= matchedFile.group(6)
			afterPart	= matchedFile.group(8)

			# form the european-style filename
			euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

			# get the full absolute file paths
			absWorkingDir = os.path.abspath('.')
			amerFilename = os.path.join(absWorkingDir, amerFilename)
			euroFilename = os.path.join(absWorkingDir, euroFilename)

			# rename the files
			print('Renaming "%s" to "%s" ...' % (amerFilename, euroFilename))
			shutil.move(amerFilename, euroFilename)

def main():
	rename_files()

if __name__ == '__main__':
	main()
