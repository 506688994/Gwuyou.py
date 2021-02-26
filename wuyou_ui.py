# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: c:\Users\1230\Desktop\Pyserial-Demo-master\ui_demo_1.py
# Compiled at: 2020-05-23 15:11:22
# Size of source mod 2**32: 12618 bytes
import sys

import qtawesome
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QScrollArea


class MainUi(object):

    def __init__(self,MainWindow):
        # 主窗口部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件

        # 左侧主部件
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件

        # 右侧主部件
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget = QtWidgets.QWidget()

        # 在右侧主布局内创建stackedWidget部件
        self.stackedWidget = QStackedWidget()

        # 自动测试部件（右侧）
        self.right_layout_auto = QtWidgets.QGridLayout()
        self.right_widget_auto = QtWidgets.QWidget()

        # 手动测试部件（右侧）
        self.right_layout_manual = QtWidgets.QGridLayout()
        self.right_widget_manual = QtWidgets.QWidget()

        # 参数校准部件（右侧）
        self.right_layout_par = QtWidgets.QGridLayout()
        self.right_widget_par = QtWidgets.QWidget()

        # 数据管理部件（右侧）.
        self.right_layout_data = QtWidgets.QGridLayout()
        self.right_widget_data = QtWidgets.QWidget()

        # 报告生成部件（右侧）
        self.right_layout_report = QtWidgets.QGridLayout()
        self.right_widget_report = QtWidgets.QWidget()

        # 通道设置部件（右侧）
        self.right_layout_com = QtWidgets.QGridLayout()
        self.right_widget_com = QtWidgets.QWidget()

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
        self.left_label = QtWidgets.QPushButton()  # 创建左侧菜单占位按钮（只是为了布局好看，无实质意义）

        # 自动测试布局内按钮及部件创建=======================================================================
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

        # 手动测试布局内按钮及部件创建======================================================================
        # 手动测试复选框模块创建
        self.manual_tab_widget = QtWidgets.QTabWidget()  # 创建手动测试窗口TAB部件
        self.manual_tab_layout = QtWidgets.QGridLayout()  # 创建网格布局
        # BMS---------------------------------------------------------------------
        self.manual_tab1_widget1 = QtWidgets.QWidget()  # 创建tab1界面
        self.manual_tab1_layout1 = QtWidgets.QGridLayout()  # 创建tab1的布局
        self.bms_read = QtWidgets.QPushButton('读取')  # 读取
        self.bms_write = QtWidgets.QPushButton('写入')  # 写入
        self.bms_recover = QtWidgets.QPushButton('恢复出厂设置')  # 恢复出厂设置
        self.bms_load = QtWidgets.QPushButton('从文件导入')  # 从文件导入
        self.bms_save = QtWidgets.QPushButton('保存到文件')  # 保存到文件
        self.bms_mos0 = QtWidgets.QPushButton('闭合支路mos')  # 打开mos
        self.bms_mos1 = QtWidgets.QPushButton('关闭支路mos')  # 关闭mos

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

        # 通道设置布局内按钮及部件创建=======================================================================
        # 串口连接部件
        self.right_com_button_star = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "1")  # 开始按钮
        self.right_com_button_com2 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "连接BMS")
        self.right_com_button_com1 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "连接安捷伦")
        self.com2_por = QtWidgets.QComboBox()  # BMS串口
        self.com2_com = QtWidgets.QComboBox()  # BMS通道
        self.com1_por = QtWidgets.QComboBox()  # 安捷伦串口
        self.com1_com = QtWidgets.QComboBox()  # 安捷伦通道
        self.right_com_label_com2 = QtWidgets.QLabel("BMS")
        self.right_com_label_com1 = QtWidgets.QLabel("安捷伦")

    def init_ui(self, main_z):
        # 主窗口
        main_z.setObjectName("MainWindow")
        main_z.setFixedSize(1024, 600)
        self.main_widget.setObjectName("main_widget")
        self.main_widget.setLayout(self.main_layout)  # 在主窗口主部件内创建网格布局

        # 左侧部件布局设置
        self.left_widget.setObjectName('left_widget')
        self.left_widget.setLayout(self.left_layout)  # 在左侧部件内创建网格布局
        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列

        # 右侧部件布局设置
        self.right_widget.setObjectName('right_widget')
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格
        self.main_layout.addWidget(self.right_widget, 0, 3, 12, 12)  # 右侧部件在第0行第4列，占8行9列

        # 窗口中心设置
        main_z.setCentralWidget(self.main_widget)  # 设置窗口主部件

        # 左侧菜单按钮设置===========================================================================
        # 左侧参菜单按钮
        self.left_button_auto.setObjectName('left_button')  # 自动测试
        self.left_button_manual.setObjectName('left_button')  # 手动测试
        self.left_button_par.setObjectName('left_button')  # 参数校准
        self.left_button_data.setObjectName('left_button')  # 数据管理
        self.left_button_report.setObjectName('left_button')  # 报告生成
        self.left_button_com.setObjectName('left_button')  # 通道设置
        self.left_label.setObjectName('left_label')  # 占位标签
        # 按钮位置
        self.left_layout.addWidget(self.left_button_auto, 2, 0, 1, 3)  # 自动测试
        self.left_layout.addWidget(self.left_button_manual, 3, 0, 1, 3)  # 手动测试
        self.left_layout.addWidget(self.left_button_par, 4, 0, 1, 3)  # 参数校准
        self.left_layout.addWidget(self.left_button_data, 5, 0, 1, 3)  # 数据管理
        self.left_layout.addWidget(self.left_button_report, 6, 0, 1, 3)  # 报告生成
        self.left_layout.addWidget(self.left_button_com, 7, 0, 1, 3)  # 通道设置
        self.left_layout.addWidget(self.left_label, 8, 0, 1, 3)  # 占位标签

        # 右侧主部件的三个按钮===================================================================================
        self.right_layout.addWidget(self.right_close, 0, 12, 1, 1)
        self.right_layout.addWidget(self.right_visit, 0, 11, 1, 1)
        self.right_layout.addWidget(self.right_mini, 0, 10, 1, 1)

        # 设置右侧主布局内的stackedWidget布局===============================================================
        self.right_layout.addWidget(self.stackedWidget, 1, 1, 11, 12)

        # 创建面板=======================================================================================
        # 自动测试面板----------------------------------------------------------------------------------
        self.right_widget_auto.setObjectName('right_widget_auto')
        self.right_widget_auto.setLayout(self.right_layout_auto)  # 设置右侧部件布局为网格
        self.right_layout.addWidget(self.right_widget_auto, 0, 0, 11, 12)  # 右侧部件在第0行第4列，占8行9列

        # 动态添加数据控件
        self.auto_add_scroll.setWidget(self.auto_add_widget)
        self.right_layout_auto.addWidget(self.auto_add_scroll, 3, 0, 7, 12)
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

        # 手动测试面板----------------------------------------------------------------------------------
        # 主面板
        self.right_widget_manual.setObjectName('right_widget_manual')
        self.right_widget_manual.setLayout(self.right_layout_manual)  # 设置右侧部件布局为网格
        self.right_layout.addWidget(self.right_widget_manual, 0, 0, 9, 12)  # 右侧部件在第0行第4列，占8行9列
        self.manual_tab_widget.setLayout(self.manual_tab_layout)  # 设置tab页面为网格布局
        self.right_layout_manual.addWidget(self.manual_tab_widget, 0, 0, 9, 12)  # 设置位置
        # bms测试
        self.manual_tab1_widget1.setLayout(self.manual_tab1_layout1)
        self.manual_tab1_layout1.addWidget(self.bms_load, 0, 0, 1, 2)
        self.manual_tab1_layout1.addWidget(self.bms_read, 1, 0, 1, 2)

        # 参数校准面板---------------------------------------------------------------------------------
        self.right_widget_par.setLayout(self.right_layout_par)  # 设置右侧部件布局为网格
        self.right_layout.addWidget(self.right_widget_par, 0, 0, 9, 12)  # 右侧部件在第0行第4列，占8行9列

        # 数据管理面板--------------------------------------------------------------------------------
        self.right_widget_data.setLayout(self.right_layout_data)  # 设置右侧部件布局为网格
        self.right_layout.addWidget(self.right_widget_data, 0, 0, 9, 12)  # 右侧部件在第0行第4列，占8行9列

        # 报告生成面板-------------------------------------------------------------------------------
        self.right_widget_report.setLayout(self.right_layout_report)  # 设置右侧部件布局为网格
        self.right_layout.addWidget(self.right_widget_report, 0, 0, 9, 12)  # 右侧部件在第0行第4列，占8行9列

        # 通道设置面板------------------------------------------------------------------------------
        self.right_widget_com.setLayout(self.right_layout_com)  # 设置右侧部件布局为网格
        self.right_layout.addWidget(self.right_widget_com, 0, 0, 9, 12)  # 右侧部件在第0行第4列，占8行9列
        self.right_layout_com.addWidget(self.right_com_label_com1, 1, 1, 1, 3)
        self.right_layout_com.addWidget(self.right_com_label_com2, 1, 4, 1, 3)

        # 实例化QComBox对象
        self.right_layout_com.addWidget(self.com1_com, 2, 1, 1, 3)
        self.right_layout_com.addWidget(self.com1_por, 3, 1, 1, 3)
        self.right_layout_com.addWidget(self.com2_com, 2, 4, 1, 3)
        self.right_layout_com.addWidget(self.com2_por, 3, 4, 1, 3)

        self.right_layout_com.addWidget(self.right_com_button_com1, 4, 1, 1, 3)
        self.right_layout_com.addWidget(self.right_com_button_com2, 4, 4, 1, 3)

        self.right_layout_com.addWidget(self.right_com_button_star, 5, 1, 4, 6)

        # 美化设置======================================================================================
        # 设置窗口透明度
        main_z.setWindowOpacity(1)  # 设置窗口透明度
        main_z.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        main_z.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框 去除窗口边框
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
        # 面板设置=========================================================================================
        # 将面板，加入stackedWidget
        self.stackedWidget.addWidget(self.right_widget_auto)
        self.stackedWidget.addWidget(self.right_widget_manual)
        self.stackedWidget.addWidget(self.right_widget_par)
        self.stackedWidget.addWidget(self.right_widget_data)
        self.stackedWidget.addWidget(self.right_widget_report)
        self.stackedWidget.addWidget(self.right_widget_com)
        # 左侧按钮事件
        self.left_button_auto.clicked.connect(self.on_pushButton1_auto)
        self.left_button_manual.clicked.connect(self.on_pushButton2_manual)
        self.left_button_par.clicked.connect(self.on_pushButton3_par)
        self.left_button_data.clicked.connect(self.on_pushButton4_data)
        self.left_button_report.clicked.connect(self.on_pushButton5_report)
        self.left_button_com.clicked.connect(self.on_pushButton6_com)
        self.right_com_button_star.clicked.connect(self.on_pushButton1_auto)

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

    # 退出进程
    def setCloseButton(self, bool):
        # 给widget定义一个setCloseButton函数，为True时设置一个关闭按钮
        if bool:
            self.right_close.clicked.connect(quit)  # 按钮信号连接到关闭窗口的槽函数

    # 最小化
    def setMinMaxButtons(self, bool):
        # 给widget定义一个setMinMaxButtons函数，为True时设置一组最小化最大化按钮
        if bool:
            self.right_mini.clicked.connect(MainWindow.showMinimized)  # 按钮信号连接到最小化窗口的槽函数
            self.right_visit.clicked.connect(self._changeNormalButton)  # 按钮信号连接切换到恢复窗口大小按钮函数

    # 最大化
    def _changeNormalButton(self):
        # 切换到恢复窗口大小按钮
        MainWindow.showMaximized()  # 先实现窗口最大化
        self.right_visit.disconnect()  # 断开原本的信号槽连接
        self.right_visit.clicked.connect(self._changeMaxButton)  # 重新连接信号和槽

    # 恢复窗口大小
    def _changeMaxButton(self):
        MainWindow.showNormal()
        self.right_visit.disconnect()
        self.right_visit.clicked.connect(self._changeNormalButton)

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


# 窗口移动事件
class Container(QtWidgets.QWidget):
    def __init__(self, window):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(window)

    # 重写三个方法使我们的窗口支持拖动,上面参数window就是拖动对象
    def mousePressEvent(self, event):  # 鼠标长按事件
        if event.button() == QtCore.Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):  # 鼠标移动事件
        if QtCore.Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 鼠标释放事件
        self.m_drag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


# 程序入门
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = MainUi(MainWindow)  # ui是Ui_MainWindow()类的实例化对象
    ui.init_ui(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    ui.setCloseButton(True)
    ui.setMinMaxButtons(True)
    MainWindow = Container(MainWindow)
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApp
