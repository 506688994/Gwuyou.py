import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from HomePages.ui_loginpage import LogIn


class LoginPageWindow(QWidget, LogIn):
    # 声明信号
    returnSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(LoginPageWindow, self).__init__(parent)
        self.Login_Ui(self)
        self.initUI()

    def initUI(self):
        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = LoginPageWindow()
    mainWindow.show()
    sys.exit(app.exec_())
