import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5.QtCore import QThread, pyqtSignal


class UI_LoginBar(QWidget):
    def __init__(self, parent=None):
        super(UI_LoginBar, self).__init__(parent)
        self.pushButton = QPushButton(self)
        self.setupUi()
        self.pushButton.clicked.connect(self.run)
        self.pushButton2.clicked.connect(self.run)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(500, 300)  # 设置大小
        self.setWindowTitle("XX登录界面")  # 设置标题
        self.setFixedSize(self.width(), self.height())  # 禁止最大化
        icon = QIcon()
        icon.addPixmap(QPixmap("..\\Image\\10.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)  # 设置窗口的图标
        self.pushButton.setGeometry(135, 230, 230, 30)
        self.pushButton2 = QPushButton(self)
        self.pushButton2.setGeometry(135, 265, 230, 30)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("登录")
        self.lable = QLabel(self)
        self.lable.setGeometry(75, 100, 350, 50)
        self.movie = QMovie("1.gif")

    def run(self):
        self.lable.setMovie(self.movie)
        if self.sender() == self.pushButton:
            self.movie.start()
        else:
            self.movie.stop()
            self.lable.setPixmap(QPixmap(""))


"""
class Thread(QThread):
    _signal = pyqtSignal(bool)
    def __init__(self, parent=None):
        super(Thread, self).__init__(parent)
        self.working = True
    def __del__(self):
        self.wait()
        self.working = False
    def run(self):
        # 线程相关代码
        while self.working is True:
            self._signal.emit(True)
            self.sleep(0.8)
            self._signal.emit(False)
            self.sleep(0.8)
class UI_LoginBar(QWidget):
    def __init__(self, parent=None):
        super(UI_LoginBar, self).__init__(parent)
        self.setupUi()
        #self.Runthread()
        # 创建一个新的线程
        self.pushButton.clicked.connect(self.Runthread)
        self.pushButton2.clicked.connect(lambda: self.thread.terminate())
    def Runthread(self):
        self.thread = Thread()
        self.thread._signal.connect(self.callback)
        self.thread.start()
    def threadstop(self):
        self.thread.terminate()
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(500, 300)  # 设置大小
        self.setWindowTitle("XX登录界面")  # 设置标题
        self.setFixedSize(self.width(), self.height())  # 禁止最大化
        icon = QIcon()
        icon.addPixmap(QPixmap("..\\Image\\10.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)  # 设置窗口的图标
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(135, 230, 230, 30)
        self.pushButton2 = QPushButton(self)
        self.pushButton2.setGeometry(135, 280, 230, 30)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("登录")
        self.lable = QLabel(self)
        self.lable.setGeometry(75, 100, 350, 50)
        self.png = QPixmap("..\\Image\\1.png")
        self.png2 = QPixmap("..\\Image\\2.png")
    def callback(self, status):
        if status is True:
            self.lable.setPixmap(self.png)
        elif status is False:
            self.lable.setPixmap(self.png2)
        else:
            self.lable.setPixmap(QPixmap(""))
# ==========================================================================
# * Founction Name    :   ModuleInit
# * Parameter         :   None
# * Return            :   None
# * Description       :   为当前模块设置Log头，方便识别，以及其他初始化设置
# ==========================================================================
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI_LoginBar()
    ui.show()
    sys.exit(app.exec_())
