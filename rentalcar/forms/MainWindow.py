# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 297)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 385, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.dataLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        self.dataLabel.setFont(font)
        self.dataLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dataLabel.setTextFormat(QtCore.Qt.AutoText)
        self.dataLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dataLabel.setWordWrap(False)
        self.dataLabel.setOpenExternalLinks(False)
        self.dataLabel.setObjectName("dataLabel")
        self.gridLayout.addWidget(self.dataLabel, 0, 0, 1, 1)
        self.atrasosLCD = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.atrasosLCD.setObjectName("atrasosLCD")
        self.gridLayout.addWidget(self.atrasosLCD, 3, 1, 1, 1)
        self.atrasosLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        self.atrasosLabel.setFont(font)
        self.atrasosLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.atrasosLabel.setTextFormat(QtCore.Qt.AutoText)
        self.atrasosLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.atrasosLabel.setWordWrap(False)
        self.atrasosLabel.setOpenExternalLinks(False)
        self.atrasosLabel.setObjectName("atrasosLabel")
        self.gridLayout.addWidget(self.atrasosLabel, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dataText = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        self.dataText.setFont(font)
        self.dataText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dataText.setTextFormat(QtCore.Qt.AutoText)
        self.dataText.setAlignment(QtCore.Qt.AlignCenter)
        self.dataText.setWordWrap(False)
        self.dataText.setOpenExternalLinks(False)
        self.dataText.setObjectName("dataText")
        self.horizontalLayout_2.addWidget(self.dataText)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.cadastradosLCD = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.cadastradosLCD.setObjectName("cadastradosLCD")
        self.gridLayout.addWidget(self.cadastradosLCD, 1, 1, 1, 1)
        self.cadastradosLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        self.cadastradosLabel.setFont(font)
        self.cadastradosLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cadastradosLabel.setTextFormat(QtCore.Qt.AutoText)
        self.cadastradosLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cadastradosLabel.setWordWrap(False)
        self.cadastradosLabel.setOpenExternalLinks(False)
        self.cadastradosLabel.setObjectName("cadastradosLabel")
        self.gridLayout.addWidget(self.cadastradosLabel, 1, 0, 1, 1)
        self.alugadosLCD = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.alugadosLCD.setObjectName("alugadosLCD")
        self.gridLayout.addWidget(self.alugadosLCD, 2, 1, 1, 1)
        self.alugadosLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(10)
        self.alugadosLabel.setFont(font)
        self.alugadosLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.alugadosLabel.setTextFormat(QtCore.Qt.AutoText)
        self.alugadosLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.alugadosLabel.setWordWrap(False)
        self.alugadosLabel.setOpenExternalLinks(False)
        self.alugadosLabel.setObjectName("alugadosLabel")
        self.gridLayout.addWidget(self.alugadosLabel, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        self.menuPrincipal = QtWidgets.QMenu(self.menubar)
        self.menuPrincipal.setObjectName("menuPrincipal")
        self.menuAcao = QtWidgets.QMenu(self.menubar)
        self.menuAcao.setObjectName("menuAcao")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPrincipal = QtWidgets.QAction(MainWindow)
        self.actionPrincipal.setObjectName("actionPrincipal")
        self.actionAdicionar = QtWidgets.QAction(MainWindow)
        self.actionAdicionar.setObjectName("actionAdicionar")
        self.actionExcluir = QtWidgets.QAction(MainWindow)
        self.actionExcluir.setObjectName("actionExcluir")
        self.actionAlugar = QtWidgets.QAction(MainWindow)
        self.actionAlugar.setObjectName("actionAlugar")
        self.actionDevolver = QtWidgets.QAction(MainWindow)
        self.actionDevolver.setObjectName("actionDevolver")
        self.actionDicas = QtWidgets.QAction(MainWindow)
        self.actionDicas.setObjectName("actionDicas")
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionTela_Inicial = QtWidgets.QAction(MainWindow)
        self.actionTela_Inicial.setObjectName("actionTela_Inicial")
        self.menuPrincipal.addAction(self.actionTela_Inicial)
        self.menuPrincipal.addAction(self.actionPrincipal)
        self.menuPrincipal.addAction(self.actionAdicionar)
        self.menuPrincipal.addAction(self.actionExcluir)
        self.menuPrincipal.addSeparator()
        self.menuPrincipal.addAction(self.actionSair)
        self.menuAcao.addAction(self.actionAlugar)
        self.menuAcao.addAction(self.actionDevolver)
        self.menuAjuda.addAction(self.actionSobre)
        self.menubar.addAction(self.menuPrincipal.menuAction())
        self.menubar.addAction(self.menuAcao.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RentalCar"))
        self.dataLabel.setText(_translate("MainWindow", "Data Atual:"))
        self.atrasosLabel.setText(_translate("MainWindow", "Atrasos:"))
        self.dataText.setText(_translate("MainWindow", "dd/mm/aaaa"))
        self.pushButton.setText(_translate("MainWindow", "Avançar Data"))
        self.cadastradosLabel.setText(_translate("MainWindow", "Veículos cadastrados:"))
        self.alugadosLabel.setText(_translate("MainWindow", "Veículos alugados:"))
        self.menuPrincipal.setTitle(_translate("MainWindow", "Principal"))
        self.menuAcao.setTitle(_translate("MainWindow", "Ação"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.actionPrincipal.setText(_translate("MainWindow", "Consultar"))
        self.actionPrincipal.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionAdicionar.setText(_translate("MainWindow", "Adicionar"))
        self.actionAdicionar.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionExcluir.setText(_translate("MainWindow", "Excluir"))
        self.actionExcluir.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionAlugar.setText(_translate("MainWindow", "Alugar"))
        self.actionAlugar.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionDevolver.setText(_translate("MainWindow", "Devolver"))
        self.actionDevolver.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionDicas.setText(_translate("MainWindow", "Dicas"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))
        self.actionSobre.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionSair.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionTela_Inicial.setText(_translate("MainWindow", "Tela Inicial"))
        self.actionTela_Inicial.setShortcut(_translate("MainWindow", "Ctrl+Return"))

