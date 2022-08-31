import threading
from multiprocessing import Queue
import multiprocessing
from threading import Event
# import queue
from PyQt5 import QtCore, QtGui, QtWidgets


class globalData():
    flag_SinglePoint = False
    flag_saveComplexSta = False
    flag_startSaveData = False
    flag_consDataSta = False
    flag_startPlotSta = False
    # 采集卡线程启动运行标志
    flag_ThreadReadHX711Running = False
    # 推理线程启动运行标志
    flag_threadInferenceRunning = False
    # 推理结果处理线程运行标志
    flag_threadInferResultNoticeRunning = False
    # 采集卡初始化完成标志，设置为True后，同时也设置flag_key = True
    flag_USBInitState = False