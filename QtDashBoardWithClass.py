## Version setting up a separate class
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

## Subclass QMainWindow to costumize your application main window
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder app!")
        button = QPushButton("Press Me!!!")
        # set my button as the central widget
        self.setCentralWidget(button)
        
app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()