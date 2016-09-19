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
		self.create_calendar()
		self.show()

	def create_app_window(self):	
		# Use super so we return parent object of this class
		super(Window, self).__init__()
		self.setGeometry(50, 50, 1000, 600)
		self.setWindowTitle("Qt Application")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

	def create_menubar(self):	
		'''Create mainMenu for application'''
		self.mainMenu = self.menuBar()
		self.mainMenu.setNativeMenuBar(False)

		self.create_mainmenu_exit_action()
		self.create_mainmenu_open_editor()
		self.create_mainmenu_open_file()
		self.create_mainmenu_save_file()

	def create_mainmenu_exit_action(self):
		'''Create exit action for file menu'''

		mbExitButton = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
		mbExitButton.setShortcut('Ctrl+Q')
		mbExitButton.setStatusTip('Quit Application')
		mbExitButton.triggered.connect(self.close_application)

		# Create file menu and add to main menu
		self.fileMenu = self.mainMenu.addMenu('File')
		
		# add exit aciton to file menu
		self.fileMenu.addAction(mbExitButton)

	def create_mainmenu_open_editor(self):
		'''create editor action for opening editor'''
		mbOpenEditor = QtGui.QAction(QtGui.QIcon(), '&Editor', self)
		mbOpenEditor.setShortcut('Ctrl+E')
		mbOpenEditor.setStatusTip('Open Editor')
		mbOpenEditor.triggered.connect(self.open_editor)

		# create editor menu and add to main menu
		self.editorMenu = self.mainMenu.addMenu('Editor')

		# add editor action to editor menu
		self.editorMenu.addAction(mbOpenEditor)

	def create_mainmenu_open_file(self):
		'''create open file action'''
		mbOpenFile = QtGui.QAction(QtGui.QIcon(), 'Open File', self)
		mbOpenFile.setShortcut('Ctrl+O')
		mbOpenFile.setStatusTip('Open File')
		mbOpenFile.triggered.connect(self.open_file)

		self.fileMenu.addAction(mbOpenFile)

	def create_mainmenu_save_file(self):
		'''create an action for saving files'''
		mbSaveFile = QtGui.QAction(QtGui.QIcon(''), '&Save File', self)
		mbSaveFile.setStatusTip('Save file to disk')
		mbSaveFile.setShortcut('Ctrl+S')
		mbSaveFile.triggered.connect(self.save_file)

		self.fileMenu.addAction(mbSaveFile)

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
		'''create tool bar button'''
		tbExitAction = QtGui.QAction(QtGui.QIcon('exit.png'), 'Flee the scene', self)
		tbExitAction.triggered.connect(self.close_application)
		# add tool buttons in
		self.toolBar.addAction(tbExitAction)

	def create_toolbar_font_dialog_action(self):
		tbFontDialogAction = QtGui.QAction(QtGui.QIcon('font.png'), 'Font', self)
		tbFontDialogAction.triggered.connect(self.font_dialog)
		self.toolBar.addAction(tbFontDialogAction)

	def create_toolbar_fontcolor_dialog_action(self):
		fontColorAction = QtGui.QAction(QtGui.QIcon('color.png'), 'Font bg Color', self)
		fontColorAction.triggered.connect(self.color_picker)
		self.toolBar.addAction(fontColorAction)

	def create_tool_bar(self):
		self.toolBar = self.addToolBar("Extraction")
		self.create_toolbar_exit_action()
		self.create_toolbar_font_dialog_action()
		self.create_toolbar_fontcolor_dialog_action()		

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

	def open_file(self):
		name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
		file = open(name, 'r')
		self.open_editor()
		with file:
			text = file.read()
			self.textEdit.setText(text)

	def open_editor(self):
		self.textEdit = QtGui.QTextEdit()
		self.setCentralWidget(self.textEdit)

	def save_file(self):
		name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
		file = open(name, 'w')
		text = self.textEdit.toPlainText()
		file.write(text)
		file.close()

	def font_dialog(self):
		font,valid = QtGui.QFontDialog.getFont()
		if valid:
			self.styleChoice.setFont(font)

	def color_picker(self):
		color = QtGui.QColorDialog.getColor()
		self.styleChoice.setStyleSheet("QWidget{background-color: $s" % color.name())

	def style_choice(self, text):
		self.styleChoice.setText(text)
		QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

	def create_calendar(self):
		cal = QtGui.QCalendarWidget(self)
		cal.move(500,200)
		cal.resize(200, 200)

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
