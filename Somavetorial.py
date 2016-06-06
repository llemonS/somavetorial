import sys
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
        self.labelresposta.setText(str(vres[0])+" i ,"+str(vres[1])+" j ,"+str(vres[2])+" k")
        self.vetorinput.clear()
    def resetbutton(self):
        self.vetores = []
        self.vetorinput.clear()
        self.labelresposta.setText("")
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())