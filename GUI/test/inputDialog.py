#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui, QtCore

class inputDialog(QtGui.QWidget):
	"""docstring for inputDialog"""
	def __init__(self, parent = None):
		super(inputDialog, self).__init__(parent)
		self.initUI()

	def initUI(self):
		self.btn = QtGui.QPushButton('Dialog', self)
		self.btn.move(30, 30)
		self.btn.clicked.connect(self.showDialog)

		self.le = QtGui.QLineEdit(self)
		self.le. move(130, 30)

		self.setGeometry(300, 300, 300, 150)
		self.setWindowTitle('Input Dialog')
		self.show()

	def showDialog(self):
		text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'User name:')
		if ok:
			self.le.setText(str(text))
		

def main():
	app = QtGui.QApplication(sys.argv)
	ex = inputDialog()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()