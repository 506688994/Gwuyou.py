import sys
import qtawesome
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow
from wuyou_ui import MainUi

logs = {"111": "222"}


class LogIn(QMainWindow):
    show_main=pyqtSignal()

    def __init__(self, parent=None):
        super(LogIn, self).__init__(parent)
        # 主窗口创建
        self.main_widget = QtWidgets.QWidget()  # 创建主窗口部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主窗口布局
        self.input_data_widget = QtWidgets.QWidget()  # 创建输入部件
        self.input_data_layout = QtWidgets.QGridLayout()  # 创建输入框布局
        self.login_button = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='red'), "登陆")  # 创建登陆按钮
        self.sig_button = QtWidgets.QPushButton('注册')  # 创建注册按钮
        self.change_button = QtWidgets.QPushButton('重置')  # 建重置密码按钮
        self.input_user = QtWidgets.QLineEdit()  # 创建账号输入框
        self.input_password = QtWidgets.QLineEdit()  # 创建密码输入框
        self.check_bear = QtWidgets.QCheckBox()  # 创建记住账号复选框
        self.check_autologin = QtWidgets.QCheckBox()  # 创建自动登陆复选框
        self.ico_user = QtWidgets.QLabel(chr(0xf002) + '' + '账号')  # 创建账号输入框图标及文字
        self.ico_password = QtWidgets.QLabel(chr(0xf002) + '' + '密码')  # 创建密码输入框图标及文字
        self.mini_button = QtWidgets.QPushButton()  # 创建最小化按钮
        self.close_button = QtWidgets.QPushButton()  # 创建关闭按钮
        self.Login_Ui()

    def Login_Ui(self):
        self.setFixedSize(350, 200)  # 设置窗口大小
        self.main_widget.setLayout(self.main_layout)  # 设置窗口部件为网格布局
        self.setCentralWidget(self.main_widget)  # 设置窗口中心

        # 部件大小设置
        self.close_button.setFixedSize(20, 20)  # 设置关闭按钮的大小
        self.mini_button.setFixedSize(20, 20)  # 设置最小化按钮大小
        self.sig_button.setFixedSize(45, 30)  # 创建账号按钮
        self.change_button.setFixedSize(45, 30)  # 重置密码
        self.input_user.setFixedHeight(30)  # 账号输入框高度
        self.input_password.setFixedHeight(30)  # 密码输入框高度
        self.ico_user.setFixedSize(45, 30)  # 账号图标设置
        self.ico_password.setFixedSize(45, 30)  # 密码图标

        # 输入框设置
        self.ico_password.setFont(qtawesome.font('fa', 16))  # 密码图标
        self.input_password.setEchoMode(2)  # 密码输入显示形式
        self.input_password.setPlaceholderText("输入密码")  # 密码框
        self.ico_user.setFont(qtawesome.font('fa', 16))  # 账号图标
        self.input_user.setPlaceholderText("输入账号")  # 账号框

        # 设置输入部件
        self.input_data_widget.setLayout(self.input_data_layout)
        self.main_layout.addWidget(self.input_data_widget, 1, 0, 3, 13)
        # 部件位置设置
        self.main_layout.addWidget(self.close_button, 0, 12, 1, 1)  # 关闭按钮
        self.main_layout.addWidget(self.mini_button, 0, 11, 1, 1)  # 最小化按钮
        self.main_layout.addWidget(self.check_bear, 4, 2, 1, 1)  # 记住密码复选框
        self.main_layout.addWidget(self.check_autologin, 4, 4, 1, 1)  # 自动登陆复选框
        self.main_layout.addWidget(self.login_button, 5, 0, 1, 13)  # 登陆按钮
        self.input_data_layout.addWidget(self.input_user, 0, 2, 1, 7)  # 账号输入框
        self.input_data_layout.addWidget(self.input_password, 2, 2, 1, 7)  # 密码输入框
        self.input_data_layout.addWidget(self.ico_user, 0, 0, 1, 2)  # 账号图标
        self.input_data_layout.addWidget(self.ico_password, 2, 0, 1, 2)  # 密码图标
        self.input_data_layout.addWidget(self.sig_button, 0, 9, 1, 1)  # 创建账号按钮
        self.input_data_layout.addWidget(self.change_button, 2, 9, 1, 1)  # 重置账号按钮

        # 美化设置
        # 设置窗口透明度
        self.main_widget.setWindowOpacity(0.9)  # 设置窗口透明度
        self.main_widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框去除窗口边框
        self.main_layout.setSpacing(0)  # 设置布局内部件缝隙

        self.close_button.setStyleSheet(  # 关闭按钮美化
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}
            button:flat{border:none;color:white;}''')
        self.mini_button.setStyleSheet(  # 最小化按钮美化
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover
            {background:green;}''')
        self.input_user.setStyleSheet(  # 输入框美化
            '''QLineEdit{
                    border:1px solid gray;
                    width:400px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.input_password.setStyleSheet(  # 输入框美化
            '''QLineEdit{
                    border:1px solid gray;
                    width:400px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.input_data_widget.setStyleSheet(  # 按钮美化
            '''
            QPushButton{
                border:none;
                color:black;
                font-size:10px;
                height:15px;
                padding-left:5px;
                padding-right:10px;
                text-align:center;
            }''')

        # 绑定按钮事件
        self.close_button.clicked.connect(self.close)
        self.login_button.clicked.connect(self.login_slot)

    def login_slot(self):
        name = self.input_user.text()
        key = self.input_password.text()
        if name not in logs:
            self.input_user.setText('')
            self.input_user.setFocus()
            pass
        if logs[name] != key:
            self.input_password.setText('')
            self.input_password.setFocus()
            pass
        self.ui1=MainUi.init_ui(MainUi.init_ui)
        self.ui1.show()

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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = LogIn()
    gui.show()
    sys.exit(app.exec_())
