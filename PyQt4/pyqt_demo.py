import sys, pdb
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

	def __init__(self):
		self.create_app_window()
		self.create_menubar()
		self.home()

	def home(self):
		
		self.create_tool_bar()
		self.create_quitbutton()
		self.create_checkbox()
		self.create_downloadbutton()
		self.create_progress_bar()
		self.create_style_choice_label()
		self.create_comboBox()
		self.show()

	def create_app_window(self):	
		# Use super so we return parent object of this class
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("Qt Application")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

	def create_menubar(self):	
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
		
	def create_quitbutton(self):
		btn = QtGui.QPushButton("Quit", self)
		btn.setToolTip('Click to quit')
		btn.clicked.connect(self.close_application)

		#There is sizeHint and minimumSizeHint. 
		#The sizeHint code will return what QT thinks is the best side for your button. 
		#The minimumSizeHint will just return what QT thinks is the smallest reasonable size for your button.
		btn.resize(btn.minimumSizeHint())
		btn.move(100, 100)

	def create_toolbar_exit_action(self):
	    # create tool bar button
		tbExitAction = QtGui.QAction(QtGui.QIcon('exit.png'), 'Flee the scene', self)
		tbExitAction.triggered.connect(self.close_application)
		# add tool buttons in
		self.toolBar.addAction(tbExitAction)

	def create_toolbar_font_dialog_action(self):
		tbFontDialogAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Font', self)
		tbFontDialogAction.triggered.connect(self.font_dialog)
		self.toolBar.addAction(tbFontDialogAction)

	def create_tool_bar(self):
		self.toolBar = self.addToolBar("Extraction")
		pdb.set_trace()
		self.create_toolbar_exit_action()
		self.create_toolbar_font_dialog_action()

	def create_checkbox(self):
		'create and configure a checkbox object'

		checkBox = QtGui.QCheckBox('Enlarge Window', self)
		checkBox.move(100, 150)
		checkBox.resize(200,50)
		#checkBox.toggle()
		checkBox.stateChanged.connect(self.enlarge_window)

	def create_downloadbutton(self):
		dl_btn = QtGui.QPushButton("Download", self)
		dl_btn.setToolTip("Click to start download")
		dl_btn.resize(dl_btn.sizeHint())
		dl_btn.move(200, 200)
		dl_btn.clicked.connect(self.download)

	def download(self):
		self.completed = 0

		while self.completed < 100:
			self.completed += 0.001
			self.progress.setValue(self.completed)

	def create_progress_bar(self):
		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(100, 80, 250, 20)

	def create_style_choice_label(self):
		self.styleChoice = QtGui.QLabel("Mac", self)
		self.styleChoice.move(50,150)

	def create_comboBox(self):
		comboBox = QtGui.QComboBox(self)
		comboBox.addItem("motif")
		comboBox.addItem("Windows")
		comboBox.addItem("cde")
		comboBox.addItem("Plastique")
		comboBox.addItem("Cleanlooks")
		comboBox.addItem("windowsvista")
		comboBox.move(50, 250)

		comboBox.activated[str].connect(self.style_choice)
	def font_dialog(self):
		font,valid = QtGui.QFontDialog.getFont()
		if valid:
			self.styleChoice.setFont(font)

	def style_choice(self, text):
		self.styleChoice.setText(text)
		QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

	def enlarge_window(self, state):

		# how did state get passed over?
		if state == QtCore.Qt.Checked:
			self.setGeometry(50, 50, 1000, 600)
		else:
			self.setGeometry(50, 50, 500, 300)

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
