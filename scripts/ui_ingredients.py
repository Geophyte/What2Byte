# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ingredients.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DoneDialog(object):
    def setupUi(self, DoneDialog):
        if not DoneDialog.objectName():
            DoneDialog.setObjectName(u"DoneDialog")
        DoneDialog.resize(415, 383)
        self.verticalLayout = QVBoxLayout(DoneDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DoneDialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.ingredients = QLabel(DoneDialog)
        self.ingredients.setObjectName(u"ingredients")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ingredients.sizePolicy().hasHeightForWidth())
        self.ingredients.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.ingredients)

        self.close_Button = QPushButton(DoneDialog)
        self.close_Button.setObjectName(u"close_Button")
        self.close_Button.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.close_Button)


        self.retranslateUi(DoneDialog)

        QMetaObject.connectSlotsByName(DoneDialog)
    # setupUi

    def retranslateUi(self, DoneDialog):
        DoneDialog.setWindowTitle(QCoreApplication.translate("DoneDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DoneDialog", u"USUNI\u0118TO", None))
        self.ingredients.setText(QCoreApplication.translate("DoneDialog", u"TextLabel", None))
        self.close_Button.setText(QCoreApplication.translate("DoneDialog", u"ZAMKNIJ", None))
    # retranslateUi

