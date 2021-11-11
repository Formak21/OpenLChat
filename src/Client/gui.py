import sys
import datetime

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainwindow.ui', self)
        self.setFixedSize(280, 210)
        self.pushButton.clicked.connect(self.run)

    def encode(self, text):
        return

    def decode(self, text):
        return

    def send(self):
        name = self.NameLine.text()
        text = self.TextLine.text()
        time = datetime.datetime.now()
        if len(name) > 0 and len(text) > 0:
            pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
