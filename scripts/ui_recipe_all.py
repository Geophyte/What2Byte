
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_all.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RecipeAllWindow(object):
    def setupUi(self, RecipeAllWindow):
        if not RecipeAllWindow.objectName():
            RecipeAllWindow.setObjectName(u"RecipeAllWindow")
        RecipeAllWindow.resize(567, 400)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RecipeAllWindow.sizePolicy().hasHeightForWidth())
        RecipeAllWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(RecipeAllWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_2 = QHBoxLayout(self.page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.recipe_list = QListWidget(self.page)
        self.recipe_list.setObjectName(u"recipe_list")

        self.verticalLayout_2.addWidget(self.recipe_list)

        self.email_button = QPushButton(self.page)
        self.email_button.setObjectName(u"email_button")
        self.email_button.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.email_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.recipe_text = QLabel(self.page)
        self.recipe_text.setObjectName(u"recipe_text")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.recipe_text.sizePolicy().hasHeightForWidth())
        self.recipe_text.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.recipe_text)

        self.close_button = QPushButton(self.page)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.close_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(0, 50))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.mail_adress = QLineEdit(self.page_2)
        self.mail_adress.setObjectName(u"mail_adress")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mail_adress.sizePolicy().hasHeightForWidth())
        self.mail_adress.setSizePolicy(sizePolicy3)
        self.mail_adress.setMinimumSize(QSize(0, 50))
        self.mail_adress.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.mail_adress)

        self.send_button = QPushButton(self.page_2)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setMinimumSize(QSize(0, 50))

        self.verticalLayout_3.addWidget(self.send_button)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        RecipeAllWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(RecipeAllWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 567, 20))
        RecipeAllWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(RecipeAllWindow)
        self.statusbar.setObjectName(u"statusbar")
        RecipeAllWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RecipeAllWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RecipeAllWindow)
    # setupUi

    def retranslateUi(self, RecipeAllWindow):
        RecipeAllWindow.setWindowTitle(QCoreApplication.translate("RecipeAllWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("RecipeAllWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">LISTA PRZEPIS\u00d3W</span></p></body></html>", None))
        self.email_button.setText(QCoreApplication.translate("RecipeAllWindow", u"PRZE\u015aLIJ BRAKUJ\u0104CE SK\u0141ADNIKI NA MAIL", None))
        self.label_2.setText(QCoreApplication.translate("RecipeAllWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">WYBRANY PRZEPIS</span></p></body></html>", None))
        self.recipe_text.setText("")
        self.close_button.setText(QCoreApplication.translate("RecipeAllWindow", u"ZAKO\u0143CZ", None))
        self.label_3.setText(QCoreApplication.translate("RecipeAllWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">PODAJ MAIL</span></p></body></html>", None))
        self.mail_adress.setPlaceholderText(QCoreApplication.translate("RecipeAllWindow", u"MAIL", None))
        self.send_button.setText(QCoreApplication.translate("RecipeAllWindow", u"PRZE\u015aLIJ", None))
    # retranslateUi

