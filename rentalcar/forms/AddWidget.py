# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddWidget(object):
    def setupUi(self, AddWidget):
        AddWidget.setObjectName("AddWidget")
        AddWidget.resize(407, 297)
        self.gridLayoutWidget = QtWidgets.QWidget(AddWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 3, 1, 1)
        self.anoLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.anoLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.anoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.anoLabel.setObjectName("anoLabel")
        self.gridLayout.addWidget(self.anoLabel, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 4, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 0, 1, 1)
        self.anoInput = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.anoInput.setMinimum(1900)
        self.anoInput.setMaximum(2020)
        self.anoInput.setProperty("value", 2017)
        self.anoInput.setObjectName("anoInput")
        self.gridLayout.addWidget(self.anoInput, 3, 2, 1, 1)
        self.modeloLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.modeloLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.modeloLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.modeloLabel.setObjectName("modeloLabel")
        self.gridLayout.addWidget(self.modeloLabel, 2, 1, 1, 1)
        self.okButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.okButton.setAutoDefault(True)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 5, 2, 1, 1)
        self.diariaLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.diariaLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.diariaLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.diariaLabel.setObjectName("diariaLabel")
        self.gridLayout.addWidget(self.diariaLabel, 4, 1, 1, 1)
        self.cancelarButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cancelarButton.setAutoDefault(True)
        self.cancelarButton.setObjectName("cancelarButton")
        self.gridLayout.addWidget(self.cancelarButton, 5, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 0, 1, 1)
        self.diariaInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.diariaInput.setObjectName("diariaInput")
        self.gridLayout.addWidget(self.diariaInput, 4, 2, 1, 1)
        self.marcaLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.marcaLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.marcaLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.marcaLabel.setObjectName("marcaLabel")
        self.gridLayout.addWidget(self.marcaLabel, 0, 1, 1, 1)
        self.modeloInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.modeloInput.setObjectName("modeloInput")
        self.gridLayout.addWidget(self.modeloInput, 2, 2, 1, 1)
        self.marcaInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.marcaInput.setObjectName("marcaInput")
        self.gridLayout.addWidget(self.marcaInput, 0, 2, 1, 1)
        self.marcaInput.raise_()
        self.marcaLabel.raise_()
        self.diariaLabel.raise_()
        self.modeloLabel.raise_()
        self.anoLabel.raise_()
        self.cancelarButton.raise_()
        self.diariaInput.raise_()
        self.okButton.raise_()
        self.anoInput.raise_()
        self.modeloInput.raise_()

        self.retranslateUi(AddWidget)
        QtCore.QMetaObject.connectSlotsByName(AddWidget)
        AddWidget.setTabOrder(self.marcaInput, self.modeloInput)
        AddWidget.setTabOrder(self.modeloInput, self.anoInput)
        AddWidget.setTabOrder(self.anoInput, self.diariaInput)
        AddWidget.setTabOrder(self.diariaInput, self.okButton)
        AddWidget.setTabOrder(self.okButton, self.cancelarButton)

    def retranslateUi(self, AddWidget):
        _translate = QtCore.QCoreApplication.translate
        AddWidget.setWindowTitle(_translate("AddWidget", "Form"))
        self.anoLabel.setText(_translate("AddWidget", "Ano"))
        self.modeloLabel.setText(_translate("AddWidget", "Modelo"))
        self.okButton.setText(_translate("AddWidget", "Ok"))
        self.diariaLabel.setText(_translate("AddWidget", "Diária"))
        self.cancelarButton.setText(_translate("AddWidget", "Cancelar"))
        self.diariaInput.setToolTip(_translate("AddWidget", "Valor da diária"))
        self.marcaLabel.setText(_translate("AddWidget", "Marca"))
        self.modeloInput.setToolTip(_translate("AddWidget", "Marca do carro"))
        self.marcaInput.setToolTip(_translate("AddWidget", "Modelo do Carro"))

