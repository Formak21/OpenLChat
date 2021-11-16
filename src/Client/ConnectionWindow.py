from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject
from ui_ConnectionWindow import Ui_ConnectionWindow
from ErrorDialog import ErrorDialog


class Communicate(QObject):
    MainFromConnection = pyqtSignal(object)


class ConnectionWidget(QMainWindow, Ui_ConnectionWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.communication = Communicate()
        self.ConnectButton.clicked.connect(self.connect)

    def connect(self):
        IpPort = (self.IPLine.text(), self.PortLine.text())
        if sum([int(bool(i)) for i in IpPort]) == 2:
            self.communication.emit(IpPort)
            self.close()
