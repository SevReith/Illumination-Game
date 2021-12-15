from PyQt5.QtWidgets import QMdiArea, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QDoubleValidator
from Views import sub_win_market

class Market_View(QMdiArea):
    """description of class"""

    def __init__(self, cap_mdl, mar_mdl, pro_mdl, mat_mdl, main_ctrl, pro_ctrl, mat_ctrl):
        super().__init__()
        #load main window
        #self._panel = uic.loadUi('Views\Panel_Test1.ui', self)
        self._panel_market = sub_win_market.Ui_Form()
        self._panel_market.setupUi(self)
        
        self._model_capital = cap_mdl
        self._model_market = mar_mdl
        self._model_product = pro_mdl
        self._model_material = mat_mdl
        self._controller_capital_market = main_ctrl
        self._controller_product = pro_ctrl
        self._controller_material = mat_ctrl
        
        #connect widgets to market model
        self._model_market.marketvolume_changed.connect(self.update_lbl_marketvolume)
        self._model_market.sales_cumulated_changed.connect(self.update_lbl_sales_vol_annually)
        self._model_market.marketshare_cumulated_changed.connect(self.update_lbl_marketshare)
        self._model_market.forecast_generated.connect(self.update_lbl_forecast)
        self._model_market.products_sold.connect(self.update_lbls_sales)
        self._model_market.yearly_summary_flag_changed.connect(self.show_yearly_summary)

        #connect widgets to product model
        #self._model_product[0].sales_price_changed.connect(self.update_lbl_bottom)
        for i in range(3):
            self._model_product[i].sales_price_changed.connect(self.update_lbl_bottom)

        #update and configure panel widgets
        self._panel_market.led_set_price.setValidator(QDoubleValidator(0.00, 99999.99, 2))
        self._panel_market.led_set_price.returnPressed.connect(self.sub_led_price_entered)
        self.update_lbl_marketvolume(self._model_market.marketvolume_annually)
        self.update_lbl_bottom()
        self.update_lbl_forecast()
        self.update_lbls_material_name()
        self.update_lbls_material_price()
        
    @pyqtSlot(int)
    def update_lbl_marketvolume(self, vol):
        """Update label marketvolume."""
        self._panel_market.lbl_marketvolume_number.setText(f'{self._model_market.marketvolume_annually:,.0f}€')
        
    @pyqtSlot(int)
    def update_lbl_sales_vol_annually(self, sales):
        self._panel_market.lbl_sales_volume_amount.setText(f'{sales:,}€')

    @pyqtSlot(float)
    def update_lbl_marketshare(self, share):
        self._panel_market.lbl_marketshare_number.setText(f'{share:.4f}%')

    @pyqtSlot(int)
    def update_lbl_forecast(self):
        """collects forecast numbers of the last 3 months and updates labels with it"""
        #forecast collection
        forecast2 = 0
        forecast1 = 0
        forecast0 = 0
        fc_archive = self._model_market.sales_forecast_archive
        length = len(fc_archive)
        if length >= 3:
            forecast0 = fc_archive[- 1]
            forecast1 = fc_archive[- 2]
            forecast2 = fc_archive[- 3]
        elif length == 2:
            forecast0 = fc_archive[- 1]
            forecast1 = fc_archive[- 2]
        else:
            forecast0 = fc_archive[- 1]
        #label updates
        self._panel_market.lbl_forecast_current.setText(f'{forecast0:,}')
        self._panel_market.lbl_forecast_last_month.setText(f'{forecast1:,}')
        self._panel_market.lbl_forecast_2months.setText(f'{forecast2:,}')

    @pyqtSlot(int)
    def update_lbls_sales(self):
        """collects sales numbers of the last 3 months and updates labels with it"""
        #sales collection
        sales2 = 0
        sales1 = 0
        sales0 = 0
        sa_archive = self._model_market.sales_archive
        length = len(sa_archive)
        if length >= 3:
            sales0 = sa_archive[length - 1]['units']
            sales1 = sa_archive[length - 2]['units']
            sales2 = sa_archive[length - 3]['units']
        elif length == 2:
            sales0 = sa_archive[length - 1]['units']
            sales1 = sa_archive[length - 2]['units']
        elif length == 1:
            sales0 = sa_archive[length - 1]['units']
        else:
            pass
        #label update   
        self._panel_market.lbl_sales_current.setText(f'{sales0:,}')
        self._panel_market.lbl_sales_last_month.setText(f'{sales1:,}')
        self._panel_market.lbl_sales_2months.setText(f'{sales2:,}')

    def update_lbls_material_price(self):
        prod = self._controller_product.get_active_product_index()
        self._panel_market.lbl_mat_price1.setText(f'{self._model_product[prod].bill_of_materials[0].price}{self._model_capital.currency_sign}')
        self._panel_market.lbl_mat_price2.setText(f'{self._model_product[prod].bill_of_materials[1].price}{self._model_capital.currency_sign}')
        self._panel_market.lbl_mat_price3.setText(f'{self._model_product[prod].bill_of_materials[2].price}{self._model_capital.currency_sign}')
        self._panel_market.lbl_mat_price4.setText(f'{self._model_product[prod].bill_of_materials[3].price}{self._model_capital.currency_sign}')
        self._panel_market.lbl_mat_price5.setText(f'{self._model_product[prod].bill_of_materials[4].price}{self._model_capital.currency_sign}')
        self._panel_market.lbl_mat_price6.setText(f'{self._model_product[prod].bill_of_materials[5].price}{self._model_capital.currency_sign}')

    def update_lbls_material_name(self):
        prod = self._controller_product.get_active_product_index()
        self._panel_market.lbl_txt_mat1.setText(f'{self._model_product[prod].bill_of_materials[0].name}:')
        self._panel_market.lbl_txt_mat2.setText(f'{self._model_product[prod].bill_of_materials[1].name}:')
        self._panel_market.lbl_txt_mat3.setText(f'{self._model_product[prod].bill_of_materials[2].name}:')
        self._panel_market.lbl_txt_mat4.setText(f'{self._model_product[prod].bill_of_materials[3].name}:')
        self._panel_market.lbl_txt_mat5.setText(f'{self._model_product[prod].bill_of_materials[4].name}:')
        self._panel_market.lbl_txt_mat6.setText(f'{self._model_product[prod].bill_of_materials[5].name}:')

    @pyqtSlot(float)
    def update_lbl_bottom(self):
        """Update the current sales price label."""
        prod = self._controller_product.get_active_product_index()
        self._panel_market.lbl_bottom.setText(f'Current Price: {self._model_product[prod].sales_price}{self._model_capital.currency_sign}')

    def sub_led_price_entered(self):
        """safes a new sales price entered in the line edit in market after pressing return. only float values are accepted."""
        prod = self._controller_product.get_active_product_index()
        new_price = float(self._panel_market.led_set_price.text())
        self._model_product[prod].sales_price = new_price

    @pyqtSlot(bool)
    def show_yearly_summary(self):
        archive = self._model_market.sales_archive[-1]
        keys = ['year', 'units cumulated', 'volume cumulated', 'share cumulated']
        text = f'In year {archive[keys[0]]} your sold a total of {archive[keys[1]]:,.0f} units!\nThis accounted for a total income of {archive[keys[2]]:,.0f}€ and a market share of {archive[keys[3]]:.4f}%!'
        self.display_notification_message('Yearly Summary', text)
        self._model_market.yearly_summary_flag = False

    def display_notification_message(self, title, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(title)
        msg.setInformativeText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()   
        