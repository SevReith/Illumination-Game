class Capital(object):
    """description of class"""

    START_CAPITAL = 10000

    def __init__(self, init_amount = START_CAPITAL):
        self.currency_name = "Euro"
        self.currency_sign = "€"
        self.amount = init_amount
        self.total_income_archive = []
        self.total_cost_archive = []

    def subtract(self, number):
        self.amount -= number
        self.total_cost_archive.append(number)

    def add(self, number):
        self.amount += number
        self.total_income_archive.append(number)