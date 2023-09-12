# Importing the components we need
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


# The sys module is resposible for processing command line arguments 
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("My firts MainWindow App!!!")

button = QPushButton()
button.setText("Press me")

window.setCentralWidget(button)


window.show()
# Start the event loop 
app.exec()