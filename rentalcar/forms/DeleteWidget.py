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
        self.verticalLayoutWidget = QtWidgets.QWidget(DeleteWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 382, 282))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeView = QtWidgets.QTreeView(self.verticalLayoutWidget)
        self.treeView.setUniformRowHeights(True)
        self.treeView.setSortingEnabled(True)
        self.treeView.setAnimated(True)
        self.treeView.setWordWrap(True)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sairButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sairButton.setObjectName("sairButton")
        self.horizontalLayout_4.addWidget(self.sairButton)
        self.excluirButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.excluirButton.setObjectName("excluirButton")
        self.horizontalLayout_4.addWidget(self.excluirButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(DeleteWidget)
        QtCore.QMetaObject.connectSlotsByName(DeleteWidget)

    def retranslateUi(self, DeleteWidget):
        _translate = QtCore.QCoreApplication.translate
        DeleteWidget.setWindowTitle(_translate("DeleteWidget", "Form"))
        self.treeView.setToolTip(_translate("DeleteWidget", "Carros que podem ser removidos"))
        self.sairButton.setText(_translate("DeleteWidget", "Sair"))
        self.excluirButton.setText(_translate("DeleteWidget", "Excluir"))

