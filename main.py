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

        self.animation_thread = QThread()

        self.animation_show = QPropertyAnimation(self.ui.hidden_menu, b"minimumWidth")
        self.animation_show.moveToThread(self.animation_thread)    
        self.animation_show.setStartValue(0)
        self.animation_show.setEndValue(250)
        self.animation_show.setDuration(150)    
        self.animation_hide = QPropertyAnimation(self.ui.hidden_menu, b"minimumWidth")
        self.animation_hide.moveToThread(self.animation_thread)
        
        self.animation_hide.setStartValue(250)
        self.animation_hide.setEndValue(0)
        self.animation_hide.setDuration(150)
        self.animation_hide.finished.connect(self.ui.hidden_frame.hide)

        self.animation_thread.start()

        # Toggle button               
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
        
        # Check width
        if menu_width != 250:            
            self.animation_show.start()
        
        else:    
            self.animation_hide.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
