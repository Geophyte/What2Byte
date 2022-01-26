# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scan.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ScanWindow(object):
    def setupUi(self, ScanWindow):
        if not ScanWindow.objectName():
            ScanWindow.setObjectName(u"ScanWindow")
        ScanWindow.resize(636, 425)
        self.centralwidget = QWidget(ScanWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.code = QLineEdit(self.page)
        self.code.setObjectName(u"code")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.code.sizePolicy().hasHeightForWidth())
        self.code.setSizePolicy(sizePolicy1)
        self.code.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.code)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.corfirm_button1 = QPushButton(self.page)
        self.corfirm_button1.setObjectName(u"corfirm_button1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.corfirm_button1.sizePolicy().hasHeightForWidth())
        self.corfirm_button1.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.corfirm_button1)

        self.sub_button = QPushButton(self.page)
        self.sub_button.setObjectName(u"sub_button")
        sizePolicy2.setHeightForWidth(self.sub_button.sizePolicy().hasHeightForWidth())
        self.sub_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.sub_button)

        self.close_button = QPushButton(self.page)
        self.close_button.setObjectName(u"close_button")
        sizePolicy2.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.close_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 50))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.stackedWidget_2 = QStackedWidget(self.page_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.category_0 = QListWidget(self.page_3)
        self.category_0.setObjectName(u"category_0")

        self.verticalLayout_5.addWidget(self.category_0)

        self.stackedWidget_2.addWidget(self.page_3)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_6 = QVBoxLayout(self.page_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.category_1 = QListWidget(self.page_5)
        self.category_1.setObjectName(u"category_1")

        self.verticalLayout_6.addWidget(self.category_1)

        self.stackedWidget_2.addWidget(self.page_5)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_7 = QVBoxLayout(self.page_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.category_2 = QListWidget(self.page_4)
        self.category_2.setObjectName(u"category_2")

        self.verticalLayout_7.addWidget(self.category_2)

        self.stackedWidget_2.addWidget(self.page_4)

        self.verticalLayout_2.addWidget(self.stackedWidget_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(0, 50))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.amount = QSpinBox(self.page_2)
        self.amount.setObjectName(u"amount")
        sizePolicy2.setHeightForWidth(self.amount.sizePolicy().hasHeightForWidth())
        self.amount.setSizePolicy(sizePolicy2)
        self.amount.setAlignment(Qt.AlignCenter)
        self.amount.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.amount.setMaximum(100000)
        self.amount.setSingleStep(10)
        self.amount.setValue(500)
        self.amount.setDisplayIntegerBase(10)

        self.verticalLayout_3.addWidget(self.amount)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.corfirm_button2 = QPushButton(self.page_2)
        self.corfirm_button2.setObjectName(u"corfirm_button2")
        sizePolicy2.setHeightForWidth(self.corfirm_button2.sizePolicy().hasHeightForWidth())
        self.corfirm_button2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.corfirm_button2)

        self.sub_button_2 = QPushButton(self.page_2)
        self.sub_button_2.setObjectName(u"sub_button_2")
        sizePolicy2.setHeightForWidth(self.sub_button_2.sizePolicy().hasHeightForWidth())
        self.sub_button_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.sub_button_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        ScanWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ScanWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 636, 20))
        ScanWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ScanWindow)
        self.statusbar.setObjectName(u"statusbar")
        ScanWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ScanWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ScanWindow)
    # setupUi

    def retranslateUi(self, ScanWindow):
        ScanWindow.setWindowTitle(QCoreApplication.translate("ScanWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("ScanWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">SKANOWANIE</span></p></body></html>", None))
        self.code.setPlaceholderText(QCoreApplication.translate("ScanWindow", u"KOD KRESKOWY", None))
        self.corfirm_button1.setText(QCoreApplication.translate("ScanWindow", u"DODAJ", None))
        self.sub_button.setText(QCoreApplication.translate("ScanWindow", u"USU\u0143", None))
        self.close_button.setText(QCoreApplication.translate("ScanWindow", u"ZAKO\u0143CZ", None))
        self.label_2.setText(QCoreApplication.translate("ScanWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">W BAZIE NIE MA TAKIEGO KODU</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("ScanWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">WYBIERZ KATEGORI\u0118</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("ScanWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">ILO\u015a\u0106</span></p></body></html>", None))
        self.corfirm_button2.setText(QCoreApplication.translate("ScanWindow", u"DODAJ", None))
        self.sub_button_2.setText(QCoreApplication.translate("ScanWindow", u"USU\u0143", None))
    # retranslateUi

