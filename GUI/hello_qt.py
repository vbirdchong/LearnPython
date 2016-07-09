#!/usr/bin/env python
# conding=utf-8

import sys
from PyQt4 import QtCore, QtGui


class HelloPyQt(QtGui.QWidget):
	"""docstring for HelloPyQt"""
	def __init__(self, parent = None):
		super(HelloPyQt, self).__init__(parent)
		self.setWindowTitle("PyQt Test")
		self.textHello = QtGui.QTextEdit("This is a test")
		self.btnPress = QtGui.QPushButton("Press me!")

		layout = QtGui.QVBoxLayout()
		layout.addWidget(self.textHello)
		layout.addWidget(self.btnPress)
		self.setLayout(layout)

		self.btnPress.clicked.connect(self.btnPress_Clicked)

	def btnPress_Clicked(self):
		self.textHello.setText("Hello PyQt!\nThe Button has been pressed.")

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	mainWindow = HelloPyQt()
	mainWindow.show()
	sys.exit(app.exec_())

	


		