#!/user/bin/python3

import logging


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import win_main

class hdg3200_win:
    def __init__(self):
        logging.debug("-")

    def show_win(self):
        self.app = QApplication(sys.argv)
        self.MainWindow = QMainWindow()
        ui = win_main.Ui_MainWindow()
        ui.setupUi(self.MainWindow)
        self.MainWindow.show()


        sys.exit(self.app.exec_())


        ui.check_table_set_success(self.MainWindow, 1)
        ui.check_table_set_failed(self.MainWindow, 2)

    def close_win(self):
        logging.debug("-")