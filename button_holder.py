from PySide6.QtWidgets import QMainWindow, QPushButton

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
        
    