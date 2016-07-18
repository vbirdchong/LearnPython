#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui

class fontDialog(QtGui.QWidget):
	"""docstring for fontDialog"""
	def __init__(self, parent = None):
		super(fontDialog, self).__init__(parent)
		self.initUI()

	def initUI(self):
		vbox = QtGui.QVBoxLayout()

		btn = QtGui.QPushButton('Dialog', self)
		btn.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		btn.move(20, 20)

		vbox.addWidget(btn)
		btn.clicked.connect(self.showDialog)

		self.lbl = QtGui.QLabel('Knowledge only matters.', self)
		self.lbl.move(130, 20)

		vbox.addWidget(self.lbl)
		self.setLayout(vbox)

		self.setGeometry(300, 300, 300, 150)
		self.setWindowTitle('Font Dialog')
		self.show()

	def showDialog(self):
		font, ok = QtGui.QFontDialog.getFont()
		if ok:
			self.lbl.setFont(font)

def main():
	app = QtGui.QApplication(sys.argv)
	ex = fontDialog()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
		