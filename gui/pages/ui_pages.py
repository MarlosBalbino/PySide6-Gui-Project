""" from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore """

from ctypes import alignment
from copy import deepcopy

from numpy import spacing
from qt_core import *
from gui.widgets.my_widgets import MyFrame


class Ui_application_pages(object):

    object_list = []

    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(622, 515)
        application_pages.setWindowTitle("application_pages")

        self.page_1 = QWidget()
        self.verticalLayout = QVBoxLayout(self.page_1)       
        self.label_3 = QLabel(self.page_1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setText("Divices")
        self.verticalLayout.addWidget(self.label_3)
        application_pages.addWidget(self.page_1)





        self.page_2 = QWidget()

        self.main_Layout = QVBoxLayout(self.page_2)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area_contents = QWidget()
        self.scroll_area_contents_layout = QVBoxLayout(self.scroll_area_contents)       

        self.contents_frame = QFrame(self.scroll_area_contents)
        self.contents_frame.setStyleSheet("background-color: blue")
        #self.contents_frame.setMinimumHeight(2400)
        self.contents_frame.setMinimumWidth(500)
        
        self.spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        self.contents_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
      

        self.scroll_area_contents_layout.addWidget(self.contents_frame)
        self.scroll_area.setWidget(self.scroll_area_contents)
        self.main_Layout.addWidget(self.scroll_area)
    

        self.contents_frame_layout = QVBoxLayout(self.contents_frame)
        self.contents_frame_layout.setSpacing(15)

        self.add_picture_btn = QPushButton("add", parent=self.contents_frame)
        self.add_picture_btn.move(10, 10)
        
        self.add_spacer_btn = QPushButton("spacer", parent=self.contents_frame)
        self.add_spacer_btn.move(10, 50)

        self.remove_picture_btn = QPushButton("remove pic", parent=self.contents_frame)
        self.remove_picture_btn.move(10, 90)

        self.remove_spacer_btn = QPushButton("remove spc", parent=self.contents_frame)
        self.remove_spacer_btn.move(10, 130)

        self.add_picture_btn.clicked.connect(self.add_picture)
        self.add_spacer_btn.clicked.connect(self.add_spacer)
        self.remove_picture_btn.clicked.connect(self.remove_picture)
        self.remove_spacer_btn.clicked.connect(self.remove_spacer)

        





        application_pages.addWidget(self.page_2)

        self.page_3 = QWidget()
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.label = QLabel(self.page_3)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Charts")
        self.verticalLayout_3.addWidget(self.label)
        application_pages.addWidget(self.page_3)

    def add_picture(self):
        self.picture = QFrame()
        self.picture.setMaximumSize(QSize(50, 50))
        self.picture.setMinimumSize(QSize(50, 50))
        self.picture.setStyleSheet("background-color: grey")
        
        self.contents_frame_layout.addWidget(self.picture, alignment=Qt.AlignRight)
        
    def add_spacer(self):
        self.contents_frame_layout.addSpacerItem(self.spacer)

    def remove_spacer(self):
        self.contents_frame_layout.removeItem(self.spacer)

    def remove_picture(self):
        self.picture.deleteLater()