import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from module_main_page.module_main_page_logic import module_main_page_logic


class MainWindow(QMainWindow, module_main_page_logic):
    def __init__(self):
        super(MainWindow, self).__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = MainWindow()
    window.show()
    app.exec_()
