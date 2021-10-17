import sys
#from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)
from PyQt5.QtCore import Qt
from Illumination_Game import *

class GUI(QWidget):
    """description of class"""

    def __init__(self):
        super().__init__()
        self.initGUI()


    def initGUI(self):
        #adding main panel buttons
        buttonEndTurn = QPushButton(self)
        buttonEndTurn.setText('End Turn')
        buttonEndTurn.setGeometry(0,900,280,60)
        buttonEndTurn.clicked.connect(endTurnClicked)

        self.setFixedSize(1280, 960)
        self.setWindowTitle('Illumination Game')
        self.show()



def endTurnClicked():
    lightBulb.subtractProduct(5)
    print(lightBulb.productName, lightBulb.getProductAmount, sep=': ')         



    
def runGUI():
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())
