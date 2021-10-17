class ProductionLayout(object):
    """Parent of all four layout classes."""


    def __init__(self, name, rSpace):
        self.layoutName = name
        self.requiredSpace = rSpace


    def printName(self):
        print(self.layoutName, self.requiredSpace, sep= ' ' )


class FixedPositionLayout(ProductionLayout):
    """description of class"""
    pass
