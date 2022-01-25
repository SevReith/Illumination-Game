from PyQt5.QtCore import QObject, pyqtSignal

class Material(QObject):
    """parten of all materials"""

    stock_changed = pyqtSignal(int)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        self._price = val

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, val):
        self._quality = val

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, val):
        self._amount = val
        self.stock_changed.emit(val)

    @property
    def required_amount(self):
        return self._required_amount

    @required_amount.setter
    def required_amount(self, val):
        self._required_amount = val

    @property
    def seller_name(self):
        return self._seller_name

    @property
    def required_for(self):
        return self._required_for

    def __init__(self, name, price, quality, init_amount = 0, req_amount = 1, req_for = [0], seller_name = 'Ozeania'):
        """Req for indicates the product, that uses a material."""
        super().__init__()
        self._name = name
        self._price = price
        self._quality = quality
        self._amount = init_amount
        self._required_amount = req_amount
        self._seller_name = seller_name
        self._required_for = req_for


class Glass_Bulb(Material):

    def __init__(self, config):
        super().__init__(name = config['name'], price = config['price'], quality = config['quality'], init_amount = 0, req_amount = 0, req_for = config['required_for_prodcut'], seller_name = config['seller_name'])


class Coiled_Filament(Material):

    def __init__(self, config):
        super().__init__(name = config['name'], price = config['price'], quality = config['quality'], init_amount = 0, req_amount = 0, req_for = config['required_for_prodcut'], seller_name = config['seller_name'])

class Lead_In_Wires(Material):

    def __init__(self, config):
        super().__init__(name = config['name'], price = config['price'], quality = config['quality'], init_amount = 0, req_amount = 0, req_for = config['required_for_prodcut'], seller_name = config['seller_name'])


class Socket(Material):

    def __init__(self, config):
        super().__init__(name = config['name'], price = config['price'], quality = config['quality'], init_amount = 0, req_amount = 0, req_for = config['required_for_prodcut'], seller_name = config['seller_name'])


class Protective_Gas(Material):

    def __init__(self, config):
        super().__init__(name = config['name'], price = config['price'], quality = config['quality'], init_amount = 0, req_amount = 0, req_for = config['required_for_prodcut'], seller_name = config['seller_name'])


class Packaging(Material):

    def __init__(self, config):
        super().__init__(name = config['name'], price = config['price'], quality = config['quality'], init_amount = 0, req_amount = 0, req_for = config['required_for_prodcut'], seller_name = config['seller_name'])

class Alu_Glass_Bulbs(Material):

    def __init__(self, config):
        super().__init__(name = config['name'], price = config['price'], quality = config['quality'], init_amount = 0, req_amount = 0, req_for = config['required_for_prodcut'], seller_name = config['seller_name'])
        
class Mount(Material):

    def __init__(self, config):
        super().__init__(name = config['name'], price = config['price'], quality = config['quality'], init_amount = 0, req_amount = 0, req_for = config['required_for_prodcut'], seller_name = config['seller_name'])

class Plastic_Housing(Material):

    def __init__(self, config):
        super().__init__(name = config['name'], price = config['price'], quality = config['quality'], init_amount = 0, req_amount = 0, req_for = config['required_for_prodcut'], seller_name = config['seller_name'])

class LED(Material):
   
    def __init__(self, config):
        super().__init__(name = config['name'], price = config['price'], quality = config['quality'], init_amount = 0, req_amount = 0, req_for = config['required_for_prodcut'], seller_name = config['seller_name'])

class Plastic_Bulb(Material):

    def __init__(self, config):
        super().__init__(name = config['name'], price = config['price'], quality = config['quality'], init_amount = 0, req_amount = 0, req_for = config['required_for_prodcut'], seller_name = config['seller_name'])
        