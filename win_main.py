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


class Ui_MainWindow(object):
    def __init__(self):
        self.test_thread = None # msg with self

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.check_list = QtWidgets.QTableWidget(self.centralwidget)
        self.check_list.setGeometry(QtCore.QRect(400, 50, 600, 600))
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


        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 50, 291, 301))
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
        self.pBtGenrateLogs.setGeometry(QtCore.QRect(30, 180, 75, 23))
        self.pBtGenrateLogs.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 150, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")


        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 360, 291, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 54, 12))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 30, 211, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(50, 60, 211, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gatewayMac_label = QtWidgets.QLabel(self.groupBox_2)
        self.gatewayMac_label.setGeometry(QtCore.QRect(20, 90, 54, 12))
        self.gatewayMac_label.setObjectName("label_3")
        self.gatewayMac = QtWidgets.QLineEdit(self.groupBox_2)
        self.gatewayMac.setGeometry(QtCore.QRect(50, 90, 211, 20))
        self.gatewayMac.setObjectName("gatewayMac")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pBtTestStart.clicked.connect(self.start_test)
        self.pBtGenrateLogs.clicked.connect(self.generate_logs)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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

        self.groupBox.setTitle(_translate("MainWindow", "测试"))
        self.label.setText(_translate("MainWindow", "日期"))
        self.lineEdit.setText(_translate("MainWindow", "2018-04-12"))
        self.label_2.setText(_translate("MainWindow", "时间"))
        self.lineEdit_2.setText(_translate("MainWindow", "15:27:33"))
        self.pBtTestStart.setText(_translate("MainWindow", "开始测试"))
        self.pBtGenrateLogs.setText(_translate("MainWindow", "生产日志"))
        self.pushButton_3.setText(_translate("MainWindow", "查看日志"))

        self.groupBox_2.setTitle(_translate("MainWindow", "信息"))
        self.label_3.setText(_translate("MainWindow", "状态"))
        self.lineEdit_3.setText(_translate("MainWindow", "就绪"))
        self.gatewayMac_label.setText(_translate("MainWindow", "MAC"))
        self.gatewayMac.setText(_translate("MainWindow", "-----"))

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

    def check_table_set_success(self, index):
        self.check_table_set_result(index, 0)

    def check_table_set_failed(self, index):
        self.check_table_set_result(index, 1)

    def start_test(self):
        print("-")
        if self.test_thread:
            if not self.test_thread.isFinished():
                print("测试还未完成，等几秒在继续")
        self.retranslateCheckListItemUi()
        self.pBtTestStart.setEnabled(False)
        self.test_thread = gw_test.MyThread()  # msg with self
        self.test_thread.test_status_signal.connect(self.status_set)
        self.test_thread.test_step_signal.connect(self.updata_step)
        self.test_thread.test_end_signal.connect(self.one_test_end)
        self.test_thread.start()

    def status_set(self, status_msg):
        # status_msg : {"type": "status", "msg": "testing ..."}
        _translate = QtCore.QCoreApplication.translate
        if status_msg["type"] == "status":
            self.lineEdit_3.setText(_translate("MainWindow", status_msg["msg"]))
        elif status_msg["type"] == "gw_mac":
            self.gatewayMac.setText(_translate("MainWindow", status_msg["msg"]))
        # self.progressBar.setProperty("value", int(msg) % 100)

    def updata_step(self, step_msg):
        # step_msg : {"step": 0, "result": 0, "info": "rssi : -100"}
        print("step : %d, result : %d" % (step_msg["step"], step_msg["result"]))
        for n, l in enumerate(gwmap.GatewayCheckListMap):
            if l["id"] == step_msg["step"]:
                self.check_table_set_result(n, step_msg["result"], step_msg["info"])



    def one_test_end(self, end_msg):
        # end_msg : {"result": 0, "info" : "ALL SUCCESS"}
        print("one_test_end, result : %d, info : %s" % (end_msg["result"], end_msg["info"]))
        print("++++++++++++++++++++++")
        print("MAC:%s" % self.gatewayMac.text())
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

        self.pBtTestStart.setEnabled(True)
        #if not self.test_thread.isFinished():
        #    print("test_thread is still running")

    def generate_logs(self):
        if not self.test_thread.isFinished():
            print("test_thread is still running")