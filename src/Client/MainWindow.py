import datetime
import sys
import net
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject
from ui_MainWindow import Ui_MainWindow
from ConnectionDialog import ConnectionDialog
from ErrorDialog import ErrorDialog


class Communicate(QObject):
    MainFromConnection = pyqtSignal(object)
    MainToError = pyqtSignal(object)


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(505, 354)
        self.communication = Communicate()
        self.ConnectionDialog = ConnectionDialog()
        self.ConnectionDialog.communication.MainFromConnection.connect(self.set_ip_port)
        self.ErrorDialog = ErrorDialog()
        self.communication.MainToError.connect(self.ErrorDialog.set_error)
        self.IsConnectionWorks = False
        self.ip = str()
        self.port = int()
        self.LastReload = datetime.datetime.now()
        self.ExitButton.clicked.connect(self.on_exit)
        self.ReconnectButton.clicked.connect(self.on_reconnect)
        self.ReloadButton.clicked.connect(self.reload)
        self.SendButton.clicked.connect(self.send)
        self.on_reconnect()
        self.reload()
        # self.auto_reload()

    def auto_reload(self):
        while True:
            if datetime.datetime.now() - self.LastReload == datetime.timedelta(seconds=5):
                self.reload()

    def on_reconnect(self):
        self.IsConnectionWorks = False
        self.reconnect()

    def reconnect(self):
        while not self.IsConnectionWorks:
            self.on_connection_lost()
            self.get_ip_port()
        self.Server = net.OpenLChatClient((self.ip, self.port))
        self.on_connection_back()

    def get_ip_port(self):
        self.ConnectionDialog.exec()

    def set_ip_port(self, ip_port):
        if ip_port[0].count('.') == 3 and ip_port[0].replace('.', '').isnumeric() and len(ip_port[0]) <= 16 and len(
                ip_port[1]) <= 5 and ip_port[1].isnumeric():
            self.ip = ip_port[0]
            self.port = int(ip_port[1])
            self.setWindowTitle(f"OpenLChat {self.ip}:{str(self.port)}")
            self.IsConnectionWorks = self.ConnectionChecker()
        else:
            self.on_error('Error 1 \nIncorrect IPv4 address or Port.')
            self.IsConnectionWorks = False

    def ConnectionChecker(self) -> bool:
        return net.check_connection((self.ip, self.port))

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
        self.communication.MainToError.emit(text)
        self.ErrorDialog.exec()

    def send(self):
        if 0 < len(bytearray(self.NameEdit.text(), encoding='utf-8')) <= 16 and 0 < len(
                bytearray(self.TextLine.text(), encoding='utf-8')) <= 256:
            code = self.Server.send_message({'name': self.NameEdit.text(), 'message': self.TextLine.text()})
            if code == 'success':
                return
            elif code == 'data_err' or code == 'len_err':
                self.on_error('Unexpected error.')
            else:
                self.on_error('disconnected.')
                self.on_reconnect()
        else:
            self.on_error('Error 2 \nMessage/name is empty or long')

    def reload(self):
        base = self.Server.get_base()
        if type(base) == str:
            self.on_error('disconnected.')
            self.on_reconnect()
            return
        self.MessagesWidget.clear()
        for i in base:
            self.MessagesWidget.addItem(f'[{i["name"]}] - {i["message"]}')
        self.LastReload = datetime.datetime.now()

    def on_exit(self):
        ex.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
