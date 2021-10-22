from Layout import *

class Factory(object):
    """It's the factory."""

    FIXED_COST_PER_M2 = 20
    STANDARD_SIZE_M2 = 100

    def __init__(self, name, layout, cost_per_m = FIXED_COST_PER_M2, size = STANDARD_SIZE_M2):
        self.name = name
        self.size = size
        self.layout_list = [layout]
        self.free_space = size - layout.get_size()
        self.fixed_cost_per_m2 = cost_per_m
        self.fixed_cost_archive = []
        self.production_capacity_archive = []

    def add_layout(self, layout):
        self.layout_list.append(layout)

    def calculate_fixed_cost(self):
        """calculates the fixed cost for the entire factory. The space occupied by production layouts,
        is calculated with the according production time modifiers.
        Returns the total cost."""
        cost = 0
        remaining_size = self.size
        for layout in self.layout_list:
            cost += layout.get_size() * self.fixed_cost_per_m2 * (1 - layout.get_prod_time_modifier())
            remaining_size -= layout.get_size()
        cost += remaining_size * self.fixed_cost_per_m2
        self.fixed_cost_archive.append(cost)
        return cost
        
    def calculate_production(self, prod_time):
        """calculates the effective production from all exisiting layouts for one product. 
        returns the total production capacity."""
        new_products = 0 
        total_time_unit_capacity = 0
        for layout in self.layout_list:
            total_time_unit_capacity += layout.calculate_time_unit_capacity(prod_time)
        self.production_capacity_archive.append(total_time_unit_capacity)
        return total_time_unit_capacity
