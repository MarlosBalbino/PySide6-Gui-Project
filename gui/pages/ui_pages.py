""" from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore """

from ctypes import alignment
from qt_core import *


class Ui_application_pages(object):
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
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.label_2 = QLabel(self.page_2)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setText("ASCADA")
        self.verticalLayout_2.addWidget(self.label_2)
        application_pages.addWidget(self.page_2)

        self.page_3 = QWidget()
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.label = QLabel(self.page_3)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Charts")
        self.verticalLayout_3.addWidget(self.label)
        application_pages.addWidget(self.page_3)

        # QMetaObject.connectSlotsByName(application_pages)
    # setupUi
