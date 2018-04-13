import logging
import hdtHttp as http
import win
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
import gw_check_map as gwmap


host = "192.168.69.134"

# url = "http://" + host + "/cgi-bin/luci"
# data = {"luci_username": "root", "luci_password": ""}
# headers = {'Content-Type' : 'application/x-www-form-urlencoded'}

class GatewayTest:
    def __init__(self):
        print("-")

    def run(self):
        self.req = http.HttpReq(host)
        # win.status_set("检测网关中")
        self.req.gatewaydetect()
        # win.status_set("检测到网关开始测试")
        self.req.test_start()

'''
def GatewayTestThread(win):
    win.status_set("GatewayTestThread start")
    test = GatewayTest()
    test.run(win)
'''

class MyThread(QThread):
    test_status_signal = pyqtSignal(str)  # 信号类型：int
    test_step_signal = pyqtSignal(dict)

    def __init__(self, sec=1000, parent=None):
        super().__init__()
        self.sec = sec  # 默认1000秒

    def run(self):
        print("---")
        self.test_status("GatewayTestThread start")
        self.req = http.HttpReq(host)
        self.test_status("检测网关中")
        self.req.gatewaydetect()
        self.test_status("检测到网关开始测试")
        self.test_step(gwmap.GATEWAY_CHECK_STEP_ID_MOD_CONN, 0)
        self.test_step(gwmap.GATEWAY_CHECK_STEP_ID_MOD_SN, 0)
        # self.req.test_start()

    def test_status(self, msg):
        self.test_status_signal.emit(msg)  # 发射信号

    def test_step(self, step, result):
        step_msg = {"step": step, "result": result}
        # print("step : %d, result : %d" % (step_msg["step"], step_msg["result"]))
        self.test_step_signal.emit(step_msg)


