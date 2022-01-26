# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_available.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RecipeAvailableWindow(object):
    def setupUi(self, RecipeAvailableWindow):
        if not RecipeAvailableWindow.objectName():
            RecipeAvailableWindow.setObjectName(u"RecipeAvailableWindow")
        RecipeAvailableWindow.resize(563, 378)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RecipeAvailableWindow.sizePolicy().hasHeightForWidth())
        RecipeAvailableWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(RecipeAvailableWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.recipe_list = QListWidget(self.centralwidget)
        self.recipe_list.setObjectName(u"recipe_list")

        self.verticalLayout.addWidget(self.recipe_list)

        self.done_button = QPushButton(self.centralwidget)
        self.done_button.setObjectName(u"done_button")
        self.done_button.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.done_button)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.recipe_text = QLabel(self.centralwidget)
        self.recipe_text.setObjectName(u"recipe_text")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.recipe_text.sizePolicy().hasHeightForWidth())
        self.recipe_text.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.recipe_text)

        self.close_button = QPushButton(self.centralwidget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.close_button)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        RecipeAvailableWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(RecipeAvailableWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 563, 20))
        RecipeAvailableWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(RecipeAvailableWindow)
        self.statusbar.setObjectName(u"statusbar")
        RecipeAvailableWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RecipeAvailableWindow)

        QMetaObject.connectSlotsByName(RecipeAvailableWindow)
    # setupUi

    def retranslateUi(self, RecipeAvailableWindow):
        RecipeAvailableWindow.setWindowTitle(QCoreApplication.translate("RecipeAvailableWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("RecipeAvailableWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">LISTA PRZEPIS\u00d3W</span></p></body></html>", None))
        self.done_button.setText(QCoreApplication.translate("RecipeAvailableWindow", u"ROBI\u0118", None))
        self.label_2.setText(QCoreApplication.translate("RecipeAvailableWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">WYBRANY PRZEPIS</span></p></body></html>", None))
        self.recipe_text.setText("")
        self.close_button.setText(QCoreApplication.translate("RecipeAvailableWindow", u"ZAKO\u0143CZ", None))
    # retranslateUi

