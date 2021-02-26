# -*- coding:utf-8 -*-
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt, pyqtSignal, QPoint
from PyQt5.QtGui import QFont, QEnterEvent, QPainter, QColor, QPen, QTextCursor
from PyQt5.QtGui import QIcon
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

import uart1
import uart2
from HomePages.ui_mainpage import MainUi

# LeftTabWidget
# 样式
StyleSheet = """
/*标题栏*/
TitleBar {
    background-color: red;
}
/*最小化最大化关闭按钮通用默认背景*/
#buttonMinimum,#buttonMaximum,#buttonClose {
    border: none;
    background-color: red;
}
/*悬停*/
#buttonMinimum:hover,#buttonMaximum:hover {
    background-color: red;
    color: white;
}
#buttonClose:hover {
    color: white;
}
/*鼠标按下不放*/
#buttonMinimum:pressed,#buttonMaximum:pressed {
    background-color: Firebrick;
}
#buttonClose:pressed {
    color: white;
    background-color: Firebrick;
}
"""


class TitleBar(QWidget):
    # 窗口最小化信号
    windowMinimumed = pyqtSignal()
    # 窗口最大化信号
    windowMaximumed = pyqtSignal()
    # 窗口还原信号
    windowNormaled = pyqtSignal()
    # 窗口关闭信号
    windowClosed = pyqtSignal()
    # 窗口移动
    windowMoved = pyqtSignal(QPoint)

    def __init__(self, *args, **kwargs):
        super(TitleBar, self).__init__(*args, **kwargs)
        # 支持qss设置背景
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.mPos = None
        self.iconSize = 20  # 图标的默认大小
        # 设置默认背景颜色,否则由于受到父窗口的影响导致透明
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(palette.Window, QColor(240, 240, 240))
        self.setPalette(palette)
        # 布局
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        # 窗口图标
        self.iconLabel = QLabel(self)
        #         self.iconLabel.setScaledContents(True)
        layout.addWidget(self.iconLabel)
        # 窗口标题
        self.titleLabel = QLabel(self)
        self.titleLabel.setMargin(2)
        layout.addWidget(self.titleLabel)
        # 中间伸缩条
        layout.addSpacerItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        # 利用Webdings字体来显示图标
        font = self.font() or QFont()
        font.setFamily('Webdings')
        # 最小化按钮
        self.buttonMinimum = QPushButton(
            '0', self, clicked=self.windowMinimumed.emit, font=font, objectName='buttonMinimum')
        layout.addWidget(self.buttonMinimum)
        # 最大化/还原按钮
        self.buttonMaximum = QPushButton(
            '1', self, clicked=self.showMaximized, font=font, objectName='buttonMaximum')
        layout.addWidget(self.buttonMaximum)
        # 关闭按钮
        self.buttonClose = QPushButton(
            'r', self, clicked=self.windowClosed.emit, font=font, objectName='buttonClose')
        layout.addWidget(self.buttonClose)
        # 初始高度
        self.setHeight()

    def showMaximized(self):
        if self.buttonMaximum.text() == '1':
            # 最大化
            self.buttonMaximum.setText('2')
            self.windowMaximumed.emit()
        else:  # 还原
            self.buttonMaximum.setText('1')
            self.windowNormaled.emit()

    def setHeight(self, height=38):
        """设置标题栏高度"""
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)
        # 设置右边按钮的大小
        self.buttonMinimum.setMinimumSize(height, height)
        self.buttonMinimum.setMaximumSize(height, height)
        self.buttonMaximum.setMinimumSize(height, height)
        self.buttonMaximum.setMaximumSize(height, height)
        self.buttonClose.setMinimumSize(height, height)
        self.buttonClose.setMaximumSize(height, height)

    def setTitle(self, title):
        """设置标题"""
        self.titleLabel.setText(title)

    def setIcon(self, icon):
        """设置图标"""
        self.iconLabel.setPixmap(icon.pixmap(self.iconSize, self.iconSize))

    def setIconSize(self, size):
        """设置图标大小"""
        self.iconSize = size

    def enterEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        super(TitleBar, self).enterEvent(event)

    def mouseDoubleClickEvent(self, event):
        super(TitleBar, self).mouseDoubleClickEvent(event)
        self.showMaximized()

    def mousePressEvent(self, event):
        """鼠标点击事件"""
        if event.button() == Qt.LeftButton:
            self.mPos = event.pos()
        event.accept()

    def mouseReleaseEvent(self, event):
        # 鼠标弹起事件
        self.mPos = None
        event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mPos:
            self.windowMoved.emit(self.mapToGlobal(event.pos() - self.mPos))
        event.accept()


# 枚举左上右下以及四个定点
Left, Top, Right, Bottom, LeftTop, RightTop, LeftBottom, RightBottom = range(8)


class FramelessWindow(QWidget):
    # 四周边距
    Margins = 5

    def __init__(self, *args, **kwargs):
        super(FramelessWindow, self).__init__(*args, **kwargs)

        self._pressed = False
        self.Direction = None
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 无边框
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框
        # 鼠标跟踪
        self.setMouseTracking(True)
        # 布局
        layout = QVBoxLayout(self, spacing=0)
        # 预留边界用于实现无边框窗口调整大小
        layout.setContentsMargins(
            self.Margins, self.Margins, self.Margins, self.Margins)
        # 标题栏
        self.titleBar = TitleBar(self)
        layout.addWidget(self.titleBar)
        # 信号槽
        self.titleBar.windowMinimumed.connect(self.showMinimized)
        self.titleBar.windowMaximumed.connect(self.showMaximized)
        self.titleBar.windowNormaled.connect(self.showNormal)
        self.titleBar.windowClosed.connect(self.close)
        self.titleBar.windowMoved.connect(self.move)
        self.windowTitleChanged.connect(self.titleBar.setTitle)
        self.windowIconChanged.connect(self.titleBar.setIcon)

    def setTitleBarHeight(self, height=38):
        """设置标题栏高度"""
        self.titleBar.setHeight(height)

    def setIconSize(self, size):
        """设置图标的大小"""
        self.titleBar.setIconSize(size)

    def setWidget(self, widget):
        """设置自己的控件"""
        if hasattr(self, '_widget'):
            return
        self._widget = widget
        # 设置默认背景颜色,否则由于受到父窗口的影响导致透明
        self._widget.setAutoFillBackground(True)
        palette = self._widget.palette()
        palette.setColor(palette.Window, QColor(240, 240, 240))
        self._widget.setPalette(palette)
        self._widget.installEventFilter(self)
        self.layout().addWidget(self._widget)

    def move(self, pos):
        if self.windowState() == Qt.WindowMaximized or self.windowState() == Qt.WindowFullScreen:
            # 最大化或者全屏则不允许移动
            return
        super(FramelessWindow, self).move(pos)

    def showMaximized(self):
        """最大化,要去除上下左右边界,如果不去除则边框地方会有空隙"""
        super(FramelessWindow, self).showMaximized()
        self.layout().setContentsMargins(0, 0, 0, 0)

    def showNormal(self):
        """还原,要保留上下左右边界,否则没有边框无法调整"""
        super(FramelessWindow, self).showNormal()
        self.layout().setContentsMargins(
            self.Margins, self.Margins, self.Margins, self.Margins)

    def eventFilter(self, obj, event):
        """事件过滤器,用于解决鼠标进入其它控件后还原为标准鼠标样式"""
        if isinstance(event, QEnterEvent):
            self.setCursor(Qt.ArrowCursor)
        return super(FramelessWindow, self).eventFilter(obj, event)

    def paintEvent(self, event):
        """由于是全透明背景窗口,重绘事件中绘制透明度为1的难以发现的边框,用于调整窗口大小"""
        super(FramelessWindow, self).paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(255, 255, 255, 1), 2 * self.Margins))
        painter.drawRect(self.rect())

    def mousePressEvent(self, event):
        """鼠标点击事件"""
        super(FramelessWindow, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self._mpos = event.pos()
            self._pressed = True

    def mouseReleaseEvent(self, event):
        '''鼠标弹起事件'''
        super(FramelessWindow, self).mouseReleaseEvent(event)
        self._pressed = False
        self.Direction = None

    def mouseMoveEvent(self, event):
        """鼠标移动事件"""
        super(FramelessWindow, self).mouseMoveEvent(event)
        pos = event.pos()
        xPos, yPos = pos.x(), pos.y()
        wm, hm = self.width() - self.Margins, self.height() - self.Margins
        if self.isMaximized() or self.isFullScreen():
            self.Direction = None
            self.setCursor(Qt.ArrowCursor)
            return
        if event.buttons() == Qt.LeftButton and self._pressed:
            self._resizeWidget(pos)
            return
        if xPos <= self.Margins and yPos <= self.Margins:
            # 左上角
            self.Direction = LeftTop
            self.setCursor(Qt.SizeFDiagCursor)
        elif wm <= xPos <= self.width() and hm <= yPos <= self.height():
            # 右下角
            self.Direction = RightBottom
            self.setCursor(Qt.SizeFDiagCursor)
        elif wm <= xPos and yPos <= self.Margins:
            # 右上角
            self.Direction = RightTop
            self.setCursor(Qt.SizeBDiagCursor)
        elif xPos <= self.Margins and hm <= yPos:
            # 左下角
            self.Direction = LeftBottom
            self.setCursor(Qt.SizeBDiagCursor)
        elif 0 <= xPos <= self.Margins <= yPos <= hm:
            # 左边
            self.Direction = Left
            self.setCursor(Qt.SizeHorCursor)
        elif wm <= xPos <= self.width() and self.Margins <= yPos <= hm:
            # 右边
            self.Direction = Right
            self.setCursor(Qt.SizeHorCursor)
        elif wm >= xPos >= self.Margins >= yPos >= 0:
            # 上面
            self.Direction = Top
            self.setCursor(Qt.SizeVerCursor)
        elif self.Margins <= xPos <= wm and hm <= yPos <= self.height():
            # 下面
            self.Direction = Bottom
            self.setCursor(Qt.SizeVerCursor)

    def _resizeWidget(self, pos):
        """调整窗口大小"""
        if self.Direction is None:
            return
        mpos = pos - self._mpos
        xPos, yPos = mpos.x(), mpos.y()
        geometry = self.geometry()
        x, y, w, h = geometry.x(), geometry.y(), geometry.width(), geometry.height()
        if self.Direction == LeftTop:  # 左上角
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
        elif self.Direction == RightBottom:  # 右下角
            if w + xPos > self.minimumWidth():
                w += xPos
                self._mpos = pos
            if h + yPos > self.minimumHeight():
                h += yPos
                self._mpos = pos
        elif self.Direction == RightTop:  # 右上角
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
            if w + xPos > self.minimumWidth():
                w += xPos
                self._mpos.setX(pos.x())
        elif self.Direction == LeftBottom:  # 左下角
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            if h + yPos > self.minimumHeight():
                h += yPos
                self._mpos.setY(pos.y())
        elif self.Direction == Left:  # 左边
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            else:
                return
        elif self.Direction == Right:  # 右边
            if w + xPos > self.minimumWidth():
                w += xPos
                self._mpos = pos
            else:
                return
        elif self.Direction == Top:  # 上面
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
            else:
                return
        elif self.Direction == Bottom:  # 下面
            if h + yPos > self.minimumHeight():
                h += yPos
                self._mpos = pos
            else:
                return
        self.setGeometry(x, y, w, h)


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.mainui_widget = MainUi()
        layout.addWidget(self.mainui_widget)

        self.uart1 = uart1.Uart(self)
        self.uart2 = uart2.Uart(self)

        self.create_signal_slot()  # 初始化信号
        # 设置信号与槽

    def create_signal_slot(self):
        # Action
        # self.BmsTestPageUi.BmsTest_Signal.connect(self.write_data2)  # 打开关闭工厂模式
        self.mainui_widget.BmsTestPageUi.BmsTest_Signal.connect(self.write_data2)  # 发送bms工程测试指令
        self.mainui_widget.setComPageUi.SetCom_Signal1.connect(self.open_serial1)  # 打开串口一
        self.mainui_widget.setComPageUi.SetCom_Signal2.connect(self.open_serial2)  # 打开串口二
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
        com_name = self.mainui_widget.setComPageUi.com1_com.currentText()
        com_baud = int(self.mainui_widget.setComPageUi.com1_por.currentText())
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
        self.mainui_widget.setComPageUi.right_com_label_com1.setText('  已打开')
        # self.set_widgets_enabled(False)#设置其他为灰色不可点击
        self.mainui_widget.setComPageUi.SetCom_Signal1.disconnect()
        self.mainui_widget.setComPageUi.SetCom_Signal1.connect(self.close_serial1)

    def close_serial1(self):
        # close Serial #
        self.uart1.close()
        # self.set_widgets_enabled(True)  # 设置其他为可点击
        self.mainui_widget.setComPageUi.right_com_label_com1.setText('  已关闭')
        self.mainui_widget.setComPageUi.SetCom_Signal1.disconnect()
        self.mainui_widget.setComPageUi.SetCom_Signal1.connect(self.open_serial1)

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
        com_name = self.mainui_widget.setComPageUi.com2_com.currentText()
        com_baud = int(self.mainui_widget.setComPageUi.com2_por.currentText())
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
        self.mainui_widget.setComPageUi.right_com_label_com2.setText('  已打开')
        # self.set_widgets_enabled(False)#设置其他为灰色不可点击
        self.mainui_widget.setComPageUi.SetCom_Signal2.disconnect()
        self.mainui_widget.setComPageUi.SetCom_Signal2.connect(self.close_serial2)

    def close_serial2(self):
        # close Serial #
        self.uart2.close()
        # self.set_widgets_enabled(True)  # 设置其他为可点击
        self.mainui_widget.setComPageUi.right_com_label_com2.setText('  已关闭')
        self.mainui_widget.setComPageUi.SetCom_Signal2.disconnect()
        self.mainui_widget.setComPageUi.SetCom_Signal2.connect(self.open_serial2)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    mainWnd = FramelessWindow()
    mainWnd.setWindowTitle('测试标题栏')
    mainWnd.setWindowIcon(QIcon('Qt.ico'))
    mainWnd.resize(QSize(800, 500))
    mainWnd.setWidget(MainWindow(mainWnd))  # 把自己的窗口添加进来
    mainWnd.show()
    sys.exit(app.exec_())
