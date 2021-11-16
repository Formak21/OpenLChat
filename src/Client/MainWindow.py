import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_MainWindow import Ui_MainWindow
from ConnectionWindow import ConnectionWidget
from ErrorDialog import ErrorDialog

class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(505, 354)
        self.ExitButton.clicked.connect(self.exit)
        self.on_connection_lost()
        self.Connection = ConnectionWidget()
        self.Connection.show()


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

    def exit(self):
        ex.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
