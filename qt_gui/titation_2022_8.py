# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'titation_2022_8.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_main = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_main.sizePolicy().hasHeightForWidth())
        self.pushButton_main.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_main.setFont(font)
        self.pushButton_main.setCheckable(True)
        self.pushButton_main.setAutoRepeat(False)
        self.pushButton_main.setAutoExclusive(True)
        self.pushButton_main.setObjectName("pushButton_main")
        self.verticalLayout.addWidget(self.pushButton_main)
        self.pushButton_module1 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_module1.sizePolicy().hasHeightForWidth())
        self.pushButton_module1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_module1.setFont(font)
        self.pushButton_module1.setCheckable(True)
        self.pushButton_module1.setAutoExclusive(True)
        self.pushButton_module1.setObjectName("pushButton_module1")
        self.verticalLayout.addWidget(self.pushButton_module1)
        self.pushButton_module2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_module2.sizePolicy().hasHeightForWidth())
        self.pushButton_module2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_module2.setFont(font)
        self.pushButton_module2.setCheckable(True)
        self.pushButton_module2.setAutoExclusive(True)
        self.pushButton_module2.setObjectName("pushButton_module2")
        self.verticalLayout.addWidget(self.pushButton_module2)
        self.pushButton_module3 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_module3.sizePolicy().hasHeightForWidth())
        self.pushButton_module3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_module3.setFont(font)
        self.pushButton_module3.setCheckable(True)
        self.pushButton_module3.setAutoExclusive(True)
        self.pushButton_module3.setObjectName("pushButton_module3")
        self.verticalLayout.addWidget(self.pushButton_module3)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.horizontalLayout.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.label = QtWidgets.QLabel(self.main_page)
        self.label.setGeometry(QtCore.QRect(80, 40, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.main_page)
        self.lcdNumber.setGeometry(QtCore.QRect(330, 40, 111, 41))
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setObjectName("lcdNumber")
        self.stackedWidget.addWidget(self.main_page)
        self.module_1 = QtWidgets.QWidget()
        self.module_1.setObjectName("module_1")
        self.label_2 = QtWidgets.QLabel(self.module_1)
        self.label_2.setGeometry(QtCore.QRect(180, 60, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.module_1)
        self.module_2 = QtWidgets.QWidget()
        self.module_2.setObjectName("module_2")
        self.label_3 = QtWidgets.QLabel(self.module_2)
        self.label_3.setGeometry(QtCore.QRect(220, 60, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.module_2)
        self.module_3 = QtWidgets.QWidget()
        self.module_3.setObjectName("module_3")
        self.label_4 = QtWidgets.QLabel(self.module_3)
        self.label_4.setGeometry(QtCore.QRect(180, 70, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.module_3)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout.setStretch(0, 20)
        self.horizontalLayout.setStretch(1, 80)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_main.setText(_translate("MainWindow", "主页"))
        self.pushButton_module1.setText(_translate("MainWindow", "功能模块1"))
        self.pushButton_module2.setText(_translate("MainWindow", "功能模块2"))
        self.pushButton_module3.setText(_translate("MainWindow", "功能模块3"))
        self.pushButton_5.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "当前传感器读数"))
        self.label_2.setText(_translate("MainWindow", "功能模块1"))
        self.label_3.setText(_translate("MainWindow", "功能模块2"))
        self.label_4.setText(_translate("MainWindow", "功能模块3"))
