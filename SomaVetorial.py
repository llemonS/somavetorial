# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SomavetorialGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import math
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(419, 358)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 30, 61, 26))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.vetorinput = QtGui.QLineEdit(self.centralwidget)
        self.vetorinput.setGeometry(QtCore.QRect(10, 30, 251, 27))
        self.vetorinput.setText(_fromUtf8(""))
        self.vetorinput.setObjectName(_fromUtf8("vetorinput"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 411, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 411, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.labelresposta = QtGui.QLabel(self.centralwidget)
        self.labelresposta.setGeometry(QtCore.QRect(10, 80, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelresposta.setFont(font)
        self.labelresposta.setObjectName(_fromUtf8("labelresposta"))
        self.ResetButton = QtGui.QPushButton(self.centralwidget)
        self.ResetButton.setGeometry(QtCore.QRect(340, 30, 61, 26))
        self.ResetButton.setObjectName(_fromUtf8("ResetButton"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 140, 59, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 230, 59, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.labelmodulo = QtGui.QLabel(self.centralwidget)
        self.labelmodulo.setGeometry(QtCore.QRect(10, 160, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelmodulo.setFont(font)
        self.labelmodulo.setObjectName(_fromUtf8("labelmodulo"))
        self.labelunitario = QtGui.QLabel(self.centralwidget)
        self.labelunitario.setGeometry(QtCore.QRect(8, 250, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelunitario.setFont(font)
        self.labelunitario.setObjectName(_fromUtf8("labelunitario"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 419, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHUE = QtGui.QMenu(self.menubar)
        self.menuHUE.setObjectName(_fromUtf8("menuHUE"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionBRBR = QtGui.QAction(MainWindow)
        self.actionBRBR.setObjectName(_fromUtf8("actionBRBR"))
        self.menuHUE.addAction(self.actionBRBR)
        self.menubar.addAction(self.menuHUE.menuAction())
        self.label.setBuddy(self.label)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.somavetorial)
        self.vetores = []
        self.ResetButton.clicked.connect(self.resetbutton)
    def somavetorial(self, MainWindow):
        vetor = str(self.vetorinput.text())
        self.vetores.append(vetor.split(','))
        self.vetores = [map(float, x) for x in self.vetores]
        vres = map(sum, zip(*self.vetores))
        modulo3 = math.sqrt((vres[0]**2) + (vres[1]**2) + (vres[2]**2))
        unitario = (vres[0]/modulo3,vres[1]/modulo3,vres[2]/modulo3)
        self.labelresposta.setText(str(vres[0])+" i ,"+str(vres[1])+" j ,"+str(vres[2])+" k")
        self.labelmodulo.setText("%.3f" % modulo3 + " Newtons")
        self.labelunitario.setText("%.3f" % unitario[0]+" i ,"+ "%.3f" % unitario[1]+ " j ,"+ "%.3f" % unitario[2] + " k")
        self.vetorinput.clear()
    def resetbutton(self, MainWindow):
        self.vetores = []
        self.vetorinput.clear()
        self.labelresposta.setText("")
        self.labelmodulo.setText('')
        self.labelunitario.setText('')

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SomaVetorial", None))
        self.pushButton.setText(_translate("MainWindow", "Inserir", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Insira os vetores abaixo: (ex: 1,2,3)</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Vetor Resultante:</span></p></body></html>", None))
        self.labelresposta.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.ResetButton.setText(_translate("MainWindow", "Reset", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Módulo:</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Unitário:</span></p></body></html>", None))
        self.labelmodulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.labelunitario.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.menuHUE.setTitle(_translate("MainWindow", "by lemonS", None))
        self.actionBRBR.setText(_translate("MainWindow", "HUE, BR", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

