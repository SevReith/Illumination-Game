# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 300, 901))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.button_end_turn = QtWidgets.QPushButton(self.frame)
        self.button_end_turn.setGeometry(QtCore.QRect(0, 840, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_end_turn.setFont(font)
        self.button_end_turn.setObjectName("button_end_turn")
        self.button_factory = QtWidgets.QPushButton(self.frame)
        self.button_factory.setGeometry(QtCore.QRect(0, 720, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_factory.setFont(font)
        self.button_factory.setObjectName("button_factory")
        self.button_market = QtWidgets.QPushButton(self.frame)
        self.button_market.setGeometry(QtCore.QRect(0, 660, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_market.setFont(font)
        self.button_market.setObjectName("button_market")
        self.button_accounting = QtWidgets.QPushButton(self.frame)
        self.button_accounting.setGeometry(QtCore.QRect(0, 600, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_accounting.setFont(font)
        self.button_accounting.setObjectName("button_accounting")
        self.lbl_turn = QtWidgets.QLabel(self.frame)
        self.lbl_turn.setGeometry(QtCore.QRect(0, 0, 300, 120))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_turn.setFont(font)
        self.lbl_turn.setObjectName("lbl_turn")
        self.lbl_capital = QtWidgets.QLabel(self.frame)
        self.lbl_capital.setGeometry(QtCore.QRect(0, 121, 300, 120))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_capital.setFont(font)
        self.lbl_capital.setObjectName("lbl_capital")
        self.lbl_factory_blueprint = QtWidgets.QLabel(self.centralwidget)
        self.lbl_factory_blueprint.setGeometry(QtCore.QRect(300, 0, 1300, 900))
        self.lbl_factory_blueprint.setText("")
        self.lbl_factory_blueprint.setObjectName("lbl_factory_blueprint")
        self.rbtn_production = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_production.setGeometry(QtCore.QRect(1070, 380, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rbtn_production.setFont(font)
        self.rbtn_production.setObjectName("rbtn_production")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_end_turn.setText(_translate("MainWindow", "End Turn"))
        self.button_factory.setText(_translate("MainWindow", "Factory"))
        self.button_market.setText(_translate("MainWindow", "Market"))
        self.button_accounting.setText(_translate("MainWindow", "Accounting"))
        self.lbl_turn.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_capital.setText(_translate("MainWindow", "TextLabel"))
        self.rbtn_production.setText(_translate("MainWindow", "Production"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
