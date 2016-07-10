#!/usr/bin/env python
# coding = utf-8

import sys
from PyQt4 import QtGui, QtCore

class mainWindow(QtGui.QMainWindow):
	"""docstring for mainWindow"""
	def __init__(self, parent = None):
		super(mainWindow, self).__init__(parent)
		
		self.setGeometry(500, 300, 250, 250)
		self.setWindowTitle('Menu Bar')
		self.setWindowIcon(QtGui.QIcon('./linux.png'))

		exitAction = QtGui.QAction('&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(QtGui.qApp.quit)
		# exitAction.connect(exitAction,
		# 			QtCore.SIGNAL('triggered()'),
		# 			QtGui.qApp,
		# 			QtCore.SLOT('quit()'))

		self.statusBar()
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAction)
		

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)		
	mainWin = mainWindow()
	mainWin.show()
	sys.exit(app.exec_())


# import sys
# from PyQt4 import QtGui

# class Example(QtGui.QMainWindow):

#     def __init__(self):
#         super(Example, self).__init__()

#         self.initUI()

#     def initUI(self):               

#         exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
#         exitAction.setShortcut('Ctrl+Q')
#         exitAction.setStatusTip('Exit application')
#         exitAction.triggered.connect(QtGui.qApp.quit)

#         self.statusBar()

#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu('&File')
#         fileMenu.addAction(exitAction)

#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('Menubar')    
#         self.show()


# def main():

#     app = QtGui.QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()