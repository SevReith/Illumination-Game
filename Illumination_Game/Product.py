class Product(object):
    """Parent of all products"""

    def __init__(self, name, amount, time, val):
        self.productName = name
        self.productAmount = amount
        self.production_time = time
        self.base_value = val

    def addProduct(self, number):
        self.productAmount = self.productAmount + number

    def subtractProduct(self, number):
        self.productAmount = self.productAmount - number

    def getProductAmount(self):
        return self.productAmount