
#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui, QtCore

class MyWidget(QtGui.QWidget):
	"""docstring for MyWidget"""
	def __init__(self, parent = None):
		super(MyWidget, self).__init__(parent)
		widget = QtGui.QWidget()
		widget.resize(50, 50)
		widget.setWindowTitle('Simple')
		

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	my_widget = MyWidget()
	my_widget.show()

	sys.exit(app.exec_())



