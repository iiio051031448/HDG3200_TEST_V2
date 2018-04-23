import logging
import hdtHttp as http
import win
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
import gw_check_map as gwmap
import queue

def_host = "192.168.199.134"

# url = "http://" + host + "/cgi-bin/luci"
# data = {"luci_username": "root", "luci_password": ""}
# headers = {'Content-Type' : 'application/x-www-form-urlencoded'}

wait_trigger_q = queue.Queue()

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
    test_status_signal = pyqtSignal(dict)  # 信号类型：int
    test_step_signal = pyqtSignal(dict)
    test_end_signal = pyqtSignal(dict)
    test_confirm_signal = pyqtSignal(dict)

    def __init__(self, gw_host=def_host, parent=None):
        super().__init__()
        self.is_repeat = False
        self.gw_host = gw_host

    def run(self):
        print("---")
        # TODO: started with a test id(time + seq)
        #logging.debug("gateway host ip : [%s]" % (self.gw_host))
        self.up_test_start_time(time.strftime("%Y-%m-%d %H:%M:%S"))
        self.test_status("GatewayTestThread start")
        self.req = http.HttpReq(self.gw_host,  self.test_step, self.confirm_msg)
        self.test_status("检测网关中")
        self.req.gatewaydetect()
        mac=self.req.gateway_get_mac()
        logging.debug("gateway MAC : %s", mac)
        self.up_gw_mac(mac)
        print("wait mac trigger ++++")
        resp_msg = wait_trigger_q.get()
        print("wait mac trigger ----")
        print(resp_msg)
        self.is_repeat = resp_msg['is_repeat']
        if not resp_msg['data']:
            logging.debug("stop check")
            self.end_test(0, "SKIP")
            return


        # TODO: if failed.

        self.test_status("检测到网关开始测试")
        test_result = self.req.test_start()
        self.up_test_end_time(time.strftime("%Y-%m-%d %H:%M:%S"))
        if test_result:
            logging.debug("test success.")
            self.end_test(0, "ALL TEST SUCCESS")
            #return True
        else :
            logging.debug("test failed.")
            self.end_test(1, "ERROR")
            #return False

    def send_status(self, type, msg):
        st_msg = {"type": type, "msg": msg}
        self.test_status_signal.emit(st_msg)

    def test_status(self, msg):
        self.send_status("status", msg)

    def up_gw_mac(self, mac):
        self.send_status("gw_mac", mac)

    def up_test_start_time(self, start_time):
        self.send_status("start_time", start_time)

    def up_test_end_time(self, end_time):
        self.send_status("end_time", end_time)

    def test_step(self, step, result, info=None):
        step_msg = {"step": step, "result": result, "info": info}
        # print("step : %d, result : %d" % (step_msg["step"], step_msg["result"]))
        self.test_step_signal.emit(step_msg)

    def end_test(self, result, info):
        end_msg = {"result": result, "info" : info,  "is_repeat": self.is_repeat}
        # logging.debug("one_test_end, result : %d, info : %s" % (end_msg["result"], end_msg["info"]))
        self.test_end_signal.emit(end_msg)

    def confirm_msg(self, type, data):
        cf_msg =  {"type": type, "data": data}
        self.test_confirm_signal.emit(cf_msg)
        print("wait trigger ++++")
        resp_msg = wait_trigger_q.get()
        print("wait trigger ----")
        return resp_msg



