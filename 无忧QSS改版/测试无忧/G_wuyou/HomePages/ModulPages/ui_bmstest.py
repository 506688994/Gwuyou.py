# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets


class Ui_BmsTest(object):

    def __init__(self):
        # 参数校准部件（右侧）
        self.manual_widget_bms = QtWidgets.QWidget()#创建部件
        self.manual_layout_bms = QtWidgets.QGridLayout()#创建布局

        self.bms_factory_widget = QtWidgets.QWidget()#创建工厂测试指令部件
        self.bms_factory_layout = QtWidgets.QGridLayout()#创建工厂测试部件网格布局

        self.bms_read = QtWidgets.QPushButton('读取')  # 读取
        self.bms_write = QtWidgets.QPushButton('写入')  # 写入
        self.bms_recover = QtWidgets.QPushButton('恢复出厂设置')  # 恢复出厂设置
        self.bms_load = QtWidgets.QPushButton('从文件导入')  # 从文件导入
        self.bms_save = QtWidgets.QPushButton('保存到文件')  # 保存到文件

        # 工厂测试指令
        self.bms_mos1_0 = QtWidgets.QPushButton('支路mos闭合')  # 打开mos
        self.bms_mos1_1 = QtWidgets.QPushButton('支路mos断开')  # 关闭mos
        self.bms_mos2_0 = QtWidgets.QPushButton('充电mos闭合')
        self.bms_mos2_1 = QtWidgets.QPushButton('充电mos断开')
        self.bms_mos3_0 = QtWidgets.QPushButton('放电mos闭合')
        self.bms_mos3_1 = QtWidgets.QPushButton('放电mos断开')
        self.bms_led_r_0 = QtWidgets.QPushButton('打开红色led')
        self.bms_led_r_1 = QtWidgets.QPushButton('关闭红色led')
        self.bms_led_g_0 = QtWidgets.QPushButton('打开绿色led')
        self.bms_led_g_1 = QtWidgets.QPushButton('关闭绿色led')
        self.bms_buzzer_0 = QtWidgets.QPushButton('打开蜂鸣器')
        self.bms_buzzer_1 = QtWidgets.QPushButton('关闭蜂鸣器')
        self.bms_voice_0 = QtWidgets.QPushButton('打开语音')
        self.bms_voice_1 = QtWidgets.QPushButton('关闭语音')
        self.bms_relay_0 = QtWidgets.QPushButton('闭合继电器')
        self.bms_relay_1 = QtWidgets.QPushButton('断开继电器')
        self.bms_fan_0 = QtWidgets.QPushButton('打开风扇')
        self.bms_fan_1 = QtWidgets.QPushButton('关闭风扇')

        #测试指令返回值
        self.bms_mos1 = QtWidgets.QLabel('电压')
        self.bms_mos2 = QtWidgets.QLabel('电压')
        self.bms_mos3 = QtWidgets.QLabel('电压')
        self.bms_led_r = QtWidgets.QLabel('电压')
        self.bms_led_g = QtWidgets.QLabel('电压')
        self.bms_buzzer = QtWidgets.QLabel('电压')
        self.bms_voice = QtWidgets.QLabel('电压')
        self.bms_relay = QtWidgets.QLabel('电压')
        self.bms_fan = QtWidgets.QLabel('电压')



    def setupUi(self):
        # 手动测试面板----------------------------------------------------------------------------------
        # 主面板

        self.manual_widget_bms.setLayout(self.manual_layout_bms)  # 设置主界面布局为网格


        self.bms_factory_widget.setLayout(self.bms_factory_layout)  # 设置工厂测试指令布局
        self.manual_layout_bms.addWidget(self.bms_factory_widget,0,0,9,12)#把工厂测试部件放到主界面布局内

        # 工厂测试命令按钮位置设置
        self.bms_factory_layout.addWidget(self.bms_mos1_0, 0, 1, 1, 1)  # 支路mos闭合
        self.bms_factory_layout.addWidget(self.bms_mos1_1, 0, 2, 1, 1)  # 支路mos断开
        self.bms_factory_layout.addWidget(self.bms_mos2_0, 1, 1, 1, 1)  # 充电mos闭合
        self.bms_factory_layout.addWidget(self.bms_mos2_1, 1, 2, 1, 1)  # 充电mos断开
        self.bms_factory_layout.addWidget(self.bms_mos3_0, 2, 1, 1, 1)  # 放电mos闭合
        self.bms_factory_layout.addWidget(self.bms_mos3_1, 2, 2, 1, 1)  # 放电mos断开

        self.bms_factory_layout.addWidget(self.bms_led_r_0, 3, 1, 1, 1)  # 打开红色led
        self.bms_factory_layout.addWidget(self.bms_led_r_1, 3, 2, 1, 1)  # 关闭红色led
        self.bms_factory_layout.addWidget(self.bms_led_g_0, 4, 1, 1, 1)  # 打开绿色led
        self.bms_factory_layout.addWidget(self.bms_led_g_1, 4, 2, 1, 1)  # 关闭绿色led

        self.bms_factory_layout.addWidget(self.bms_buzzer_0, 5, 1, 1, 1)  # 打开蜂鸣器
        self.bms_factory_layout.addWidget(self.bms_buzzer_1, 5, 2, 1, 1)  # 关闭蜂鸣器
        self.bms_factory_layout.addWidget(self.bms_voice_0, 6, 1, 1, 1)  # 打开语音模块
        self.bms_factory_layout.addWidget(self.bms_voice_1, 6, 2, 1, 1)  # 关闭语音模块

        self.bms_factory_layout.addWidget(self.bms_relay_0, 7, 1, 1, 1)  # 闭合继电器
        self.bms_factory_layout.addWidget(self.bms_relay_1, 7, 2, 1, 1)  # 断开继电器
        self.bms_factory_layout.addWidget(self.bms_fan_0, 8, 1, 1, 1)  # 打开风扇
        self.bms_factory_layout.addWidget(self.bms_fan_1, 8, 2, 1, 1)  # 关闭风扇

        #工厂测试返回值
        self.bms_factory_layout.addWidget(self.bms_mos1, 0, 0, 1, 1)  # 支路mos
        self.bms_factory_layout.addWidget(self.bms_mos2, 1, 0, 1, 1)  # 充电mos
        self.bms_factory_layout.addWidget(self.bms_mos3, 2, 0, 1, 1)  # 放电mos
        self.bms_factory_layout.addWidget(self.bms_led_r, 3, 0, 1, 1)  # 红色led
        self.bms_factory_layout.addWidget(self.bms_led_g, 4, 0, 1, 1)  # 绿色led
        self.bms_factory_layout.addWidget(self.bms_buzzer, 5, 0, 1, 1)  # 蜂鸣器
        self.bms_factory_layout.addWidget(self.bms_voice, 6, 0, 1, 1)  # 语音模块
        self.bms_factory_layout.addWidget(self.bms_relay, 7, 0, 1, 1)  # 继电器
        self.bms_factory_layout.addWidget(self.bms_fan, 8, 0, 1, 1)  # 风扇



