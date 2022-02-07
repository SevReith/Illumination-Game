from PyQt5.QtWidgets import QMdiArea, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
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
        self._model_capital.credit_limit_changed.connect(self.update_lbl_credit_limit)

        #update label
        self.update_lbl_credit_limit(self._model_capital.credit_limit)

    def update_plot_profit(self, x_axis, y_axis):
        """Update the mpl_tab1_canvas plot with profit."""
        try:
            self._panel_accounting.mpl_tab1_canvas.plot_simple_graph(x_axis, y_axis, title='Profit', x_title='Turns', y_title='Profit in €')
        except ValueError:
            print(f'A ValueError occured in Capital_View: {ValueError.__name__}')

    @pyqtSlot(float)
    def update_lbl_credit_limit(self, credit: float) -> None:
        self._panel_accounting.lbl_credit.setText(f'{credit:,.2f}€')

    @pyqtSlot(float)
    def update_lbl_cost(self, cost: float):
        self._panel_accounting.lbl_cost_number.setText(f'{cost:,.2f}€')

    @pyqtSlot(float)
    def update_lbl_income(self, income: float):
        self._panel_accounting.lbl_income_number.setText(f'{income:,.2f}€')

    @pyqtSlot(float, float)
    def update_lbl_profit(self, cost: float, income: float):
        profit = round(income - cost, 2)
        self._panel_accounting.lbl_profit_number.setText(f'{profit:,.2f}€')
        row = self._panel_accounting.tableWidget.rowCount()
        self._panel_accounting.tableWidget.insertRow(row)
        self._panel_accounting.tableWidget.setItem(row, 0, QTableWidgetItem(f'{cost:,.2f}'))
        self._panel_accounting.tableWidget.setItem(row, 1, QTableWidgetItem(f'{income:,.2f}'))
        self._panel_accounting.tableWidget.setItem(row, 2, QTableWidgetItem(f'{profit:,.2f}'))

    @pyqtSlot(float, float, float, float)
    def update_table_cost_detail(self, tot_cost: float, fixed_cost: float, mat_cost: float, build_cost: float):
        """Take total cost, fixed cost, material cost and building cost and add them
        to a new row in the cost detail table."""
        row = self._panel_accounting.tableWidget_2.rowCount()
        self._panel_accounting.tableWidget_2.insertRow(row)
        self._panel_accounting.tableWidget_2.setItem(row, 0, QTableWidgetItem(f'{tot_cost:,.2f}'))
        self._panel_accounting.tableWidget_2.setItem(row, 1, QTableWidgetItem(f'{fixed_cost:,.2f}'))
        self._panel_accounting.tableWidget_2.setItem(row, 2, QTableWidgetItem(f'{mat_cost:,.2f}'))
        self._panel_accounting.tableWidget_2.setItem(row, 3, QTableWidgetItem(f'{build_cost:,.2f}'))
     