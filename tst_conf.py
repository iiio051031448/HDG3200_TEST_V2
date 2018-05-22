# -*- coding: utf-8 -*-

import logging
import os
import json
import hdt_logger

TST_CONF_FILE="tst.conf"

TST_CONF_ITEM_BAT_FILE="batch_file"
TST_CONF_ITEM_OPERATOR="operator"
TST_CONF_ITEM_GW_IP="gw_ip"


class TstConf:
    def __init__(self):
        hdt_logger.HDLogger.logger.debug('-')
        self.conf_list = None
        if not os.path.exists(TST_CONF_FILE):
            self.conf_list = {"batch_file": "",
                              "operator": "操作员",
                              "gw_ip": "192.168.0.66"}
            self.file = open(TST_CONF_FILE, "w+")
            conf_json_str = json.dumps(self.conf_list)
            self.file.write(conf_json_str)
            self.file.close()
        else:
            self.file = open(TST_CONF_FILE, "r+")
            conf_json_str = self.file.read()
            hdt_logger.HDLogger.logger.debug(conf_json_str)
            self.conf_list = json.loads(conf_json_str)
            self.file.close()


    def save_conf_list(self):
        self.file = open(TST_CONF_FILE, "w+")
        conf_json_str = json.dumps(self.conf_list)
        self.file.write(conf_json_str)
        self.file.close()

    def update_batch_file(self, batch_file):
        self.conf_list['batch_file'] = batch_file
        self.save_conf_list()

    def update_operator(self, operator):
        self.conf_list['operator'] = operator
        self.save_conf_list()

    def update_gw_ip(self, gw_ip):
        self.conf_list['gw_ip'] = gw_ip
        self.save_conf_list()


if __name__ == "__main__":
    t_conf = TstConf()
    t_conf.update_batch_file("123")
    t_conf.update_operator("jack")
    t_conf.update_gw_ip("192.168.0.99")
