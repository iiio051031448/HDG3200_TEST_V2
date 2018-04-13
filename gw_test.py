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
    test_end_signal = pyqtSignal(dict)

    def __init__(self, sec=1000, parent=None):
        super().__init__()
        self.sec = sec

    def run(self):
        print("---")
        self.test_status("GatewayTestThread start")
        self.req = http.HttpReq(host,  self.test_step)
        self.test_status("检测网关中")
        self.req.gatewaydetect()
        self.test_status("检测到网关开始测试")
        if self.req.test_start():
            logging.debug("test success.")
            self.end_test(0, "ALL TEST SUCCESS")
            #return True
        else :
            logging.debug("test failed.")
            self.end_test(1, "ERROR")
            #return False

    def test_status(self, msg):
        self.test_status_signal.emit(msg)  # 发射信号

    def test_step(self, step, result, info=None):
        step_msg = {"step": step, "result": result, "info": info}
        # print("step : %d, result : %d" % (step_msg["step"], step_msg["result"]))
        self.test_step_signal.emit(step_msg)

    def end_test(self, result, info):
        end_msg = {"result": result, "info" : info}
        # logging.debug("one_test_end, result : %d, info : %s" % (end_msg["result"], end_msg["info"]))
        self.test_end_signal.emit(end_msg)


