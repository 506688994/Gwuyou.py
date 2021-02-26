# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: c:\Users\1230\Desktop\Pyserial-Demo-master\ui_demo_1.py
# Compiled at: 2020-05-23 15:11:22
# Size of source mod 2**32: 12618 bytes
import sys
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from Ui_demo_1 import Ui_Form
import time


class Pyqt5_Serial(QtWidgets.QWidget, Ui_Form):
    # 初始化
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("测试无忧")
        self.ser = serial.Serial()
        self.port_check()
        self.input1 = '+HAC_MODULE: READCALINFO'

        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))

    def init(self):
        # 串口检测按钮
        self.s1__box_1.clicked.connect(self.port_check)

        # 串口信息显示
        self.s1__box_2.currentTextChanged.connect(self.port_imf)

        # 打开串口按钮
        self.open_button.clicked.connect(self.port_open)

        # 关闭串口按钮
        self.close_button.clicked.connect(self.port_close)

        # 发送数据按钮
        self.s3__send_button.clicked.connect(self.data_send)

        # 定时发送数据
        self.timer_send = QTimer()
        self.timer_send.timeout.connect(self.data_send)
        self.timer_send_cb.stateChanged.connect(self.data_send_timer)

        # 定时器接收数据
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.data_receive)  # 计时器结束调用 data_receiver 方法

        # 清除发送窗口
        self.s3__clear_button.clicked.connect(self.send_data_clear)

        # 清除接收窗口
        self.s2__clear_button.clicked.connect(self.receive_data_clear)

    # 串口检测
    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        # print(type(serial.tools.list_ports.comports()))

        # print(port_list)
        self.s1__box_2.clear()  # 清除框内的内容
        for port in port_list:
            # print(port)
            # print(port[0])
            # print(port[1])
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]  # 将串口信息添加进字典
            # print(self.Com_Dict)
            self.s1__box_2.addItem(port[0])  # 将串口信息写入控件 展示出来
        if len(self.Com_Dict) == 0:
            self.state_label.setText(" 无串口")

    # 串口信息
    def port_imf(self):
        # 显示选定的串口的详细信息
        imf_s = self.s1__box_2.currentText()
        if imf_s != "":
            self.state_label.setText(self.Com_Dict[self.s1__box_2.currentText()])

    # 打开串口
    def port_open(self):
        self.ser.port = self.s1__box_2.currentText()  # 串口号
        # print(self.ser.port)
        self.ser.baudrate = int(self.s1__box_3.currentText())  # 波特率
        # print(self.ser.baudrate)
        self.ser.bytesize = int(self.s1__box_4.currentText())  # 数据位
        # print(self.ser.stopbits)
        self.ser.stopbits = int(self.s1__box_6.currentText())  # 停止位
        # print(self.ser.parity)
        self.ser.parity = self.s1__box_5.currentText()  # 校验位
        # print('打开串口成功')
        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")  # 弹出一个警告框
            return None

        # 打开串口接收定时器，周期为2ms
        self.timer.start(2)

        if self.ser.isOpen():
            self.open_button.setEnabled(False)  # 设置打开按钮为灰色,不可点击
            self.close_button.setEnabled(True)  # 设置关闭按钮为正常,可点击
            self.formGroupBox1.setTitle("串口状态（已开启）")

    # 关闭串口
    def port_close(self):
        self.timer.stop()  # 停止串口接收器
        self.timer_send.stop()  # 停止定时发送定时器
        try:
            self.ser.close()
        except:
            pass
        self.open_button.setEnabled(True)  # 设置打开按钮为正常,可点击
        self.close_button.setEnabled(False)  # 设置关闭按钮为灰色,不可点击
        self.lineEdit_3.setEnabled(True)
        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))
        self.formGroupBox1.setTitle("串口状态（已关闭）")

    # 发送数据
    def data_send(self):
        mosz0 = 'BB AA 04 64 FF 08 97'
        mosz1 = 'BB AA 04 64 FF 09 96'
        mosc0 = 'BB AA 04 64 FF 0A 95'
        mosc1 = 'BB AA 04 64 FF 0B 94'
        mosf0 = 'BB AA 04 64 FF 0C 93'
        mosf1 = 'BB AA 04 64 FF 0B 92'
        ledr0 = 'BB AA 04 64 FF 20 BF'
        ledr1 = 'BB AA 04 64 FF 21 BE'
        ledg0 = 'BB AA 04 64 FF 22 BD'
        ledg1 = 'BB AA 04 64 FF 23 BC'
        bz0 = 'BB AA 04 64 FF 24 BB'
        bz1 = 'BB AA 04 64 FF 25 BA'
        vc0 = 'BB AA 04 64 FF 26 B9'
        vc1 = 'BB AA 04 64 FF 27 B8'
        relay0 = 'BB AA 04 64 FF 28 B7'
        relay1 = 'BB AA 04 64 FF 29 B6'
        fan0 = 'BB AA 04 64 FF 2A B5'
        fan1 = 'BB AA 04 64 FF 2B B4'
        list2=[]
        if self.mos1.checkState():
            list2.append(mosz0)
            list2.append(mosz1)
        else:
            pass
        if self.mos2.checkState():
            list2.append(mosc0)
            list2.append(mosc1)
        else:
            pass
        if self.mos3.checkState():
            list2.append(mosf0)
            list2.append(mosf1)
        else:
            pass
        if self.ledr.checkState():
            list2.append(ledr1)
            list2.append(ledr0)
        else:
            pass
        if self.ledg.checkState():
            list2.append(ledg1)
            list2.append(ledg0)
        else:
            pass
        if self.bz.checkState():
            list2.append(bz0)
            list2.append(bz1)
        else:
            pass
        if self.vc.checkState():
            list2.append(vc0)
            list2.append(vc1)
        else:
            pass
        if self.relay.checkState():
            list2.append(relay0)
            list2.append(relay1)
        else:
            pass
        if self.fan.checkState():
            list2.append(fan0)
            list2.append(fan1)
        else:
            pass
        if self.ser.isOpen():
            for p in list2:
                time.sleep(1)
                input_s = p.strip()  # 去除首尾的空格
                print(input_s)
                input_s = bytes.fromhex(input_s)
                print(input_s)
                self.ser.write(input_s)


        else:
            pass

    # 接收数据
    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return None
        if num > 0:
            data = self.ser.read(num)
            num = len(data)
            # hex显示
            out_s = ''
            for i in range(0, len(data)):
                out_s = out_s + '{:02X}'.format(data[i]) + ' '
            self.s2__receive_text.insertPlainText(out_s)

            # 统计接收字符的数量
            self.data_num_received += num
            self.lineEdit.setText(str(self.data_num_received))

            # 获取到text光标
            textCursor = self.s2__receive_text.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            self.s2__receive_text.setTextCursor(textCursor)
        else:
            pass

    # 定时发送数据
    def data_send_timer(self):
        if self.timer_send_cb.isChecked():
            self.timer_send.start(int(self.lineEdit_3.text()))
            self.lineEdit_3.setEnabled(False)
        else:
            self.timer_send.stop()
            self.lineEdit_3.setEnabled(True)

    # 清除显示
    def send_data_clear(self):
        self.s3__send_text.setText("")

    def receive_data_clear(self):
        self.s2__receive_text.setText("")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5_Serial()
    myshow.show()
    sys.exit(app.exec_())
