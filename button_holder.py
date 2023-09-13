from PySide6.QtWidgets import QMainWindow, QSlider, QPushButton
from PySide6.QtCore import Qt

# Building on top of QMainWindow
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Button Holder app!!")
        
        def button_clicked(data):
         print("You clicked the button, didn't you??" , data)
         
        
        button = QPushButton("Press me!!")
        self.setCentralWidget(button)
        button.setCheckable(True)
        
        button.clicked.connect(button_clicked)



class SliderMove(QMainWindow):
    def __init__(self):
        super().__init__()
        
        def respond_to_slider(data2):
            print("slider moved to : ", data2)
    
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(50)
        self.setCentralWidget(slider)

        slider.valueChanged.connect(respond_to_slider)
    
        #slider.show()
        ## window.setCentralWidget(slider)

    