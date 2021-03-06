import requests
import logging
import json
import gw_check_map as gwmap
import threading
import queue
import time
import hdt_logger

HDG_TEST_STEP_1_MOD_TEST = "module-test"
HDG_TEST_STEP_2_GATEWAY_TEST = "gateway-test"
HDG_TEST_STEP_3_SYSTEM_TEST = "system-test"
HDG_TEST_STEP_4_FINISH_TEST = "finish-test"


class HttpReq:
    def __init__(self, host, step_up_func, cf_msg_func):
        self.host = host
        self.url = "http://" + host + "/cgi-bin/luci"
        self.http_get_timeout = 1
        self.step = ""
        self.test_list = {HDG_TEST_STEP_1_MOD_TEST: self.mod_check,
                          HDG_TEST_STEP_2_GATEWAY_TEST: self.gateway_check,
                          HDG_TEST_STEP_3_SYSTEM_TEST: self.system_check,
                          HDG_TEST_STEP_4_FINISH_TEST: self.finish_test}

        self.step_up_func = step_up_func
        self.cf_msg_func = cf_msg_func
        self.ra_mac = None
        self.test_status = None

    def updata_test_status_box(self, msg):
        if self.test_status:
            self.test_status(msg)

    def update_test_step(self, step, result, info=None):
        if self.step_up_func:
            self.step_up_func(step, result, info)
        self.updata_test_status_box(gwmap.GatewayCheckListMap[step]["table_msg"][0])

    def gateway_login(self):
        data = {"luci_username": "root", "luci_password": "TYSmartCC2017"}
        try:
            f = requests.post(self.url, data, timeout=1, allow_redirects=False)
            if not f.url or not f.status_code or not f.cookies.get('sysauth') or not f.headers['Location']:
                return False
            hdt_logger.HDLogger.logger.debug(f.url)
            hdt_logger.HDLogger.logger.debug(f.status_code)
            hdt_logger.HDLogger.logger.debug(f.cookies.get('sysauth'))
            hdt_logger.HDLogger.logger.debug(f.headers['Location'])
            if f.status_code != 302:
                hdt_logger.HDLogger.logger.error("need a 302 response")
                return False
            if not f.headers['Location']:
                hdt_logger.HDLogger.logger.error("Location is None")
                return False

            self.cookie = f.cookies.get('sysauth')

            self.furl = "http://" + self.host + f.headers['Location']
            hdt_logger.HDLogger.logger.debug(self.furl)

            return True
        except requests.exceptions.Timeout:
            hdt_logger.HDLogger.logger.debug("connection timeout")
            return False

    def gatewaydetect(self):
        while True:
            if self.gateway_login():
                break
            else:
                hdt_logger.HDLogger.logger.debug("login failed. try again")
                time.sleep(1)

    def http_get(self, url, time_out):
        try:
            get = requests.get(url, timeout=time_out, allow_redirects=False, cookies={'sysauth': self.cookie})
            hdt_logger.HDLogger.logger.debug("HTTP get resp status code:[%d]" % get.status_code)
            if get.status_code != 200:
                return None
            return get
        except requests.exceptions.Timeout:
            hdt_logger.HDLogger.logger.error("connection timeout")
            self.handle_error()
            #TODO: how do do with this

    def gateway_get_mac(self):
        purl = self.furl + "/admin/factory/mac_check"
        # {"status":"OK","ret":[{"mac":"D0:6F:4A:F3:A4:BF","ifname":"ra"},{"mac":"D0:6F:4A:F3:A4:C0","ifname":"lan"},{"mac":"D0:6F:4A:F3:A4:C1","ifname":"wan"}],"value":"001"}
        p = self.http_get(purl, 5)
        if p and p.text:
            hdt_logger.HDLogger.logger.debug(p.text)
            ret_json = json.loads(p.text)
            if ret_json:
                for it in ret_json['ret']:
                    if it["ifname"] == "ra":
                        return it["mac"]

    def mod_check_pingcheck(self, resp, action):
        # {"status":"OK","ret":"PING CHECK SUCCESS","action":"pingcheck","value":"001"}
        hdt_logger.HDLogger.logger.debug(resp)
        ret_json = json.loads(resp)
        hdt_logger.HDLogger.logger.debug(ret_json['ret'])
        ret_str  = ret_json['ret']
        errorindex = ret_str.find("ERROR")
        if errorindex >= 0:
            hdt_logger.HDLogger.logger.error(self.step + " - " + action + " check error")
            if action == "pingcheck":
                self.update_test_step(gwmap.GATEWAY_CHECK_STEP_ID_MOD_CONN, 1)
            return False
        else:
            hdt_logger.HDLogger.logger.debug(self.step + " - " + action + " check success")
            if action == "pingcheck":
                self.update_test_step(gwmap.GATEWAY_CHECK_STEP_ID_MOD_CONN, 0)
            return True

    def mod_check_sn_check(self, resp, action):
        # {"status":"OK","ret":"GET MOD INFO SUCCESS","action":"sn_check","value":"001"}
        hdt_logger.HDLogger.logger.debug(resp)
        if self.mod_check_pingcheck(resp, action):
            self.update_test_step(gwmap.GATEWAY_CHECK_STEP_ID_MOD_SN, 0)
            return True
        else:
            self.update_test_step(gwmap.GATEWAY_CHECK_STEP_ID_MOD_SN, 1)
            return False

    def mod_check_rssi(self, resp, action):
        # {"status":"OK","ret":"RSSI:18317","action":"rssi","value":"001"}
        hdt_logger.HDLogger.logger.debug(resp)
        ret_json = json.loads(resp)
        hdt_logger.HDLogger.logger.debug(ret_json['ret'])
        ret_str = ret_json['ret']
        rssi_v = int(ret_str.split(':')[1])
        if rssi_v < -45:
            hdt_logger.HDLogger.logger.error(self.step + " - " "rssi check error")
            self.update_test_step(gwmap.GATEWAY_CHECK_STEP_ID_MOD_RSSI, 1, ret_str)
            return False
        else:
            hdt_logger.HDLogger.logger.error(self.step + " - " "rssi check success")
            self.update_test_step(gwmap.GATEWAY_CHECK_STEP_ID_MOD_RSSI, 0)
            return True

    def mod_check_reset(self, resp, action):
        # {"status":"OK","ret":"MODULE RESET SUCCESS","action":"reset","value":"001"}
        hdt_logger.HDLogger.logger.debug(resp)
        if self.mod_check_pingcheck(resp, action):
            self.update_test_step(gwmap.GATEWAY_CHECK_STEP_ID_MOD_REST, 0)
            return True
        else:
            self.update_test_step(gwmap.GATEWAY_CHECK_STEP_ID_MOD_REST, 1)
            return False

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
            if not p:
                return False
            if not mod_check_actions[check](p.text, check):
                # -------- for pingcheck need retry --------
                retry_count = 0
                if check == "pingcheck":
                    while True:
                        if retry_count < 5:
                            self.updata_test_status_box("模块通信测试失败，第 %d 次尝试" % (retry_count))
                            hdt_logger.HDLogger.logger.error(
                                "check failed. will try again. retry_count:[%d]" % (retry_count))
                            time.sleep(2)
                            retry_count += 1
                            p = self.http_get(purl, 5)
                            if not p:
                               return False
                            if mod_check_actions[check](p.text, check):
                                self.updata_test_status_box("模块通信测试成功")
                                break
                        else:
                            # retry too many time, treat as an error.
                            return False
                # -------- retry END --------
                else:
                    return False
        return True


    def gateway_port_check(self):
        purl = self.furl + "/admin/factory/" + "port_test"
        p = self.http_get(purl, 5)
        if not p or not p.text:
            return False
        hdt_logger.HDLogger.logger.debug(p.text)

        resp_json = json.loads(p.text)
        # ret = resp_json["ret"]
        if int(resp_json["ret"]) == 0:
            hdt_logger.HDLogger.logger.debug("port check success")
            self.update_test_step(gwmap.GATEWAY_CHECK_STEP_ID_DEV_PORT, 0)
            return True
        else:
            hdt_logger.HDLogger.logger.debug("port check failed.")
            self.update_test_step(gwmap.GATEWAY_CHECK_STEP_ID_DEV_PORT, 1)
            return False

    def _gateway_led_check_set_led_color(self, color):
        purl = self.furl + "/admin/factory/led_test/" + color
        p = self.http_get(purl, 5)
        if not p or not p.text:
            hdt_logger.HDLogger.logger.error("set led color failed")
            return False
        hdt_logger.HDLogger.logger.debug(p.text)
        resp_json = json.loads(p.text)
        # ret = resp_json["ret"]
        if int(resp_json["ret"]) == 0:
            hdt_logger.HDLogger.logger.debug("set led color to [" + color + "] success")
            resp_msg = self.cf_msg_func("led", color)
            hdt_logger.HDLogger.logger.debug(resp_msg)
            if resp_msg['reply'] == 1:
                return True
            else:
                return False
        else:
            hdt_logger.HDLogger.logger.debug("set led color to [" + color + "] faild")
            return False

    def gateway_led_check(self):
        led_color_list = ["red", "green", "blue"]
        step_id = gwmap.GATEWAY_CHECK_STEP_ID_DEV_LED_R
        for color in led_color_list:
            if self._gateway_led_check_set_led_color(color):
                # wait user input
                hdt_logger.HDLogger.logger.debug("set color over")
                self.update_test_step(step_id, 0)
            else:
                hdt_logger.HDLogger.logger.debug("set color failed.")
                self.update_test_step(step_id, 1)
                return False
            step_id = step_id + 1
        return True

    def _do_gateway_button_check(self, button):
        purl = self.furl + "/admin/factory/button_test/" + button
        p = self.http_get(purl, 5)
        if not p or not p.text:
            hdt_logger.HDLogger.logger.error("get [%s] button status failed." % (button))
            return False, False
        hdt_logger.HDLogger.logger.debug(p.text)
        resp_json = json.loads(p.text)
        # ret = resp_json["ret"]
        if resp_json["ret"] == "lo":
            return True, True
        else:
            return True, False

    def _gateway_button_check(self, button, retry):
        hdt_logger.HDLogger.logger.debug("-")
        if not retry:
            resp_msg = self.cf_msg_func("button", button)
        else:
            resp_msg = self.cf_msg_func("button-retry", button)
        hdt_logger.HDLogger.logger.debug(resp_msg)
        if resp_msg['reply'] == 0:
            hdt_logger.HDLogger.logger.error("test Failed and exit")
            return False, True

        timer_cont = 0
        while True:
            hdt_logger.HDLogger.logger.debug("detect button timer %d" % (timer_cont))
            http_ret, button_ret = self._do_gateway_button_check(button)
            if not http_ret:
                return False, False
            if not button_ret:
                if timer_cont >= 5:
                    return False, False
                time.sleep(1)  # TODO: 0.5s is better ?
                timer_cont += 1
                continue
            break
        return True, False

    def gateway_button_check(self):
        hdt_logger.HDLogger.logger.debug("-")

        step_id = gwmap.GATEWAY_CHECK_STEP_ID_DEV_BUTTON_RESET

        for bt in gwmap.button_list:
            is_retry = False
            while True:
                ret, exit_ret = self._gateway_button_check(bt, is_retry)
                if not ret:
                    if not exit_ret:
                        is_retry = True
                        continue
                    self.update_test_step(step_id, 1)
                    return False
                else:
                    self.update_test_step(step_id, 0)
                    step_id += 1
                    break
        return True

    def gateway_check(self):
        hdt_logger.HDLogger.logger.debug("-")
        self.gateway_port_check()
        if not self.gateway_led_check():
            return False
        if not self.gateway_button_check():
            return False
        return True

    def system_check_factory_info_check(self):
        purl = self.furl + "/admin/factory/data_check"
        p = self.http_get(purl, 5)
        if not p or not p.text:
            hdt_logger.HDLogger.logger.error("get factory info failed.")
            return False
        hdt_logger.HDLogger.logger.debug(p.text)
        resp_json = json.loads(p.text)
        # ret = resp_json["ret"]
        if not resp_json["ret"]:
            return False
        for fi_item in resp_json['ret']:
            hdt_logger.HDLogger.logger.debug(fi_item)
            if not fi_item['dname'] or not fi_item['value']:
                return False
            if not gwmap.factory_datas[fi_item['dname']]:
                return False
            else:
                if gwmap.factory_datas[fi_item['dname']] != fi_item['value']:
                    hdt_logger.HDLogger.logger.error("%s = %s" % (gwmap.factory_datas[fi_item['dname']], fi_item['value']))
                    return False
                else:
                    hdt_logger.HDLogger.logger.debug(fi_item['dname'] + "check success.")
        return True

    def system_check_mac_check(self):
        purl = self.furl + "/admin/factory/mac_check"
        p = self.http_get(purl, 5)
        if not p or not p.text:
            hdt_logger.HDLogger.logger.error("get mac list failed.")
            return False
        hdt_logger.HDLogger.logger.debug(p.text)
        resp_json = json.loads(p.text)
        # ret = resp_json["ret"]
        if not resp_json["ret"]:
            return False
        mac={}
        for mac_item in resp_json["ret"]:
            mac[mac_item["ifname"]] = [int(x, 16) for x in mac_item['mac'].split(":")]
        if mac['ra'][5] + 1 != mac['lan'][5] or mac['ra'][5] + 2 != mac['wan'][5]:
            return False
        hdt_logger.HDLogger.logger.debug(mac)

        resp_msg = self.cf_msg_func("mac", "get mac")
        hdt_logger.HDLogger.logger.debug(resp_msg)
        if resp_msg['reply'] == 0:
            return False
        if not resp_msg['data']:
            return False
        hdt_logger.HDLogger.logger.debug(resp_msg['data'])
        t_mac = [int(x, 16) for x in resp_msg['data'].split(':')]
        hdt_logger.HDLogger.logger.debug(t_mac)
        if mac['ra'] != t_mac:
            return False
        self.ra_mac = mac['ra']

        return True

    def system_check_write_sn(self):
        sn = ""

        hdt_logger.HDLogger.logger.debug('-')
        hdt_logger.HDLogger.logger.debug(self.ra_mac)
        for mac_char in self.ra_mac:
            sn += "%02X" % mac_char

        purl = self.furl + "/admin/factory/data_set?dname=sn&dvalue=" + sn
        p = self.http_get(purl, 5)
        if not p or not p.text:
            hdt_logger.HDLogger.logger.error("data_set failed.")
            return False
        hdt_logger.HDLogger.logger.debug(p.text)
        resp_json = json.loads(p.text)
        # ret = resp_json["ret"]
        if not resp_json["ret"]:
            return False
        hdt_logger.HDLogger.logger.debug("resp_json['ret']:[%s] == sn:[%s]" % (resp_json['ret'], sn))
        if resp_json['ret'] != sn:
            hdt_logger.HDLogger.logger.error("sn write failed.")
            return False

        return True

    def system_check(self):
        hdt_logger.HDLogger.logger.debug("-")
        step_id = gwmap.GATEWAY_CHECK_STEP_ID_SYS_READ_DATA
        if not self.system_check_factory_info_check():
            self.update_test_step(step_id, 1)
            return False
        else:
            self.update_test_step(step_id, 0)
        step_id += 1
        if not self.system_check_mac_check():
            self.update_test_step(step_id, 1)
            return False
        else:
            self.update_test_step(step_id, 0)
        step_id += 1
        if not self.system_check_write_sn():
            self.update_test_step(step_id, 1)
            return False
        else:
            self.update_test_step(step_id, 0)

        return True

    # TODO: this function same to system_check_write_sn
    def finish_test_write_factory_flag(self):
        sn = ""
        hdt_logger.HDLogger.logger.debug('-')
        purl = self.furl + "/admin/factory/data_set?dname=factory_reset&dvalue=done"
        p = self.http_get(purl, 5)
        if not p or not p.text:
            hdt_logger.HDLogger.logger.error("data_set failed.")
            return False
        hdt_logger.HDLogger.logger.debug(p.text)
        resp_json = json.loads(p.text)
        # ret = resp_json["ret"]
        if not resp_json["ret"]:
            return False
        if resp_json['ret'] != "done":
            hdt_logger.HDLogger.logger.error("factory flag write failed.")
            return False

        return True

    def finish_test_reset_data(self):
        hdt_logger.HDLogger.logger.debug('-')
        purl = self.furl + "/admin/factory/reset"
        p = self.http_get(purl, 5)
        if not p or not p.text:
            hdt_logger.HDLogger.logger.error("data_set failed.")
            return False
        hdt_logger.HDLogger.logger.debug(p.text)
        resp_json = json.loads(p.text)
        # ret = resp_json["ret"]
        if not resp_json["ret"]:
            return False
        if resp_json['ret'] != '0':
            return False
        return True

    def finish_test(self):
        hdt_logger.HDLogger.logger.debug("-")
        step_id = gwmap.GATEWAY_CHECK_STEP_ID_SYS_END_MARK
        if not self.finish_test_write_factory_flag():
            self.update_test_step(step_id, 1)
            return False
        else:
            self.update_test_step(step_id, 0)
        step_id += 1
        if not self.finish_test_reset_data():
            self.update_test_step(step_id, 1)
            return False
        else:
            self.update_test_step(step_id, 0)

        return True

    def handle_error(self):
        hdt_logger.HDLogger.logger.error("get error")


    def test_start(self):
        self.updata_test_status_box("模块测试 ...")
        if not self.test_list[HDG_TEST_STEP_1_MOD_TEST]():
            hdt_logger.HDLogger.logger.debug("mod check failed.")
            return False

        self.updata_test_status_box("网关测试 ...")
        if not self.test_list[HDG_TEST_STEP_2_GATEWAY_TEST]():
            return False

        self.updata_test_status_box("系统测试 ...")
        if not self.test_list[HDG_TEST_STEP_3_SYSTEM_TEST]():
            return False

        self.updata_test_status_box("结束测试 ...")
        if not self.test_list[HDG_TEST_STEP_4_FINISH_TEST]():
            return False

        return True