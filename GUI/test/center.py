#!/usr/bin/env python
# coding=utf-8

import sys
from PyQt4 import QtGui, QtCore

class Center(QtGui.QWidget):
	"""docstring for Center"""
	def __init__(self, parent = None):
		super(Center, self).__init__(parent)
		
		self.setWindowTitle("Center")
		self.setWindowIcon(QtGui.QIcon('./linux.png'))
		self.resize(350, 250)
		self.center()
		
	def center(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width() - size.width()) / 2,
					(screen.height() - size.height()) / 2)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	center = Center()
	center.show()
	sys.exit(app.exec_())

