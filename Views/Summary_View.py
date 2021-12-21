
from PyQt5.QtCore import pyqtSlot
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

        self._panel_summary.btn_tab1_update.clicked.connect(self.create_yearly_summary)
        self._model_market.yearly_summary_flag_changed.connect(self.create_yearly_summary)
 
    @pyqtSlot(bool)
    def create_yearly_summary(self):
        """Calculate all required numbers and update labely and plots for the past 12 turns."""
        produced, prod_archive = self.calculate_units_produced()
        self.update_lbl_produced(produced)
        lbl_text = self.calculate_units_sold()
        self.update_lbl_sold(lbl_text[0])
        lbl_text = self.calculate_income()
        self.update_lbl_income(lbl_text[0])
        lbl_text = self.calculate_cost()
        self.update_lbl_cost(lbl_text[0])
        lbl_text = self.calculate_profit()
        self.update_lbl_profit(lbl_text[0])
        self.update_lbl_marketshare()
        x_axis = self.calculate_xaxis_with_turns()
        self._panel_summary.mpl_tab1_canvas.plot_simple_graph(x_axis, prod_archive, title=f'Production of the past 12 turns', 
            x_title='Turns', y_title='Units produced')
        self.show()

    def update_lbl_produced(self, total_prod:int):
        """Update label lbtl_tab1_produced."""
        self._panel_summary.lbl_tab1_produced.setText(f'{total_prod:,}')

    def update_lbl_sold(self, total_sales:int):
        """Update label lbtl_tab1_sold."""
        self._panel_summary.lbl_tab1_sold.setText(f'{total_sales:,}')

    def update_lbl_income(self, total_sales:float):
        """Update label lbtl_tab1_sold.""" 
        self._panel_summary.lbl_tab1_income.setText(f'{total_sales:,.2f} €')

    def update_lbl_cost(self, total_cost:float):
        """Update label lbtl_tab1_sold."""
        self._panel_summary.lbl_tab1_cost.setText(f'{total_cost:,.2f} €')

    def update_lbl_profit(self, profit:int):
        """Update label lbtl_tab1_sold."""
        self._panel_summary.lbl_tab1_profit.setText(f'{profit:,.2f} €')

    def update_lbl_marketshare(self):
        share = self._model_market.sales_archive
        try:
            self._panel_summary.lbl_tab1_marketshare.setText(f"{share[-1]['share cumulated']:.4f} %")
        except IndexError:
            self._panel_summary.lbl_tab1_marketshare.setText(f"0 %")

    def calculate_profit(self, months:int = 12):
        """Calculate the profits of the period specified in months.
        Returns cumulated profit and profit array -> float, float[]"""
        cost = self._model_capital.total_cost_archive
        sales = self._model_market.sales_archive
        total_cost = 0
        total_sales = 0
        profit_archive = []
        if not months:
            months = len(cost)
        for i in range(months):
            try:
                total_sales += sales[-i-1]['volume']
                total_cost += cost[-i-1]
                profit_archive.append(sales[-i-1]['volume'] - cost[-i-1])
            except IndexError:
                break
        return (total_sales - total_cost), profit_archive

    def calculate_cost(self, months:int = 12):
        """Calculate cumulated cost for the period specified by months.
        Return totals cost and cost archive: -> float, float[]"""
        cost = self._model_capital.total_cost_archive
        total_cost = 0
        cost_archive = []
        for i in range(months):
            try:
                total_cost += cost[-i-1]
                cost_archive.append(cost[-i-1])
            except IndexError:
                break
        return total_cost, cost_archive

    def calculate_income(self, months:int = 12):
        """Calculate cumulated income for the period specified by months.
        Return totals income and income archive: -> float, float[]"""
        sales = self._model_market.sales_archive
        total_sales = 0
        sales_archive = []
        for i in range(months):
            try:
                total_sales += sales[-i-1]['volume']
                sales_archive.append(sales[-i-1]['volume'])
            except IndexError:
                break
        return total_sales, sales_archive

    def calculate_units_sold(self, months:int = 12):
        """Calculate cumulated units sold for the period specified by months.
        Return totals units sold and units sold archive: -> float, float[]"""
        sales = self._model_market.sales_archive
        total_sales = 0
        sales_archive = []
        for i in range(months):
            try:
                total_sales += sales[-i-1]['units']
                sales_archive.append(sales[-i-1]['units'])
            except IndexError:
                break
        return total_sales, sales_archive

    def calculate_units_produced(self, months:int = 12):
        """Calculate cumulated units produced for the period specified by months.
        Return totals units produced and units produced archive: -> float, float[]"""
        prod = self._model_factory.production_archive
        total_prod = 0
        production_archive = []
        for i in range(months):
            try:
                total_prod += prod[-1 -i]
                production_archive.append(prod[-1 -i])
            except IndexError:
                production_archive.append(0)
        return total_prod, production_archive

    def calculate_xaxis_with_turns(self, months:int = 12):
        """Create an array giving the last turns from current turn - months.
        Reurns that array. -> int[]"""
        cur_turn = self._model_factory.current_turn - 1 
        x_axis = [(cur_turn- i) for i in range(months)]
        return x_axis
        