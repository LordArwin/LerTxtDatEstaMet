# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaPrincipal(object):
    def setupUi(self, TelaPrincipal):
        TelaPrincipal.setObjectName("TelaPrincipal")
        TelaPrincipal.setEnabled(True)
        TelaPrincipal.resize(440, 445)
        self.centralwidget = QtWidgets.QWidget(TelaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.calendario = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendario.setObjectName("calendario")
        self.gridLayout.addWidget(self.calendario, 4, 0, 1, 2)
        self.checkTipo = QtWidgets.QCheckBox(self.centralwidget)
        self.checkTipo.setObjectName("checkTipo")
        self.gridLayout.addWidget(self.checkTipo, 5, 1, 1, 1)
        self.botaoGerar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoGerar.setObjectName("botaoGerar")
        self.gridLayout.addWidget(self.botaoGerar, 5, 0, 1, 1)
        self.escolheArquivo = QtWidgets.QPushButton(self.centralwidget)
        self.escolheArquivo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("seletor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.escolheArquivo.setIcon(icon)
        self.escolheArquivo.setAutoDefault(False)
        self.escolheArquivo.setFlat(False)
        self.escolheArquivo.setObjectName("escolheArquivo")
        self.gridLayout.addWidget(self.escolheArquivo, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        TelaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 21))
        self.menubar.setObjectName("menubar")
        self.menuSair = QtWidgets.QMenu(self.menubar)
        self.menuSair.setObjectName("menuSair")
        TelaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaPrincipal)
        self.statusbar.setObjectName("statusbar")
        TelaPrincipal.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSair.menuAction())

        self.retranslateUi(TelaPrincipal)
        self.escolheArquivo.clicked.connect(TelaPrincipal.file)
        self.botaoGerar.clicked.connect(TelaPrincipal.gerar)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipal)

    def retranslateUi(self, TelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        TelaPrincipal.setWindowTitle(_translate("TelaPrincipal", "Tela Principal"))
        self.checkTipo.setText(_translate("TelaPrincipal", "Somente Mês e Ano"))
        self.botaoGerar.setText(_translate("TelaPrincipal", "Gerar"))
        self.escolheArquivo.setText(_translate("TelaPrincipal", "..."))
        self.label_2.setText(_translate("TelaPrincipal", "Selecione o Arquivo:"))
        self.menuSair.setTitle(_translate("TelaPrincipal", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_TelaPrincipal()
    ui.setupUi(TelaPrincipal)
    TelaPrincipal.show()
    sys.exit(app.exec_())
