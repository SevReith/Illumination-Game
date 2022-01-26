from random import Random
from PyQt5.QtCore import QObject, pyqtSignal

class Market(QObject):
    """description of class"""

    forecast_generated = pyqtSignal(int)
    sales_modifier_generated = pyqtSignal(float)
    products_sold = pyqtSignal(int)
    marketvolume_changed = pyqtSignal(int)
    marketshare_cumulated_changed = pyqtSignal(float)
    sales_cumulated_changed = pyqtSignal(int)
    yearly_summary_flag_changed = pyqtSignal(bool)

    @property
    def marketvolume_annually(self):
        return self._config['marketvolume_annually']

    @marketvolume_annually.setter
    def marketvolume_annually(self, val):
        self._config['marketvolume_annually'] = val
        self.marketvolume_changed.emit(val)

    @property
    def total_marketvolume_p_month(self):
        return self._total_marketvolume_p_month

    @total_marketvolume_p_month.setter
    def total_marketvolume_p_month(self, val):
        self._total_marketvolume_p_month = val

    @property
    def marketshare_month(self):
        return self._marketshare_month

    @marketshare_month.setter
    def marketshare_month(self, val):
        self._marketshare_month = val

    @property
    def forecasted_sales(self):
        return self._config['init_forecast']

    @forecasted_sales.setter
    def forecasted_sales(self, val):
        self._config['init_forecast'] = val
        self.forecast_generated.emit(val)

    @property
    def average_monthly_sales_growth_rate(self):
        return self._config['average_monthly_sales_growth_rate']

    @average_monthly_sales_growth_rate.setter
    def average_monthly_sales_growth_rate(self, val):
        self._config['average_monthly_sales_growth_rate'] = val

    @property
    def sales_modifier(self):
        return self._config['sales_modifier']

    @sales_modifier.setter
    def sales_modifier(self, val):
        self._config['sales_modifier'] = val
        self.sales_modifier_generated.emit(val)

    @property
    def sales_archive(self):
        return self._sales_archive

    @sales_archive.setter
    def sales_archive(self, new_list):
        self._sales_archive = new_list
        length = len(new_list)
        self.products_sold.emit(new_list[length - 1]['units'])
        self.sales_cumulated_changed.emit(new_list[length - 1]['volume cumulated'])
        self.marketshare_cumulated_changed.emit(new_list[length - 1]['share cumulated'])

    @property
    def marketshare_yearly(self):
        ms_annually = [share['share cumulated'] for share in self._sales_archive]
        return ms_annually

    @property
    def sales_forecast_archive(self):
        return self._sales_forecast_archive

    @sales_forecast_archive.setter
    def sales_forecast_archive(self, new_list):
        self._sales_forecast_archive = new_list

    @property
    def competitor_list(self):
        return self._competitor_list

    @property
    def winning_marketshare(self):
        return self._config['winning_marketshare']

    @winning_marketshare.setter
    def winning_marketshare(self, val):
        self._config['winning_marketshare'] = val

    @property
    def yearly_summary_flag(self):
        return self._yearly_summary_flag

    @yearly_summary_flag.setter
    def yearly_summary_flag(self, flag: bool):
        self._yearly_summary_flag = flag
        if flag:
            self.yearly_summary_flag_changed.emit(flag)

    def __init__(self, config):
        super().__init__()
        self._config = config
        self._total_marketvolume_p_month = config['marketvolume_annually']/12 # volume per month or turn respectively        
        self._marketshare_month = 0
        self._sales_forecast_archive = [0]
        self._sales_archive = [] # {'turn': 0, 'year': 0, 'units': 0, 'volume': 0, 'units cumulated': 0, 'volume cumulated': 0, 'share cumulated': 0}
        self._competitor_list = []        
        self.random_number_generater = Random()
        self._yearly_summary_flag = False

    def add_item_to_sales_archive(self, sales):
        self._sales_archive.append(sales)

    def add_item_to_forecasted_archive(self, forecast):
        self._sales_forecast_archive.append(forecast)

    def get_last_month_sales_units(self):
        return   self._sales_archive[len(self._sales_archive) - 1]['units']

    def get_last_forecast(self):
        return self._sales_forecast_archive[-1]
