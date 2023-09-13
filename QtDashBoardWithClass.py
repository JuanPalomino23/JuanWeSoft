## Version setting up a separate class
import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder,  SliderMove

        
app = QApplication(sys.argv)
window = ButtonHolder()
window2 = SliderMove()

window.show()
window2.show()
app.exec()