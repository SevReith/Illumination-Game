from PyQt5.QtCore import QObject, pyqtSignal
import Models.Layout

class Factory(QObject):
    """It's the factory."""

    # FIXED_COST_PER_M2 = 15
    # STANDARD_SIZE_M2 = 100
    # STANDARD_ADD_COST_M2 = 1000
    # FINAL_TURN = 60
    # WORKING_MONTH = 35 * 4

    cur_turn_changed = pyqtSignal(int)
    final_turn_changed = pyqtSignal(int)
    size_changed = pyqtSignal(int)
    free_space_changed = pyqtSignal(int)
    factory_characteristics_changed = pyqtSignal(int, int, float, float)
    products_manufacured = pyqtSignal(int)
    layout_nb_changed = pyqtSignal(int, int, int, int)
        
    @property
    def current_turn(self):
        return self._current_turn

    @current_turn.setter
    def current_turn(self, value):
        self._current_turn = value
        self.cur_turn_changed.emit(value)

    @property
    def final_turn(self):
        return self._config['final_turn']

    @final_turn.setter
    def final_turn(self, value):
        self._config['final_turn'] = value
        self.final_turn_changed.emit(value)

    @property
    def name(self):
        return self._config['name']

    @property
    def size(self):
        return self._config['size']

    @size.setter
    def size(self, value):
        self._config['size'] = value
        self.size_changed.emit(value)
        self.factory_characteristics_changed.emit(value, self.free_space, self.total_cost, self._config['fixed_cost_per_m2'])

    @property
    def working_month(self):
        return self._config['working_month']

    @working_month.setter
    def working_month(self, val):
        self._config['working_month'] = val

    @property
    def layout_list(self):
        return self._layout_list

    @layout_list.setter
    def layout_list(self, new_list):
        self._layout_list = new_list

    @property
    def free_space(self):
        return self._free_space

    @free_space.setter
    def free_space(self, value):
        self._free_space = value
        self.free_space_changed.emit(value)
        self.factory_characteristics_changed.emit(self.size, value, self.total_cost, self._config['fixed_cost_per_m2'])

    @property
    def fixed_cost_per_m2(self):
        return self._config['fixed_cost_per_m2']

    @fixed_cost_per_m2.setter
    def fixed_cost_per_m2(self, value):
        self._config['fixed_cost_per_m2'] = value
        self.factory_characteristics_changed.emit(self.size, self.free_space, self.total_cost, value)

    @property
    def build_cost_per_m2(self):
        return self._config['standard_build_cost_per_m2']

    @build_cost_per_m2.setter
    def build_cost_per_m2(self, val):
        self._config['standard_build_cost_per_m2'] = val

    @property
    def fixed_cost_archive(self):
        return self._fixed_cost_archive

    @fixed_cost_archive.setter
    def fixed_cost_archive(self, new_list):
        self._fixed_cost_archive = new_list

    @property
    def total_cost(self):
        return self._total_cost

    @total_cost.setter
    def total_cost(self, value):
        self._total_cost = value
        self.factory_characteristics_changed.emit(self.size, self.free_space, value, self._config['fixed_cost_per_m2'])

    @property
    def production_capacity_archive(self):
        return self._production_capacity_archive

    @property
    def current_tuc(self):
        return self._current_tuc

    @current_tuc.setter
    def current_tuc(self, val):
        self._current_tuc = val
        self._production_capacity_archive.append(val)

    @property
    def material_capacity_archive(self):
        return self._material_capacity_archive

    @material_capacity_archive.setter
    def material_capacity_archive(self, new_list):
        self._material_capacity_archive = new_list

    @property
    def production_archive(self):
        return self._production_archive

    @production_archive.setter
    def production_archive(self, new_list):
        self._production_archive = new_list
        self.products_manufacured.emit(new_list[len(new_list) - 1])

    @property
    def staff_list(self):
        return self._staff_list

    @property
    def nb_fixed_position(self):
        return self._layout_numbers['Fixed Position Layout']

    @nb_fixed_position.setter
    def nb_fixed_position(self, val):
        self._layout_numbers['Fixed Position Layout'] = val
        self.layout_nb_changed.emit(val, self._layout_numbers['Process Layout'], self._layout_numbers['Cellular Layout'], self._layout_numbers['Line Layout'])

    @property
    def nb_process(self):
        return self._layout_numbers['Process Layout']

    @nb_process.setter
    def nb_process(self, val):
        self._layout_numbers['Process Layout'] = val
        self.layout_nb_changed.emit(self._layout_numbers['Fixed Position Layout'], val, self._layout_numbers['Cellular Layout'], self._layout_numbers['Line Layout'])

    @property
    def nb_cellular(self):
        return self._layout_numbers['Cellular Layout']

    @nb_cellular.setter
    def nb_cellular(self, val):
        self._layout_numbers['Cellular Layout'] = val
        self.layout_nb_changed.emit(self._layout_numbers['Fixed Position Layout'], self._layout_numbers['Process Layout'], val, self._layout_numbers['Line Layout'])

    @property
    def nb_line(self):
        return self._layout_numbers['Line Layout']

    @nb_line.setter
    def nb_line(self, val):
        self._layout_numbers['Line Layout'] = val
        self.layout_nb_changed.emit(self._layout_numbers['Fixed Position Layout'], self._layout_numbers['Process Layout'], self._layout_numbers['Cellular Layout'], val)

    def __init__(self, config, layout_config, layout):
        super().__init__()
        self._config = config
        self._layout_config = layout_config
        self._layout_list = layout
        self._current_turn = 0
        # calculate space occupied by layouts and counte existing layouts
        occupied_space = 0
        self._layout_numbers = {
            'Fixed Position Layout': 0,
            'Process Layout': 0,
            'Cellular Layout': 0,
            'Line Layout': 0
        }
        count = 0
        for lay in self._layout_list:
            occupied_space += lay.required_space
            if lay.name in self._layout_numbers:
                self._layout_numbers[lay.name] += 1
            # activate all layouts
            self._layout_list[count].is_active = True
            count += 1
        self._free_space = config['size'] - occupied_space

        self._fixed_cost_archive = []
        self._total_cost = config['size'] * config['fixed_cost_per_m2']
        self._current_tuc = 0
        self._production_capacity_archive = []
        self._material_capacity_archive = []
        self._production_archive = []
        self._staff_list = []

    def add_layout_to_list(self, lay: Models.Layout.Production_Layout):
        self._layout_list.append(lay)
