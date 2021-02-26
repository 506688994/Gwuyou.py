# -*- coding: utf-8 -*-
import sys
import qtawesome
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QApplication


class MainUi(object):

    def __init__(self):
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

    def setupUi(self, form):
        # 主窗口
        form.setObjectName("form")
        form.setFixedSize(1024, 600)
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
        form.setCentralWidget(self.main_widget)  # 设置窗口主部件

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

        # 面板设置=========================================================================================
        # 将面板，加入stackedWidget
        '''self.stackedWidget.addWidget(self.right_widget_auto)
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
        self.stackedWidget.setCurrentIndex(5)'''
        # self.right_close.clicked.connect(quit)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainUi()
    ui.setupUi(MainWindow)
    ui.setCloseButton(True)
    ui.setMinMaxButtons(True)
    MainWindow = Container(MainWindow)
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApp
