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

    PRIZE = 0.2
    QUALITY = 0.7
    NAME = 'Glass Bulb'

    def __init__(self, req_amount = 1, init_amount = 0, name = NAME, prize = PRIZE, qual = QUALITY, req_for = [0]):
        super().__init__(name, prize, qual, init_amount, req_amount, req_for)


class Coiled_Filament(Material):

    PRIZE = 0.3
    QUALITY = 0.7
    NAME = 'Coiled Filament'

    def __init__(self, req_amount = 1, init_amount = 0, name = NAME, prize = PRIZE, qual = QUALITY, req_for = [0, 1]):
        super().__init__(name, prize, qual, init_amount, req_amount, req_for)

class Lead_In_Wires(Material):

    PRIZE = 0.1
    QUALITY = 0.7
    NAME = 'Lead In Wires'

    def __init__(self, req_amount = 2, init_amount = 0, name = NAME, prize = PRIZE, qual = QUALITY, req_for = [0]):
        super().__init__(name, prize, qual, init_amount, req_amount)


class Socket(Material):

    PRIZE = 0.2
    QUALITY = 0.7
    NAME = 'Socket'

    def __init__(self, req_amount = 1, init_amount = 0, name = NAME, prize = PRIZE, qual = QUALITY, req_for = [0, 1, 2]):
        super().__init__(name, prize, qual, init_amount, req_amount, req_for)


class Protective_Gas(Material):

    PRIZE = 0.3
    QUALITY = 0.7
    NAME = 'Protective Gas'

    def __init__(self, req_amount = 1, init_amount = 0, name = NAME, prize = PRIZE, qual = QUALITY, req_for = [0, 1]):
        super().__init__(name, prize, qual, init_amount, req_amount, req_for)


class Packaging(Material):

    PRIZE = 0.15
    QUALITY = 0.7
    NAME = 'Packaging'

    def __init__(self, req_amount = 1, init_amount = 0, name = NAME, prize = PRIZE, qual = QUALITY, req_for = [0, 1, 2]):
        super().__init__(name, prize, qual, init_amount, req_amount, req_for)