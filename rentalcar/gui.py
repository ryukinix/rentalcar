# coding: utf-8

from rentalcar import forms

import sys
from PyQt5 import QtWidgets

class Main(QtWidgets.QMainWindow):
    "Janela principal contendo todos os menus e informações"
    def __init__(self):
        super().__init__()
        ui = forms.Ui_MainWindow()
        ui.setupUi(self)

def create():
    "Cria a aplicação e a janela"
    app = QtWidgets.QApplication(sys.argv)
    window = Main()

    return app, window


def main():
    "Realiza todos os procedimentos para abrir a aplicação"
    app, window = create()

    window.show()
    sys.exit(app.exec_())
