from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_ConnectionWindow import Ui_ConnectionWindow


class ConnectionWidget(QMainWindow, Ui_ConnectionWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

