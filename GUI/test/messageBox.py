#!/usr/bin/env python
# coding=utf-8

import sys
from PyQt4 import QtCore, QtGui

class MessageBox(QtGui.QWidget):
	"""docstring for MessageBox"""
	def __init__(self, parent = None):
		super(MessageBox, self).__init__(parent)
		self.setGeometry(500, 300, 350, 250)
		self.setWindowTitle("Message Box")
		self.setWindowIcon(QtGui.QIcon('./linux.png'))

	def closeEvent(self, event):
		reply = QtGui.QMessageBox.question(self, 
						"Message Info", 
						"Are you sure to quit?",
						QtGui.QMessageBox.No,
						QtGui.QMessageBox.Yes)
		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	message_box = MessageBox()
	message_box.show()
	sys.exit(app.exec_())
