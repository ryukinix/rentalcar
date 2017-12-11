#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

import sys
from PyQt5 import QtWidgets
from GUI.MainWindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)


window.show()
sys.exit(app.exec_())
