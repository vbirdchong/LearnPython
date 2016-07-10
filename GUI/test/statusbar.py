#!/usr/bin/env python
# coding=utf-8

import sys
from PyQt4 import QtGui, QtCore

class mainWindow(QtGui.QMainWindow):
	"""docstring for mainWindow"""
	def __init__(self, parent = None):
		super(mainWindow, self).__init__(parent)
		self.setGeometry(400, 400, 300, 200)
		self.setWindowTitle("StatusBar")
		self.setWindowIcon(QtGui.QIcon('./linux.png'))
		self.statusBar().showMessage('Ready')

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	mainWin = mainWindow()
	mainWin.show()
	sys.exit(app.exec_())


		