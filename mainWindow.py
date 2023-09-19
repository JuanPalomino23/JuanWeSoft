from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon 
from Widget import Widget

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app # Declare an app member
        self.setWindowTitle("Custom MainWindow")
        
         
        ##Menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("file")
        #file_menu.addAction("Quit")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)
        
        
        
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        
        #a brunch of other menu options jus for the fun of it
        Window_menu = menu_bar.addMenu("Window")
        Setting_menu = menu_bar.addMenu("Settings")
        Help_menu = menu_bar.addMenu("Help")
        
        # Working with toolbars
        toolbar = QToolBar("My main toobal") 
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        
        Quitaction = QAction(QIcon("QuitAction.png"), "Quit action",self)
        
        Quitaction.triggered.connect(self.quit_app)
        
        toolbar.addAction(Quitaction)### Add toolbar action
        
        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        
        toolbar.addAction(action1)### Add toolbar action
        
        action2 = QAction(QIcon("SomeAction.png"),"Some Action", self)
        action2.setStatusTip("Status message for some action")
        action2.triggered.connect(self.toolbar_button_click)
        action2.setCheckable(True)
        
        toolbar.addAction(action2)### Add toolbar action
        
        #### Add separator in toolbaar
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton('Clik here'))
        
        
        #Working  with statusBar
        self.setStatusBar(QStatusBar(self))
        
        #button1 = QPushButton("Butoon 1")
        #button1.clicked.connect(self.button1_clicked)
        #self.setCentralWidget(button1)
        
        Widget1 = Widget()
        self.setCentralWidget(Widget1)
        
        
        
    #def button1_clicked(self):
    #    self.statusBar().showMessage("Button1 clicked", 1000)
         
    def quit_app(self):
        self.app.quit()
        
    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app",1000)