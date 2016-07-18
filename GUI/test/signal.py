#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
	"""docstring for Example"""
	def __init__(self, parent = None):
		super(Example, self).__init__(parent)
		self.intiUI()

	def intiUI(self):
		lcd = QtGui.QLCDNumber(self)
		sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)

		vbox = QtGui.QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(sld)

		self.setLayout(vbox)
		sld.valueChanged.connect(lcd.display)

		self.setGeometry(300, 300, 600, 250)
		self.setWindowTitle('Singal & Slot')
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
		