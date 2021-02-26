# -*- coding: utf-8 -*-
import sys

import qtawesome
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, QPoint
from PyQt5.QtGui import QFont, QEnterEvent, QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from call_autotestpage import AutoTestPageWindow
from call_bmstest import BmsTestPageWindow
from call_orderset import OrderSetPageWindow
from call_setcompage import SetComPageWindow

class MainUi(object):

    def __init__(self):
        # 主窗口部件
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局

        # 左侧主部件
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件

        # 右侧主部件
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget = QtWidgets.QWidget()

        # 手动测试部件（右侧）
        self.right_layout_manual = QtWidgets.QGridLayout()
        self.right_widget_manual = QtWidgets.QWidget()

        # 在右侧主布局内创建stackedWidget部件
        self.stackedWidget = QStackedWidget()

        # 对各个部件进行定义
        self.setComPageUi = SetComPageWindow()  # 通道设置
        self.AutoTestPageUi = AutoTestPageWindow()  # 自动测试
        self.BmsTestPageUi = BmsTestPageWindow()  # bms测试面板
        self.OrderSetPageUi = OrderSetPageWindow()  # 指令集面板

        # 右侧主窗口部件的三个按钮
        self.right_mini = QtWidgets.QPushButton()  # 最小化按钮
        self.right_visit = QtWidgets.QPushButton()  # 最大化按钮
        self.right_close = QtWidgets.QPushButton()  # 关闭按钮

        # 左侧参菜单按钮创建
        self.left_button_auto = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "自动测试")
        self.left_button_manual = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "手动调试")
        self.left_button_par = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "参数校准")
        self.left_button_data = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "数据管理")
        self.left_button_report = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "报告生成")
        self.left_button_com = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "通道设置")
        self.left_button_order = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "指令设置")
        self.left_label = QtWidgets.QPushButton()  # 创建左侧菜单占位按钮（只是为了布局好看，无实质意义）

        # 手动测试布局内按钮及部件创建======================================================================
        # 手动测试复选框模块创建
        self.manual_tab_widget = QtWidgets.QTabWidget()  # 创建手动测试窗口TAB部件
        self.manual_tab_layout = QtWidgets.QGridLayout()  # 创建网格布局
        # BMS---------------------------------------------------------------------
        self.manual_tab1_widget1 = QtWidgets.QWidget()  # 创建tab1界面
        self.manual_tab1_layout1 = QtWidgets.QGridLayout()  # 创建tab1的布局
        self.manual_tab1_widget2 = QtWidgets.QWidget()  # 创建tab2界面
        self.manual_tab1_layout2 = QtWidgets.QGridLayout()  # 创建tab2的布局
        self.manual_tab1_widget3 = QtWidgets.QWidget()  # 创建tab3界面
        self.manual_tab1_layout3 = QtWidgets.QGridLayout()  # 创建tab3的布局
        self.manual_tab1_widget4 = QtWidgets.QWidget()  # 创建tab4界面
        self.manual_tab1_layout4 = QtWidgets.QGridLayout()  # 创建tab4的布局
        self.manual_tab1_widget5 = QtWidgets.QWidget()  # 创建tab5界面
        self.manual_tab1_layout5 = QtWidgets.QGridLayout()  # 创建tab5的布局
        self.manual_tab1_widget6 = QtWidgets.QWidget()  # 创建tab6界面
        self.manual_tab1_layout6 = QtWidgets.QGridLayout()  # 创建tab6的布局

        self.manual_tab_widget.addTab(self.manual_tab1_widget1, 'BMS')
        self.manual_tab_widget.addTab(self.manual_tab1_widget2, 'CDS')
        self.manual_tab_widget.addTab(self.manual_tab1_widget3, 'MPS')
        self.manual_tab_widget.addTab(self.manual_tab1_widget4, 'UART')
        self.manual_tab_widget.addTab(self.manual_tab1_widget5, '电量表')
        self.manual_tab_widget.addTab(self.manual_tab1_widget6, '4G模块')

    def setupUi(self,form):
        # 主窗口
        form.setCentralWidget(self.main_widget)
        self.main_widget.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # 左侧部件布局设置
        self.left_widget.setObjectName('left_widget')
        self.left_widget.setLayout(self.left_layout)  # 在左侧部件内创建网格布局
        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列

        # 右侧部件布局设置
        self.right_widget.setObjectName('right_widget')
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格
        self.main_layout.addWidget(self.right_widget, 0, 3, 12, 12)  # 右侧部件在第0行第4列，占8行9列

        # 窗口中心设置
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        # self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        # 左侧菜单按钮设置===========================================================================
        # 左侧参菜单按钮
        self.left_layout.addWidget(self.left_button_auto, 2, 0, 1, 3)  # 自动测试
        self.left_layout.addWidget(self.left_button_manual, 3, 0, 1, 3)  # 手动测试
        self.left_layout.addWidget(self.left_button_par, 4, 0, 1, 3)  # 参数校准
        self.left_layout.addWidget(self.left_button_data, 5, 0, 1, 3)  # 数据管理
        self.left_layout.addWidget(self.left_button_report, 6, 0, 1, 3)  # 报告生成
        self.left_layout.addWidget(self.left_button_com, 7, 0, 1, 3)  # 通道设置
        self.left_layout.addWidget(self.left_button_order, 8, 0, 1, 3)  # 指令集设置
        self.left_layout.addWidget(self.left_label, 9, 0, 1, 3)  # 占位标签

        # 右侧主部件的三个按钮===================================================================================
        self.right_layout.addWidget(self.right_close, 0, 12, 1, 1)
        self.right_layout.addWidget(self.right_visit, 0, 11, 1, 1)
        self.right_layout.addWidget(self.right_mini, 0, 10, 1, 1)

        # 设置右侧主布局内的stackedWidget布局===============================================================
        self.right_layout.addWidget(self.stackedWidget, 1, 1, 11, 12)

        # 手动测试面板----------------------------------------------------------------------------------
        self.right_widget_manual.setLayout(self.right_layout_manual)  # 设置右侧部件布局为网格
        self.right_layout.addWidget(self.right_widget_manual, 0, 0, 9, 12)  # 右侧部件在第0行第4列，占8行9列
        self.manual_tab_widget.setLayout(self.manual_tab_layout)  # 设置tab页面为网格布局
        self.right_layout_manual.addWidget(self.manual_tab_widget, 0, 0, 9, 12)  # 设置位置

        # bms测试
        self.manual_tab1_widget1.setLayout(self.manual_tab1_layout1)
        self.manual_tab1_layout1.addWidget(self.BmsTestPageUi)  # bms测试

        # CDS测试
        self.manual_tab1_widget2.setLayout(self.manual_tab1_layout2)

        # MPS测试
        self.manual_tab1_widget3.setLayout(self.manual_tab1_layout3)

        # UART测试
        self.manual_tab1_widget4.setLayout(self.manual_tab1_layout4)

        # 电量表测试
        self.manual_tab1_widget5.setLayout(self.manual_tab1_layout5)

        # 4G模块测试
        self.manual_tab1_widget6.setLayout(self.manual_tab1_layout6)
        """
        # 美化设置======================================================================================
        # 设置窗口透明度
        form.setWindowOpacity(1)  # 设置窗口透明度
        form.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        form.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框 去除窗口边框
        self.main_layout.setSpacing(0)  # 设置布局内部件缝隙
        # 右侧边框美化----------------------------------------------------------------------------------
        self.right_widget.setStyleSheet(
            '''QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica None", Helvetica, Arial, sans-serif;
            }
        ''')

        # 左侧按钮美化-----------------------------------------------------------------------------------
        self.left_widget.setStyleSheet(
            '''
            QPushButton{border:none;color:white;}
            QWidget#left_widget{
                background:gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
            QPushButton#left_label{    
                border:none;
                font-size:18px;
                font-weight:700;
                font-family: Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        # 三个按钮美化------------------------------------------------------------------------------------
        # 三个按钮美化（设置按钮大小）
        self.right_close.setFixedSize(16, 16)
        self.right_visit.setFixedSize(16, 16)
        self.right_mini.setFixedSize(16, 16)
        # 设置外观
        self.right_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}
            right_button:flat{border:none;color:white;}''')
        self.right_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.right_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
            """
        # 面板设置=========================================================================================
        # 将面板，加入stackedWidget
        self.stackedWidget.addWidget(self.AutoTestPageUi)
        self.stackedWidget.addWidget(self.right_widget_manual)
        # self.stackedWidget.addWidget(self.right_widget_par)
        # self.stackedWidget.addWidget(self.right_widget_data)
        # self.stackedWidget.addWidget(self.right_widget_report)
        # self.stackedWidget.setLayout(self.)
        self.stackedWidget.addWidget(self.setComPageUi)
        self.stackedWidget.addWidget(self.OrderSetPageUi)
        # 左侧按钮事件
        self.left_button_auto.clicked.connect(self.on_pushButton1_auto)
        self.left_button_manual.clicked.connect(self.on_pushButton2_manual)
        self.left_button_par.clicked.connect(self.on_pushButton3_par)
        self.left_button_data.clicked.connect(self.on_pushButton4_data)
        self.left_button_report.clicked.connect(self.on_pushButton5_report)
        self.left_button_com.clicked.connect(self.on_pushButton6_com)
        # self.setComPageUi.right_com_button_star.clicked.connect(self.on_pushButton1_auto)

    def on_pushButton1_auto(self):
        self.stackedWidget.setCurrentIndex(0)  # 第一个面板

    def on_pushButton2_manual(self):
        self.stackedWidget.setCurrentIndex(1)  # 第二个

    def on_pushButton3_par(self):
        self.stackedWidget.setCurrentIndex(2)

    def on_pushButton4_data(self):
        self.stackedWidget.setCurrentIndex(3)

    def on_pushButton5_report(self):
        self.stackedWidget.setCurrentIndex(4)

    def on_pushButton6_com(self):
        self.stackedWidget.setCurrentIndex(5)
        # self.right_close.clicked.connect(quit)


def main():
    app = QApplication(sys.argv)
    G_wuyou = QtWidgets.QMainWindow()
    ui = MainUi()
    ui.setupUi(G_wuyou)
    G_wuyou.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
