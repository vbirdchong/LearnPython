#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui

class CButton(QtGui.QPushButton):
	"""docstring for CButton"""
	def __init__(self, title, parent):
		super(CButton, self).__init__(title, parent)
		self.setAcceptDrops(True)

	def dragEnterEvent(self, e):
		if e.mimeData().hasFormat('text/plain'):
			e.accept()
		else:
			e.ignore()

	def dropEvent(self, e):
		self.setText(e.mimeData().text())


class Example(QtGui.QWidget):
	"""docstring for Example"""
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		edit = QtGui.QLineEdit('', self)
		edit.setDragEnabled(True)
		edit.move(30, 65)

		button = CButton('Button', self)
		button.move(190, 65)

		self.setWindowTitle('Simple drag & drop')
		self.setGeometry(300, 300, 300, 200)


def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	ex.show()
	app.exec_()


if __name__ == '__main__':
	main()