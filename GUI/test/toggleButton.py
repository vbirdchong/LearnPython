#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui, QtCore

class CToggleButton(QtGui.QWidget):
	"""docstring for CToggleButton"""
	def __init__(self, parent = None):
		super(CToggleButton, self).__init__(parent)
		self.initUI()

	def initUI(self):
		self.col = QtGui.QColor(0, 0, 0)

		redBut = QtGui.QPushButton('Red', self)
		redBut.setCheckable(True)
		redBut.move(10, 10)
		redBut.clicked[bool].connect(self.setColor)

		greenBun = QtGui.QPushButton('Green', self)
		greenBun.setCheckable(True)
		greenBun.move(10, 60)
		greenBun.clicked[bool].connect(self.setColor)

		blueBut = QtGui.QPushButton('Blue', self)
		blueBut.setCheckable(True)
		blueBut.move(10, 110)
		blueBut.clicked[bool].connect(self.setColor)

		self.square = QtGui.QFrame(self)
		self.square.setGeometry(150, 20, 100, 100)
		self.square.setStyleSheet('QWidget { background-color: %s }' % self.col.name)

		self.setGeometry(300, 300, 280, 170)
		self.setWindowTitle('Toggle button')
		self.show()

	def setColor(self, pressed):
		source = self.sender()

		if pressed:
			val = 255
		else:
			val = 0

		if source.text() == "Red":
			self.col.setRed(val)
		elif source.text() == "Green":
			self.col.setGreen(val)
		else:
			self.col.setBlue(val)

		self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())


def main():
	app = QtGui.QApplication(sys.argv)
	ex = CToggleButton()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()





