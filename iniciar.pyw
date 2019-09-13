import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from Tela import Ui_TelaPrincipal
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from leitor import Leitor

class Editor(QtWidgets.QMainWindow):

    def __init__(self):
       
        super(Editor, self).__init__()
        self.ui=Ui_TelaPrincipal()
        self.ui.setupUi(self)
        self.show()
        self.fileName = None
        self.ui.checkplanilha.setChecked(True)


        

    def file(self):

        options = QFileDialog.Options()

        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Documentos (*.dat *.txt)", options=options)
        if self.fileName:
            print(self.fileName)
            self.ui.escolheArquivo.setText(self.fileName.split("/")[-1])

    def gerar(self):
        if self.fileName != None:
            l = Leitor(self.fileName,str(self.ui.calendario.selectedDate().toPyDate()))
            if self.ui.checkplanilha.isChecked():
                l.escreverXls()
            elif self.ui.checkDia.isChecked():
                l.lerArquivoDia()
            else:
                l.lerArquivoMes()
            
    def clickCheck(self):
        if self.ui.checkplanilha.isChecked():
            self.ui.checkplanilha.setChecked(False)
        if self.ui.checkmes.isChecked():
            self.ui.checkmes.setChecked(False)
    
    def clickCheckMes(self):
        if self.ui.checkplanilha.isChecked():
            self.ui.checkplanilha.setChecked(False)
        if self.ui.checkDia.isChecked():
            self.ui.checkDia.setChecked(False)


    def clickCheckPlan(self):
        if self.ui.checkDia.isChecked():
            self.ui.checkDia.setChecked(False)
        if self.ui.checkmes.isChecked():
            self.ui.checkmes.setChecked(False)
def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Editor()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
