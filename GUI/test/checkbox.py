#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui, QtCore

class checkBox(QtGui.QWidget):
	"""docstring for checkBox"""
	def __init__(self, parent = None):
		super(checkBox, self).__init__(parent)
		self.initUI()

	def initUI(self):
		cb = QtGui.QCheckBox('Show title', self)
		cb.move(20, 20)
		cb.toggle()
		cb.stateChanged.connect(self.changeTitle)

		self.setGeometry(300, 300, 300, 150)
		self.setWindowTitle('QtGui.QCheckBox')
		self.show()

	def changeTitle(self, state):
		if state == QtCore.Qt.Checked:
			self.setWindowTitle('QtGui.QCheckBox')
		else:
			self.setWindowTitle('')

def main():
	app = QtGui.QApplication(sys.argv)
	ex = checkBox()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
		