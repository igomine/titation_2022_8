'''
python 3.8
pyqt5
'''

import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from module_main_page.module_main_page_logic import module_main_page_logic
from module_main_page.thread_read_hx711 import ThreadReadHX711
from globalFile import globalData


class MainWindow(QMainWindow, module_main_page_logic):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__connect()
        # 去掉标题栏
        self.setWindowFlag(Qt.FramelessWindowHint)
        # 启动读取传感器线程
        self.thread_read_hx711 = ThreadReadHX711(self)
        globalData.flag_ThreadReadHX711Running = True
        self.thread_read_hx711.start()

    def __connect(self):
        self.pushButton_main.clicked.connect(self.on_stack_control)
        self.pushButton_module1.clicked.connect(self.on_stack_control)
        self.pushButton_module2.clicked.connect(self.on_stack_control)
        self.pushButton_module3.clicked.connect(self.on_stack_control)

    # def on_pushbutton_main(self):
    #     print("on_pushbutton_main")
    #     self.stackedWidget.setCurrentIndex(0)
    #
    # def on_pushbutton_module1(self):
    #     print("module1")
    #     self.stackedWidget.setCurrentIndex(1)

    def on_stack_control(self):  # 页面控制函数
        sender = self.sender().objectName()  # 获取当前信号 sender
        index = {
            "pushButton_main": 0,  # page_0
            "pushButton_module1": 1,  # page_1
            "pushButton_module2": 2,  # page_2
            "pushButton_module3": 3,  # page_2
        }
        self.stackedWidget.setCurrentIndex(index[sender])  # 根据信号 index 设置所显示的页面

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = MainWindow()
    window.show()
    app.exec_()
