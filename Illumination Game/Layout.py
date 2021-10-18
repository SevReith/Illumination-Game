WORKING_MONTH = 35 * 4

class ProductionLayout(object):
    """Parent of all four layout classes."""

    def __init__(self, name, space, time_mod):
        self.layout_name = name
        self.required_space = space
        self.production_time_modifier = time_mod


    def calculate_time_unit_capacity(self, prod_time):
        return WORKING_MONTH / (prod_time - (prod_time * self.production_time_modifier))

    def printName(self):
        print(self.layout_name, self.required_space, sep= ' ' )


class FixedPositionLayout(ProductionLayout):
    """description of class"""
    pass
