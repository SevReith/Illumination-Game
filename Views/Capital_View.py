from PyQt5.QtWidgets import QMdiArea, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from Views import *
from Views import sub_win_accounting

class Capital_View(QMdiArea):
    """description of class"""

    def __init__(self, cap_mdl):
        super().__init__()

        self._panel_accounting = sub_win_accounting.Ui_Form()
        self._panel_accounting.setupUi(self)

        self._model_capital = cap_mdl

        #connect widgets to capital model
        self._model_capital.latest_cost_changed.connect(self.update_lbl_cost)
        self._model_capital.latest_income_changed.connect(self.update_lbl_income)
        self._model_capital.latest_profit_changed.connect(self.update_lbl_profit)
    

    @pyqtSlot(float)
    def update_lbl_cost(self, cost):
        self._panel_accounting.lbl_cost_number.setText(f'{cost:,.2f}{self._model_capital.currency_sign}')

    @pyqtSlot(float)
    def update_lbl_income(self, income):
        self._panel_accounting.lbl_income_number.setText(f'{income:,.2f}{self._model_capital.currency_sign}')

    @pyqtSlot(float, float)
    def update_lbl_profit(self, cost, income):
        profit = round(income - cost, 2)
        self._panel_accounting.lbl_profit_number.setText(f'{profit:,.2f}{self._model_capital.currency_sign}')
        row = self._panel_accounting.tableWidget.rowCount()
        self._panel_accounting.tableWidget.insertRow(row)
        self._panel_accounting.tableWidget.setItem(row, 0, QTableWidgetItem(f'{cost:,.2f}'))
        self._panel_accounting.tableWidget.setItem(row, 1, QTableWidgetItem(f'{income:,.2f}'))
        self._panel_accounting.tableWidget.setItem(row, 2, QTableWidgetItem(f'{profit:,.2f}'))
     