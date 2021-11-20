import datetime
import sys
import net
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject, pyqtSlot, QThread
from ui_MainWindow import Ui_MainWindow
from ConnectionDialog import ConnectionDialog
from ErrorDialog import ErrorDialog


class Communicate(QObject):
    MainFromConnection = pyqtSignal(object)
    MainToError = pyqtSignal(object)
    StopAutoUpdater = pyqtSignal()


class AutoUpdater(QObject):
    running = False
    AutoUpdateTrigger = pyqtSignal()

    def run(self):
        while True:
            self.AutoUpdateTrigger.emit()
            QThread.msleep(7000)

    def stop(self):
        self.terminate()


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(545, 380)
        self.communication = Communicate()

        self.ConnectionDialog = ConnectionDialog()
        self.ConnectionDialog.communication.MainFromConnection.connect(self.set_ip_port)
        self.ErrorDialog = ErrorDialog()
        self.communication.MainToError.connect(self.ErrorDialog.set_error)
        self.IsConnectionWorks = False
        self.ip = str()
        self.port = int()
        self.LastReload = datetime.datetime.now()
        self.Server = None

        self.AutoUpdaterThread = QThread()
        self.AutoUpdater = AutoUpdater()
        self.AutoUpdater.moveToThread(self.AutoUpdaterThread)
        self.AutoUpdater.AutoUpdateTrigger.connect(self.reload)
        self.communication.StopAutoUpdater.connect(self.AutoUpdater.stop)
        self.AutoUpdaterThread.started.connect(self.AutoUpdater.run)

        self.ExitButton.clicked.connect(self.close)
        self.ReconnectButton.clicked.connect(self.on_reconnect)
        self.ReloadButton.clicked.connect(self.reload)
        self.SendButton.clicked.connect(self.send)
        self.on_reconnect()

    def on_reconnect(self):
        self.IsConnectionWorks = False
        self.communication.StopAutoUpdater.emit()
        self.reconnect()
        self.reload()
        self.AutoUpdaterThread.start()

    def reconnect(self):
        self.on_connection_lost()
        while not self.IsConnectionWorks:
            self.ConnectionDialog.exec()
        self.Server = net.OpenLChatClient((self.ip, self.port))
        self.on_connection_back()

    def set_ip_port(self, ip_port):
        if ip_port[0].count('.') == 3 and ip_port[0].replace('.', '').isnumeric() and len(ip_port[0]) <= 16 and len(
                ip_port[1]) <= 5 and ip_port[1].isnumeric():
            self.ip = ip_port[0]
            self.port = int(ip_port[1])
            self.setWindowTitle(f"OpenLChat {self.ip}:{str(self.port)}")
            self.IsConnectionWorks = net.check_connection((self.ip, self.port))
        else:
            self.on_error('Error 1 \nIncorrect IPv4 address or Port.')
            self.IsConnectionWorks = False

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
            code = self.Server.send_message(
                {'name': self.NameEdit.text(), 'message': self.TextLine.text().replace('"', "'")})

            if code == 'success':
                self.reload()
                self.TextLine.clear()
                return
            elif code == 'data_err' or code == 'len_err':
                self.on_error('Unexpected error.')
                self.reload()
            else:
                self.on_error('disconnected.')
                self.on_reconnect()
        else:
            self.on_error('Error 2 \nMessage/name is empty or long')

    @pyqtSlot()
    def reload(self):
        base = self.Server.get_base()
        if type(base) == str:
            self.on_error('disconnected.')
            self.on_reconnect()
            return
        self.MessagesWidget.clear()
        for i in base:
            self.MessagesWidget.addItem(f'[{i["name"]}] - {i["message"]}')
        self.MessagesWidget.scrollToBottom()
        self.LastReload = datetime.datetime.now()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
