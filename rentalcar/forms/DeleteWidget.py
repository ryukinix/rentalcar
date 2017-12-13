# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeleteWidget(object):
    def setupUi(self, DeleteWidget):
        DeleteWidget.setObjectName("DeleteWidget")
        DeleteWidget.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(DeleteWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeView = QtWidgets.QTreeView(DeleteWidget)
        self.treeView.setUniformRowHeights(True)
        self.treeView.setSortingEnabled(True)
        self.treeView.setAnimated(True)
        self.treeView.setWordWrap(True)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sairButton = QtWidgets.QPushButton(DeleteWidget)
        self.sairButton.setObjectName("sairButton")
        self.horizontalLayout_4.addWidget(self.sairButton)
        self.excluirButton = QtWidgets.QPushButton(DeleteWidget)
        self.excluirButton.setObjectName("excluirButton")
        self.horizontalLayout_4.addWidget(self.excluirButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(DeleteWidget)
        QtCore.QMetaObject.connectSlotsByName(DeleteWidget)

    def retranslateUi(self, DeleteWidget):
        _translate = QtCore.QCoreApplication.translate
        DeleteWidget.setWindowTitle(_translate("DeleteWidget", "Form"))
        self.treeView.setToolTip(_translate("DeleteWidget", "Carros cadastrados"))
        self.sairButton.setText(_translate("DeleteWidget", "Sair"))
        self.excluirButton.setText(_translate("DeleteWidget", "Excluir"))

