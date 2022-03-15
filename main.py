import sys
import os
from turtle import width
from qt_core import *

# IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import *


# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ASCADA")

        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Toggle button
        self.ui.toggle_btn.clicked.connect(self.hidden_menu)               
        self.ui.hidden_btn.clicked.connect(self.hidden_menu)        
        self.ui.btn_1.clicked.connect(self.toggle_button)
        
        # EXIBE A APLICAÇÂO
        self.show()

    def toggle_button(self):
        # Get left menu width
        menu_width = self.ui.left_menu.width()

        # Check width
        width = 50
        if menu_width == 50:
            width = 240

        # Start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(150)
        self.animation.start()

    def hidden_menu(self):
        # Get hidden menu width
        menu_width = self.ui.hidden_menu.width()

        # Check width
        width = 0
        if menu_width == 0:
            width = 250
            self.ui.hidden_menu.setFixedWidth(250)
        else:
            self.ui.hidden_menu.setFixedWidth(0)
         
        # Start animation
        # self.animation = QPropertyAnimation(self.ui.hidden_menu, b"minimumWidth")  
        # self.animation.setStartValue(menu_width)
        # self.animation.setEndValue(width)
        # self.animation.setDuration(500)
        # self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        # self.animation.start()

        print(self.ui.hidden_menu.width())

        self.hidden_frame()

    def hidden_frame(self):
        # Get hidden menu width
        menu_width = self.ui.hidden_frame.width()

        # Check width
        width = 0
        if menu_width == 0:
            width = 3840
            self.ui.hidden_frame.setFixedWidth(3840)
        else:
            self.ui.hidden_frame.setFixedWidth(0)    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
