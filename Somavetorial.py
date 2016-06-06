import sys
import math
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "SomavetorialGUI.ui" # Enter file here.

 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.somavetorial)
        self.vetores = []
        self.ResetButton.clicked.connect(self.resetbutton)
    def somavetorial(self):
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
    def resetbutton(self):
        self.vetores = []
        self.vetorinput.clear()
        self.labelresposta.setText("")
        self.labelmodulo.setText('')
        self.labelunitario.setText('')
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())