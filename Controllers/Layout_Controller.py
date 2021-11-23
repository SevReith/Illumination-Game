from PyQt5.QtCore import QObject, pyqtSlot
from Models.Layout import Fixed_Position_Layout, Process_Layout, Cellular_Layout, Line_Layout


class Layout_Controller(QObject):
    """description of class"""
    def __init__(self, lay_model):
        super().__init__()

        self._model_layout = lay_model

    def add_department_process(self):
        """Add a department to the process layout. Calculate and save cost for the next department, 
        increase layout size."""
        i = self.find_process_layout_index()
        if not i == -1:
            self._model_layout[i].departments += 1
            self._model_layout[i].department_building_cost = int(self.calculate_next_dept_cost(self._model_layout[i].department_building_cost))
            self._model_layout[i].size += self._model_layout[i].department_size

    def add_department_celluluar(self):
        """Add a department to the celulluar layout. Calculate and save cost for the next department, 
        increase layout size."""
        i = self.find_cellular_layout_index()
        if not i == -1:
            self._model_layout[i].departments += 1
            self._model_layout[i].department_building_cost = int(self.calculate_next_dept_cost(self._model_layout[i].department_building_cost, factor=1.33))
            self._model_layout[i].size += self._model_layout[i].department_size

    def calculate_next_dept_cost(self, old_cost, factor = 1.2):
        """Return the input cost times factor."""
        return old_cost * factor

    def collect_process_info(self):
        """Return current process layout nb, size, build time and cost"""
        i = self.find_process_layout_index()
        return self._model_layout[i].departments, self._model_layout[i].department_size, self._model_layout[i].department_building_time, self._model_layout[i].department_building_cost, self._model_layout[i].department_production_bonus

    def collect_cellular_info(self):
        """Return current cellular layout nb, size, build time and cost"""
        i = self.find_cellular_layout_index()
        return self._model_layout[i].departments, self._model_layout[i].department_size, self._model_layout[i].department_building_time, self._model_layout[i].department_building_cost, self._model_layout[i].department_production_bonus

    def find_process_layout_index(self):
        """Return the index of the process layout in the layout model.
        -> -1, if no process layout is found"""
        i = 0
        for lay in self._model_layout:            
            if type(lay) is Process_Layout:
                return i
            i += 1
        return -1

    def find_cellular_layout_index(self):
        """Return the index of the cellular layout in the layout model.
        -> -1, if no cellular layout is found"""
        i = 0
        for lay in self._model_layout:
            if type(lay) is Cellular_Layout:
                return i
            i += 1
        return -1
