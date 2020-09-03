import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot


@Slot()
def say_hello():
    print("Button clicked")

#Creating the qt application
app = QApplication(sys.argv)

#Button creation
button = QPushButton("Click Me")

#Button connection to function
button.clicked.connect(say_hello)
button.show()

#App run
app.exec_()






#signals and slots lets widgets communicate with other widgets or the code
#will log when a button is clicked

