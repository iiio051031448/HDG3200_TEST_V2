import requests
import logging
import json

HDG_TEST_STEP_1_MOD_TEST = "module-test"
HDG_TEST_STEP_2_GATEWAY_TEST = "gateway-test"


class HttpReq:
    def __init__(self, host):
        self.host = host
        self.url = "http://" + host + "/cgi-bin/luci"
        self.http_get_timeout = 1
        self.step = ""
        self.test_list = {HDG_TEST_STEP_1_MOD_TEST: self.mod_check,
                          HDG_TEST_STEP_2_GATEWAY_TEST: self.gateway_check}

    def gateway_login(self):
        data = {"luci_username": "root", "luci_password": ""}
        try:
            f = requests.post(self.url, data, timeout=1, allow_redirects=False)
            logging.debug(f.url)
            logging.debug(f.status_code)
            logging.debug(f.cookies.get('sysauth'))
            logging.debug(f.headers['Location'])

            self.cookie = f.cookies.get('sysauth')

            self.furl = "http://" + self.host + f.headers['Location']
            logging.debug(self.furl)

            return True
        except requests.exceptions.Timeout:
            logging.debug("connection timeout")


    def gatewaydetect(self):
        while True:
            if self.gateway_login():
                break
            else:
                logging.debug("login failed. try again")

    def http_get(self, url, time_out):
        try:
            get = requests.get(url, timeout=time_out, allow_redirects=False, cookies={'sysauth': self.cookie})
            return get
        except requests.exceptions.Timeout:
            logging.error("connection timeout")
            self.handle_error()
            #TODO: how do do with this

    def mod_check_pingcheck(self, resp, action):
        # {"status":"OK","ret":"PING CHECK SUCCESS","action":"pingcheck","value":"001"}
        logging.debug(resp)
        ret_json = json.loads(resp)
        logging.debug(ret_json['ret'])
        ret_str  = ret_json['ret']
        errorindex = ret_str.find("ERROR")
        if errorindex >= 0:
            logging.error(self.step + " - " + action + " check error")
            return False
        else:
            logging.debug(self.step + " - " + action + " check success")
            return True


    def mod_check_sn_check(self, resp, action):
        # {"status":"OK","ret":"GET MOD INFO SUCCESS","action":"sn_check","value":"001"}
        logging.debug(resp)
        self.mod_check_pingcheck(resp, action)

    def mod_check_rssi(self, resp, action):
        # {"status":"OK","ret":"RSSI:18317","action":"rssi","value":"001"}
        logging.debug(resp)
        ret_json = json.loads(resp)
        logging.debug(ret_json['ret'])
        ret_str = ret_json['ret']
        rssi_v = int(ret_str.split(':')[1])
        if rssi_v >= -45:
            logging.error(self.step + " - " "rssi check error")
        else:
            logging.error(self.step + " - " "rssi check success")

    def mod_check_reset(self, resp, action):
        # {"status":"OK","ret":"MODULE RESET SUCCESS","action":"reset","value":"001"}
        logging.debug(resp)
        self.mod_check_pingcheck(resp, action)

    def mod_check(self):
        mod_check_list = ['pingcheck', 'sn_check', 'rssi', 'reset']
        #mod_check_list = ['pingcheck']
        mod_check_actions = {'pingcheck': self.mod_check_pingcheck,
                             'sn_check': self.mod_check_sn_check,
                             'rssi': self.mod_check_rssi,
                             'reset':self.mod_check_reset}

        for check in mod_check_list:
            purl = self.furl + "/admin/factory/module_check/" + check
            p = self.http_get(purl, 5)
            mod_check_actions[check](p.text, check)

    def gateway_port_check(self):
        purl = self.furl + "/admin/factory/" + "port_test"
        p = self.http_get(purl, 5)
        logging.debug(p.text)

        resp_json = json.loads(p.text)
        # ret = resp_json["ret"]
        if int(resp_json["ret"]) == 0:
            logging.debug("port check success")
            return True
        else:
            logging.debug("port check failed.")
            return False


    def _gateway_led_check_set_led_color(self, color):
        purl = self.furl + "/admin/factory/led_test/" + color
        p = self.http_get(purl, 5)
        if not p.text:
            logging.error("set led color failed")
            return False
        logging.debug(p.text)
        resp_json = json.loads(p.text)
        # ret = resp_json["ret"]
        if int(resp_json["ret"]) == 0:
            logging.debug("set led color to [" + color + "] success")
            return True
        else:
            logging.debug("set led color to [" + color + "] faild")
            return False

    def gateway_led_check(self):
        led_color_list = ["red", "green", "blue"]
        for color in led_color_list:
            if self._gateway_led_check_set_led_color(color):
                # wait user input
                logging.debug("set color over")
            else:
                logging.debug("set color failed.")
                return False



    def gateway_check(self):
        logging.debug("-")
        self.gateway_port_check()
        self.gateway_led_check()

    def handle_error(self):
        logging.error("get error")

    def test_start(self):
       # for (step, func) in self.test_list.items():
       #     self.step = step
       #     func()

       # self.test_list[HDG_TEST_STEP_1_MOD_TEST]()
       self.test_list[HDG_TEST_STEP_2_GATEWAY_TEST]()