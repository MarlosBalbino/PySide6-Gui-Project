import sys
import os
import time
import threading
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
        #self.ui.toggle_btn.clicked.connect(self.toggle_button)          
        self.ui.toggle_btn.clicked.connect(self.hidden_menu)        
        self.ui.hidden_btn.clicked.connect(self.hidden_menu)
        
        # EXIBE A APLICAÇÂO
        self.show()

    # def toggle_button(self):
    #     # Get left menu width
    #     menu_width = self.ui.left_menu.width()

    #     # Check width
    #     width = 50
    #     if menu_width == 50:
    #         width = 240

    #     # Start animation
    #     self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
    #     self.animation.setStartValue(menu_width)
    #     self.animation.setEndValue(width)
    #     self.animation.setDuration(150)
    #     self.animation.start()

    @Slot()
    def hidden_menu(self):
        # Get hidden menu width
        menu_width = self.ui.hidden_menu.width()
        
        self.animation = QPropertyAnimation(self.ui.hidden_menu, b"minimumWidth")   

        # Check width
        if menu_width != 250:
            self.ui.hidden_frame.show()
            self.animation.setStartValue(menu_width)
            self.animation.setEndValue(250)
            self.animation.setDuration(150)
            self.animation.start()
        
        else:
            self.animation.setStartValue(menu_width)
            self.animation.setEndValue(0)
            self.animation.setDuration(150)
            self.animation.finished.connect(self.ui.hidden_frame.hide)
            self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
