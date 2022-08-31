import time
from PyQt5.QtCore import *
import datetime
import math
from threading import Event
from hx711 import HX711
from globalFile import globalData
import time
import random
import json
import os.path
import sys
import math


class KalmanFilterZrd:
    def __init__(self, err_est, err_mea, proc_noiss):
        self.err_est = err_est
        self.err_mea = err_mea
        self.proc_noise = proc_noiss
        self.current_estimate = 0.0
        self.last_estimate = 0.0
        self.kalman_gain = 0.0

    def kalman(self, ADC_Value):
        self.kalman_gain = self.err_est / (self.err_est + self.err_mea)
        self.current_estimate = self.last_estimate + self.kalman_gain * (ADC_Value - self.last_estimate)
        self.err_est = (1.0 - self.kalman_gain) * self.err_est + math.fabs(
            self.last_estimate - self.current_estimate) * self.proc_noise
        self.last_estimate = self.current_estimate
        return self.current_estimate


class ThreadReadHX711(QThread):
    def __init__(self, qmain_window):
        super(ThreadReadHX711, self).__init__()
        self.qmainwin = qmain_window
        self.hx = HX711(18, 17)
        self.kalman_filter_zrd = KalmanFilterZrd(9800.0, 9800.0, 10.0)
        frequency = 0.5
        next_due = 0

    def run(self):
        self.hx.set_reading_format("MSB", "MSB")
        self.hx.set_reference_unit(1)
        self.hx.reset()
        while globalData.flag_ThreadReadHX711Running:
            try:
                while not self.hx.is_ready():
                    pass
                val = self.hx.get_weight(3)
                if val < 0:
                    val = 0
                xhat = self.kalman_filter_zrd.kalman(val)
                print(xhat)
            except (KeyboardInterrupt, SystemExit):
                print("KeyboardInterrupt, SystemExit")

        # print("infer thread quit")
        # 首先推出infer notice线程
        # globalData.flag_threadInferResultNoticeRunning = False
        # QThread.msleep(1)
        # self.thread_infer_result_notice.quit()
        globalData.qsize = 0
        # self.qmainwin.textBrowserThreadPaddleInference.append("threadInference_quit")
        # self.qmainwin.textBrowserThreadPaddleInference.moveCursor(
        #     self.qmainwin.textBrowserThreadDaqAccess.textCursor().End)
        self.print_to_infer_console("推理线程退出", "red")
        return None