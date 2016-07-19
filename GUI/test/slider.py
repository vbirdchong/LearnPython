#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui, QtCore

class CSlider(QtGui.QWidget):
	"""docstring for CSlider"""
	def __init__(self, parent = None):
		super(CSlider, self).__init__(parent)
		self.initUI()

	def initUI(self):
		sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
		sld.setFocusPolicy(QtCore.Qt.NoFocus)
		sld.setGeometry(30, 40, 100, 30)
		sld.valueChanged[int].connect(self.changeValue)

		self.label = QtGui.QLabel(self)
		self.label.setPixmap(QtGui.QPixmap('./0.jpg'))
		self.label.setGeometry(160, 40, 300, 300)

		self.setGeometry(300, 300, 600, 600)
		self.setWindowTitle('QtGui.QSlider')
		self.show()

	def changeValue(self, value):
		print("value = %d" % value)
		if value == 0:
			self.label.setPixmap(QtGui.QPixmap('./0.jpg'))
		elif value > 0 and value <= 30:
			self.label.setPixmap(QtGui.QPixmap('./1.jpg'))
		elif value > 30 and value < 80:
			self.label.setPixmap(QtGui.QPixmap('./2.jpg'))
		else:
			self.label.setPixmap(QtGui.QPixmap('./3.png'))

def main():
	app = QtGui.QApplication(sys.argv)
	ex = CSlider()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()