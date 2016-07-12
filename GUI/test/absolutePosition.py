#!/usr/bin/env python
# conding = utf-8

import sys
from PyQt4 import QtGui

class absolutePosi(QtGui.QWidget):
	"""docstring for absolutePosi"""
	def __init__(self, parent = None):
		super(absolutePosi, self).__init__(parent)
		self.initUI()

	def initUI(self):
		lb_1 = QtGui.QLabel('PyQt4', self)
		lb_1.move(15, 10)

		lb_2 = QtGui.QLabel('Learning', self)
		lb_2.move(35, 30)

		lb_3 = QtGui.QLabel('by python', self)
		lb_3.move(55, 50)

		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Absolute')
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	ex = absolutePosi()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
		