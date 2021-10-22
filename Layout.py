WORKING_MONTH = 35 * 4

class Production_Layout(object):
    """Parent of all four layout classes."""

    def __init__(self, name, space, time_mod):
        self.layout_name = name
        self.required_space = space
        self.production_time_modifier = time_mod
        self.maintenance_cost_modifier = 1.0
        self.is_active = True
        self.machinery_list = []

    def calculate_time_unit_capacity(self, prod_time):
        return WORKING_MONTH / (prod_time - (prod_time * self.production_time_modifier))

    def destroy(self):
        self.is_active = False

    def get_name(self):
        return self.layout_name

    def get_size(self):
        return self.required_space

    def get_prod_time_modifier(self):
        return self.production_time_modifier


class Fixed_Position_Layout(Production_Layout):
    """description of class"""
    STANDARD_SIZE = 30
    STANDARD_PROD_TIME_MODIFIER = 0.2
    
    def __init__(self, name, space = STANDARD_SIZE, time_mod = STANDARD_PROD_TIME_MODIFIER):
        super().__init__(name, space, time_mod)