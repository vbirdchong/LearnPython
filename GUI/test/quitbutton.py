#!/usr/bin/env python
# coding=utf-8

import sys
from PyQt4 import QtGui, QtCore

class QuitButton(QtGui.QWidget):
	"""docstring for QuitButton"""
	def __init__(self, parent = None):
		super(QuitButton, self).__init__(parent)
		
		self.setGeometry(300, 300, 250, 100)
		self.setWindowTitle("QuitButton")
		self.setWindowIcon(QtGui.QIcon("./linux.png"))

		quit = QtGui.QPushButton('Quit', self)
		quit.setGeometry(20, 20, 60, 40)

		self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp,
			QtCore.SLOT('quit()'))


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	quitBut = QuitButton()
	quitBut.show()
	sys.exit(app.exec_())

