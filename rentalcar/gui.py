from rentalcar import forms

import sys
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = forms.Ui_MainWindow()
    ui.setupUi(window)


    window.show()
    sys.exit(app.exec_())
