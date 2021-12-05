from PyQt5.QtCore import QObject, pyqtSignal

class Production_Layout(QObject):
    """Parent of all four layout classes."""

    layout_was_activated = pyqtSignal(bool)
    layout_size_changed = pyqtSignal(int)

    WORKING_MONTH = 35 * 4

    @property
    def layout_name(self):
        return self._layout_name

    @layout_name.setter
    def layout_name(self, name):
        self._layout_name = name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, val):
        self._size = val
        self.layout_size_changed.emit(val)

    @property
    def required_space(self):
        return self._required_space

    @property
    def production_time_modifier(self):
        return self._production_time_modifier

    @production_time_modifier.setter
    def production_time_modifier(self, val):
        self._production_time_modifier = val

    @property
    def maintenance_cost_modifier(self):
        return self._maintenance_cost_modifier

    @maintenance_cost_modifier.setter
    def maintenance_cost_modifier(self, val):
        self._maintenance_cost_modifier = val

    @property
    def quality_modfier(self):
        return self._quality_modifier

    @quality_modfier.setter
    def quality_modifier(self, val):
        self._quality_modifier = val

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, flag):
        self._is_active = flag
        self.layout_was_activated.emit(flag)

    @property
    def building_cost(self):
        return self._building_cost

    @building_cost.setter
    def building_cost(self, val):
        self._building_cost = val

    @property
    def building_time(self):
        return self._building_time

    @building_time.setter
    def building_time(self, val):
        self._building_time = val

    @property
    def built_in_turn(self):
        return self._built_in_turn

    @built_in_turn.setter
    def built_in_turn(self, turn):
        self._built_in_turn = turn

    @property
    def activation_turn(self):
        return self._activation_turn

    @activation_turn.setter
    def activation_turn(self, val):
        self._activation_turn = val

    @property
    def worker_list(self):
        return self._worker_list

    @property
    def machinery_list(self):
        return self._machinery_list

    @property
    def max_number(self):
        return self._max_number

    @max_number.setter
    def max_number(self, val):
        self._max_number = val

    def __init__(self, name, space, time_mod, cost_mod, qual_mod, cost=0, build_time=1, max_number = -1):
        super().__init__()
        self._layout_name = name
        self._required_space = space
        self._size = space
        self._production_time_modifier = time_mod
        self._maintenance_cost_modifier = cost_mod
        self._quality_modifier = qual_mod
        self._is_active = False
        self._building_cost = cost
        self._building_time = build_time
        self._built_in_turn = 0
        self._activation_turn = 0
        self._worker_list = []
        self._machinery_list = []
        self._max_number = max_number

    def calculate_tuc(self, work_time, prod_time):
        tuc = work_time / (prod_time * (1 + self.production_time_modifier))
        return tuc


class Fixed_Position_Layout(Production_Layout):
    """description of class"""
    STANDARD_SIZE = 30
    STANDARD_PROD_TIME_MODIFIER = 1.3
    STANDARD_COST_MODIFIER = 3.5
    STANDARD_QUALITY_MODIFIER = 2
    BUILDING_COST = 10000
    BUILDING_TIME = 2

    def __init__(self, name, space=STANDARD_SIZE, time_mod=STANDARD_PROD_TIME_MODIFIER, cost_mod=STANDARD_COST_MODIFIER, qual_mod = STANDARD_QUALITY_MODIFIER):
        super().__init__(name, space, time_mod, cost_mod, qual_mod, cost = self.BUILDING_COST, build_time = self.BUILDING_TIME)


class Process_Layout(Production_Layout):
    """standard process or job shop layout"""

    STANDARD_SIZE = 60
    STANDARD_PROD_TIME_MODIFIER = 0.15
    STANDARD_COST_MODIFIER = 4.5
    STANDARD_QUALITY_MODIFIER = 1.5
    BUILDING_COST = 30000
    BUILDING_TIME = 4
    INIT_DEPARTMENTS = 3
    DEPARTMENT_SIZE = 20
    DEPARTMENT_BUILDING_COST = 7000
    DEPARTMENT_BUILDING_TIME = 1
    DEPARTMENT_PROD_BONUS = 0.15

    @property
    def departments(self):
        return self._special_characteristics['departments']

    @departments.setter
    def departments(self, val):
        self._special_characteristics['departments'] = val

    @property
    def department_size(self):
        return self._special_characteristics['dep size']

    @department_size.setter
    def department_size(self, val):
        self._special_characteristics['dep size'] = val

    @property
    def department_building_cost(self):
        return self._special_characteristics['dep build cost']

    @department_building_cost.setter
    def department_building_cost(self, val):
        self._special_characteristics['dep build cost'] = val

    @property
    def department_building_time(self):
        return self._special_characteristics['dep build time']

    @property
    def department_production_bonus(self):
        return self._special_characteristics['dep prod bonus']

    @department_production_bonus.setter
    def department_production_bonus(self, val):
        self._special_characteristics['dep prod bonus'] = val

    @property
    def department_quality_bonus(self):
        return self._special_characteristics['dep quality bonus']

    @department_quality_bonus.setter
    def department_quality_bonus(self, val):
        self._special_characteristics['dep quality bonus'] = val

    def __init__(self, name, space=STANDARD_SIZE, time_mod=STANDARD_PROD_TIME_MODIFIER, cost_mod=STANDARD_COST_MODIFIER, qual_mod = STANDARD_QUALITY_MODIFIER):
        super().__init__(name, space, time_mod, cost_mod, qual_mod, cost = self.BUILDING_COST, build_time = self.BUILDING_TIME, max_number = 1)
        self._special_characteristics = {
            'departments': self.INIT_DEPARTMENTS,
            'dep size': self.DEPARTMENT_SIZE,
            'dep build cost': self.DEPARTMENT_BUILDING_COST,
            'dep build time': self.DEPARTMENT_BUILDING_TIME,
            'dep prod bonus': self.DEPARTMENT_PROD_BONUS,
            'dep quality bonus': 0.03
            }

    def calculate_tuc(self, work_time, prod_time):
        tuc = work_time / (prod_time * (1 + self.production_time_modifier))
        tuc += tuc * (1 + self.department_production_bonus) ** self.departments
        return tuc


class Cellular_Layout(Production_Layout):
    """standard process or job shop layout"""

    STANDARD_SIZE = 80
    STANDARD_PROD_TIME_MODIFIER = -0.3
    STANDARD_COST_MODIFIER = 6
    STANDARD_QUALITY_MODIFIER = 1.0
    BUILDING_COST = 100000
    BUILDING_TIME = 7
    INIT_DEPARTMENTS = 3
    DEPARTMENT_SIZE = 25
    DEPARTMENT_BUILDING_COST = 33000
    DEPARTMENT_BUILDING_TIME = 1
    DEPARTMENT_PROD_BONUS = 0.25

    @property
    def departments(self):
        return self._special_characteristics['departments']

    @departments.setter
    def departments(self, val):
        self._special_characteristics['departments'] = val

    @property
    def department_size(self):
        return self._special_characteristics['dep size']

    @department_size.setter
    def department_size(self, val):
        self._special_characteristics['dep size'] = val

    @property
    def department_building_cost(self):
        return self._special_characteristics['dep build cost']

    @department_building_cost.setter
    def department_building_cost(self, val):
        self._special_characteristics['dep build cost'] = val

    @property
    def department_building_time(self):
        return self._special_characteristics['dep build time']

    @property
    def department_production_bonus(self):
        return self._special_characteristics['dep prod bonus']

    @department_production_bonus.setter
    def department_production_bonus(self, val):
        self._special_characteristics['dep prod bonus'] = val

    @property
    def department_quality_bonus(self):
        return self._special_characteristics['dep quality bonus']

    @department_quality_bonus.setter
    def department_quality_bonus(self, val):
        self._special_characteristics['dep quality bonus'] = val
    
    def __init__(self, name, space=STANDARD_SIZE, time_mod=STANDARD_PROD_TIME_MODIFIER, cost_mod=STANDARD_COST_MODIFIER, qual_mod = STANDARD_QUALITY_MODIFIER):
        super().__init__(name, space, time_mod, cost_mod, qual_mod, cost = self.BUILDING_COST, build_time = self.BUILDING_TIME, max_number = 1)
        self._special_characteristics = {
            'departments': self.INIT_DEPARTMENTS,
            'dep size': self.DEPARTMENT_SIZE,
            'dep build cost': self.DEPARTMENT_BUILDING_COST,
            'dep build time': self.DEPARTMENT_BUILDING_TIME,
            'dep prod bonus': self.DEPARTMENT_PROD_BONUS,
            'dep quality bonus': 0.03
            }

    def calculate_tuc(self, work_time, prod_time):
        tuc = work_time / (prod_time * (1 + self.production_time_modifier))
        tuc += tuc * (1 + self.department_production_bonus) ** self.departments
        return tuc


class Line_Layout(Production_Layout):
    """standard process or job shop layout"""

    STANDARD_SIZE = 100
    STANDARD_PROD_TIME_MODIFIER = -0.99
    STANDARD_COST_MODIFIER = 7
    STANDARD_QUALITY_MODIFIER = 0.9
    BUILDING_COST = 1000000
    BUILDING_TIME = 14
    
    def __init__(self, name, space=STANDARD_SIZE, time_mod=STANDARD_PROD_TIME_MODIFIER, cost_mod=STANDARD_COST_MODIFIER, qual_mod = STANDARD_QUALITY_MODIFIER):
        super().__init__(name, space, time_mod, cost_mod, qual_mod, cost = self.BUILDING_COST, build_time = self.BUILDING_TIME)
