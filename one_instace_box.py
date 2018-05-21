# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'one_instace_box.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_one_instance_warning(object):
    def setupUi(self, one_instance_warning):
        one_instance_warning.setObjectName("one_instance_warning")
        one_instance_warning.resize(425, 179)
        """
        self.buttonBox = QtWidgets.QDialogButtonBox(one_instance_warning)
        self.buttonBox.setGeometry(QtCore.QRect(50, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        """
        self.label = QtWidgets.QLabel(one_instance_warning)
        self.label.setGeometry(QtCore.QRect(30, 30, 371, 61))
        self.label.setObjectName("label")

        self.retranslateUi(one_instance_warning)
        # self.buttonBox.accepted.connect(one_instance_warning.accept)
        # self.buttonBox.rejected.connect(one_instance_warning.reject)
        QtCore.QMetaObject.connectSlotsByName(one_instance_warning)

    def retranslateUi(self, one_instance_warning):
        _translate = QtCore.QCoreApplication.translate
        one_instance_warning.setWindowTitle(_translate("one_instance_warning", "信息"))
        self.label.setText(_translate("one_instance_warning", "<html><head/><body><p><span style=\" font-size:12pt;\">已经有一个实例再运行，请先关闭已经在运行的实例</span></p><p><span style=\" font-size:12pt;\">如果没有实例运行，请尝试删除【one.lock】文件</span></p></body></html>"))

