# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Ui_Files\ui_ErrorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ErrorDialog(object):
    def setupUi(self, ErrorDialog):
        ErrorDialog.setObjectName("ErrorDialog")
        ErrorDialog.resize(300, 120)
        self.pushButton = QtWidgets.QPushButton(ErrorDialog)
        self.pushButton.setGeometry(QtCore.QRect(215, 86, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(ErrorDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 271, 51))
        self.label.setObjectName("label")

        self.retranslateUi(ErrorDialog)
        QtCore.QMetaObject.connectSlotsByName(ErrorDialog)

    def retranslateUi(self, ErrorDialog):
        _translate = QtCore.QCoreApplication.translate
        ErrorDialog.setWindowTitle(_translate("ErrorDialog", "Notification"))
        self.pushButton.setText(_translate("ErrorDialog", "OK"))
        self.label.setText(_translate("ErrorDialog", "ERROR MESSAGE IS HERE"))
