from rentalcar import forms

import sys
from PyQt5 import QtWidgets

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        ui = forms.Ui_MainWindow()
        ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()

    window.show()
    sys.exit(app.exec_())
