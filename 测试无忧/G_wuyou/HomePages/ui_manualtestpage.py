# -*- coding: utf-8 -*-
import sys
import qtawesome
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_ManualTest(object):

    def __init__(self):
        # 参数校准部件（右侧）
        self.right_layout_manual = QtWidgets.QGridLayout()
        self.right_widget_manual = QtWidgets.QWidget()
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

    def setupUi(self,form):
        # 手动测试面板----------------------------------------------------------------------------------
        # 主面板
        self.right_widget_manual.setObjectName('right_widget_manual')
        self.right_widget_manual.setLayout(self.right_layout_manual)  # 设置右侧部件布局为网格
        form.setCentralWidget(self.right_widget_manual)  # 设置窗口主部件
        self.manual_tab_widget.setLayout(self.manual_tab_layout)  # 设置tab页面为网格布局
        self.right_layout_manual.addWidget(self.manual_tab_widget, 0, 0, 9, 12)  # 设置位置
        # bms测试
        self.manual_tab1_widget1.setLayout(self.manual_tab1_layout1)
        self.manual_tab1_layout1.addWidget(self.bms_load, 0, 0, 1, 2)
        self.manual_tab1_layout1.addWidget(self.bms_read, 1, 0, 1, 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ManualTest()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
