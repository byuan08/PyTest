import sys
from PyQt4 import QtGui

app = QtGui.QAppication(sys.argv)
window = QtGui.QWidget()
window.setGeometry(0, 0, 500, 300)
window.setWindowTitle("My PyWQt App")

window.show()
