# -*- coding: utf-8 -*-
import sys
import qtawesome
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QScrollArea, QApplication
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg


class Ui_AutoTestPage(object):
    def __init__(self):

        # 自动测试部件（右侧）
        self.right_widget_auto = QtWidgets.QWidget()  # 布局
        self.right_layout_auto = QtWidgets.QGridLayout()  # 部件

        # 搜索框创建及设置
        self.console_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='#F76677', font=18), "开始")
        self.right_rate_layout = QtWidgets.QGridLayout()  # 控制部件网格布局层
        self.right_rate_widget = QtWidgets.QWidget()  # 控制部件
        self.right_process_bar = QtWidgets.QProgressBar()  # 进度部件
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '搜索  ')
        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件

        # 动态添加测试状态控件
        self.x = ['a', '3']  # 创建一个按钮列表
        self.widgetList = []  # 创建一个控件列表
        self.auto_add_scroll = QScrollArea()  # 创建一个滚动条
        self.auto_add_scroll.setWidgetResizable(True)
        self.auto_add_widget = QtWidgets.QWidget()  # 创建显示控件部件
        self.auto_add_widget.setGeometry(QtCore.QRect(0, 0, 380, 280))
        self.auto_add_layout = QtWidgets.QVBoxLayout(self.auto_add_widget)  # 创建动态添加控件布局
        self.addButton = QtWidgets.QPushButton('添加控件')  # 添加控件按钮
        self.delButton = QtWidgets.QPushButton('删除控件')  # 删除控件按钮

        # 动态图表的创建
        self.charp = pg.GraphicsWindow()  # 创建一个图表部件

    def setupUi(self):
        # 创建面板=======================================================================================
        # 自动测试面板----------------------------------------------------------------------------------
        self.right_widget_auto.setObjectName('right_widget_auto')
        self.right_widget_auto.setLayout(self.right_layout_auto)  # 设置右侧部件布局为网格

        # 动态添加数据控件
        self.auto_add_scroll.setWidget(self.auto_add_widget)
        self.right_layout_auto.addWidget(self.auto_add_scroll, 3, 6, 7, 6)
        self.auto_add_layout.addWidget(self.addButton)
        self.auto_add_layout.addWidget(self.delButton)
        self.addButton.clicked.connect(self.add)
        self.delButton.clicked.connect(self.delete)

        # 搜索框
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input.setPlaceholderText("输入ID号、版本编号，回车进行搜索")
        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)  # 搜索框位置
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 11)
        self.right_layout_auto.addWidget(self.right_bar_widget, 0, 0, 1, 12)  #

        # 进度条创建
        self.right_process_bar.setValue(30)
        self.right_process_bar.setFixedHeight(3)  # 设置进度条高度
        self.right_process_bar.setTextVisible(False)  # 不显示进度条文字
        self.right_rate_widget.setLayout(self.right_rate_layout)
        self.console_button_3.setIconSize(QtCore.QSize(30, 30))
        self.right_rate_layout.addWidget(self.console_button_3, 0, 1)
        self.right_rate_layout.setAlignment(QtCore.Qt.AlignCenter)  # 设置布局内部件居中显示
        self.right_layout_auto.addWidget(self.right_process_bar, 10, 0, 1, 12)
        self.right_layout_auto.addWidget(self.right_rate_widget, 11, 0, 1, 12)

        # 添加一个图形
        self.right_layout_auto.addWidget(self.charp, 3, 0, 7, 6)
        p6 = self.charp.addPlot(title="绘图数据更新")
        curve = p6.plot(pen='y')  # 图形使用黄色画笔进行绘制
        data = np.random.normal(size=(10, 1000))  # 生成随机数据
        ptr = 0  # 初始为0

        # 定义一个更新函数
        def update():
            global curve, data, ptr, p6
            curve.setData(data[ptr % 10])  # 设置图形的数据值
            if ptr == 0:
                p6.enableAutoRange('xy', False)  ## 在第一个图形绘制的时候停止自动缩放
            ptr += 1

        timer = QtCore.QTimer()  # 实例化一个计时器
        timer.timeout.connect(update)  # 计时器信号连接到update()函数
        timer.start(200)  # 计时器间隔200毫秒

        # 搜索框美化--------------------------------------------------------------------------------------
        self.right_bar_widget_search_input.setStyleSheet(  # 搜索框美化
            '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            }''')

        # 动态添加控件滚动面板美化
        self.auto_add_scroll.setStyleSheet(
            '''QWidget#auto_add_scroll
            {
                color:#232C51;
                background:white;
            }''')
        self.auto_add_scroll.setStyleSheet('''
                    QWidget
                    {
                        color:#232C51;
                        background:white;
                        border-radius:10px;
                    }
                        QScrollBar:vertical
                    {
                        border-radius:7px;
                        background:white;
                        padding-top:14px;
                        padding-bottom:14px;

                    }
                    QScrollBar::handle:vertical
                    {
                        background:darkgray;
                        border-radius:6px;
                        margin-left:1px;
                        margin-right:1px;
                    }
                    QScrollBar::handle:vertical:hover
                    {
                        background:gray;
                        border-radius:6px;
                    }
                    QScrollBar::add-line:vertical
                    {
                        height:14px;width:8px;
                        image:url('./pictures/down-arrow.jpg');
                    }
                    QScrollBar::sub-line:vertical
                    {
                        height:14px;width:8px;
                        image:url('');
                    }
                    QScrollBar::add-line:vertical:hover
                    {
                        height:14px;width:8px;
                        image:url('./pictures/down-down-arrow.jpg');
                        subcontrol-position:bottom;
                    }
                    QScrollBar::sub-line:vertical:hover
                    {
                        height:14px;width:8px;
                        image:url('');
                        subcontrol-position:top;
                    }
                    QScrollBar::add-page:vertical
                    {
                        background:white;
                    }
                    QScrollBar::sub-page:vertical
                    {
                        background:white; 
                    }
                    ''')

        # 进度条和开始按钮美化-------------------------------------------------------------------------------
        self.right_process_bar.setStyleSheet('''QProgressBar::chunk {background-color: #F76677;}''')  # 进度条和播放按钮美化
        self.right_rate_widget.setStyleSheet('''QPushButton {border:none;}''')

    def add(self):
        for j in range(0, len(self.x)):
            self.widgetList.append(j)
            self.widgetList[j] = QtWidgets.QPushButton()
            self.widgetList[j].setStyleSheet(
                '''QPushButton{
                border:none;
                color:black;
                font-size:24px;
                height:30px;
                padding-left:10px;
                padding-right:20px;
                text-align:center;
            }
            QPushButton:hover{
                color:black;
                border:1px solid #F77777;
                border-radius:15px;
                background:LightGray;
            }''')
            self.widgetList[j].setText(self.x[j])
            self.auto_add_layout.addWidget(self.widgetList[j])
            # self.widgetList[j].clicked.connect(lambda: self.table(self.sender().text()))

    def table(self, n):
        # 用于测试，因为只是测试，所有仅仅用打印来证明不是只是最后一个按钮有效，每次点击都会不同
        # 解决pyqt5循环生成按钮并且直接连接事件，但是点击按钮的时候只是响应最后一个事件
        print(n)

    def delete(self):  # 点击事件
        for i in range(self.auto_add_layout.count())[2:]:
            self.auto_add_layout.itemAt(i).widget().deleteLater()


if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance()
