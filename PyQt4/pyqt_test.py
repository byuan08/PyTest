import sys, pdb
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

	def __init__(self):

		# Use super so we return parent object of this class
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("Qt Application")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

		# Create mainMenu for application
		mainMenu = self.menuBar()
		mainMenu.setNativeMenuBar(False)

		# Create file menu and add to main menu
		fileMenu = mainMenu.addMenu('File')

		# Create exit action for file menu
		mbExitButton = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
		mbExitButton.setShortcut('Ctrl+Q')
		mbExitButton.setStatusTip('Quit Application')
		mbExitButton.triggered.connect(self.close_application)

		# exit aciton to file menu
		fileMenu.addAction(mbExitButton)

		# 
		self.statusBar()


		self.home()

	def home(self):
		btn = QtGui.QPushButton("Quit", self)
		btn.setToolTip('Click to quit')
		btn.clicked.connect(self.close_application)

		#There is sizeHint and minimumSizeHint. 
		#The sizeHint code will return what QT thinks is the best side for your button. 
		#The minimumSizeHint will just return what QT thinks is the smallest reasonable size for your button.
		btn.resize(btn.minimumSizeHint())
		btn.move(100, 100)

		tbExitButton = QtGui.QAction(QtGui.QIcon('exit.png'), 'Flee the scene', self)
		tbExitButton.triggered.connect(self.close_application)

		self.toolBar = self.addToolBar("Extraction")
		self.toolBar.addAction(tbExitButton)

		self.show()

	def close_application(self):
		
		choice = QtGui.QMessageBox.question(self, 'Extract!', 
											'Are you sure to exit?', 
											QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

		if choice == QtGui.QMessageBox.Yes:
			print("Exiting")
			sys.exit()
		else:
			pass

		

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())


if __name__ == "__main__":
	run()


