# -*- coding: utf-8 -*-
import sys

import serial
import serial.tools.list_ports
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from HomePages.ui_setcompage import Ui_SetComPage


class SetComPageWindow(QWidget, Ui_SetComPage):
    SetCom_Signal1 = pyqtSignal()
    SetCom_Signal2 = pyqtSignal()

    def __init__(self, parent=None):
        super(SetComPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.refresh_serial()
        self.initUI()

    def initUI(self):
        # 设置布局
        self.setLayout(self.right_layout_com)
        self.right_com_button_com1.clicked.connect(lambda: self.SetCom_Signal1.emit())  # 打开串口一
        self.right_com_button_com2.clicked.connect(lambda: self.SetCom_Signal2.emit())  # 打开串口二
        self.right_com_button_star.clicked.connect(self.refresh_serial)  # 刷新串口列表


    def refresh_serial(self):
        # refresh Serial #
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.com1_com.clear()
        self.com2_com.clear()
        for port in port_list:
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]  # 将串口信息添加进字典
            self.com1_com.addItem(port[0])
            self.com2_com.addItem(port[0])  # 将串口信息写入控件 展示出来
        if len(self.Com_Dict) == 0:
            self.right_com_label_com1.setText(" 无串口")
            self.right_com_label_com2.setText(" 无串口")

def main():
    app = QApplication(sys.argv)
    my_win = SetComPageWindow()
    my_win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
