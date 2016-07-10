#!/usr/bin/env python
# coding=utf-8

import sys
from PyQt4 import QtGui

class Icon(QtGui.QWidget):
	"""docstring for Icon"""
	def __init__(self, parent = None):
		super(Icon, self).__init__(parent)
		
		# set the window locaton(300,300) and size(400,400)
		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle('Icon')
		self.setWindowIcon(QtGui.QIcon("./linux.png"))


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	icon = Icon()
	icon.show()
	sys.exit(app.exec_())
		