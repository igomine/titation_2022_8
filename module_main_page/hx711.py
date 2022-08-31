import time
import random
import json
import os.path
import sys
import numpy
import math

sys.path.append('./')
from hx711 import HX711

referenceUnit = 1


def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()

    print("Bye!")
    sys.exit()


hx = HX711(18, 17)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(1)
hx.reset()
# hx.tare()

init_data = {"sensor_value": "0.0"}
if os.path.exists("/home/pi/Documents/electron_projs/igomine/userData/sensor.json") == False:
    with open("/home/pi/Documents/electron_projs/igomine/userData/sensor.json", 'a+', encoding='utf-8') as fp:
        updata_data = init_data
        json.dump(updata_data, fp)
        fp.close()

class kalman_filter_zrd:
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


class kalman_filter:
    def __init__(self, Q, R):
        self.Q = Q
        self.R = R

        self.P_k_k1 = 1
        self.Kg = 0
        self.P_k1_k1 = 1
        self.x_k_k1 = 0
        self.ADC_OLD_Value = 0
        self.Z_k = 0
        self.kalman_adc_old = 0

    def kalman(self, ADC_Value):

        self.Z_k = ADC_Value

        if (abs(self.kalman_adc_old - ADC_Value) >= 60):
            self.x_k1_k1 = ADC_Value * 0.382 + self.kalman_adc_old * 0.618
        else:
            self.x_k1_k1 = self.kalman_adc_old;

        self.x_k_k1 = self.x_k1_k1
        self.P_k_k1 = self.P_k1_k1 + self.Q

        self.Kg = self.P_k_k1 / (self.P_k_k1 + self.R)

        kalman_adc = self.x_k_k1 + self.Kg * (self.Z_k - self.kalman_adc_old)
        self.P_k1_k1 = (1 - self.Kg) * self.P_k_k1
        self.P_k_k1 = self.P_k1_k1

        self.kalman_adc_old = kalman_adc

        return kalman_adc


kalman_filter = kalman_filter(0.001, 0.1)
kalman_filter_zrd = kalman_filter_zrd(9800.0, 9800.0, 10.0)
frequency = 0.5
next_due = 0
# KalmanFilterInit_zrd()
while True:
    try:
        while not hx.is_ready():
            pass
        val = hx.get_weight(3)

        if val < 0:
            val = 0
        # print(val)
        xhat = kalman_filter_zrd.kalman(val)
        # xhat = kalman_filter.kalman(val)

        if next_due < time.time():
            with open('/home/pi/Documents/electron_projs/igomine/userData/sensor.json', 'r+', encoding='utf-8') as fp:
                updata_data = json.load(fp)
                updata_data["sensor_value"] = str(xhat)
                fp.seek(0, 0)
                fp.truncate()
                json.dump(updata_data, fp)
                fp.close()
            next_due = frequency + time.time()
            print(xhat)
        # hx.power_down()
        # hx.power_up()
        # time.sleep(0.2)

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()

# init_data = {"random_value": "123"}
# if os.path.exists("d:/userData/xxx.json"):
#     # print("有")
#     with open('d:/userData/xxx.json', 'r+', encoding='utf-8') as fp:
#         updata_data = json.load(fp)
#         # updata_data["random_value"] = updata_data["random_value"] + 5
#         updata_data["random_value"] = str(float(updata_data["random_value"]) + 0.3)
#         fp.close()
# else:
#     # print("wu")
#     # with open('../userData/xxx.json', 'w+', encoding='utf-8') as fp:
#     #     fp.close()
#     with open("d:/userData/xxx.json", 'a+', encoding='utf-8') as fp:
#         updata_data = init_data
#         fp.close()

# # with open('./foobar.json', 'r+', encoding='utf-8') as fp:
# #     updata_data = json.load(fp)
# #     updata_data["random_value"] = updata_data["random_value"] + 5

# with open('d:/userData/xxx.json', 'w', encoding='utf-8') as fp:
#     json.dump(updata_data, fp)
#     fp.close()

# print(round(float(updata_data["random_value"]),3))
