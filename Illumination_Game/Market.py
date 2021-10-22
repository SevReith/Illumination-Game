from random import Random

class Market(object):
    """description of class"""

    def __init__(self, init_forecast = 0):
        self.forecasted_sales = init_forecast
        self.sales_forecast_archive = []
        self.sales_modifer = 1
        self.random_number_generater = Random()

    def generate_sales_forecast(self, prod_id, min=1000, max=100000, step=100):
        """prod_id can take values from 0-2. 0: light bulbs; 1: halogen lamp; 2: led light"""
        self.forecasted_sales = self.random_number_generater.randrange(min, max, step)
        self.sales_forecast_archive.append(self.forecasted_sales)
        return self.forecasted_sales

    def generate_sales_modifier(self, min=50, max=150, step=1):
        self.sales_modifer = self.random_number_generater.randrange(min, max, step) / 100
        return self.sales_modifer

    def get_current_forecast(self):
        return self.forecasted_sales