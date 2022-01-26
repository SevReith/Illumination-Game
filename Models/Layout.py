from PyQt5.QtCore import QObject, pyqtSignal

class Production_Layout(QObject):
    """Parent of all four layout classes."""

    layout_was_activated = pyqtSignal(bool)
    layout_size_changed = pyqtSignal(int)

    @property
    def name(self):
        return self._config['name']

    @name.setter
    def name(self, name):
        self._config['name'] = name

    @property
    def size(self):
        return self._config['size']

    @size.setter
    def size(self, val):
        self._config['size'] = val
        self.layout_size_changed.emit(val)

    @property
    def required_space(self):
        return self._config['size']

    @property
    def production_time_modifier(self):
        return self._config['standard_production_time_modifier']

    @production_time_modifier.setter
    def production_time_modifier(self, val):
        self._config['standard_production_time_modifier'] = val

    @property
    def maintenance_cost_modifier(self):
        return self._config['standard_cost_modifier']

    @maintenance_cost_modifier.setter
    def maintenance_cost_modifier(self, val):
        self._config['standard_cost_modifier'] = val

    @property
    def quality_modfier(self):
        return self._config['standard_quality_modifier']

    @quality_modfier.setter
    def quality_modifier(self, val):
        self._config['standard_quality_modifier'] = val

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, flag):
        self._is_active = flag
        self.layout_was_activated.emit(flag)

    @property
    def building_cost(self):
        return self._config['building_cost']

    @building_cost.setter
    def building_cost(self, val):
        self._config['building_cost'] = val

    @property
    def building_time(self):
        return self._config['building_time']

    @building_time.setter
    def building_time(self, val):
        self._config['building_time'] = val

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
        return self._config['max_number']

    @max_number.setter
    def max_number(self, val):
        self._config['max_number'] = val

    def __init__(self, config):
        super().__init__()
        self._config = config
        self._is_active = False
        self._built_in_turn = 0
        self._activation_turn = 0
        self._worker_list = []
        self._machinery_list = []
        
    def calculate_tuc(self, work_time, prod_time):
        tuc = work_time / (prod_time * (1 + self.production_time_modifier))
        return tuc


class Fixed_Position_Layout(Production_Layout):
    """Fixed Position Layout Subclass."""

    def __init__(self, config):
        super().__init__(config)


class Process_Layout(Production_Layout):
    """standard process or job shop layout"""

    @property
    def departments(self):
        return self._special_characteristics['init_departments']

    @departments.setter
    def departments(self, val):
        self._special_characteristics['init_departments'] = val

    @property
    def department_size(self):
        return self._special_characteristics['dep_size']

    @department_size.setter
    def department_size(self, val):
        self._special_characteristics['dep_size'] = val

    @property
    def department_building_cost(self):
        return self._special_characteristics['dep_build_cost']

    @department_building_cost.setter
    def department_building_cost(self, val):
        self._special_characteristics['dep_build_cost'] = val

    @property
    def department_building_time(self):
        return self._special_characteristics['dep_build_time']

    @property
    def department_production_bonus(self):
        return self._special_characteristics['ep_prod_bonus']

    @department_production_bonus.setter
    def department_production_bonus(self, val):
        self._special_characteristics['ep_prod_bonus'] = val

    @property
    def department_quality_bonus(self):
        return self._special_characteristics['dep_quality_bonus']

    @department_quality_bonus.setter
    def department_quality_bonus(self, val):
        self._special_characteristics['dep_quality_bonus'] = val

    def __init__(self, config):
        super().__init__(config)    
        self._special_characteristics = config['departments']

    def calculate_tuc(self, work_time, prod_time):
        tuc = work_time / (prod_time * (1 + self.production_time_modifier))
        tuc += tuc * (1 + self.department_production_bonus) ** self.departments
        return tuc


class Cellular_Layout(Production_Layout):
    """standard process or job shop layout"""

    @property
    def departments(self):
        return self._special_characteristics['init_departments']

    @departments.setter
    def departments(self, val):
        self._special_characteristics['init_departments'] = val

    @property
    def department_size(self):
        return self._special_characteristics['dep_size']

    @department_size.setter
    def department_size(self, val):
        self._special_characteristics['dep_size'] = val

    @property
    def department_building_cost(self):
        return self._special_characteristics['dep_build_cost']

    @department_building_cost.setter
    def department_building_cost(self, val):
        self._special_characteristics['dep_build_cost'] = val

    @property
    def department_building_time(self):
        return self._special_characteristics['dep_build_time']

    @property
    def department_production_bonus(self):
        return self._special_characteristics['ep_prod_bonus']

    @department_production_bonus.setter
    def department_production_bonus(self, val):
        self._special_characteristics['ep_prod_bonus'] = val

    @property
    def department_quality_bonus(self):
        return self._special_characteristics['dep_quality_bonus']

    @department_quality_bonus.setter
    def department_quality_bonus(self, val):
        self._special_characteristics['dep_quality_bonus'] = val

    def __init__(self, config):
        super().__init__(config)    
        self._special_characteristics = config['departments']

    def calculate_tuc(self, work_time, prod_time):
        tuc = work_time / (prod_time * (1 + self.production_time_modifier))
        tuc += tuc * (1 + self.department_production_bonus) ** self.departments
        return tuc


class Line_Layout(Production_Layout):
    """standard process or job shop layout"""

    def __init__(self, config):
        super().__init__(config)