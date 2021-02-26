# -*- coding: utf-8 -*-
import sys
import qtawesome
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_OrderSet(object):

    def __init__(self):
        # 参数校准部件（右侧）
        self.orderset_widget = QtWidgets.QWidget()#创建部件
        self.orderset_layout = QtWidgets.QGridLayout()#创建布局
        self.order_view = QtWidgets.QTableWidget(9,1)#创建指令集输入列表
        self.F = ['指令']
        self.orderlist = ['支路mos闭合','支路mos断开','充电mos闭合','充电mos断开','放电mos闭合','放电mos断开','']

    def setupUi(self):
        self.orderset_widget.setLayout(self.orderset_layout)  # 设置主界面布局为网格
        self.orderset_layout.addWidget(self.order_view,0,0,9,12)
        self.order_view.setShowGrid(False)
        self.order_view.setColumnWidth(400,300)
        self.order_view.setHorizontalHeaderLabels(self.F)
        self.order_view.setVerticalHeaderLabels(self.orderlist)
        #self.input_table = self.order_view.item(0, 0).text()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_OrderSet()
    ui.setupUi()
    MainWindow.show()
    sys.exit(app.exec_())