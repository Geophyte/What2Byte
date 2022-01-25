# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(527, 342)
        Main.setWindowOpacity(5.000000000000000)
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.main_button = QPushButton(self.page)
        self.main_button.setObjectName(u"main_button")
        self.main_button.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.main_button)

        self.stackedWidget.addWidget(self.page)
        self.choose = QWidget()
        self.choose.setObjectName(u"choose")
        self.gridLayout_2 = QGridLayout(self.choose)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scan_button_2 = QPushButton(self.choose)
        self.scan_button_2.setObjectName(u"scan_button_2")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_button_2.sizePolicy().hasHeightForWidth())
        self.scan_button_2.setSizePolicy(sizePolicy)
        self.scan_button_2.setMinimumSize(QSize(0, 0))
        self.scan_button_2.setMaximumSize(QSize(16777215, 16777215))
        self.scan_button_2.setIconSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.scan_button_2, 0, 0, 1, 1)

        self.available_receips_button = QPushButton(self.choose)
        self.available_receips_button.setObjectName(u"available_receips_button")
        sizePolicy.setHeightForWidth(self.available_receips_button.sizePolicy().hasHeightForWidth())
        self.available_receips_button.setSizePolicy(sizePolicy)
        self.available_receips_button.setMinimumSize(QSize(0, 0))
        self.available_receips_button.setMaximumSize(QSize(16777215, 16777215))
        self.available_receips_button.setAutoRepeatDelay(300)
        self.available_receips_button.setAutoRepeatInterval(100)

        self.gridLayout_2.addWidget(self.available_receips_button, 0, 1, 1, 1)

        self.storage_button = QPushButton(self.choose)
        self.storage_button.setObjectName(u"storage_button")
        sizePolicy.setHeightForWidth(self.storage_button.sizePolicy().hasHeightForWidth())
        self.storage_button.setSizePolicy(sizePolicy)
        self.storage_button.setMinimumSize(QSize(0, 0))
        self.storage_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.storage_button, 1, 0, 1, 1)

        self.all_recipes_button = QPushButton(self.choose)
        self.all_recipes_button.setObjectName(u"all_recipes_button")
        sizePolicy.setHeightForWidth(self.all_recipes_button.sizePolicy().hasHeightForWidth())
        self.all_recipes_button.setSizePolicy(sizePolicy)
        self.all_recipes_button.setMinimumSize(QSize(0, 0))
        self.all_recipes_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.all_recipes_button, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.choose)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 527, 20))
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Witaj w What2bite !</span></p></body></html>", None))
        self.main_button.setText(QCoreApplication.translate("Main", u"Rozpocznij", None))
        self.scan_button_2.setText(QCoreApplication.translate("Main", u"SKANOWANIE", None))
        self.available_receips_button.setText(QCoreApplication.translate("Main", u"DOST\u0118PNE PRZEPISY", None))
        self.storage_button.setText(QCoreApplication.translate("Main", u"SPI\u017bARNIA", None))
        self.all_recipes_button.setText(QCoreApplication.translate("Main", u"WSZYSTKIE PRZEPISY", None))
    # retranslateUi

