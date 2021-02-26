# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: c:\Users\1230\Desktop\Pyserial-Demo-master\ui_demo_1.py
# Compiled at: 2020-05-23 15:11:22
# Size of source mod 2**32: 12618 bytes
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName('Form')  #主界面
        Form.resize(1280, 768)

        self.formgroupBox = QtWidgets.QGroupBox(Form) #功能区测试模块
        self.formgroupBox.setGeometry(QtCore.QRect(210, 20, 950, 66))
        self.formgroupBox.setObjectName("groupBox")
        self.mos1 = QtWidgets.QCheckBox(self.formgroupBox)      #支路mos闭合
        self.mos1.setGeometry(QtCore.QRect(20, 30, 89, 16))
        self.mos1.setObjectName("MOS1")
        self.mos2 = QtWidgets.QCheckBox(self.formgroupBox)      # 充电mos闭合
        self.mos2.setGeometry(QtCore.QRect(120, 30, 89, 16))
        self.mos2.setObjectName("MOS2")
        self.mos2.setChecked(True)
        self.mos3 = QtWidgets.QCheckBox(self.formgroupBox)      # 放电mos闭合
        self.mos3.setGeometry(QtCore.QRect(220, 30, 89, 16))
        self.mos3.setObjectName("MOS3")
        self.mos3.setChecked(True)
        self.ledr = QtWidgets.QCheckBox(self.formgroupBox)      # 红色LED
        self.ledr.setGeometry(QtCore.QRect(320, 30, 89, 16))
        self.ledr.setObjectName("ledr")
        self.ledg = QtWidgets.QCheckBox(self.formgroupBox)      # 绿色LED
        self.ledg.setGeometry(QtCore.QRect(420, 30, 89, 16))
        self.ledg.setObjectName("ledg")
        self.bz = QtWidgets.QCheckBox(self.formgroupBox)  # 蜂鸣器
        self.bz.setGeometry(QtCore.QRect(520, 30, 89, 16))
        self.bz.setObjectName("bz")
        self.vc = QtWidgets.QCheckBox(self.formgroupBox)  # 语音
        self.vc.setGeometry(QtCore.QRect(620, 30, 89, 16))
        self.vc.setObjectName("vc")
        self.relay = QtWidgets.QCheckBox(self.formgroupBox)  # 继电器
        self.relay.setGeometry(QtCore.QRect(720, 30, 89, 16))
        self.relay.setObjectName("relay")
        self.fan = QtWidgets.QCheckBox(self.formgroupBox)  # 风扇
        self.fan.setGeometry(QtCore.QRect(820, 30, 89, 16))
        self.fan.setObjectName("fan")


        self.formgroupBox1 = QtWidgets.QGroupBox(Form)
        self.formgroupBox1.setGeometry(QtCore.QRect(210, 150, 950, 66))
        self.formgroupBox1.setObjectName("jiaozhun")
        self.dci = QtWidgets.QCheckBox(self.formgroupBox1)  #电流校准
        self.dci.setGeometry(QtCore.QRect(20, 30, 89, 16))
        self.dci.setObjectName("dci")
        self.dcv = QtWidgets.QCheckBox(self.formgroupBox1)  #电压校准
        self.dcv.setGeometry(QtCore.QRect(120, 30, 89, 16))
        self.dcv.setObjectName("dcv")

        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setGeometry(QtCore.QRect(20, 20, 167, 301))       #串口设置界面
        self.formGroupBox.setObjectName('formGroupBox')
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName('formLayout')
        self.s1__lb_1 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_1.setObjectName('s1__lb_1')

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.s1__lb_1)
        self.s1__box_1 = QtWidgets.QPushButton(self.formGroupBox)
        self.s1__box_1.setAutoRepeatInterval(100)
        self.s1__box_1.setDefault(True)
        self.s1__box_1.setObjectName('s1__box_1')
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.s1__box_1)
        self.s1__lb_2 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_2.setObjectName('s1__lb_2')
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.s1__lb_2)
        self.s1__box_2 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_2.setObjectName('s1__box_2')
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.s1__box_2)
        self.s1__lb_3 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_3.setObjectName('s1__lb_3')
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.s1__lb_3)
        self.s1__box_3 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_3.setObjectName('s1__box_3')
        self.s1__box_3.addItem('')
        self.s1__box_3.addItem('')
        self.s1__box_3.addItem('')
        self.s1__box_3.addItem('')
        self.s1__box_3.addItem('')
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.s1__box_3)
        self.s1__lb_4 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_4.setObjectName('s1__lb_4')
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.s1__lb_4)
        self.s1__box_4 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_4.setObjectName('s1__box_4')
        self.s1__box_4.addItem('')
        self.s1__box_4.addItem('')
        self.s1__box_4.addItem('')
        self.s1__box_4.addItem('')
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.s1__box_4)
        self.s1__lb_5 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_5.setObjectName('s1__lb_5')
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.s1__lb_5)
        self.s1__box_5 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_5.setObjectName('s1__box_5')
        self.s1__box_5.addItem('')
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.s1__box_5)
        self.open_button = QtWidgets.QPushButton(self.formGroupBox)
        self.open_button.setObjectName('open_button')
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.open_button)
        self.close_button = QtWidgets.QPushButton(self.formGroupBox)
        self.close_button.setObjectName('close_button')
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.close_button)
        self.s1__lb_6 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_6.setObjectName('s1__lb_6')
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.s1__lb_6)
        self.s1__box_6 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_6.setObjectName('s1__box_6')
        self.s1__box_6.addItem('')
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.s1__box_6)
        self.state_label = QtWidgets.QLabel(self.formGroupBox)
        self.state_label.setText('')
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName('state_label')
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.state_label)

        self.verticalGroupBox = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox.setGeometry(QtCore.QRect(210, 660, 1061, 101))         #接收区
        self.verticalGroupBox.setObjectName('verticalGroupBox')
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName('verticalLayout')
        self.s2__receive_text = QtWidgets.QTextBrowser(self.verticalGroupBox)
        self.s2__receive_text.setObjectName('s2__receive_text')
        self.verticalLayout.addWidget(self.s2__receive_text)

        self.verticalGroupBox_2 = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox_2.setGeometry(QtCore.QRect(210, 580, 1061, 70))        #发送区
        self.verticalGroupBox_2.setObjectName('verticalGroupBox_2')
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.s3__send_text = QtWidgets.QTextEdit(self.verticalGroupBox_2)
        self.s3__send_text.setObjectName('s3__send_text')
        self.verticalLayout_2.addWidget(self.s3__send_text)

        self.s3__send_button = QtWidgets.QPushButton(Form)                          #发送按钮
        self.s3__send_button.setGeometry(QtCore.QRect(1200, 360, 61, 31))
        self.s3__send_button.setObjectName('s3__send_button')
        self.s3__clear_button = QtWidgets.QPushButton(Form)                         #发送清除按钮
        self.s3__clear_button.setGeometry(QtCore.QRect(1200, 400, 61, 31))
        self.s3__clear_button.setObjectName('s3__clear_button')
        self.formGroupBox1 = QtWidgets.QGroupBox(Form)
        self.formGroupBox1.setGeometry(QtCore.QRect(20, 660, 171, 101))             #串口状态
        self.formGroupBox1.setObjectName('formGroupBox1')
        self.formLayout_2 = QtWidgets.QFormLayout(self.formGroupBox1)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName('formLayout_2')
        self.label = QtWidgets.QLabel(self.formGroupBox1)
        self.label.setObjectName('label')
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formGroupBox1)                         #已发送、接收
        self.label_2.setObjectName('label_2')
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formGroupBox1)
        self.lineEdit.setObjectName('lineEdit')
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formGroupBox1)
        self.lineEdit_2.setObjectName('lineEdit_2')
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.s2__clear_button = QtWidgets.QPushButton(Form)
        self.s2__clear_button.setGeometry(QtCore.QRect(1200, 80, 61, 31))        #接收清除
        self.s2__clear_button.setObjectName('s2__clear_button')
        self.timer_send_cb = QtWidgets.QCheckBox(Form)          #定时发送
        self.timer_send_cb.setGeometry(QtCore.QRect(1200, 300, 71, 16))
        self.timer_send_cb.setObjectName('timer_send_cb')
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)         #ms/次窗口
        self.lineEdit_3.setGeometry(QtCore.QRect(1200, 260, 61, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName('lineEdit_3')
        self.dw = QtWidgets.QLabel(Form)            #ms/次
        self.dw.setGeometry(QtCore.QRect(1240, 280, 54, 20))
        self.dw.setObjectName('dw')
        self.verticalGroupBox.raise_()
        self.verticalGroupBox_2.raise_()
        self.formGroupBox.raise_()
        self.s3__send_button.raise_()
        self.s3__clear_button.raise_()
        self.formGroupBox.raise_()
        #功能区测试
        self.mos1.raise_()
        self.mos2.raise_()
        self.mos3.raise_()
        self.ledr.raise_()
        self.ledg.raise_()
        self.bz.raise_()
        self.vc.raise_()
        self.relay.raise_()
        self.fan.raise_()
        #参数校准
        self.dci.raise_()
        self.dcv.raise_()

        self.s2__clear_button.raise_()
        self.timer_send_cb.raise_()
        self.lineEdit_3.raise_()
        self.dw.raise_()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate('Form', 'Form'))
        self.formGroupBox.setTitle(_translate('Form', '串口设置'))
        self.s1__lb_1.setText(_translate('Form', '串口检测：'))
        self.s1__box_1.setText(_translate('Form', '检测串口'))
        self.s1__lb_2.setText(_translate('Form', '串口选择：'))
        self.s1__lb_3.setText(_translate('Form', '波特率：'))
        self.s1__box_3.setItemText(0, _translate('Form','9600'))
        self.s1__box_3.setItemText(1, _translate('Form', '115200'))
        self.s1__lb_4.setText(_translate('Form', '数据位：'))
        self.s1__box_4.setItemText(0, _translate('Form', '8'))
        self.s1__lb_5.setText(_translate('Form', '校验位：'))
        self.s1__box_5.setItemText(0, _translate('Form', 'N'))
        self.open_button.setText(_translate('Form', '打开串口'))
        self.close_button.setText(_translate('Form', '关闭串口'))
        self.s1__lb_6.setText(_translate('Form', '停止位：'))
        self.s1__box_6.setItemText(0, _translate('Form', '1'))
        self.verticalGroupBox.setTitle(_translate('Form', '接受区'))
        self.verticalGroupBox_2.setTitle(_translate('Form', '发送区'))
        self.s3__send_text.setHtml(_translate('Form', '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;">\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">123456</p></body></html>'))
        self.s3__send_button.setText(_translate('Form', '发送'))
        self.s3__clear_button.setText(_translate('Form', '清除'))
        self.formGroupBox1.setTitle(_translate('Form', '串口状态'))
        self.label.setText(_translate('Form', '已接收：'))
        self.label_2.setText(_translate('Form', '已发送：'))
        self.s2__clear_button.setText(_translate('Form', '清除'))
        self.timer_send_cb.setText(_translate('Form', '测试间隔'))
        self.lineEdit_3.setText(_translate('Form', '1000'))
        self.dw.setText(_translate('Form', 'ms'))

        self.formgroupBox.setTitle(_translate("MainWindow", "功能区测试模块"))     #功能区测试模块
        self.mos1.setText(_translate("MainWindow", "支路MOS"))
        self.mos2.setText(_translate("MainWindow", "充电MOS"))
        self.mos3.setText(_translate("MainWindow", "放电MOS"))
        self.ledr.setText(_translate("MainWindow", "红色LED"))
        self.ledg.setText(_translate("MainWindow", "绿色LED"))
        self.bz.setText(_translate("MainWindow", "蜂鸣器"))
        self.vc.setText(_translate("MainWindow", "语音模块"))
        self.relay.setText(_translate("MainWindow", "继电器"))
        self.fan.setText(_translate("MainWindow", "风扇"))

        self.formgroupBox1.setTitle(_translate("MainWindow", "参数校准模块"))     #校准模块
        self.dci.setText(_translate("MainWindow", "电流归零"))
        self.dcv.setText(_translate("MainWindow", "电压校准"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    Ui_Form().setupUi(widget)
    sys.exit(app.exec_())
