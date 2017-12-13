# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FreeWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FreeWidget(object):
    def setupUi(self, FreeWidget):
        FreeWidget.setObjectName("FreeWidget")
        FreeWidget.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(FreeWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeView = QtWidgets.QTreeView(FreeWidget)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setUniformRowHeights(True)
        self.treeView.setSortingEnabled(True)
        self.treeView.setAnimated(True)
        self.treeView.setWordWrap(True)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sairButton = QtWidgets.QPushButton(FreeWidget)
        self.sairButton.setObjectName("sairButton")
        self.horizontalLayout_4.addWidget(self.sairButton)
        self.liberarButton = QtWidgets.QPushButton(FreeWidget)
        self.liberarButton.setAutoDefault(True)
        self.liberarButton.setObjectName("liberarButton")
        self.horizontalLayout_4.addWidget(self.liberarButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(FreeWidget)
        QtCore.QMetaObject.connectSlotsByName(FreeWidget)

    def retranslateUi(self, FreeWidget):
        _translate = QtCore.QCoreApplication.translate
        FreeWidget.setWindowTitle(_translate("FreeWidget", "Form"))
        self.treeView.setToolTip(_translate("FreeWidget", "Carros cadastrados"))
        self.sairButton.setText(_translate("FreeWidget", "Sair"))
        self.liberarButton.setText(_translate("FreeWidget", "Liberar/Devolver"))

