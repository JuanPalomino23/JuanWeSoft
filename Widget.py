from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QMessageBox")
        
        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)
        
        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)
        
        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)
        
        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)
        
        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)
        
        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)
        
        #################
        button_3A = QPushButton("Click")
        button_3A.clicked.connect(self.button_3A_clicked)
        button_3A.pressed.connect(self.button_3A_pressed)
        button_3A.released.connect(self.button_3A_released)
        
        # set up  the  Layout 
        layout1 = QVBoxLayout()
        layout1.addWidget(button_hard)
        layout1.addWidget(button_critical)
        layout1.addWidget(button_question)
        layout1.addWidget(button_information)
        layout1.addWidget(button_warning)
        layout1.addWidget(button_about)
        
        layout1.addWidget(button_3A)
        
        self.setLayout(layout1)
    
    ### Hard Way
    def button_clicked_hard(self):
        #print("Hard")
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("HARD WAY")
        message.setText("Something happened")
        message.setInformativeText("Do you want to do something about it?")
        message.setIcon(QMessageBox.Icon.Critical)
        message.setStandardButtons(QMessageBox.Ok| QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        
        ret = message.exec()
        if ret == QMessageBox.Ok :
            print("User chose OK")
            
        else : 
            print("User chose Cancel")
            
        
    ### Critical Way : Critical
    def button_clicked_critical(self):
        #print("Critical")
        ret = QMessageBox.critical(self,"Critical Way",
                                   "Critical. Do you want to do something about it!",
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok :
            print("User chose OK")
        else :
            print("User chose Cancel")
        
        
    #### Question    
    def button_clicked_question(self):
        #print("Question")
        ret = QMessageBox.question(self,"Question Way",
                                   "Question. Do you want to do something about it!",
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok :
            print("User chose OK")
        else :
            print("User chose Cancel")
    
    ### Information
    def button_clicked_information(self):
        #print("Information")
        ret = QMessageBox.information(self,"Information Way",
                                   "Information. Do you want to do something about it!",
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok :
            print("User chose OK")
        else :
            print("User chose Cancel")
            
    ### Warning
    def button_clicked_warning(self):
        #print("Warning")
        ret = QMessageBox.warning(self,"Warning Way",
                                   "Warning. Do you want to do something about it!",
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok :
            print("User chose OK")
        else :
            print("User chose Cancel")
    
    ### About
    def button_clicked_about(self):
        #print("About")
        ret = QMessageBox.information(self,"About Way",
                                   "About it. Do you want to do something about it!",
                                    QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok :
            print("User chose OK")
        else :
            print("User chose Cancel")
    
    
    def button_3A_clicked(self):
        print("clicked button_3A")
        
    def button_3A_pressed(self):
        print("pressed button_3A")
        
    def button_3A_released(self):
        print("released button_3A")