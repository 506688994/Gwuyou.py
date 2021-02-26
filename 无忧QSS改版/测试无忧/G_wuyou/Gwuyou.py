import sys

from PyQt5.QtGui import QTextCursor
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

import uart1
import uart2
from HomePages.ui_mainpage import MainUi


class GWuYou(QMainWindow, MainUi):
    version = '1.0.0'

    def __init__(self, parent=None):
        super(GWuYou, self).__init__(parent)
        self.setupUi(self)
        self.uart1 = uart1.Uart(self)
        self.uart2 = uart2.Uart(self)

        self.create_signal_slot()  # 初始化信号
    # 设置信号与槽
    def create_signal_slot(self):
        # Action
        # self.BmsTestPageUi.BmsTest_Signal.connect(self.write_data2)  # 打开关闭工厂模式
        self.BmsTestPageUi.BmsTest_Signal.connect(self.write_data2)  # 发送bms工程测试指令
        self.setComPageUi.SetCom_Signal1.connect(self.open_serial1)  # 打开串口一
        self.setComPageUi.SetCom_Signal2.connect(self.open_serial2)  # 打开串口二
        self.uart1.readyRead.connect(self.receive_serial1)  # 接收数据
        self.uart2.readyRead.connect(self.receive_serial2)  # 接收数据

        # self.uart.signal_update_standard_gui.connect(self.update_standard_gui)
        # self.tabWidget_other.currentChanged.connect(self.update_standard_gui)

    def send_read_mcu(self):
        # 工厂模式 #
        if self.uart2.isOpen():
            start = b'\xb3\x00'
            self.uart2.write(start)

    # **********************************************
    #                 串口一
    # **********************************************
    def open_serial1(self):
        # com Open Code here #
        com_name = self.setComPageUi.com1_com.currentText()
        com_baud = int(self.setComPageUi.com1_por.currentText())
        self.uart1.setPortName(com_name)
        self.uart1.setBaudRate(com_baud)

        try:
            if not self.uart1.open(QSerialPort.ReadWrite):
                QMessageBox.critical(self, '严重错误', '串口打开失败')
                return
        except Exception as e:
            print(e)
            QMessageBox.critical(self, '严重错误', '串口打开失败')
            return
        self.setComPageUi.right_com_label_com1.setText('  已打开')
        # self.set_widgets_enabled(False)#设置其他为灰色不可点击
        self.setComPageUi.SetCom_Signal1.disconnect()
        self.setComPageUi.SetCom_Signal1.connect(self.close_serial1)

    def close_serial1(self):
        # close Serial #
        self.uart1.close()
        # self.set_widgets_enabled(True)  # 设置其他为可点击
        self.setComPageUi.right_com_label_com1.setText('  已关闭')
        self.setComPageUi.SetCom_Signal1.disconnect()
        self.setComPageUi.SetCom_Signal1.connect(self.open_serial1)

    def write_data1(self, data):
        # write data serial2 #
        if self.uart1.isOpen():
            data = data.strip()
            self.uart1.write(bytes.fromhex(data))
            print(data)
        else:
            if not self.uart1.open(QSerialPort.ReadWrite):
                QMessageBox.critical(self, '严重错误', '串口未打开')
                return

    def receive_serial1(self):
        # 串口一接受数据
        tab_widget_current_index = self.tabWidget.currentIndex()
        if tab_widget_current_index == 0:  # 收发模式
            try:
                msg = self.uart1.com_receive_normal(self.hexShowing_checkBox.isChecked(),
                                                    self.comboBox_codetype.currentText())
                self.textEdit_Recive.moveCursor(QTextCursor.End)
                self.textEdit_Recive.insertPlainText(msg)
            except Exception as e:
                print(e)
                QMessageBox.critical(self, '严重错误', '串口接收数据错误')
        else:
            self.uart1.com_receive_standard()  # 标准模式读取

    # ***********************************************
    #                   串口二
    # ***********************************************
    def open_serial2(self):
        # com Open Code here #
        com_name = self.setComPageUi.com2_com.currentText()
        com_baud = int(self.setComPageUi.com2_por.currentText())
        self.uart2.setPortName(com_name)
        self.uart2.setBaudRate(com_baud)

        try:
            if not self.uart2.open(QSerialPort.ReadWrite):
                QMessageBox.critical(self, '严重错误', '串口打开失败')
                return
        except Exception as e:
            print(e)
            QMessageBox.critical(self, '严重错误', '串口打开失败')
            return
        self.setComPageUi.right_com_label_com2.setText('  已打开')
        # self.set_widgets_enabled(False)#设置其他为灰色不可点击
        self.setComPageUi.SetCom_Signal2.disconnect()
        self.setComPageUi.SetCom_Signal2.connect(self.close_serial2)

    def close_serial2(self):
        # close Serial #
        self.uart2.close()
        # self.set_widgets_enabled(True)  # 设置其他为可点击
        self.setComPageUi.right_com_label_com2.setText('  已关闭')
        self.setComPageUi.SetCom_Signal2.disconnect()
        self.setComPageUi.SetCom_Signal2.connect(self.open_serial2)

    def write_data2(self, data):
        print('22')
        # write data serial2 #
        if self.uart2.isOpen():
            data = data.strip()
            self.uart2.write(bytes.fromhex(data))
            print(data)
        else:
            print('11')
            if not self.uart2.open(QSerialPort.ReadWrite):
                QMessageBox.critical(self, '严重错误', '串口未打开')
                return

    def receive_serial2(self):
        # 串口二接受数据
        tab_widget_current_index = self.tabWidget.currentIndex()
        if tab_widget_current_index == 0:  # 收发模式
            try:
                msg = self.uart2.com_receive_normal(self.hexShowing_checkBox.isChecked(),
                                                    self.comboBox_codetype.currentText())

                self.textEdit_Recive.moveCursor(QTextCursor.End)
                self.textEdit_Recive.insertPlainText(msg)
            except Exception as e:
                print(e)
                QMessageBox.critical(self, '严重错误', '串口接收数据错误')
        else:
            self.uart2.com_receive_standard()  # 标准模式读取

    """
    def update_standard_gui(self, index_receive):
        # 读参数
        index = self.tabWidget_other.currentIndex()
        if index == 0 and index_receive in (0, 2):  # 读参数模式
            # self.tableWidget_para.setRowCount(len(self.uart2.watch_paras)+len(self.uart2.wave_paras))
            for key in self.uart2.watch_paras:
                lis = self.tableWidget_para.findItems(key, Qt.MatchExactly)
                value = self.uart2.watch_paras[key]
                if len(lis) > 0 and lis[0].column() == 0:  # 有该元素
                    row = lis[0].row()
                    self.tableWidget_para.item(row, 1).setText(value)
                else:  # 没有该元素
                    length = self.tableWidget_para.rowCount()
                    self.tableWidget_para.insertRow(length)
                    self.tableWidget_para.setItem(length, 0, QTableWidgetItem(key))
                    self.tableWidget_para.setItem(length, 1, QTableWidgetItem(value))
                    self.tableWidget_para.sortByColumn(0, 0)

            for key in self.uart2.wave_paras:
                lis = self.tableWidget_para.findItems(key, Qt.MatchExactly)
                value = self.uart2.wave_paras[key]
                if len(lis) > 0 and lis[0].column() == 0:  # 有该元素
                    row = lis[0].row()
                    self.tableWidget_para.item(row, 1).setText(value)
                else:  # 没有该元素
                    length = self.tableWidget_para.rowCount()
                    self.tableWidget_para.insertRow(length)
                    self.tableWidget_para.setItem(length, 0, QTableWidgetItem(key))
                    self.tableWidget_para.setItem(length, 1, QTableWidgetItem(value))
                    self.tableWidget_para.sortByColumn(0, 0)

        elif index == 1 and index_receive == 1:  # 改参数模式
            # item.paras.value = value
            error_keys = list()
            for key in self.uart2.change_paras:
                value_str = self.uart2.change_paras[key]
                try:
                    pos, va = value_str.split(',', 1)
                except:
                    print('read change para error')
                    error_keys.append(key)
                    # self.uart2.change_paras.pop(key)
                    pass
                else:  # 正常解析
                    if key in self.paraWidgets:
                        self.paraWidgets[key].para_value.setText(va)
                    else:
                        para_widget = Widget_ParaItem(key, pos, va, self.uart2)
                        self.paraWidgets[key] = para_widget
                        para_list_widget_item = QListWidgetItem(self.listWidget_para)
                        self.listWidget_para.addItem(para_list_widget_item)
                        self.listWidget_para.setItemWidget(
                            para_list_widget_item, para_widget)
                        size = para_widget.minimumSizeHint()
                        para_list_widget_item.setSizeHint(size)
                # #
                # index_2 = int(key)
                # if index_2 >= len(self.paraWidgets):
                #
                #     # self.listWidget_para.addItem()
                #     self.paraWidgets.append(para_widget)
                #     para_listWidgetItem = QListWidgetItem(self.listWidget_para)
                #     self.listWidget_para.addItem(para_listWidgetItem)
                #     self.listWidget_para.setItemWidget(
                #         para_listWidgetItem, para_widget)
                #     size = para_widget.minimumSizeHint()
                #     para_listWidgetItem.setSizeHint(size)
                # self.paraWidgets[index_2].index = key
                # self.paraWidgets[index_2].para_value.setText(self.uart2.change_paras[key])
                # self.paraWidgets[index_2].paras.value = self.uart2.change_paras[key]
            for k in error_keys:
                del self.uart2.change_paras[k]
        elif index == 2 and index_receive == 2:  # 波形模式
            # self.graphicsView.add_new_data(self.uart2.wave_paras)
            if not self.wave_thread.dic_queue.full():
                self.wave_thread.dic_queue.put(self.uart2.wave_paras)
        elif index_receive == -1:  # 修改参数成功
            # ss = self.uart2.standard_rx_data[1:].data().decode(errors='ignore')
            # self.uart2.standard_rx_data.clear()
            if len(self.uart2.list_of_msg) > 0:
                ss = self.uart2.list_of_msg[0].data().decode(errors='ignore')
                QMessageBox.information(self, '成功', '成功修改参数为：' + ss)

    
    # =================================================
    # 窗口拖动方法
    # =================================================
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
    """


def main():
    app = QApplication(sys.argv)
    my_win = GWuYou()
    my_win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
