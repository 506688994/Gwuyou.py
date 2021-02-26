# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *

from HomePages.ModulPages.ui_bmstest import Ui_BmsTest

class BmsTestPageWindow(QWidget, Ui_BmsTest):
    # 声明信号
    BmsTest_Signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(BmsTestPageWindow, self).__init__(parent)
        self.setupUi()
        self.initUI()
        # 声明工厂测试指令
        self.order_mos1_0 = 'BB AA 04 64 FF 08 97'
        self.order_mos1_1 = 'BB AA 04 64 FF 09 96'
        self.order_mos2_0 = 'BB AA 04 64 FF 0A 95'
        self.order_mos2_1 = 'BB AA 04 64 FF 0B 94'
        self.order_mos3_0 = 'BB AA 04 64 FF 0C 93'
        self.order_mos3_1 = 'BB AA 04 64 FF 0B 92'
        self.order_led_r_0 = 'BB AA 04 64 FF 20 BF'
        self.order_led_r_1 = 'BB AA 04 64 FF 21 BE'
        self.order_led_g_0 = 'BB AA 04 64 FF 22 BD'
        self.order_led_g_1 = 'BB AA 04 64 FF 23 BC'
        self.order_buzzer_0 = 'BB AA 04 64 FF 24 BB'
        self.order_buzzer_1 = 'BB AA 04 64 FF 25 BA'
        self.order_voice_0 = 'BB AA 04 64 FF 26 B9'
        self.order_voice_1 = 'BB AA 04 64 FF 27 B8'
        self.order_relay_0 = 'BB AA 04 64 FF 28 B7'
        self.order_relay_1 = 'BB AA 04 64 FF 29 B6'
        self.order_fan_0 = 'BB AA 04 64 FF 2A B5'
        self.order_fan_1 = 'BB AA 04 64 FF 2B B4'

    def initUI(self):
        # 连接信号
        self.setLayout(self.manual_layout_bms)  # 布局
        self.BmsTest_Signal.connect(self.showWrite)  # 定义信号源
        self.bms_mos1_0.clicked.connect(self.showWrite)  # 支路mos闭合
        self.bms_mos1_1.clicked.connect(self.showWrite)  # 支路mos断开
        self.bms_mos2_0.clicked.connect(self.showWrite)
        self.bms_mos2_1.clicked.connect(self.showWrite)
        self.bms_mos3_0.clicked.connect(self.showWrite)
        self.bms_mos3_1.clicked.connect(self.showWrite)
        self.bms_led_r_0.clicked.connect(self.showWrite)
        self.bms_led_r_1.clicked.connect(self.showWrite)
        self.bms_led_g_0.clicked.connect(self.showWrite)
        self.bms_led_g_1.clicked.connect(self.showWrite)
        self.bms_voice_0.clicked.connect(self.showWrite)
        self.bms_voice_1.clicked.connect(self.showWrite)
        self.bms_buzzer_0.clicked.connect(self.showWrite)
        self.bms_buzzer_1.clicked.connect(self.showWrite)
        self.bms_relay_0.clicked.connect(self.showWrite)
        self.bms_relay_1.clicked.connect(self.showWrite)
        self.bms_fan_0.clicked.connect(self.showWrite)
        self.bms_fan_1.clicked.connect(self.showWrite)

    def showWrite(self):
        # 发射信号
        sender = self.sender()
        if sender == self.bms_mos1_0:
            self.BmsTest_Signal.emit(self.order_mos1_0)
            print(self.BmsTest_Signal)
        elif sender == self.bms_mos1_1:
            self.BmsTest_Signal.emit(self.order_mos1_1)
        elif sender == self.bms_mos2_0:
            self.BmsTest_Signal.emit(self.order_mos2_0)
        elif sender == self.bms_mos2_1:
            self.BmsTest_Signal.emit(self.order_mos2_1)
        elif sender == self.bms_mos3_0:
            self.BmsTest_Signal.emit(self.order_mos3_0)
        elif sender == self.bms_mos3_1:
            self.BmsTest_Signal.emit(self.order_mos3_1)
        elif sender == self.bms_led_r_0:
            self.BmsTest_Signal.emit(self.order_led_r_0)
        elif sender == self.bms_led_r_1:
            self.BmsTest_Signal.emit(self.order_led_r_1)
        elif sender == self.bms_led_g_0:
            self.BmsTest_Signal.emit(self.order_led_g_0)
        elif sender == self.bms_led_g_1:
            self.BmsTest_Signal.emit(self.order_led_g_1)
        elif sender == self.bms_voice_0:
            self.BmsTest_Signal.emit(self.order_voice_0)
        elif sender == self.bms_voice_1:
            self.BmsTest_Signal.emit(self.order_voice_1)
        elif sender == self.bms_buzzer_0:
            self.BmsTest_Signal.emit(self.order_buzzer_0)
        elif sender == self.bms_buzzer_1:
            self.BmsTest_Signal.emit(self.order_buzzer_1)
        elif sender == self.bms_relay_0:
            self.BmsTest_Signal.emit(self.order_relay_0)
        elif sender == self.bms_relay_1:
            self.BmsTest_Signal.emit(self.order_relay_1)
        elif sender == self.bms_fan_0:
            self.BmsTest_Signal.emit(self.order_fan_0)
        elif sender == self.bms_fan_1:
            self.BmsTest_Signal.emit(self.order_fan_1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = BmsTestPageWindow()
    mainWindow.show()
    sys.exit(app.exec_())
