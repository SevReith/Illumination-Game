# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sub_win_accounting.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 631, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mpl_tab1_canvas = Mpl_Canvas(self.verticalLayoutWidget)
        self.mpl_tab1_canvas.setObjectName("mpl_tab1_canvas")
        self.verticalLayout.addWidget(self.mpl_tab1_canvas)
        self.lbl_txt_tab1_last_month = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_txt_tab1_last_month.setFont(font)
        self.lbl_txt_tab1_last_month.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_txt_tab1_last_month.setObjectName("lbl_txt_tab1_last_month")
        self.verticalLayout.addWidget(self.lbl_txt_tab1_last_month)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_txt_cost = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_txt_cost.setObjectName("lbl_txt_cost")
        self.horizontalLayout_2.addWidget(self.lbl_txt_cost)
        self.lbl_cost_number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_cost_number.setObjectName("lbl_cost_number")
        self.horizontalLayout_2.addWidget(self.lbl_cost_number)
        self.lbl_txt_income = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_txt_income.setObjectName("lbl_txt_income")
        self.horizontalLayout_2.addWidget(self.lbl_txt_income)
        self.lbl_income_number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_income_number.setObjectName("lbl_income_number")
        self.horizontalLayout_2.addWidget(self.lbl_income_number)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_txt_profit = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_txt_profit.setObjectName("lbl_txt_profit")
        self.horizontalLayout.addWidget(self.lbl_txt_profit)
        self.lbl_profit_number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_profit_number.setObjectName("lbl_profit_number")
        self.horizontalLayout.addWidget(self.lbl_profit_number)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_tab1_show_summary = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_tab1_show_summary.setObjectName("btn_tab1_show_summary")
        self.horizontalLayout_3.addWidget(self.btn_tab1_show_summary)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 401, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 521, 451))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Accounting"))
        self.lbl_txt_tab1_last_month.setText(_translate("Form", "Last Month"))
        self.lbl_txt_cost.setText(_translate("Form", "Cost:"))
        self.lbl_cost_number.setText(_translate("Form", "0"))
        self.lbl_txt_income.setText(_translate("Form", "Income:"))
        self.lbl_income_number.setText(_translate("Form", "0"))
        self.lbl_txt_profit.setText(_translate("Form", "Profit:"))
        self.lbl_profit_number.setText(_translate("Form", "0"))
        self.btn_tab1_show_summary.setText(_translate("Form", "Show Detailed Summary"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Overview"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Cost"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Income"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Profit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Monthly Summary"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Total Cost"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Fixed Cost"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Supply Cost"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Building Cost"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Cost Structure"))
from Views.Mpl_Canvas import Mpl_Canvas


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
