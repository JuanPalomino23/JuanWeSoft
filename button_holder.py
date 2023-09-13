from PySide6.QtWidgets import QWidget, QSlider, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt

# Building on top of QMainWindow
class ButtonHolder(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QWidget app!!")
        
        button = QPushButton("Press me!!")
        #self.setCentralWidget(button)
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)
        
        
        
        
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(50)
        #self.setCentralWidget(slider)
        slider.valueChanged.connect(self.respond_to_slider)
        
        button_layout = QVBoxLayout()
        button_layout.addWidget(button)
        button_layout.addWidget(slider)
        
        self.setLayout(button_layout)
        #slider_layout = QHBoxLayout()
        #lider_layout.addWidget(slider)
        
    def button_clicked(self, data):
         print("You clicked the button, didn't you??" , data)


 #class SliderMove(QMainWindow):
    #def __init__(self):
       #super().__init__()
        #self.setWindowTitle("Slider Title app")
    
# slider:
    
        #slider.show()
        ## window.setCentralWidget(slider)

    def respond_to_slider(self, data2):
            print("slider moved to : ", data2)