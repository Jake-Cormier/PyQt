from PySide2.QtWidgets import QtGui, QtCore
import sys
class MyGui(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setGeometry(50,50,700,400)
        self.setWindowTitle("My GUI Program")
        self.show()

app = QtGui.QApplication(sys.argv)
mygui = MyGui()
sys.exit(app.exec_())