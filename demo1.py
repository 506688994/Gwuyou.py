# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_MainPage(object):
    def setupUi(self, MainPage):
        MainPage.setObjectName("MainPage")
        MainPage.resize(739, 449)
        self.layoutWidget = QtWidgets.QWidget(MainPage)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 80, 521, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.gridLayout.setObjectName("gridLayout")
        self.driveButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.driveButton.setFont(font)
        self.driveButton.setObjectName("driveButton")
        self.gridLayout.addWidget(self.driveButton, 2, 0, 1, 1)
        self.rangingButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rangingButton.setFont(font)
        self.rangingButton.setObjectName("rangingButton")
        self.gridLayout.addWidget(self.rangingButton, 1, 0, 1, 1)
        self.cameraButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cameraButton.setFont(font)
        self.cameraButton.setObjectName("cameraButton")
        self.gridLayout.addWidget(self.cameraButton, 0, 0, 1, 1)

        self.retranslateUi(MainPage)
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "小车控制器"))
        self.driveButton.setText(_translate("MainPage", "打开电机驱动控制界面"))
        self.rangingButton.setText(_translate("MainPage", "打开超声波测距控制界面"))
        self.cameraButton.setText(_translate("MainPage", "打开摄像头控制界面"))
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainPage()
    ui.setupUi(MainWindow)
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApp