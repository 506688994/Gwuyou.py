import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *

from HomePages.ui_autotestpage import Ui_AutoTestPage


class AutoTestPageWindow(QWidget, Ui_AutoTestPage):
    # 声明信号
    returnSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(AutoTestPageWindow, self).__init__(parent)
        self.setupUi()
        self.initUI()
    def initUI(self):
        self.setLayout(self.right_layout_auto)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = AutoTestPageWindow()
    mainWindow.show()
    sys.exit(app.exec_())