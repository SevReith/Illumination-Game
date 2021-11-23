from PyQt5.QtCore import QObject, pyqtSignal
import Models.Layout

class Factory(QObject):
    """It's the factory."""

    FIXED_COST_PER_M2 = 15
    STANDARD_SIZE_M2 = 100
    STANDARD_ADD_COST_M2 = 1000
    FINAL_TURN = 120
    WORKING_MONTH = 35 * 4

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
        return self._final_turn

    @final_turn.setter
    def final_turn(self, value):
        self._final_turn = value
        self.final_turn_changed.emit(value)

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        self.size_changed.emit(value)
        self.factory_characteristics_changed.emit(value, self.free_space, self.total_cost, self.fixed_cost_per_m2)

    @property
    def working_month(self):
        return self._working_month

    @working_month.setter
    def working_month(self, val):
        self._working_month = val

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
        self.factory_characteristics_changed.emit(self.size, value, self.total_cost, self.fixed_cost_per_m2)

    @property
    def fixed_cost_per_m2(self):
        return self._fixed_cost_per_m2

    @fixed_cost_per_m2.setter
    def fixed_cost_per_m2(self, value):
        self._fixed_cost_per_m2 = value
        self.factory_characteristics_changed.emit(self.size, self.free_space, self.total_cost, value)

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
        self.factory_characteristics_changed.emit(self.size, self.free_space, value, self.fixed_cost_per_m2)

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
        return self._layout_numbers['Fixed Position']

    @nb_fixed_position.setter
    def nb_fixed_position(self, val):
        self._layout_numbers['Fixed Position'] = val
        self.layout_nb_changed.emit(val, self._layout_numbers['Process'], self._layout_numbers['Cellular'], self._layout_numbers['Line'])

    @property
    def nb_process(self):
        return self._layout_numbers['Process']

    @nb_process.setter
    def nb_process(self, val):
        self._layout_numbers['Process'] = val
        self.layout_nb_changed.emit(self._layout_numbers['Fixed Position'], val, self._layout_numbers['Cellular'], self._layout_numbers['Line'])

    @property
    def nb_cellular(self):
        return self._layout_numbers['Cellular']

    @nb_cellular.setter
    def nb_cellular(self, val):
        self._layout_numbers['Cellular'] = val
        self.layout_nb_changed.emit(self._layout_numbers['Fixed Position'], self._layout_numbers['Process'], val, self._layout_numbers['Line'])

    @property
    def nb_line(self):
        return self._layout_numbers['Line']

    @nb_line.setter
    def nb_line(self, val):
        self._layout_numbers['Line'] = val
        self.layout_nb_changed.emit(self._layout_numbers['Fixed Position'], self._layout_numbers['Process'], self._layout_numbers['Cellular'], val)

    def __init__(self, name, layout, cost_per_m=FIXED_COST_PER_M2, size=STANDARD_SIZE_M2, final_turn=FINAL_TURN, wk_month=WORKING_MONTH):
        super().__init__()
        self._current_turn = 0
        self._final_turn = final_turn
        self._name = name
        self._size = size
        self._working_month = wk_month
        self._layout_list = layout
        self._free_space = size - self._layout_list[0].required_space * len(layout)
        self._fixed_cost_per_m2 = cost_per_m
        self._fixed_cost_archive = []
        self._total_cost = size * cost_per_m
        self._current_tuc = 0
        self._production_capacity_archive = []
        self._material_capacity_archive = []
        self._production_archive = []
        self._staff_list = []
        self._layout_numbers = {
            'Fixed Position': 2,
            'Process': 0,
            'Cellular': 0,
            'Line': 0
        }

        #activate first layout
        self._layout_list[0].is_active = True
        self._layout_list[1].is_active = True

    def add_layout_to_list(self, lay: Models.Layout.Production_Layout):
        self._layout_list.append(lay)

    def update_layout_numbers(self):
        pass
