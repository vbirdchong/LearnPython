#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui, QtCore

class Communicate(QtCore.QObject):
	closeApp = QtCore.pyqtSignal()


class Example(QtGui.QMainWindow):
	"""docstring for Example"""
	def __init__(self, parent = None):
		super(Example, self).__init__(parent)
		self.initUI()

	def initUI(self):
		self.c = Communicate()
		self.c.closeApp.connect(self.close)

		self.setGeometry(300, 300, 300, 150)
		self.setWindowTitle('Emit Signal')
		self.show()

	def mousePressEvent(self, event):
		self.c.closeApp.emit()


def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()


		
		

