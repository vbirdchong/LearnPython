#! /usr/bin/env python
# -*- coding = utf-8 -*-

import shelve
import pyperclip
import sys

# python.exe multiClipBoard.py save <keyword> - Saves clipboard to keyword
# python.exe multiClipBoard.py <keyword> - Load keyword to clipboard
# python.exe multiClipBoard.py list -Loads all keywords to clipboard
# python.exe multiClipBoard.py delete <keyword>- Delete keyword 

def main():
	mcbShelf = shelve.open('mcb')

	if len(sys.argv) == 3:
		if sys.argv[1].lower() == 'save':
			mcbShelf[sys.argv[2]] = pyperclip.paste()
		elif sys.argv[1].lower() == 'delete':
			if mcbShelf.has_key(sys.argv[2]):
				del mcbShelf[sys.argv[2]]
				# clean the clipboard
				pyperclip.copy('')
	elif len(sys.argv) == 2:
		if sys.argv[1].lower() == 'list':
			pyperclip.copy(str(list(mcbShelf.keys())))
		elif sys.argv[1] in mcbShelf:
			pyperclip.copy(mcbShelf[sys.argv[1]])

	mcbShelf.close()


if __name__ == '__main__':
	main()