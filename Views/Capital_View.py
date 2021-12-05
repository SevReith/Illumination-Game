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
        self._model_capital.cost_detail_changed.connect(self.update_table_cost_detail)
    

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

    @pyqtSlot(float, float, float, float)
    def update_table_cost_detail(self, tot_cost, fixed_cost, mat_cost, build_cost):
        """Take total cost, fixed cost, material cost and building cost and add them
        to a new row in the cost detail table."""
        row = self._panel_accounting.tableWidget_2.rowCount()
        self._panel_accounting.tableWidget_2.insertRow(row)
        self._panel_accounting.tableWidget.setItem(row, 0, QTableWidgetItem(f'{tot_cost:,.2f}'))
        self._panel_accounting.tableWidget.setItem(row, 1, QTableWidgetItem(f'{fixed_cost:,.2f}'))
        self._panel_accounting.tableWidget.setItem(row, 2, QTableWidgetItem(f'{mat_cost:,.2f}'))
        self._panel_accounting.tableWidget.setItem(row, 3, QTableWidgetItem(f'{build_cost:,.2f}'))
     