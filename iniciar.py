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

    def file(self):

        options = QFileDialog.Options()

        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Documentos (*.txt)", options=options)
        if self.fileName:
            print(self.fileName)
            self.ui.escolheArquivo.setText(self.fileName.split("/")[-1])

    def gerar(self):
        if self.fileName != None:
            if self.ui.checkTipo.isChecked():
                l = Leitor(self.fileName,str(self.ui.calendario.selectedDate().toPyDate()))
                l.lerArquivoMes()
            else:
                l = Leitor(self.fileName,str(self.ui.calendario.selectedDate().toPyDate()))
                l.lerArquivoDia()



def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Editor()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
