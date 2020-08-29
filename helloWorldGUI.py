from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My App")

        label = QLabel("Test label")

        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

app = QApplication(sys.argv)
#argv pass command line arguments into the application
#if it doesn't need command line arguments just pass an empty list / empty brackets

window = MainWindow()
window.show() #very important to actually see it the window is invisible by default


app.exec_() #underscore is to know it is locked


# event loop  | QApplication | setting a window title | your first widget

 # QApplication
    # it holds the Qt event loop
    #One QApplication instance is always required
    #the app sits witing in the event loop until an action is taken QApplication.exec_()
    #It has an event queue and will pass ot the handler and once complete will circle back to the event loop

#Window QMainWindow
    #Main focus for user of your application
    # every application needs at least one (can have more than one main window)
    #application will exit when last main window is closed