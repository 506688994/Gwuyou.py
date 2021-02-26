# !/usr/bin/python 3.6.5
# coding=utf-8

import serial
import serial.tools.list_ports
import threading

'''
    1、扫描串口列表
    2、打开串口
    3、向串口写数据
    4、从串口读数据
    5、关闭串口

    init 初始化串口
        --> 创建线程：
            1. 如果串口未打开，则用于实时扫描串口，检测是否有新设备插入
                有新设备插入：添加到设备列表，并刷新UI的设备列表提供选择
                没有新设备：继续扫描
            2. 如果串口已打开，则用于监测串口是否有接收到数据
                如果有则读取数据，并发送给UI
                如果没有则继续扫描
        参数：主窗口，端口列表，接收窗口
        返回：线程实例(用于关闭窗口前，先关闭线程)

    open 打开串口
        --> 参数：端口号，波特率，超时时间
            返回：串口实例（打开成功）/ None(打开失败)

    close 关闭串口
        --> 参数：串口实例
            返回：0（关闭成功）/ -1（关闭失败）

    write 写数据
    read 读数据

'''

SERIAL_IS_OPEN = False  # 默认串口关闭
port_name_list = []  # 端口名称列表
port_com_list = []  # 端口号列表
MySerial = None  # 打开的串口


def 扫描串口():
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) > 0:
        return port_list
    else:
        return None


def 打开串口(port="COM4", bps=115200, timex=5):
    try:
        # 打开串口
        ser = serial.Serial(port, bps, timeout=timex)

        if ser.is_open:
            global SERIAL_IS_OPEN
            SERIAL_IS_OPEN = True
            print("--- 串口打开 ---")
            return ser

    except Exception as e:
        print("--- 打开异常 ---: ", e)
        return None


def 发送数据(ser, text, code="utf-8"):
    try:
        result = ser.write(text.encode(code))
        if result == len(text):
            print("--- 发送成功 ---：", text)
            return result
        else:
            print("--- 发送错误 ---：", "data len:", len(text), "send len:", result)
            return None
    except Exception as e:
        print("--- 发送异常 ---：", e)


def 读取数据(ser, code="utf-8"):
    if ser.in_waiting:
        str = ser.read(ser.in_waiting).decode(code)
        print("--- 读到数据 ---：", str)
        return str
    else:
        return None


def 关闭串口(ser):
    if ser.is_open:
        try:
            global SERIAL_IS_OPEN
            SERIAL_IS_OPEN = False
            ser.close()
            print("--- 串口关闭 ---")
            return 0
        except Exception as e:
            print("--- 关闭异常 ---：", e)
            return -1
    else:
        print("--- 错误 ---：串口未打开！")
        return -1


class SERIAL:
    def __init__(self):
        self.ser = None
        self.get_str = ''
        self.master = None
        self.show_com = None
        self.read_text_win = None
        self.serialThread = None

    def serial_thread(self, master, list_port, text_read):
        global SERIAL_IS_OPEN, port_name_list, port_com_list
        global MySerial
        while True:
            if SERIAL_IS_OPEN:
                self.get_str = 读取数据(MySerial)
                if self.get_str:
                    # print(self.get_str)
                    text_read.insert(tk.END, self.get_str)
                    master.update()
            else:
                port_list = 扫描串口()
                if len(port_name_list) is not len(port_list):  # 只判断列表长度，不可靠。需修改为列表内容判断比较可靠
                    port_name_list.clear()
                    port_com_list.clear()
                    for i in range(0, len(port_list)):
                        port_name_list.append(port_list[i].description)
                        port_com_list.append(port_list[i].device)
                        list_port["values"] = port_name_list
                        if list_port.get() is "":  # 如果当前UI中的端口列表为空，则指定显示第一个
                            list_port.current(0)
                    master.update()

    @classmethod
    def init(cls, master, list_port, text_read):
        cls.master = master
        cls.show_com = list_port
        cls.read_text_win = text_read
        cls.serialThread = threading.Thread(target=cls.serial_thread,
                                            args=(SERIAL, cls.master, cls.show_com, cls.read_text_win))
        cls.serialThread.start()
        return cls.serialThread

    @classmethod
    def open(cls, port=None, bps=115200, timex=5):
        global port_name_list, port_com_list, MySerial
        if not port:
            port_name = cls.show_com.get()
            index = port_name_list.index(port_name)
            MySerial = 打开串口(port_com_list[index], bps, timex)
        else:
            MySerial = 打开串口(port, bps, timex)

    @staticmethod
    def write(text, coding="gbk"):
        global MySerial, SERIAL_IS_OPEN
        if SERIAL_IS_OPEN:
            发送数据(MySerial, text, coding)

    @staticmethod
    def read(coding="gbk"):
        global MySerial, SERIAL_IS_OPEN
        str = None
        if SERIAL_IS_OPEN:
            str = 读取数据(MySerial, coding)
        return str

    @staticmethod
    def close():
        global MySerial, SERIAL_IS_OPEN
        if SERIAL_IS_OPEN and MySerial:
            关闭串口(MySerial)


if __name__ == "__main__":
    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.title("测试窗口")
    root.geometry("300x300")

    list_box = ttk.Combobox(
        root, width=22, textvariable=port_name_list, state="readonly")
    list_box.place(x=10, y=10)

    text_box = tk.Text(root, width=25, heigh=10)
    text_box.place(x=10, y=50)

    def open_serial():
        SERIAL.open()

    def send_date():
        SERIAL.write("hello python serial\n", coding="gbk")

    def close_serial():
        SERIAL.close()

    SERIAL.init(root, list_box, text_box)

    button0 = tk.Button(root, text="打开串口", command=open_serial)
    button0.place(x=10, y=200)
    button1 = tk.Button(root, text="发送数据", command=send_date)
    button1.place(x=70, y=200)
    button2 = tk.Button(root, text="关闭串口", command=close_serial)
    button2.place(x=130, y=200)

    root.mainloop()
