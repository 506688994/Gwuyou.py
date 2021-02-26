# -*- coding: utf-8 -*-
import sys
import qtawesome
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_SetComPage(object):

    def __init__(self):
        # 参数校准部件（右侧）
        self.right_layout_com = QtWidgets.QGridLayout()
        self.right_widget_com = QtWidgets.QWidget()
        # 通道设置布局内按钮及部件创建=======================================================================
        # 串口连接部件
        # 串口一
        self.right_com_label_com1 = QtWidgets.QLabel("安捷伦")
        self.com1_com = QtWidgets.QComboBox()  # 串口
        self.com1_por = QtWidgets.QComboBox()  # 波特率
        self.com1_por.addItem('')
        self.com1_por.addItem('')
        self.right_com_button_com1 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "连接安捷伦")
        # 串口二
        self.right_com_label_com2 = QtWidgets.QLabel("BMS")
        self.com2_com = QtWidgets.QComboBox()  # 串口
        self.com2_por = QtWidgets.QComboBox()  # 波特率
        self.com2_por.addItem('')
        self.com2_por.addItem('')
        self.right_com_button_com2 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "连接BMS")
        # 开始按钮
        self.right_com_button_star = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "刷新串口")  # 开始按钮

    def setupUi(self, form):
        # 主窗口
        # 窗口中心设置
        #form.setCentralWidget(self.right_widget_com)  # 设置窗口主部件
        # 通道设置面板------------------------------------------------------------------------------
        self.right_widget_com.setLayout(self.right_layout_com)  # 设置右侧部件布局为网格
        #self.right_layout_com.setContentsMargins(0,0,0,0)

        # 实例化QComBox对象
        # 串口一
        self.right_layout_com.addWidget(self.right_com_label_com1, 1, 1, 1, 3)  # 标签
        self.right_layout_com.addWidget(self.com1_com, 2, 1, 1, 3)  # 串口
        self.right_layout_com.addWidget(self.com1_por, 3, 1, 1, 3)  # 波特率
        self.com1_por.setItemText(0,'9600')
        self.com1_por.setItemText(1,'115200')
        self.right_layout_com.addWidget(self.right_com_button_com1, 7, 1, 1, 3)  # 打开串口

        # 串口二
        self.right_layout_com.addWidget(self.right_com_label_com2, 1, 4, 1, 3)  # 标签
        self.right_layout_com.addWidget(self.com2_com, 2, 4, 1, 3)#串口
        self.right_layout_com.addWidget(self.com2_por, 3, 4, 1, 3)#波特率
        self.com2_por.setItemText(0, '9600')
        self.com2_por.setItemText(1, '115200')
        self.right_layout_com.addWidget(self.right_com_button_com2, 7, 4, 1, 3)  # 打开串口

        # 开始测试按钮
        self.right_layout_com.addWidget(self.right_com_button_star, 8, 1, 4, 6)  # 开始按钮

        # 通道设置面板按钮美化------------------------------------------------------------------------------
        self.right_widget_com.setStyleSheet(
            '''QPushButton{
                border:none;
                color:black;
                font-size:24px;
                height:60px;
                padding-left:10px;
                padding-right:20px;
                text-align:center;
            }
            QPushButton:hover{
                color:black;
                border:2px solid #F3F3F5;
                border-radius:20px;
                background:LightGray;
            }
        ''')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SetComPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
