class Product(object):
    """Parent of all products"""

    def __init__(self, name, amount):
        self.productName = name
        self.productAmount = amount

    def addProduct(self, number):
        self.productAmount = self.productAmount + number

    def subtractProduct(self, number):
        self.productAmount = self.productAmount - number

    def getProductAmount(self):
        return self.productAmount