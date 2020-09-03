from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

app = QApplication([])


window = QWidget()
layout = QVBoxLayout() # Define slider widget, note the orientation argument:
slider = QSlider(Qt.Horizontal) 
button = QPushButton('Im just a Button man')
layout.addWidget(QLabel('Hello World!'))
layout.addWidget(button)
layout.addWidget(slider) #Add the slider
window.setLayout(layout)
window.show()
app.exec_()