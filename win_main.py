# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
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
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(30, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 180, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 150, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)




        self.retranslateUi(MainWindow)
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

        self.check_list_map = [{"table_msg": ["项目", "子项", "结果", "信息"], "table_items": []},
                          {"table_msg": ["1.1 模块测试-通信测试", None, 0, None], "table_items": []},
                          {"table_msg": ["1.2 模块测试-SN测试", None, 0, None], "table_items": []},
                          {"table_msg": ["1.3 模块测试-信号强度测试", None, 0, None], "table_items": []},
                          {"table_msg": ["1.4 模块测试-重启测试", None, 0, None], "table_items": []},
                          {"table_msg": ["2.1 设备测试-端口测试", None, 0, None], "table_items": []},
                          {"table_msg": ["2.2 设备测试-灯光测试", "红", 0, None], "table_items": []},
                          {"table_msg": ["", "绿", 0, None], "table_items": []},
                          {"table_msg": ["", "蓝", 0, None], "table_items": []},
                          {"table_msg": ["2.3 设备测试-按键测试", "RESET键", 0, None], "table_items": []},
                          {"table_msg": ["", "SMARTCONFIG键", 0, None], "table_items": []},
                          {"table_msg": ["3.1 系统测试-读取数据", None, 0, None], "table_items": []},
                          {"table_msg": ["3.2 系统测试-校验MAC", None, 0, None], "table_items": []},
                          {"table_msg": ["3.3 系统测试-写入SN", None, 0, None], "table_items": []},
                          {"table_msg": ["4.1 结束测试-写入标记", None, 0, None], "table_items": []},
                          {"table_msg": ["4.1 结束测试-写入标记", None, 0, None], "table_items": []}];
        #'''
        for r, row_list in enumerate(self.check_list_map):
            for c, item_v in enumerate(row_list["table_msg"]):
                print(item_v)
                print("%d, %d" % (r, c))

                item = self.check_list.item(r, c)
                row_list["table_items"].extend([item])
                if item_v != None:
                    if item_v == 0:
                        item.setText(_translate("MainWindow", "wait"))
                    else:
                        item.setText(_translate("MainWindow", item_v))
                else:
                    item.setText(_translate("MainWindow", ""))

        self.check_list.setSortingEnabled(__sortingEnabled)



        self.groupBox.setTitle(_translate("MainWindow", "测试"))
        self.label.setText(_translate("MainWindow", "日期"))
        self.lineEdit.setText(_translate("MainWindow", "2018-04-12"))
        self.label_2.setText(_translate("MainWindow", "时间"))
        self.lineEdit_2.setText(_translate("MainWindow", "15:27:33"))
        self.pushButton.setText(_translate("MainWindow", "开始测试"))
        self.pushButton_2.setText(_translate("MainWindow", "生产日志"))
        self.pushButton_3.setText(_translate("MainWindow", "查看日志"))

    def check_table_set_result(self, MainWindow, index, result):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        if result == 0:
            row_back_color = QtGui.QColor(0, 180, 0)
            result_str = "成功"
        else:
            row_back_color = QtGui.QColor(230, 0, 0)
            result_str = "失败"

        self.check_list_map[index]["table_items"][2].setText(_translate("MainWindow", result_str))
        for item in self.check_list_map[index]["table_items"]:
            item.setBackground(row_back_color)

    def check_table_set_success(self, MainWindow, index):
        self.check_table_set_result(MainWindow, index, 0)

    def check_table_set_failed(self, MainWindow, index):
        self.check_table_set_result(MainWindow, index, 1)