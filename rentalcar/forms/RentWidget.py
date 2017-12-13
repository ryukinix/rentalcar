# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RentWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RentWidget(object):
    def setupUi(self, RentWidget):
        RentWidget.setObjectName("RentWidget")
        RentWidget.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(RentWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.codigoLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.codigoLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.codigoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.codigoLabel.setObjectName("codigoLabel")
        self.gridLayout.addWidget(self.codigoLabel, 0, 1, 1, 1)
        self.locatarioLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.locatarioLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.locatarioLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.locatarioLabel.setObjectName("locatarioLabel")
        self.gridLayout.addWidget(self.locatarioLabel, 1, 1, 1, 1)
        self.codigoInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.codigoInput.setObjectName("codigoInput")
        self.gridLayout.addWidget(self.codigoInput, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.okButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 4, 2, 1, 1)
        self.dataInput = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dataInput.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 12, 12), QtCore.QTime(0, 0, 0)))
        self.dataInput.setObjectName("dataInput")
        self.gridLayout.addWidget(self.dataInput, 2, 2, 1, 1)
        self.locatarioInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.locatarioInput.setObjectName("locatarioInput")
        self.gridLayout.addWidget(self.locatarioInput, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 3, 1, 1)
        self.dataLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dataLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dataLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dataLabel.setObjectName("dataLabel")
        self.gridLayout.addWidget(self.dataLabel, 2, 1, 1, 1)
        self.cancelarButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cancelarButton.setObjectName("cancelarButton")
        self.gridLayout.addWidget(self.cancelarButton, 4, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 3, 1, 1)
        self.prazoLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.prazoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prazoLabel.setObjectName("prazoLabel")
        self.gridLayout.addWidget(self.prazoLabel, 3, 1, 1, 1)
        self.prazoInput = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.prazoInput.setMinimum(1)
        self.prazoInput.setMaximum(30)
        self.prazoInput.setObjectName("prazoInput")
        self.gridLayout.addWidget(self.prazoInput, 3, 2, 1, 1)

        self.retranslateUi(RentWidget)
        QtCore.QMetaObject.connectSlotsByName(RentWidget)

    def retranslateUi(self, RentWidget):
        _translate = QtCore.QCoreApplication.translate
        RentWidget.setWindowTitle(_translate("RentWidget", "Form"))
        self.codigoLabel.setText(_translate("RentWidget", "Código"))
        self.locatarioLabel.setText(_translate("RentWidget", "Locatário"))
        self.okButton.setText(_translate("RentWidget", "Ok"))
        self.dataLabel.setText(_translate("RentWidget", "Data de Locação"))
        self.cancelarButton.setText(_translate("RentWidget", "Cancelar"))
        self.prazoLabel.setText(_translate("RentWidget", "Prazo"))

