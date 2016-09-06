#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui, QtCore

class CComboBox(QtGui.QWidget):
	"""docstring for CComboBox"""
	def __init__(self):
		super(CComboBox, self).__init__()
		self.intiUI()

	def intiUI(self):
		self.lbl = QtGui.QLabel('Ubuntu', self)

		combo = QtGui.QComboBox(self)
		combo.addItem('Ubuntu')
		combo.addItem('Mandriva')
		combo.addItem('Fedora')
		combo.addItem('Red Hat')
		combo.addItem('Gentoo')

		combo.move(50, 50)
		self.lbl.move(50, 150)

		combo.activated[str].connect(self.onAction)

		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('QtGui.QComboBox')
		self.show()

	def onAction(self, text):
		self.lbl.setText(text)
		self.lbl.adjustSize()


def main():
	app = QtGui.QApplication(sys.argv)
	ex = CComboBox()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
		