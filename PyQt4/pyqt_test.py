import sys
from PyQt4 import QtGui, QtCore

# app = QtGui.QApplication(sys.argv)
# window = QtGui.QWidget()

# #(Starting x, starting y, width, height)
# window.setGeometry(0, 0, 500, 300)
# window.setWindowTitle("PyQt App")

# window.show()
# sys.exit(app.exec_())

class Window(QtGui.QMainWindow):

	def __init__(self):
		# Use super so we return parent object of this class
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("Qt Application")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
		self.home()

	def home(self):
		btn = QtGui.QPushButton("Quit", self)
		btn.setToolTip('Click to quit')
		btn.clicked.connect(self.close_application)
		
		#There is sizeHint and minimumSizeHint. 
		#The sizeHint code will return what QT thinks is the best side for your button. 
		#The minimumSizeHint will just return what QT thinks is the smallest reasonable size for your button.
		btn.resize(btn.minimumSizeHint())
		btn.move(0, 0)
		self.show()

	def close_application(self):
		print("Exiting")
		sys.exit()

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())


if __name__ == "__main__":
	run()


