from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from ui_ConnectionDialog import Ui_ConnectionDialog


class Communicate(QObject):
    MainFromConnection = pyqtSignal(object)


class ConnectionDialog(QtWidgets.QDialog, Ui_ConnectionDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(440, 150)
        self.communication = Communicate()
        self.ConnectButton.clicked.connect(self.connect)
        self.ExitButton.clicked.connect(exit)

    def connect(self):
        ip_port = (self.IPLine.text(), self.PortLine.text())
        if sum([int(bool(i)) for i in ip_port]) == 2:
            self.communication.MainFromConnection.emit(ip_port)
            self.close()
