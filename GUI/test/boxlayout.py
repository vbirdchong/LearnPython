
#!/usr/bin/env python
# coding=utf-8

import sys
from PyQt4 import QtGui

class boxLayout(QtGui.QWidget):
	"""docstring for boxLayout"""
	def __init__(self, parent = None):
		super(boxLayout, self).__init__(parent)
		self.initUI()

	def initUI(self):
		
		okButton = QtGui.QPushButton("OK")
		cancelButton = QtGui.QPushButton("Cancel")

		goodButton = QtGui.QPushButton("Good")
		badButton = QtGui.QPushButton("Bad")

		hbox = QtGui.QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(okButton)
		hbox.addWidget(cancelButton)

		gdbox = QtGui.QHBoxLayout()
		gdbox.addStretch(2)
		gdbox.addWidget(goodButton)
		gdbox.addWidget(badButton)

		vbox = QtGui.QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)
		vbox.addLayout(gdbox)

		self.setLayout(vbox)

		self.setGeometry(300, 300, 300, 150)
		self.setWindowTitle("BoxLayout Button")
		self.setWindowIcon(QtGui.QIcon('./linux.png'))
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	boxlayout = boxLayout()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
