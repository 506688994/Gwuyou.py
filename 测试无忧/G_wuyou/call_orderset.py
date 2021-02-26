import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *

from HomePages.ui_orderset import Ui_OrderSet


class OrderSetPageWindow(QWidget, Ui_OrderSet):
    # 声明信号
    returnSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(OrderSetPageWindow, self).__init__(parent)
        self.setupUi()
        self.initUI()
    def initUI(self):
        self.setLayout(self.orderset_layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = OrderSetPageWindow()
    mainWindow.show()
    sys.exit(app.exec_())