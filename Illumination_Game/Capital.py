START_CAPITAL = 10000

class Capital(object):
    """description of class"""

    def __init__(self, init_amount = START_CAPITAL):
        self.currency_name = "Euro"
        self.currency_sign = "€"
        self.amount = init_amount

    def subtract(self, number):
        self.amount = self.amount - number

    def add(self, number):
        self.amount = self.amount + number
