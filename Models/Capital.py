from PyQt5.QtCore import QObject, pyqtSignal

class Capital(QObject):
    """Capital model."""

    capital_changed = pyqtSignal(int)
    latest_cost_changed = pyqtSignal(float)
    latest_income_changed = pyqtSignal(float)
    latest_profit_changed = pyqtSignal(float, float)
    cost_detail_changed = pyqtSignal(float, float, float, float)
    credit_limit_changed = pyqtSignal(float)

    @property
    def amount(self):
        return self._config['capital']

    @amount.setter
    def amount(self, val: float):
        self._config['capital'] = val
        self.capital_changed.emit(val)

    @property
    def currency_name(self):
        return self._config['currency_name']

    @property
    def currency_sign(self):
        return self._config['currency_sign']

    @property
    def credit_limit(self):
        return self._config['credit_limit']

    @credit_limit.setter
    def credit_limit(self, val: float):
        self._config['credit_limit'] = val
        self.credit_limit_changed.emit(val)

    @property
    def total_cost_archive(self):
        return self._total_cost_archive

    @total_cost_archive.setter
    def total_cost_archive(self, new_list):
        self._total_cost_archive = new_list
        self.latest_cost_changed.emit(new_list[-1])
        self.latest_profit_changed.emit(new_list[-1], self._total_income_archive[-1])

    @property
    def total_income_archive(self):
        return self._total_income_archive

    @total_income_archive.setter
    def total_income_archive(self, new_list):
        self._total_income_archive = new_list
        self.latest_income_changed.emit(new_list[-1])

    @property
    def cost_detail_archive(self):
        return self._cost_detail_archive

    @property
    def fixed_cost(self):
        return self._cost_detail_archive['fixed']

    @fixed_cost.setter
    def fixed_cost(self, new_list):
        self._cost_detail_archive['fixed'] = new_list

    @property
    def material_cost(self):
        return self._cost_detail_archive['material']
    
    @material_cost.setter
    def material_cost(self, new_list):
        self._cost_detail_archive['material'] = new_list

    @property
    def building_cost(self):
        return self._cost_detail_archive['building']

    @building_cost.setter
    def building_cost(self, new_list):
        self._cost_detail_archive['building'] = new_list

    @property
    def current_building_cost(self):
        return self._cost_detail_archive['cur building']

    @current_building_cost.setter
    def current_building_cost(self, val):
        self._cost_detail_archive['cur building'] = val

    def __init__(self, config):
        super().__init__()
        self._config = config
        self._total_income_archive = []
        self._total_cost_archive = []
        self._cost_detail_archive = {
                'fixed': [],
                'material': [],
                'building': [],
                'cur building': 0
        }

    def add_latest_cost_detail_to_archive(self, fixed_cost: float, mat_cost: float, build_cost: float) -> None :
        """Append the latest detailed cost to the archive.
        Emit latest total and detailed cost with cost_detail_changed signal."""
        self._cost_detail_archive['fixed'].append(fixed_cost)
        self._cost_detail_archive['material'].append(mat_cost)
        self._cost_detail_archive['building'].append(build_cost)
        self.cost_detail_changed.emit(self._total_cost_archive[-1], self._cost_detail_archive['fixed'][-1],
            self._cost_detail_archive['material'][-1], self._cost_detail_archive['building'][-1])
