from PyQt5.QtCore import QObject, pyqtSignal

class Material(QObject):
    """parten of all materials"""

    stock_changed = pyqtSignal(int)

    @property
    def name(self):
        return self._config['name']

    @name.setter
    def name(self, name):
        self._config['name'] = name

    @property
    def id(self):
        return self._config['id']

    @property
    def price(self):
        return self._config['price']

    @price.setter
    def price(self, val):
        self._config['price'] = val

    @property
    def quality(self):
        return self._config['quality']

    @quality.setter
    def quality(self, val):
        self._config['quality'] = val

    @property
    def amount(self):
        return self._config['init_stock']

    @amount.setter
    def amount(self, val):
        self._config['init_stock'] = val
        self.stock_changed.emit(val)

    @property
    def required_amount(self):
        return self._required_amount

    @required_amount.setter
    def required_amount(self, val):
        self._required_amount = val

    @property
    def seller_name(self):
        return self._config['seller_name']

    @property
    def required_for(self):
        return self._required_for

    @property
    def description(self):
        return self._config['description']

    def __init__(self, config, req_amount = 1, req_for = [0]):
        """Req_for indicates the product, that uses a material."""
        super().__init__()
        self._config = config

        self._required_amount = req_amount        
        self._required_for = req_for # deprecated


class Glass_Bulb(Material):

    def __init__(self, config):
        super().__init__(config)


class Coiled_Filament(Material):

    def __init__(self, config):
        super().__init__(config)

class Lead_In_Wires(Material):

    def __init__(self, config):
        super().__init__(config)


class Socket(Material):

    def __init__(self, config):
        super().__init__(config)


class Protective_Gas(Material):

    def __init__(self, config):
        super().__init__(config)


class Packaging(Material):

    def __init__(self, config):
        super().__init__(config)

class Alu_Glass_Bulbs(Material):

    def __init__(self, config):
        super().__init__(config)
        
class Mount(Material):

    def __init__(self, config):
        super().__init__(config)

class Plastic_Housing(Material):

    def __init__(self, config):
        super().__init__(config)

class LED(Material):
   
    def __init__(self, config):
        super().__init__(config)

class Plastic_Bulb(Material):

    def __init__(self, config):
        super().__init__(config)
        