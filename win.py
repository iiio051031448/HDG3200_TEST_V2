#!/user/bin/python3

import logging

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import win_main
import one_instace_box
#import msg_box as win_main
import time

class hdg3200_win:
    def __init__(self):
        logging.debug("-")

    def show_win(self):
        self.app = QApplication(sys.argv)
        self.MainWindow = QMainWindow()
        self.ui = win_main.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

        sys.exit(self.app.exec_())
        logging.debug("--------------- EXITTING ---------------")

    def show_one_instance_warning_box(self):
        self.app = QApplication(sys.argv)
        self.MainWindow =  QMainWindow()
        self.ui = one_instace_box.Ui_one_instance_warning()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def close_win(self):
        logging.debug("-")

    def up_status(self, msg):
        logging.debug("-")
        self.ui.status_set(msg)

if __name__ == '__main__':
    # msg_box_show()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = win_main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())