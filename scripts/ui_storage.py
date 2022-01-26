# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'storage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StorageWindow(object):
    def setupUi(self, StorageWindow):
        if not StorageWindow.objectName():
            StorageWindow.setObjectName(u"StorageWindow")
        StorageWindow.resize(800, 600)
        self.centralwidget = QWidget(StorageWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.storage = QListWidget(self.centralwidget)
        self.storage.setObjectName(u"storage")

        self.verticalLayout.addWidget(self.storage)

        self.close_button = QPushButton(self.centralwidget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(0, 70))

        self.verticalLayout.addWidget(self.close_button)

        StorageWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(StorageWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        StorageWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(StorageWindow)
        self.statusbar.setObjectName(u"statusbar")
        StorageWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StorageWindow)

        QMetaObject.connectSlotsByName(StorageWindow)
    # setupUi

    def retranslateUi(self, StorageWindow):
        StorageWindow.setWindowTitle(QCoreApplication.translate("StorageWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("StorageWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">SPI\u017bARNIA</span></p></body></html>", None))
        self.close_button.setText(QCoreApplication.translate("StorageWindow", u"ZAMKNIJ", None))
    # retranslateUi

