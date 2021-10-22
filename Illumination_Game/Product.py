class Product(object):
    """Parent of all products"""

    def __init__(self, name, amount, time, val, price):
        self.product_name = name
        self.product_amount = amount
        self.production_time = time
        self.base_value = val
        self.sales_price = price
        self.production_goal = 0
        self.production_goal_set = False
        self.bill_of_materials = []

    def add_products(self, number):
        self.product_amount += number

    def subtract_products(self, number):
        self.product_amount -= number

    def get_product_amount(self):
        return self.productAmount

    def set_production_goal(self, new_goal):
        self.production_goal = new_goal

class Light_Bulb(Product):
    """class specific for light bulbs, the starter product"""

    def __init__(self):
        super().__init__('Light Bulb', 100, 5/60, 3.8, 4.0) 