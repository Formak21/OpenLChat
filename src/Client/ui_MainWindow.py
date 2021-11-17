# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Ui_Files\ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SendButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendButton.setGeometry(QtCore.QRect(430, 330, 95, 30))
        self.SendButton.setAutoDefault(True)
        self.SendButton.setDefault(True)
        self.SendButton.setObjectName("SendButton")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(430, 20, 95, 30))
        self.ExitButton.setObjectName("ExitButton")
        self.ReloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReloadButton.setGeometry(QtCore.QRect(430, 80, 95, 30))
        self.ReloadButton.setObjectName("ReloadButton")
        self.NameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NameEdit.setGeometry(QtCore.QRect(20, 330, 80, 30))
        self.NameEdit.setObjectName("NameEdit")
        self.TextLine = QtWidgets.QLineEdit(self.centralwidget)
        self.TextLine.setGeometry(QtCore.QRect(110, 330, 310, 30))
        self.TextLine.setObjectName("TextLine")
        self.MessagesWidget = QtWidgets.QListWidget(self.centralwidget)
        self.MessagesWidget.setGeometry(QtCore.QRect(20, 20, 400, 290))
        self.MessagesWidget.setMovement(QtWidgets.QListView.Static)
        self.MessagesWidget.setObjectName("MessagesWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 315, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 315, 55, 13))
        self.label_2.setObjectName("label_2")
        self.ReconnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReconnectButton.setGeometry(QtCore.QRect(430, 50, 95, 30))
        self.ReconnectButton.setObjectName("ReconnectButton")
        self.neko = QtWidgets.QLabel(self.centralwidget)
        self.neko.setGeometry(QtCore.QRect(420, 110, 125, 230))
        self.neko.setText("")
        self.neko.setPixmap(QtGui.QPixmap("pixelneko.png"))
        self.neko.setScaledContents(True)
        self.neko.setObjectName("neko")
        self.neko.raise_()
        self.SendButton.raise_()
        self.ExitButton.raise_()
        self.ReloadButton.raise_()
        self.NameEdit.raise_()
        self.TextLine.raise_()
        self.MessagesWidget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.ReconnectButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IP:Port OpenLChat"))
        self.SendButton.setText(_translate("MainWindow", "Send"))
        self.SendButton.setShortcut(_translate("MainWindow", "Return"))
        self.ExitButton.setText(_translate("MainWindow", "Exit"))
        self.ReloadButton.setText(_translate("MainWindow", "Reload"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "Message:"))
        self.ReconnectButton.setText(_translate("MainWindow", "Reconnect"))
