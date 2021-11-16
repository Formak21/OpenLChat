import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject
from ui_MainWindow import Ui_MainWindow
from ConnectionWindow import ConnectionWidget
from ErrorDialog import ErrorDialog

class Communicate(QObject):
    MainFromConnection = pyqtSignal(object)


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(505, 354)
        self.communication = Communicate()
        self.ip = str()
        self.port = int()
        self.ExitButton.clicked.connect(self.on_exit)
        self.on_connection_lost()
        self.get_ip_port()
        self.setWindowTitle(f"OpenLChat {self.ip}:{str(self.port)}")

    def get_ip_port(self):
        self.Connection = ConnectionWidget()
        self.Connection.show()
        self.Connection.communication.MainFromConnection.connect(self.set_ip_port)

    def set_ip_port(self, ip_port):
        ip = ip_port[0]
        port = int(ip_port[1])

    def on_connection_lost(self):
        self.ReloadButton.setDisabled(True)
        self.SendButton.setDisabled(True)
        self.MessagesWidget.clear()
        self.MessagesWidget.setDisabled(True)
        self.NameEdit.setDisabled(True)
        self.TextLine.setDisabled(True)

    def on_connection_back(self):
        self.ReloadButton.setDisabled(False)
        self.SendButton.setDisabled(False)
        self.MessagesWidget.setDisabled(False)
        self.NameEdit.setDisabled(False)
        self.TextLine.setDisabled(False)
        self.MessagesWidget.clear()

    def on_error(self, text):
        pass

    def send(self):
        pass

    def reload(self):
        pass

    def on_exit(self):
        ex.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
