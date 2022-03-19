from ctypes import alignment
from qt_core import *
from gui.widgets.py_push_button import PyPushButton


class MyWidgets(object):

    def leftHiddenMenu(self, parent):
        # LEFT HIDDEN MENU
        #////////////////////////////////////////////////////////////////////
        # HIDDEN FRAME
        self.hidden_frame = QFrame(parent=parent)
        self.hidden_frame.setStyleSheet("background-color: transparent")
        self.hidden_frame.setMaximumWidth(3840)
        self.hidden_frame.setMinimumWidth(3840)
        self.hidden_frame.setMinimumHeight(2160)
        self.hidden_frame.hide()

        # HIDDEN FRAME LAYOUT
        self.hidden_layout = QHBoxLayout(self.hidden_frame)
        self.hidden_layout.setContentsMargins(0,0,0,0)
        self.hidden_layout.setSpacing(0)

        # HIDDEN MENU
        self.hidden_menu = QFrame()
        self.hidden_menu.setStyleSheet("background-color: #44475a")
        self.hidden_menu.setMaximumWidth(0)
        self.hidden_menu.setMinimumWidth(0)
        self.hidden_menu.setMaximumHeight(2160)

        # TEXT BOX
        self.text_edit = QTextEdit(self.hidden_menu)
        self.text_edit.setStyleSheet("color: white; font-size: 12pt")
        self.text_edit.setAcceptRichText(False)
        self.text_edit.move(10,10)
        self.text_edit.setMaximumWidth(220)
        self.text_edit.setMinimumHeight(360)
        self.text_edit.setMaximumHeight(720)

        # GET TEXT BTN
        self.get_text_btn = PyPushButton(
            text = "Get Text", 
            parent = self.hidden_menu, 
            icon_path = "widgets_icon.svg"
        )        
        self.get_text_btn.move(180, 380)
        self.get_text_btn.setFixedSize(50, 50)

        # HIDDEN BTN FRAME
        self.hidden_btn_frame = QFrame()
        self.hidden_btn_frame.setStyleSheet("background-color: transparent")
        self.hidden_btn_frame.setMaximumHeight(2160)

        # HIDDEN BTN
        self.hidden_btn = QPushButton(self.hidden_btn_frame)
        self.hidden_btn.setStyleSheet("background-color: transparent")
        self.hidden_btn.setFixedSize(3840, 3840)
        
        # ADD HIDDEN BTN TO HIDDEN FRAME
        self.hidden_layout.addWidget(self.hidden_menu)
        self.hidden_layout.addWidget(self.hidden_btn_frame)