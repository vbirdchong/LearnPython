#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui, QtCore

class CLineEdit(QtGui.QWidget):
	"""docstring for CLineEdit"""
	def __init__(self):
		super(CLineEdit, self).__init__()
		self.initUI()

	def initUI(self):
		self.lbl = QtGui.QLabel(self)
		qle = QtGui.QLineEdit(self)

		qle.move(60, 100)
		self.lbl.move(60, 40)

		qle.textChanged[str].connect(self.onChanged)

		self.setGeometry(300, 300, 300, 170)
		self.setWindowTitle('QtGui.QLineEdit')
		self.show()

	def onChanged(self, text):
		self.lbl.setText(text)
		self.lbl.adjustSize()

def main():
	app = QtGui.QApplication(sys.argv)
	ex = CLineEdit()
	sys.exit(app.exec_())
	

if __name__ == '__main__':
	main()