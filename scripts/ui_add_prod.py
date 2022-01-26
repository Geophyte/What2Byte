# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_product.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.product = QLabel(Dialog)
        self.product.setObjectName(u"product")
        sizePolicy.setHeightForWidth(self.product.sizePolicy().hasHeightForWidth())
        self.product.setSizePolicy(sizePolicy)
        self.product.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.product)

        self.ok_button = QPushButton(Dialog)
        self.ok_button.setObjectName(u"ok_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.ok_button)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt;\">Dodano:</span></p></body></html>", None))
        self.product.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt;\">TextLabel</span></p></body></html>", None))
        self.ok_button.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

