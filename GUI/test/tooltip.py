#!usr/bin/env python
# coding=utf-8

import sys
from PyQt4 import QtGui, QtCore

class ToolTip(QtGui.QWidget):
	"""docstring for ToolTip"""
	def __init__(self, parent = None):
		super(ToolTip, self).__init__(parent)
		
		self.setGeometry(300, 300, 450, 150)
		self.setWindowTitle("ToolTip")
		self.setWindowIcon(QtGui.QIcon("./linux.png"))
		# set the infomation of the tooltips 
		self.setToolTip("This is a <b>QWidge</b> widget")

		# we can use this method to set the font and size
		QtGui.QToolTip.setFont(QtGui.QFont('English', 15))


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	tooltip = ToolTip()
	tooltip.show()
	sys.exit(app.exec_())


		