#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui, QtCore

class CPixmap(QtGui.QWidget):
	"""docstring for CPixmap"""
	def __init__(self):
		super(CPixmap, self).__init__()
		self.intiUI()

	def intiUI(self):
		hbox = QtGui.QHBoxLayout(self)
		pixmap = QtGui.QPixmap("./linux.png")

		lbl = QtGui.QLabel(self)
		lbl.setPixmap(pixmap)

		hbox.addWidget(lbl)
		self.setLayout(hbox)

		self.move(100, 100)
		self.setWindowTitle('Linux')
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	ex = CPixmap()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
		