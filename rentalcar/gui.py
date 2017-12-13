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
from rentalcar import forms
from rentalcar import models


class Add(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_AddWidget()
        self.ui.setupUi(self)
        self.parent = parent


class Delete(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_DeleteWidget()
        self.ui.setupUi(self)
        self.parent = parent



class Fetch(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_FetchWidget()
        self.ui.setupUi(self)
        self.parent = parent



class Rent(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_RentWidget()
        self.ui.setupUi(self)
        self.parent = parent



class About(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_AboutDialog()
        self.ui.setupUi(self)
        self.parent = parent


class Free(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_FreeWidget()
        self.ui.setupUi(self)
        self.parent = parent



class Main(QtWidgets.QMainWindow):
    "Janela principal contendo todos os menus e informações"
    dateformat = "%d/%m/%Y"
    def __init__(self):
        super().__init__()
        self.ui = forms.Ui_MainWindow()
        self.ui.setupUi(self)
        self.central_widget = QtWidgets.QStackedWidget()
        self.tela_inicial_widget = self.ui.centralwidget
        self.add_widget = Add(self)
        self.rent_widget = Rent(self)
        self.delete_widget = Delete(self)
        self.free_widget = Free(self)
        self.fetch_widget = Fetch(self)
        self.about_dialog = About(self)
        self.widgets = [
            self.tela_inicial_widget,
            self.add_widget,
            self.rent_widget,
            self.delete_widget,
            self.free_widget,
            self.fetch_widget,
        ]
        self.setupUi()

    def widget_changer(self, widget):
        return lambda _: self.central_widget.setCurrentWidget(widget)

    def setupUi(self):
        "Inicializa parâmetros especiais da UI"
        for w in self.widgets:
            self.central_widget.addWidget(w)
        self.central_widget.addWidget(self.ui.centralwidget)
        self.central_widget.setCurrentWidget(self.tela_inicial_widget)
        self.setCentralWidget(self.central_widget)
        self.ui.actionAdicionar.triggered.connect(self.widget_changer(self.add_widget))
        self.ui.actionAlugar.triggered.connect(self.widget_changer(self.rent_widget))
        self.ui.actionExcluir.triggered.connect(self.widget_changer(self.delete_widget))
        self.ui.actionDevolver.triggered.connect(self.widget_changer(self.free_widget))
        self.ui.actionConsultar.triggered.connect(self.widget_changer(self.fetch_widget))
        self.ui.actionTela_Inicial.triggered.connect(self.widget_changer(self.tela_inicial_widget))
        self.ui.actionSair.triggered.connect(self.close)
        self.ui.actionSobre.triggered.connect(lambda _: self.about_dialog.show())
        self.ui.dataText.setText(models.date.strftime(self.dateformat))
        self.ui.avancarDataButton.clicked.connect(self.update_date)

    def update_date(self):
        self.ui.dataText.setText(models.increase_day().strftime(self.dateformat))



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
