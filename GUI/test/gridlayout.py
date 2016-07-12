
#!/usr/bin/env python
#coding = utf-8

import sys
from PyQt4 import QtGui

class gridLayout(QtGui.QWidget):
	"""docstring for gridLayout"""
	def __init__(self, parent = None):
		super(gridLayout, self).__init__(parent)
		self.initUI()

	def initUI(self):
		grid = QtGui.QGridLayout()
		self.setLayout(grid)

		names = ['Cls', 'Bck', ', ', 'Close',
				 '7', '8', '9', '/',
				 '4', '5', '6', '*',
				 '1', '2', '3', '-',
				 '0', '.', '=', '+']

		positions = [(i,j) for i in xrange(5) for j in xrange(4)]

		for position, name in zip(positions, names):
			if name == '':
				continue
			button = QtGui.QPushButton(name)
			grid.addWidget(button, *position)


		self.move(300, 300)
		# self.setGeometry(300, 300, 300, 300)
		self.setWindowTitle('Calculator')
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	gridlayout = gridLayout()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
		