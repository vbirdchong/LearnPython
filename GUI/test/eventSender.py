#!/usr/bin/env python
# coding=utf-8

import sys
from PyQt4 import QtGui, QtCore

class eventSender(QtGui.QMainWindow):
	"""docstring for eventSender"""
	def __init__(self, parent = None):
		super(eventSender, self).__init__(None)
		self.initUI()

	def initUI(self):
		btn1 = QtGui.QPushButton("Button 1", self)
		btn1.move(30, 50)

		btn2 = QtGui.QPushButton("Button 2", self)
		btn2.move(150, 50)

		btn1.clicked.connect(self.buttonClicked)
		btn2.clicked.connect(self.buttonClicked)

		self.statusBar()

		self.setGeometry(300, 300, 300, 150)
		self.setWindowTitle("Event Sender")
		self.show()

	def buttonClicked(self):
		sender = self.sender()
		self.statusBar().showMessage(sender.text() + ' was pressed')

def main():
	app = QtGui.QApplication(sys.argv)
	ex = eventSender()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()


		