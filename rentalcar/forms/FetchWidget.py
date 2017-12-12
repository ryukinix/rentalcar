# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FetchWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FetchWidget(object):
    def setupUi(self, FetchWidget):
        FetchWidget.setObjectName("FetchWidget")
        FetchWidget.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(FetchWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeView = QtWidgets.QTreeView(FetchWidget)
        self.treeView.setUniformRowHeights(True)
        self.treeView.setSortingEnabled(True)
        self.treeView.setAnimated(True)
        self.treeView.setWordWrap(True)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sairButton = QtWidgets.QPushButton(FetchWidget)
        self.sairButton.setObjectName("sairButton")
        self.horizontalLayout_4.addWidget(self.sairButton)
        self.detalhesButton = QtWidgets.QPushButton(FetchWidget)
        self.detalhesButton.setObjectName("detalhesButton")
        self.horizontalLayout_4.addWidget(self.detalhesButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(FetchWidget)
        QtCore.QMetaObject.connectSlotsByName(FetchWidget)

    def retranslateUi(self, FetchWidget):
        _translate = QtCore.QCoreApplication.translate
        FetchWidget.setWindowTitle(_translate("FetchWidget", "Form"))
        self.treeView.setToolTip(_translate("FetchWidget", "Carros cadastrados"))
        self.sairButton.setText(_translate("FetchWidget", "Sair"))
        self.detalhesButton.setText(_translate("FetchWidget", "Detalhes"))

