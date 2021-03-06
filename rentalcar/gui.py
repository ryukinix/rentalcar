#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

# stdlib
import sys
import os
from datetime import datetime

# Qt
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import (QDate, QDateTime, QRegExp,
                          QSortFilterProxyModel, Qt, QTime)
from PyQt5.QtGui import QStandardItemModel

# self-package
from rentalcar import forms
from rentalcar import models


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
            msg = "Deu merda, corrige ai. {}".format(e)
            QMessageBox.warning(self, 'Erro', msg, QMessageBox.Close, QMessageBox.Close)



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

    CODE, MODELO, MARCA = range(3)

    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_DeleteWidget()
        self.ui.setupUi(self)
        self.parent = parent
        self.setupUi()

    def setupUi(self):
        self.ui.sairButton.clicked.connect(self.sair_button)
        self.ui.excluirButton.clicked.connect(self.excluir_button)
        self.model = QStandardItemModel(0, 3, self.parent)
        self.model.setHeaderData(self.CODE, Qt.Horizontal, "Código")
        self.model.setHeaderData(self.MODELO, Qt.Horizontal, "Modelo")
        self.model.setHeaderData(self.MARCA, Qt.Horizontal, "Marca")
        self.ui.treeView.setModel(self.model)

    def excluir_button(self):
        selected = self.ui.treeView.selectedIndexes()
        if len(selected) > 0:
            index = self.ui.treeView.selectedIndexes()[0]
            item = index.model().itemFromIndex(index)
            index = self.model.index(item.row(), self.CODE)
            code = self.model.data(index)
            v = models.RentVehicle.delete(code)
        self.fetch()

    def sair_button(self):
        self.parent.focus()

    def update(self):
        self.fetch()

    def fetch(self):
        self.model.removeRows(0, self.model.rowCount())
        for v in (x for x in models.RentVehicle.objects if len(x.clients) == 0):
            self.model.insertRow(0)
            code = v.code
            model = v.model
            brand = v.brand
            self.model.setData(self.model.index(0, self.CODE), code)
            self.model.setData(self.model.index(0, self.MODELO), model)
            self.model.setData(self.model.index(0, self.MARCA), brand)



class Fetch(QtWidgets.QWidget):

    CODE, MODELO, STATUS = range(3)

    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_FetchWidget()
        self.ui.setupUi(self)
        self.parent = parent
        self.setupUi()

    def setupUi(self):
        self.ui.sairButton.clicked.connect(self.sair_button)
        self.ui.detalhesButton.clicked.connect(self.detalhes_button)
        self.model = QStandardItemModel(0, 3, self.parent)
        self.model.setHeaderData(self.CODE, Qt.Horizontal, "Código")
        self.model.setHeaderData(self.MODELO, Qt.Horizontal, "Modelo")
        self.model.setHeaderData(self.STATUS, Qt.Horizontal, "Status")
        self.ui.treeView.setModel(self.model)

    def detalhes_button(self):
        selected = self.ui.treeView.selectedIndexes()
        if len(selected) > 0:
            index = self.ui.treeView.selectedIndexes()[0]
            item = index.model().itemFromIndex(index)
            index = self.model.index(item.row(), self.CODE)
            code = self.model.data(index)
            v = models.RentVehicle.search(code)
            msg = "Detalhes: Marca: {} | Ano: {} | Diária: R$ {}".format(v.brand, v.year, v.daily)
            QMessageBox.information(self, 'Carrinho', msg, QMessageBox.Close, QMessageBox.Close)


    def sair_button(self):
        self.parent.focus()

    def update(self):
        self.fetch()

    def fetch(self):
        self.model.removeRows(0, self.model.rowCount())
        for v in models.RentVehicle.objects:
            self.model.insertRow(0)
            code = v.code
            status = v.status
            model = v.model
            self.model.setData(self.model.index(0, self.CODE), code)
            self.model.setData(self.model.index(0, self.MODELO), model)
            self.model.setData(self.model.index(0, self.STATUS), status)




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
        msg = ""
        try:
            code = int(code)
            days = int(days)
            vehicle = models.Vehicle.search(code)
            date = datetime.strptime(date_start, "%d/%m/%Y")
            diff_days = (date  - models.date).days
            if diff_days > 30 or diff_days < -1:
                QMessageBox.information(self, 'Erro',
                                        "Data de locação deve ser de 1 a 30 dias.",
                                        QMessageBox.Close, QMessageBox.Close)

            elif vehicle:
                rented = vehicle.search_rent(date, days)
                if not rented:
                    vehicle.rent(client, date,  int(days))
                    msg = "Veículo {} {} alugado para {} com sucesso!".format(vehicle.brand,
                                                                              vehicle.model,
                                                                              client)

                    self.parent.focus()
                else:
                    msg = "Veículo já está reservado para: {}".format(rented)
                    print()
            else:
                msg = "Veículo não encontrado."

        except Exception as e:
            msg = "Merda, ajuda aí: {}".format(e)

        if msg:
            QMessageBox.information(self, 'Info', msg, QMessageBox.Close, QMessageBox.Close)

    def cancelar_button(self):
        self.parent.focus()


    def update(self):
        self.ui.codigoInput.clear()
        self.ui.locatarioInput.clear()
        year, month, day = models.date.year, models.date.month, models.date.day
        self.ui.dataInput.setDateTime(QtCore.QDateTime(QtCore.QDate(year, month, day), QtCore.QTime(0, 0, 0)))

class About(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_AboutDialog()
        self.ui.setupUi(self)
        self.parent = parent

    def update(self):
        pass


class Free(QtWidgets.QWidget):
    CODE, MODELO, LOCATARIO, DATA, PRAZO = range(5)

    def __init__(self, parent):
        super().__init__()
        self.ui = forms.Ui_FreeWidget()
        self.ui.setupUi(self)
        self.parent = parent
        self.setupUi()

    def setupUi(self):
        self.ui.sairButton.clicked.connect(self.sair_button)
        self.ui.liberarButton.clicked.connect(self.liberar_button)
        self.model = QStandardItemModel(0, 5, self.parent)
        self.model.setHeaderData(self.CODE, Qt.Horizontal, "Código")
        self.model.setHeaderData(self.MODELO, Qt.Horizontal, "Modelo")
        self.model.setHeaderData(self.LOCATARIO, Qt.Horizontal, "Locatário")
        self.model.setHeaderData(self.DATA, Qt.Horizontal, "Data")
        self.model.setHeaderData(self.PRAZO, Qt.Horizontal, "Dias")
        self.ui.treeView.setModel(self.model)

    def liberar_button(self):
        selected = self.ui.treeView.selectedIndexes()
        if len(selected) > 0:
            index = self.ui.treeView.selectedIndexes()[0]
            item = index.model().itemFromIndex(index)
            index_code = self.model.index(item.row(), self.CODE)
            index_client = self.model.index(item.row(), self.LOCATARIO)
            code = self.model.data(index_code)
            client = self.model.data(index_client)
            v = models.RentVehicle.search(code)
            if v.alugado:
                msg = "Valor a ser pago equivalente a: R$ {}".format(v.total_to_pay(client))
                QMessageBox.information(self, 'Info', msg, QMessageBox.Close, QMessageBox.Close)
            v.free(client)
        self.fetch()

    def sair_button(self):
        self.parent.focus()

    def update(self):
        self.fetch()

    def fetch(self):
        self.model.removeRows(0, self.model.rowCount())
        for v in (x for x in models.RentVehicle.objects if len(x.clients) > 0):
            code = v.code
            model = v.model
            brand = v.brand
            for c in v.clients.keys():
                data, days = v.clients[c]
                self.model.insertRow(0)
                self.model.setData(self.model.index(0, self.CODE), code)
                self.model.setData(self.model.index(0, self.MODELO), model)
                self.model.setData(self.model.index(0, self.LOCATARIO), c)
                self.model.setData(self.model.index(0, self.DATA), data.strftime(models.dateformat))
                self.model.setData(self.model.index(0, self.PRAZO), days)





class Main(QtWidgets.QMainWindow):
    "Janela principal contendo todos os menus e informações"

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
        def update(_):
            widget.update()
            self.central_widget.setCurrentWidget(widget)
        return update

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
        self.ui.actionSalvar.triggered.connect(lambda _: models.RentVehicle.salvar_tudo())
        self.ui.dataText.setText(models.date.strftime(models.dateformat))
        self.ui.avancarDataButton.clicked.connect(self.update_date)

    def update_date(self):
        self.ui.dataText.setText(models.increase_day().strftime(models.dateformat))
        self.update()


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
