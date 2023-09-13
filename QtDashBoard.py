# Importing the components we need
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


# The sys module is resposible for processing command line arguments 
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("My firts MainWindow App!!!")

"""AL ABOUT BUTTON"""
def button_cliked(data):
    print("You clicked the button, didn't you??",data)
       
button = QPushButton()
button.setText("Press me")
window.setCentralWidget(button)

button.setCheckable(True)
button.clicked.connect(button_cliked)
"FINISH WITH THE BUTTON"

"ABOUT SLIDER(DESLIZADOR)"
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSlider
def respond_to_slider(data2):
    print("slider moved to : ", data2)
    
    
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(50)

slider.valueChanged.connect(respond_to_slider)
slider.show()
## window.setCentralWidget(slider)

"FINISH WITH THE SLIDER"

window.show()
# Start the event loop 
app.exec()