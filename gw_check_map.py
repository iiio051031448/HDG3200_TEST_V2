

GATEWAY_CHECK_STEP_ID_MOD_CONN = 1
GATEWAY_CHECK_STEP_ID_MOD_SN   = 2
GATEWAY_CHECK_STEP_ID_MOD_RSSI = 3
GATEWAY_CHECK_STEP_ID_MOD_REST = 4
GATEWAY_CHECK_STEP_ID_DEV_PORT = 5
GATEWAY_CHECK_STEP_ID_DEV_LED_R = 6
GATEWAY_CHECK_STEP_ID_DEV_LED_G = 7
GATEWAY_CHECK_STEP_ID_DEV_LED_B = 8
GATEWAY_CHECK_STEP_ID_DEV_BUTTON_RESET = 9
GATEWAY_CHECK_STEP_ID_DEV_BUTTON_SMARTCONFIG = 10
GATEWAY_CHECK_STEP_ID_SYS_READ_DATA = 11
GATEWAY_CHECK_STEP_ID_SYS_MAC = 12
GATEWAY_CHECK_STEP_ID_SYS_WRITE_SN = 13
GATEWAY_CHECK_STEP_ID_SYS_END_MARK = 14
GATEWAY_CHECK_STEP_ID_SYS_END_RESET = 15


GatewayCheckListMap = [{"id": 0, "table_msg": ["项目", "子项", "结果", "信息"], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_MOD_CONN, "table_msg": ["1.1 模块测试-通信测试", None, 0, None], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_MOD_SN, "table_msg": ["1.2 模块测试-SN测试", None, 0, None], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_MOD_RSSI, "table_msg": ["1.3 模块测试-信号强度测试", None, 0, None], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_MOD_REST, "table_msg": ["1.4 模块测试-重启测试", None, 0, None], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_DEV_PORT, "table_msg": ["2.1 设备测试-端口测试", None, 0, None], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_DEV_LED_R, "table_msg": ["2.2 设备测试-灯光测试", "红", 0, None], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_DEV_LED_G, "table_msg": ["", "绿", 0, None], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_DEV_LED_B, "table_msg": ["", "蓝", 0, None], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_DEV_BUTTON_RESET, "table_msg": ["2.3 设备测试-按键测试", "RESET键", 0, None], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_DEV_BUTTON_SMARTCONFIG, "table_msg": ["", "SMARTCONFIG键", 0, None], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_SYS_READ_DATA, "table_msg": ["3.1 系统测试-读取数据", None, 0, None], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_SYS_MAC, "table_msg": ["3.2 系统测试-校验MAC", None, 0, None], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_SYS_WRITE_SN, "table_msg": ["3.3 系统测试-写入SN", None, 0, None], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_SYS_END_MARK, "table_msg": ["4.1 结束测试-写入标记", None, 0, None], "table_items": []},
                      {"id": GATEWAY_CHECK_STEP_ID_SYS_END_RESET, "table_msg": ["4.2 结束测试-清除数据", None, 0, None], "table_items": []}];

button_list = {'reset': 'RESET键',
               'sm_config': 'SMARTCONFIG键'};