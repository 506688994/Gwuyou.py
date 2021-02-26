import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QHBoxLayout

from PyQt5.QtCore import Qt, pyqtSignal


class CMainWindow(QMainWindow):
    signalTest = pyqtSignal()
    signalTest1 = pyqtSignal(str)
    signalTest2 = pyqtSignal(float, float)

    def __init__(self):
        super().__init__()
        # 确认PushButton设置
        btn = QPushButton("无参信号")
        btn.clicked.connect(self.buttonClicked)
        btn1 = QPushButton("单参信号")
        btn1.clicked.connect(self.buttonClicked1)
        btn2 = QPushButton('双参信号')
        btn2.clicked.connect(self.buttonClicked2)
        hBox = QHBoxLayout()
        hBox.addStretch(1)
        hBox.addWidget(btn)
        hBox.addWidget(btn1)
        hBox.addWidget(btn2)
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(hBox)
        self.signalTest.connect(self.signalNone)
        self.signalTest1.connect(self.signalOne)
        self.signalTest2.connect(self.signalTwo)
        self.setWindowTitle('pysignal的使用')
        self.show()

    def signalNone(self):
        print("无参信号，传来的信息")

    def signalOne(self, arg1):
        print("单参信号，传来的信息:")
        print(bytes.fromhex('ff'))

    def signalTwo(self, arg1, arg2):
        print("双参信号，传来的信息:", arg1, arg2)

    def mousePressEvent(self, event):
        self.signalTest2.emit(event.pos().x(), event.pos().y())

    def buttonClicked(self):
        self.signalTest.emit()

    def buttonClicked1(self):
        self.signalTest1.emit("我是单参信号传来的")

    def buttonClicked2(self):
        self.signalTest2.emit(0, 0)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = CMainWindow()
    sys.exit(app.exec_())


