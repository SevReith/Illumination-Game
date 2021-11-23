from PyQt5.QtCore import QObject, pyqtSignal

class Capital(QObject):
    """manages capital"""

    START_CAPITAL = 10000

    capital_changed = pyqtSignal(int)
    latest_cost_changed = pyqtSignal(float)
    latest_income_changed = pyqtSignal(float)
    latest_profit_changed = pyqtSignal(float, float)

    @property
    def amount(self):
            return self._amount

    @amount.setter
    def amount(self, val):
            self._amount = val
            self.capital_changed.emit(val)

    @property
    def currency_name(self):
            return self._currency_name

    @property
    def currency_sign(self):
            return self._currency_sign

    @property
    def total_cost_archive(self):
            return self._total_cost_archive

    @total_cost_archive.setter
    def total_cost_archive(self, new_list):
            self._total_cost_archive = new_list
            self.latest_cost_changed.emit(new_list[len(new_list) - 1])
            self.latest_profit_changed.emit(new_list[len(new_list) - 1], self._total_income_archive[len(self._total_income_archive) -1])

    @property
    def total_income_archive(self):
            return self._total_income_archive

    @total_income_archive.setter
    def total_income_archive(self, new_list):
            self._total_income_archive = new_list
            self.latest_income_changed.emit(new_list[len(new_list) - 1])

    def __init__(self, cap = START_CAPITAL):
        super().__init__()

        self._amount = cap
        self._currency_name = "Euro"
        self._currency_sign = "€"
        self._total_income_archive = []
        self._total_cost_archive = []
