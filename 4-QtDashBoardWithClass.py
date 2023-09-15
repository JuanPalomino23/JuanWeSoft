## Version setting up a separate class
import sys
from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow
#from button_holder import ButtonHolder

        
app = QApplication(sys.argv)
window = MainWindow(app)
#window = ButtonHolder()
#window2 = SliderMove()

window.show()
app.exec()