import requests
import logging
import json

class HttpReq:
    def __init__(self, host):
        self.host = host
        self.url = "http://" + host + "/cgi-bin/luci"
        self.http_get_timeout = 1


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

    def mod_check_pingcheck(self, resp):
        # {"status":"OK","ret":"PING CHECK SUCCESS","action":"pingcheck","value":"001"}
        logging.debug(resp)
        ret_json = json.loads(resp)
        logging.debug(ret_json['ret'])

    def mod_check_sn_check(self, resp):
        # {"status":"OK","ret":"GET MOD INFO SUCCESS","action":"sn_check","value":"001"}
        logging.debug(resp)

    def mod_check_rssi(self, resp):
        # {"status":"OK","ret":"RSSI:18317","action":"rssi","value":"001"}
        logging.debug(resp)

    def mod_check_reset(self, resp):
        # {"status":"OK","ret":"MODULE RESET SUCCESS","action":"reset","value":"001"}
        logging.debug(resp)

    def mod_check(self):
        # mod_check_list = ['pingcheck', 'sn_check', 'rssi', 'reset']
        mod_check_list = ['pingcheck']
        mod_check_actions = {'pingcheck': self.mod_check_pingcheck,
                             'sn_check': self.mod_check_sn_check,
                             'rssi': self.mod_check_rssi,
                             'reset':self.mod_check_reset}

        for check in mod_check_list:
            purl = self.furl + "/admin/factory/module_check/" + check
            p = self.http_get(purl, 5)
            mod_check_actions[check](p.text)

    def handle_error(self):
        logging.error("get error")
