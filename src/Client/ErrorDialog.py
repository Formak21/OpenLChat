from PyQt5 import QtCore, QtWidgets
from ui_ErrorDialog import Ui_ErrorDialog


class ErrorDialog(QtWidgets.QDialog, Ui_ErrorDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
