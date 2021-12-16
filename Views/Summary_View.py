from sys import breakpointhook
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QMdiArea
from Views import sub_win_summary

class Summary_View(QMdiArea):
    """Class to collect and plot all important data from all models."""

    def __init__(self, cap_model, fac_model, mar_model, prod_model, root_directory) -> None:
        super().__init__()

        self._panel_summary = sub_win_summary.Ui_Summary()
        self._panel_summary.setupUi(self)
        
        self._model_capital = cap_model
        self._model_factory = fac_model
        self._model_market = mar_model
        self._model_product = prod_model
        self.root_directory = root_directory

        self._panel_summary.btn_tab1_update.clicked.connect(self.update_lbl_produced)
        self._panel_summary.btn_tab1_update.clicked.connect(self.update_lbl_sold)
        self._panel_summary.btn_tab1_update.clicked.connect(self.update_lbl_income)
        self._panel_summary.btn_tab1_update.clicked.connect(self.update_lbl_cost)
        self._panel_summary.btn_tab1_update.clicked.connect(self.update_lbl_profit)
        self._panel_summary.btn_tab1_update.clicked.connect(self.update_lbl_marketshare)

    def update_lbl_produced(self, months=12):
        """Update label lbtl_tab1_produced. 
        Takes months as argument, to specify for hor many turns of the production are displayed. Default 12.
        If called by clicked event, the entire archive is shown (mothns=False)."""

        prod = self._model_factory.production_archive
        total_prod = 0
        if not months:
            months = len(prod)
        for i in range(months):
            try:
                total_prod += prod[-i-1]
            except IndexError:
                break
        self._panel_summary.lbl_tab1_produced.setText(f'{total_prod:,}')

    def update_lbl_sold(self, months=12):
        """Update label lbtl_tab1_sold. 
        Takes months as argument, to specify for hor many turns of the sales are displayed. Default 12.
        If called by clicked event, the entire archive is shown (mothns=False)."""
        sales = self._model_market.sales_archive
        total_sales = 0
        if not months:
            months = len(sales)
        for i in range(months):
            try:
                total_sales += sales[-i-1]['units']
            except IndexError:
                break
        self._panel_summary.lbl_tab1_sold.setText(f'{total_sales:,}')

    def update_lbl_income(self, months=12):
        """Update label lbtl_tab1_sold. 
        Takes months as argument, to specify for hor many turns of the sales volumes are displayed. Default 12.
        If called by clicked event, the entire archive is shown (mothns=False)."""
        sales = self._model_market.sales_archive
        total_sales = 0
        if not months:
            months = len(sales)
        for i in range(months):
            try:
                total_sales += sales[-i-1]['volume']
            except IndexError:
                break
        self._panel_summary.lbl_tab1_income.setText(f'{total_sales:,.2f} €')

    def update_lbl_cost(self, months=12):
        """Update label lbtl_tab1_sold. 
        Takes months as argument, to specify for hor many turns of the cost are displayed. Default 12.
        If called by clicked event, the entire archive is shown (mothns=False)."""
        cost = self._model_capital.total_cost_archive
        total_cost = 0
        if not months:
            months = len(cost)
        for i in range(months):
            try:
                total_cost += cost[-i-1]
            except IndexError:
                break
        self._panel_summary.lbl_tab1_cost.setText(f'{total_cost:,.2f} €')

    def update_lbl_profit(self, months=12):
        """Update label lbtl_tab1_sold. 
        Takes months as argument, to specify for hor many turns of the cost are displayed. Default 12.
        If called by clicked event, the entire archive is shown (mothns=False)."""
        cost = self._model_capital.total_cost_archive
        sales = self._model_market.sales_archive
        total_cost = 0
        total_sales = 0
        if not months:
            months = len(cost)
        for i in range(months):
            try:
                total_sales += sales[-i-1]['volume']
                total_cost += cost[-i-1]
            except IndexError:
                break
        profit = total_sales - total_cost
        self._panel_summary.lbl_tab1_profit.setText(f'{profit:,.2f} €')

    def update_lbl_marketshare(self):#share cumulated
        share = self._model_market.sales_archive
        try:
            self._panel_summary.lbl_tab1_marketshare.setText(f"{share[-1]['share cumulated']:.4f} %")
        except IndexError:
            self._panel_summary.lbl_tab1_marketshare.setText(f"0 %")