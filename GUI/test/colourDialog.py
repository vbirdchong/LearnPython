#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui

class colourDialog(QtGui.QWidget):
	"""docstring for colourDialog"""
	def __init__(self, parent = None):
		super(colourDialog, self).__init__(parent)
		self.initUI()

	def initUI(self):
		colour = QtGui.QColor(0, 250, 0)

		self.btn = QtGui.QPushButton('Dialog', self)
		self.btn.move(20, 20)

		self.btn.clicked.connect(self.showDialog)

		self.frm = QtGui.QFrame(self)
		self.frm.setStyleSheet("QWidget {background-color:%s }" % colour.name())
		self.frm.setGeometry(130, 20, 100, 100)

		self.setGeometry(300, 300, 300, 150)
		self.setWindowTitle('Colour Dialog')
		self.show()

	def showDialog(self):
		colour = QtGui.QColorDialog.getColor()
		if colour.isValid():
			self.frm.setStyleSheet("QWidget {background-color:%s }" % colour.name())

def main():
	app = QtGui.QApplication(sys.argv)
	ex = colourDialog()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

