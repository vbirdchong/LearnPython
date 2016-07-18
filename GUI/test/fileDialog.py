#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui

class fileDialog(QtGui.QMainWindow):
	"""docstring for fileDialog"""
	def __init__(self, parent = None):
		super(fileDialog, self).__init__(parent)
		self.initUI()

	def initUI(self):
		self.textEdit = QtGui.QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.statusBar()

		openFile = QtGui.QAction(QtGui.QIcon('./linux.png'), 'Open', self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open new File')
		openFile.triggered.connect(self.showDialog)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)

		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('File dialog')
		self.show()

	def showDialog(self):
		fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
		f = open(fname, 'r')
		with f:
			data = f.read()
			self.textEdit.setText(data)

def main():
	app = QtGui.QApplication(sys.argv)
	ex = fileDialog()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()