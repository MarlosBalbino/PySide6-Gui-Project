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
        self.ui.toggle_btn.clicked.connect(self.toggle_button)

        # Show pages
        self.ui.btn_1.clicked.connect(self.show_page_1)
        self.ui.btn_2.clicked.connect(self.show_page_2)
        self.ui.btn_3.clicked.connect(self.show_page_3)

        # Open file
        self.ui.btn_4.clicked.connect(self.open_file)

        # Show settings
        self.ui.settings_btn.clicked.connect(self.hidden_menu)

        # LEFT HIDDEN MENU
        self.mw = MyWidgets()
        self.mw.leftHiddenMenu(self.ui.main_frame)

        # Get text button
        self.mw.get_text_btn.clicked.connect(self.get_text)
        self.mw.hidden_btn.clicked.connect(self.hidden_menu)
        
        # EXIBE A APLICAÇÂO
        self.show()

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass
    
    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_1.set_active(True)

    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.set_active(True)

    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.btn_3.set_active(True)

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

    @Slot()
    def hidden_menu(self):
        # Get hidden menu width
        menu_width = self.mw.hidden_menu.width()
        
        self.animation = QPropertyAnimation(self.mw.hidden_menu, b"minimumWidth")   

        # Check width
        if menu_width != 240:
            self.mw.hidden_frame.show()
            self.animation.setStartValue(menu_width)
            self.animation.setEndValue(240)
            self.animation.setDuration(150)
            self.animation.start()
        
        else:
            self.animation.setStartValue(menu_width)
            self.animation.setEndValue(0)
            self.animation.setDuration(150)
            self.animation.finished.connect(self.mw.hidden_frame.hide)
            self.animation.start()

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, "Open_file")
        print(file_name)

    def get_text(self):
        text = self.mw.text_edit.toPlainText()
        print(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
