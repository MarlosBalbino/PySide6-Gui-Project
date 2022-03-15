from ctypes import alignment
from qt_core import *

# IMPORT PAGES
from gui.pages.ui_pages import Ui_application_pages

# IMPORT CUSTOM WIDGETS
from gui.widgets.py_push_button import PyPushButton

import random

#IMPORT PAGES
from gui.pages.ui_pages import Ui_application_pages 

# MAIN WINDOW
class UI_MainWindow(object):

    
    # @Slot()
    # def magic(self):
    #     self.text.setText(random.choice(['sla', 'test', 'mano']))
    #     print('TESTE')

    def setup_ui(self, parent):
        
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        # SET INCINALS PARAMETERS
        parent.resize(1200, 720)
        parent.setMinimumSize(480, 360)

       
        # CREATE MAIN FRAME
        self.main_frame = QFrame()

        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.main_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

         # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        # self.central_frame.setStyleSheet("background-color: #282a36")

        self.extern_layout = QVBoxLayout(self.central_frame)
        self.extern_layout.setContentsMargins(0,0,0,0)
        self.extern_layout.setSpacing(0)

        # LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMinimumWidth(50)
        self.left_menu.setMaximumWidth(50)

        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)

        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        self.left_menu_top_frame.setStyleSheet("#left_menu_top_frame { background-color: red; }")
        
        # TOP FRAME MENU LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)

        # PUSH BTNS
        self.toggle_btn = QPushButton("Toggle")
        self.btn_1 = QPushButton("btn_1")
        self.btn_2 = QPushButton("btn_2")

        # ADD PUSH BTNS TO LAOUT
        self.left_menu_top_layout.addWidget(self.toggle_btn)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)

        # MENU SPACER
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # BOTTOM FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        self.left_menu_bottom_frame.setStyleSheet("#left_menu_bottom_frame { background-color: red }")
        
        # BOTTOM FRAME MENU LAYOUT
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bottom_layout.setSpacing(0)

        # PUSH SETTINGS BTN
        self.settings_btn = QPushButton("settings")

        # ADD PUSH BTN CONFIG TO LAYOUT
        self.left_menu_bottom_layout.addWidget(self.settings_btn)

        # LABEL VERSION
        self.left_menu_label_version = QLabel("v1.0")
        self.left_menu_label_version.setStyleSheet("color: #c3ccdf") 
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(15)
        self.left_menu_label_version.setMaximumHeight(15)

        # ADD TO LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMaximumHeight(25)
        self.top_bar.setMinimumHeight(25)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(5,0,5,0)

        # left label
        self.top_left_label = QLabel("Maciel Viado")

        # spacer
        self.spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # right label
        self.top_right_label = QLabel("Divices")
        self.top_right_label.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # add labels to top bar layout
        self.top_bar_layout.addWidget(self.top_left_label)
        self.top_bar_layout.addSpacerItem(self.spacer)
        self.top_bar_layout.addWidget(self.top_right_label)

        # APPLICATION PAGES
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_1)



        # ///////////////////////////////////////////////////////////////////
        # PUSH BUTTON
        # self.button = QPushButton("Clique aki, carai!!!")
        # self.text = QLabel("Hello World",
        #                     alignment=Qt.AlignCenter)
        # self.text.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        # self.left_bar_layout = QVBoxLayout(self.left_menu)
        # self.left_bar_layout.addWidget(self.button)
        # self.left_bar_layout.addWidget(self.text)
        # self.button.clicked.connect(self.magic)
        # ///////////////////////////////////////////////////////////////////

        

        # BOTTOM BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMaximumHeight(15)
        self.bottom_bar.setMinimumHeight(15)
        # self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.bottom_bar.setStyleSheet("background-color: #343644; color: #6272a4")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(5,0,5,0)

        # left label
        self.bottom_left_label = QLabel("MBN Enterprises")

        # spacer
        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # right label
        self.bottom_right_label = QLabel("© 2022")

        # add labels to top bar layout
        self.bottom_bar_layout.addWidget(self.bottom_left_label)
        self.bottom_bar_layout.addSpacerItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_right_label)

        # ADD WIDGETS TO CONTENT LAYOUT
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)

        # ADD WIDGETS TO MAIN FRAME LAYOUT        
        self.main_layout.addWidget(self.left_menu)        
        self.main_layout.addWidget(self.content) 

        # HIDDEN FRAME
        self.hidden_frame = QFrame(parent=self.main_frame)
        self.hidden_frame.setStyleSheet("background-color: transparent")
        # self.hidden_meunu.setMinimumWidth(55)
        self.hidden_frame.setMaximumWidth(0)
        self.hidden_frame.setMinimumHeight(2160)

        # HIDDEN MENU
        self.hidden_menu = QFrame(parent=self.main_frame)
        self.hidden_menu.setStyleSheet("background-color: #44475a")
        self.hidden_menu.setMaximumWidth(0)
        self.hidden_menu.setMinimumHeight(2160)

        # HIDDEN FRAME LAYOUT
        self.hidden_layout = QHBoxLayout(self.hidden_frame)
        self.hidden_layout.setContentsMargins(0,0,0,0)
        self.hidden_layout.setSpacing(0)

        # HIDDEN BTN
        self.hidden_btn = QPushButton()
        self.hidden_btn.setStyleSheet("background-color: transparent")
        self.hidden_btn.setFixedSize(3840, 2160)
        
        # ADD HIDDEN BTN TO HIDDEN FRAME
        self.hidden_layout.addWidget(self.hidden_btn)
        
        
        
        # ADD WIDGETS TO CENTRAL FRAME
        self.extern_layout.addWidget(self.main_frame)
        self.extern_layout.addWidget(self.bottom_bar)

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)
        
