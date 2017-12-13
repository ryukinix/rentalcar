#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

import sys
import os
from PyQt5 import QtWidgets
from rentalcar import forms
from rentalcar import models
from datetime import datetime
import decorating.stream

sys.stdout = decorating.stream.Unbuffered(sys.stdout)

class Add(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_AddWidget()
        self.ui.setupUi(self)
        self.parent = parent
        self.setupUi()
        self.default_ano = int(self.ui.anoInput.text())

    def setupUi(self):
        self.ui.okButton.clicked.connect(self.ok_action)
        self.ui.cancelarButton.clicked.connect(self.cancelar_action)

    def ok_action(self):
        brand = self.ui.marcaInput.text()
        model = self.ui.modeloInput.text()
        year = self.ui.anoInput.text()
        daily = self.ui.diariaInput.text()
        try:
            models.RentVehicle(brand, model, int(year), int(daily))
            self.parent.focus()
            self.clear_input()

        except Exception as e:
            print("Deu merda, corrige ai. {}".format(e)) # substituir dialog



    def cancelar_action(self):
        self.parent.focus()
        self.clear_input()

    def clear_input(self):
        self.ui.marcaInput.clear()
        self.ui.modeloInput.clear()
        self.ui.anoInput.setValue(self.default_ano)
        self.ui.diariaInput.clear()


    def update(self):
        pass

class Delete(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_DeleteWidget()
        self.ui.setupUi(self)
        self.parent = parent

    def update(self):
        pass


class Fetch(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_FetchWidget()
        self.ui.setupUi(self)
        self.parent = parent

    def update(self):
        pass


class Rent(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_RentWidget()
        self.ui.setupUi(self)
        self.parent = parent
        self.setupUi()

    def setupUi(self):
        self.ui.cancelarButton.clicked.connect(self.cancelar_button)
        self.ui.okButton.clicked.connect(self.ok_button)

    def ok_button(self):
        code = self.ui.codigoInput.text()
        client = self.ui.locatarioInput.text()
        date_start = self.ui.dataInput.text()
        days = self.ui.prazoInput.text()
        try:
            code = int(code)
            days = int(days)
            vehicle = models.Vehicle.search(code)
            date = datetime.strptime(date_start, "%d/%m/%Y")
            if vehicle:
                rented = vehicle.search_rent(date, days)
                if not rented:
                    vehicle.rent(client, date,  int(days))
                    print("Veiculo alugado!")
                    self.parent.focus()
                else:
                    print("Rented by: {}".format(rented))
            else:
                print("Veículo não encontrado.")

        except Exception as e:
            print("Merda: {}".format(e))

    def cancelar_button(self):
        self.parent.focus()


    def update(self):
        pass

class About(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_AboutDialog()
        self.ui.setupUi(self)
        self.parent = parent

    def update(self):
        pass


class Free(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_FreeWidget()
        self.ui.setupUi(self)
        self.parent = parent

    def update(self):
        pass


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
        widget.update()
        return lambda _: self.central_widget.setCurrentWidget(widget)

    def focus(self):
        self.central_widget.setCurrentWidget(self.tela_inicial_widget)
        self.update()

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


    def update(self):
        self.ui.cadastradosLCD.display(len(models.Vehicle.objects))
        self.ui.alugadosLCD.display(len(models.RentVehicle.get_alugados()))
        self.ui.atrasosLCD.display(models.RentVehicle.get_atrasos())

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
