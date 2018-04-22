# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import threading
import time
import gw_test
import gw_check_map as gwmap
import log_db
import tst_batch
import hdtHttp


class GatewayTestThread(QtCore.QThread):
    def __init__(self, parent=None):
        #self.win = win
        super().__init__(parent)

    def run(self):
        #self.win.status_set("GatewayTestThread start")
        #test = GatewayTest()
        #test.run(self.win)
        for i in range(1000):
            #self.sec_changed_signal.emit(i)  # 发射信号
            # time.sleep(1)
            print("---")


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_MainWindow, self).__init__() # 没有这个QFileDialog.getOpenFileName都不弹输出来
        self.test_thread = None # msg with self
        self.db_session = None
        self.db_file_path = None
        self.test_batch = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.check_list = QtWidgets.QTableWidget(self.centralwidget)
        self.check_list.setGeometry(QtCore.QRect(400, 50, 600, 660))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_list.sizePolicy().hasHeightForWidth())
        self.check_list.setSizePolicy(sizePolicy)
        #self.check_list.setAlternatingRowColors(True)
        self.check_list.setShowGrid(True)
        self.check_list.setGridStyle(QtCore.Qt.DashLine)
        self.check_list.setWordWrap(True)
        self.rowCount = 16
        self.ColumnCount = 5
        self.check_list.setRowCount(self.rowCount)
        self.check_list.setColumnCount(self.ColumnCount)
        self.check_list.setObjectName("check_list")
        item = QtWidgets.QTableWidgetItem()
        self.check_list.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.check_list.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.check_list.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        for row in range(self.rowCount):
            for column in range(self.ColumnCount):
                # print("%d, %d" % (row, column))
                self.check_list.setItem(row, column, item)
                item = QtWidgets.QTableWidgetItem()

        self.check_list.horizontalHeader().setVisible(False)
        self.check_list.horizontalHeader().setDefaultSectionSize(168)
        self.check_list.verticalHeader().setVisible(False)


        self.tst_bat_grpbox = QtWidgets.QGroupBox(self.centralwidget)
        self.tst_bat_grpbox.setGeometry(QtCore.QRect(30, 20, 291, 121))
        self.tst_bat_grpbox.setObjectName("tst_bat_grpbox")
        self.tst_bat_id_lable = QtWidgets.QLabel(self.tst_bat_grpbox)
        self.tst_bat_id_lable.setGeometry(QtCore.QRect(10, 20, 54, 12))
        self.tst_bat_id_lable.setObjectName("tst_bat_id_lable")
        self.tst_bat_id_eline = QtWidgets.QLineEdit(self.tst_bat_grpbox)
        self.tst_bat_id_eline.setGeometry(QtCore.QRect(70, 20, 160, 20))
        self.tst_bat_id_eline.setObjectName("tst_bat_id_eline")
        self.tst_bat_id_eline.setReadOnly(True)
        self.tst_bat_start_time_lable = QtWidgets.QLabel(self.tst_bat_grpbox)
        self.tst_bat_start_time_lable.setGeometry(QtCore.QRect(10, 50, 54, 12))
        self.tst_bat_start_time_lable.setObjectName("tst_bat_start_time_lable")
        self.tst_bat_success_count_eline = QtWidgets.QLineEdit(self.tst_bat_grpbox)
        self.tst_bat_success_count_eline.setGeometry(QtCore.QRect(70, 80, 61, 20))
        self.tst_bat_success_count_eline.setObjectName("tst_bat_success_count_eline")
        self.tst_bat_success_count_eline.setReadOnly(True)
        self.tst_bat_success_count_lable = QtWidgets.QLabel(self.tst_bat_grpbox)
        self.tst_bat_success_count_lable.setGeometry(QtCore.QRect(10, 70, 54, 31))
        self.tst_bat_success_count_lable.setObjectName("tst_bat_success_count_lable")
        self.tst_bat_failed_count_lable = QtWidgets.QLabel(self.tst_bat_grpbox)
        self.tst_bat_failed_count_lable.setGeometry(QtCore.QRect(140, 70, 54, 31))
        self.tst_bat_failed_count_lable.setObjectName("tst_bat_failed_count_lable")
        self.tst_bat_failed_count_eline = QtWidgets.QLineEdit(self.tst_bat_grpbox)
        self.tst_bat_failed_count_eline.setGeometry(QtCore.QRect(200, 80, 61, 20))
        self.tst_bat_failed_count_eline.setObjectName("tst_bat_failed_count_eline")
        self.tst_bat_failed_count_eline.setReadOnly(True)
        self.tst_bat_start_time_eline = QtWidgets.QLineEdit(self.tst_bat_grpbox)
        self.tst_bat_start_time_eline.setGeometry(QtCore.QRect(70, 50, 160, 20))
        self.tst_bat_start_time_eline.setObjectName("tst_bat_start_time_eline")
        self.tst_bat_start_time_eline.setReadOnly(True)


        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 150, 290, 210))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 54, 12))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(70, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 70, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pBtTestStart = QtWidgets.QPushButton(self.groupBox)
        self.pBtTestStart.setGeometry(QtCore.QRect(30, 120, 75, 23))
        self.pBtTestStart.setObjectName("pushButton")
        self.pBtGenrateLogs = QtWidgets.QPushButton(self.groupBox)
        self.pBtGenrateLogs.setGeometry(QtCore.QRect(115, 150, 75, 23))
        self.pBtGenrateLogs.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 150, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")


        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 370, 291, 191))
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 54, 12))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 30, 211, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(50, 60, 211, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")

        self.gatewayMac_label = QtWidgets.QLabel(self.groupBox_2)
        self.gatewayMac_label.setGeometry(QtCore.QRect(20, 90, 54, 12))
        self.gatewayMac_label.setObjectName("label_3")
        self.gatewayMac = QtWidgets.QLineEdit(self.groupBox_2)
        self.gatewayMac.setGeometry(QtCore.QRect(50, 90, 211, 20))
        self.gatewayMac.setObjectName("gatewayMac")

        self.onetest_start_time_lable = QtWidgets.QLabel(self.groupBox_2)
        self.onetest_start_time_lable.setGeometry(QtCore.QRect(20, 120, 54, 12))
        self.onetest_start_time_lable.setObjectName("onetest_start_time_lable")
        self.onetest_start_time_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.onetest_start_time_line.setGeometry(QtCore.QRect(80, 120, 181, 20))
        self.onetest_start_time_line.setObjectName("onetest_start_time_line")

        self.onetest_end_time_lable = QtWidgets.QLabel(self.groupBox_2)
        self.onetest_end_time_lable.setGeometry(QtCore.QRect(20, 150, 54, 12))
        self.onetest_end_time_lable.setObjectName("onetest_end_time_lable")
        self.onetest_end_time_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.onetest_end_time_line.setGeometry(QtCore.QRect(80, 150, 181, 20))
        self.onetest_end_time_line.setObjectName("onetest_end_time_line")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.new_batch_act = QtWidgets.QAction(MainWindow)
        self.new_batch_act.setObjectName("new_batch")
        self.open_batch_act = QtWidgets.QAction(MainWindow)
        self.open_batch_act.setObjectName("open_batch")
        self.menu.addAction(self.new_batch_act)
        self.menu.addAction(self.open_batch_act)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        self.pBtTestStart.clicked.connect(self.start_test)
        self.pBtGenrateLogs.clicked.connect(self.generate_logs)
        self.new_batch_act.triggered.connect(self.create_batch)
        self.open_batch_act.triggered.connect(self.open_batch)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HDG3200 Test tool"))
        self.check_list.setSortingEnabled(False)
        item = self.check_list.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.check_list.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.check_list.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        __sortingEnabled = self.check_list.isSortingEnabled()
        self.check_list.setSortingEnabled(False)
        self.retranslateCheckListItemUi()
        self.check_list.setSortingEnabled(__sortingEnabled)

        self.tst_bat_grpbox.setTitle(_translate("MainWindow", "批次信息"))
        self.tst_bat_id_lable.setText(_translate("MainWindow", "批次ID"))
        self.tst_bat_start_time_lable.setText(_translate("MainWindow", "开始时间"))
        self.tst_bat_success_count_lable.setText(_translate("MainWindow", "成功次数"))
        self.tst_bat_failed_count_lable.setText(_translate("MainWindow", "失败次数"))

        self.groupBox.setTitle(_translate("MainWindow", "测试"))
        self.label.setText(_translate("MainWindow", "日期"))
        self.lineEdit.setText(_translate("MainWindow", "2018-04-12"))
        self.label_2.setText(_translate("MainWindow", "时间"))
        self.lineEdit_2.setText(_translate("MainWindow", "15:27:33"))
        self.pBtTestStart.setText(_translate("MainWindow", "开始测试"))
        self.pBtGenrateLogs.setText(_translate("MainWindow", "生成报告"))
        self.pushButton_3.setText(_translate("MainWindow", "查看日志"))

        self.groupBox_2.setTitle(_translate("MainWindow", "信息"))
        self.label_3.setText(_translate("MainWindow", "状态"))
        self.lineEdit_3.setText(_translate("MainWindow", "就绪"))
        self.gatewayMac_label.setText(_translate("MainWindow", "MAC"))
        self.gatewayMac.setText(_translate("MainWindow", "-----"))
        self.onetest_start_time_lable.setText(_translate("MainWindow", "开始时间"))
        self.onetest_start_time_line.setText(_translate("MainWindow", ""))
        self.onetest_end_time_lable.setText(_translate("MainWindow", "结束时间"))
        self.onetest_end_time_line.setText(_translate("MainWindow", ""))

        self.menu.setTitle(_translate("MainWindow", "批次"))
        self.new_batch_act.setText(_translate("MainWindow", "新建批次"))
        self.new_batch_act.setToolTip(_translate("MainWindow", "new_bat"))
        self.open_batch_act.setText(_translate("MainWindow", "打开批次"))
        self.open_batch_act.setToolTip(_translate("MainWindow", "open_batch"))

    def retranslateCheckListItemUi(self, reset=0):
        _translate = QtCore.QCoreApplication.translate
        self.check_list_map = gwmap.GatewayCheckListMap
        row_back_color = QtGui.QColor(255, 255, 255)
        for r, row_list in enumerate(self.check_list_map):
            for c, item_v in enumerate(row_list["table_msg"]):
                print(item_v)
                print("%d, %d" % (r, c))

                item = self.check_list.item(r, c)
                if not reset: #only add to list at first init
                    row_list["table_items"].extend([item])
                item.setBackground(row_back_color)
                if item_v != None:
                    if item_v == 0:
                        item.setText(_translate("MainWindow", "wait"))
                    else:
                        item.setText(_translate("MainWindow", item_v))
                else:
                    item.setText(_translate("MainWindow", ""))

    def reset_gateway_status(self):
        _translate = QtCore.QCoreApplication.translate
        self.gatewayMac.setText(_translate("MainWindow", ""))
        self.onetest_start_time_line.setText(_translate("MainWindow", ""))
        self.onetest_end_time_line.setText(_translate("MainWindow", ""))

    def check_table_set_result(self, index, result, info=None):
        _translate = QtCore.QCoreApplication.translate
        if result == 0:
            row_back_color = QtGui.QColor(0, 180, 0)
            result_str = "成功"
        else:
            row_back_color = QtGui.QColor(230, 0, 0)
            result_str = "失败"

        self.check_list_map[index]["table_items"][2].setText(_translate("MainWindow", result_str))
        for item in self.check_list_map[index]["table_items"]:
            item.setBackground(row_back_color)
        if info:
            self.check_list_map[index]["table_items"][3].setText(_translate("MainWindow", info))
        self.progressBar.setProperty("value", (index / len( self.check_list_map) * 100))

    def check_table_set_success(self, index):
        self.check_table_set_result(index, 0)

    def check_table_set_failed(self, index):
        self.check_table_set_result(index, 1)

    def start_test(self):
        print("-")
        if self.test_batch == None:
            self.show_open_batch_warning()
            return
        if self.test_thread:
            if not self.test_thread.isFinished():
                print("测试还未完成，等几秒在继续")
                return
        self.retranslateCheckListItemUi()
        self.reset_gateway_status()
        self.pBtTestStart.setEnabled(False)
        self.test_thread = gw_test.MyThread()  # msg with self
        self.test_thread.test_status_signal.connect(self.status_set)
        self.test_thread.test_step_signal.connect(self.updata_step)
        self.test_thread.test_end_signal.connect(self.one_test_end)
        self.test_thread.test_confirm_signal.connect(self.test_confirm)
        self.test_thread.start()

    def status_set(self, status_msg):
        # status_msg : {"type": "status", "msg": "testing ..."}
        _translate = QtCore.QCoreApplication.translate
        if status_msg["type"] == "status":
            self.lineEdit_3.setText(_translate("MainWindow", status_msg["msg"]))
        elif status_msg["type"] == "gw_mac":
            self.gatewayMac.setText(_translate("MainWindow", status_msg["msg"]))
        elif status_msg["type"] == "start_time":
            self.onetest_start_time_line.setText(_translate("MainWindow", status_msg["msg"]))
        elif status_msg["type"] == "end_time":
            self.onetest_end_time_line.setText(_translate("MainWindow", status_msg["msg"]))
        # self.progressBar.setProperty("value", int(msg) % 100)

    def updata_step(self, step_msg):
        # step_msg : {"step": 0, "result": 0, "info": "rssi : -100"}
        print("step : %d, result : %d" % (step_msg["step"], step_msg["result"]))
        for n, l in enumerate(gwmap.GatewayCheckListMap):
            if l["id"] == step_msg["step"]:
                self.check_table_set_result(n, step_msg["result"], step_msg["info"])

    def one_test_end_save_record(self, result_str, failed_info_strs):
        if not self.db_session:
            print("db_session is not ready")
            return
        t_log_new = self.db_session.add_log(mac=self.gatewayMac.text(), operator="ed",
                                    start_time=self.onetest_start_time_line.text(),
                                    end_time=self.onetest_end_time_line.text(), test_id="HDG201804060001",
                                    is_repeat=False,
                                    result=result_str, failed_info=failed_info_strs, note="")

    def one_test_end(self, end_msg):
        # end_msg : {"result": 0, "info" : "ALL SUCCESS"}
        print("one_test_end, result : %d, info : %s" % (end_msg["result"], end_msg["info"]))
        print("++++++++++++++++++++++")
        print("开始时间：%s" % self.onetest_start_time_line.text())
        print("结束时间：%s" % self.onetest_end_time_line.text())
        print("MAC:%s" % self.gatewayMac.text())
        failed_info = ""
        for row in range(self.rowCount):
            line = []
            column = 0
            for column in range(self.ColumnCount):
                # print("%d, %d" % (row, column))
                item = self.check_list.item(row, column)
                # line = line + " " + item.text()
                if column == 2 and item.text() == "wait":
                    break
                line.extend([item.text()])
            if column == 2:
                break
            print("%-25s %-25s %-15s %-15s" % (line[0], line[1], line[2], line[3]))
            if end_msg["result"] == 1:
                failed_info = failed_info + ("%-25s %-25s %-15s %-15s\n" % (line[0], line[1], line[2], line[3]))

        self.one_test_end_save_record(end_msg["info"], failed_info)

        self.pBtTestStart.setEnabled(True)
        # if not self.test_thread.isFinished():
        #    print("test_thread is still running")

    def test_confirm(self,cf_msg):
        # cf_msg : {"type": "led_check", "data": "red"}
        print(cf_msg)
        if cf_msg['type'] == "led":
            reply = QMessageBox.question(self,
                                     "消息框标题",
                                     "Led灯的颜色是%s色吗?" % (cf_msg['data']),
                                     QMessageBox.Yes | QMessageBox.No)
            resp_msg = {"type": cf_msg['type'], "data": cf_msg['data'],
                        "reply": 1 if reply == QMessageBox.Yes else 0}
            hdtHttp.wait_trigger_q.put(resp_msg)
        elif cf_msg['type'] == "button":
            reply = QMessageBox.question(self,
                                     "消息框标题",
                                     "如果 %s按键已经按下 请点击Yes，并保持按键5s到检测到按键被按下。如果点击No则结束测试"
                                         % (gwmap.button_list[cf_msg['data']]),
                                     QMessageBox.Yes | QMessageBox.No)
            resp_msg = {"type": cf_msg['type'], "data": cf_msg['data'],
                        "reply": 1 if reply == QMessageBox.Yes else 0}
            hdtHttp.wait_trigger_q.put(resp_msg)
        elif cf_msg['type'] == "mac":
            value, ok = QInputDialog.getText(self, "输入框标题", "请输入MAC\n\nMAC:", QLineEdit.Normal, "MAC")
            resp_msg = {"type": cf_msg['type'], "data": value,
                        "reply": 1 if ok else 0}
            hdtHttp.wait_trigger_q.put(resp_msg)

    def generate_logs(self):
        if not self.test_thread.isFinished():
            print("test_thread is still running")


    def create_db_sesson(self, db_file_path):
        # TODO: need with try:
        self.db_session = log_db.SqlSession("sqlite:///" + db_file_path)

    def show_batch_msg(self):
        _translate = QtCore.QCoreApplication.translate
        #print (self.test_batch.t_bat_msg)
        self.tst_bat_id_eline.setText(_translate("MainWindow", self.test_batch.get_bat_id()))
        self.tst_bat_start_time_eline.setText(_translate("MainWindow", self.test_batch.get_bat_time()))
        self.tst_bat_success_count_eline.setText(_translate("MainWindow", str(self.test_batch.get_success_count())))
        self.tst_bat_failed_count_eline.setText(_translate("MainWindow", str(self.test_batch.get_failed_count())))

    def create_batch(self):
        print("create_batch")
        if not tst_batch.check_bats_dir():
            return
        filename, _ = QFileDialog.getSaveFileName(self, 'save file',
                                                  './tst_batchs/HDGZ3200_%s.tbat' % (time.strftime("%Y%m%d_%H%M%S")),
                                                  'Test Batch Files (*.tbat);;All Files (*)')
        if filename:
            print(filename)
            self.test_batch = tst_batch.TBatch(filename)
            if self.test_batch.load_batch_new():
                self.db_file_path = self.test_batch.get_db_file()
                self.create_db_sesson(self.db_file_path)
                self.show_batch_msg()


    def open_batch(self):
        print("open_batch")
        if not tst_batch.check_bats_dir():
            return False
        filename, _ = QFileDialog.getOpenFileName(self, 'Open file',
                                                  './' + tst_batch.TST_BATCH_BATS_DIR_PATH + '/',
                                                  'Test Batch Files (*.tbat);;All Files (*)')
        if filename:
            print(filename)
            self.test_batch = tst_batch.TBatch(filename)
            if self.test_batch.load_batch_exist():
                self.db_file_path = self.test_batch.get_db_file()
                self.create_db_sesson(self.db_file_path)
                self.show_batch_msg()

    def show_open_batch_warning(self):
        reply = QMessageBox.warning(self,
                                    "警告",
                                    "还没有打开批次，请新建一个批次或打开已有的批次",
                                    QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            print("Yes Yes Yes Yes")
        else:
            print("No No No No")

