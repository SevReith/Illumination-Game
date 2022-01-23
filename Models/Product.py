from PyQt5.QtCore import QObject, pyqtSignal


class Product(QObject):
    """Parent of all products"""

    sales_price_changed = pyqtSignal(float)
    actual_value_changed = pyqtSignal(float)
    base_value_changed = pyqtSignal(float)
    base_quality_changed = pyqtSignal(float)
    stock_amount_changed = pyqtSignal(int)
    production_goal_changed = pyqtSignal(bool)
    active_product_changed = pyqtSignal(bool)
      
    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, flag: bool):
        self._is_active = flag
        if flag:
            self.active_product_changed.emit(flag)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, val):
        self._amount = val
        self.stock_amount_changed.emit(val)

    @property
    def production_time(self):
        return self._production_time

    @production_time.setter
    def production_time(self, val):
        self._production_time = val

    @property
    def base_value(self):
        return self._base_value

    @base_value.setter
    def base_value(self, val):
        self._base_value = val
        self.base_value_changed.emit(val)

    @property
    def actual_value(self):
        return self._actual_value

    @actual_value.setter
    def actual_value(self, val):
        self._actual_value = val
        self.actual_value_changed.emit(val)

    @property
    def sales_price(self):
        return self._sales_price

    @sales_price.setter
    def sales_price(self, val):
        self._sales_price = val
        self.sales_price_changed.emit(val)

    @property
    def base_quality(self):
        return self._base_quality

    @base_quality.setter
    def base_quality(self, val):
        self._base_quality = val
        self.base_quality_changed.emit(val)

    @property
    def sales_price_influencer(self):
        return self._sales_price_influencer

    @sales_price_influencer.setter
    def sales_price_influencer(self, val):
        self._sales_price_influencer = val

    @property
    def license(self):
        return self._license_cost

    @license.setter
    def license(self, val):
        self._license_cost = val

    @property
    def production_goal(self):
        return self._production_goal

    @production_goal.setter
    def production_goal(self, val):
        self._production_goal = val

    @property
    def production_goal_flag(self):
        return self._production_goal_flag

    @production_goal_flag.setter
    def production_goal_flag(self, flag):
        self._production_goal_flag = flag
        self.production_goal_changed.emit(flag)

    @property
    def bill_of_materials(self):
        return self._bill_of_materials

    @bill_of_materials.setter
    def bill_of_materials(self, new_bom):
        self._bill_of_materials = new_bom

    @property
    def material_cost_archive(self):
        return self._material_cost_archive

    @material_cost_archive.setter
    def material_cost_archive(self, new_list):
        self._material_cost_archive = new_list

    def __init__(self, name, amount, time, val, price, qual, license, bom):
        super().__init__()
        self._is_active = False
        self._name = name
        self._amount = amount
        self._production_time = time
        self._base_value = val
        self._actual_value = val * 1 + qual
        self._sales_price = price
        self._base_quality = qual
        self._sales_price_influencer = 1
        self._license_cost = license
        self._production_goal = 0
        self._production_goal_flag = False
        self._bill_of_materials = bom
        self._material_cost_archive = []


class Light_Bulb(Product):
    """class specific for light bulbs, the starter product"""

    INIT_STOCK = 1000
    REQ_GLASS_BULBS = 1
    REQ_COILED_FILAMENT = 1
    REQ_LEAD_IN_WIRES = 2
    REQ_SOCKET = 1
    REQ_PROTECTIVE_GAS = 1
    REQ_PACKAGING = 1
    PROD_TIME = 3.5/60  #in hour
    BASE_VALUE = 4.3
    INIT_PRIZE = 4.0
    BASE_QUALITY = 0.7
    LICENSE_COST = 0

    def __init__(self, bom):
        """uses the parent constructor and then adds all required materials to the material list"""
        req_list = [self.REQ_GLASS_BULBS, self.REQ_COILED_FILAMENT, self.REQ_LEAD_IN_WIRES, self.REQ_SOCKET, self.REQ_PROTECTIVE_GAS, self.REQ_PACKAGING]
        actual_bom = [mat for mat in bom if 0 in mat.required_for]
        length = len(actual_bom)
        for i in range(length):
            # saves required amount and initial stock to the bom
            if i < length:
                actual_bom[i].required_amount = req_list[i]
                actual_bom[i].amount = req_list[i] * self.INIT_STOCK
            else:
                break
        super().__init__('Light Bulb', self.INIT_STOCK, self.PROD_TIME, self.BASE_VALUE, self.INIT_PRIZE, self.BASE_QUALITY, self.LICENSE_COST, actual_bom) 


class Halogen_Light(Product):
    """class specific for halogen lights, the second product"""

    INIT_STOCK = 0
    REQ_ALU_GLASS_BULBS = 1
    REQ_COILED_FILAMENT = 2
    REQ_MOUNT = 1
    REQ_SOCKET = 1
    REQ_PROTECTIVE_GAS = 1
    REQ_PACKAGING = 1
    PROD_TIME = 5.1/60  #in hour
    BASE_VALUE = 7.1
    INIT_PRIZE = 7.8
    BASE_QUALITY = 0.7
    LICENSE_COST = 250000

    #1 x Aluminosilicate Glass Bulb
    #1 x Coiled Filament
    #1 x Mount
    #1 x Socket
    #1 x Protective Gas
    #1 x Packaging

    def __init__(self, bom):
        """uses the parent constructor and then adds all required materials to the material list"""
        req_list = [self.REQ_ALU_GLASS_BULBS, self.REQ_COILED_FILAMENT, self.REQ_MOUNT, self.REQ_SOCKET, self.REQ_PROTECTIVE_GAS, self.REQ_PACKAGING]
        actual_bom = [mat for mat in bom if 1 in mat.required_for]
        length = len(actual_bom)
        for i in range(length):
            # saves required amount and initial stock to the bom
            if i < length:
                actual_bom[i].required_amount = req_list[i]
                actual_bom[i].amount = req_list[i] * self.INIT_STOCK
            else:
                break
        super().__init__('Halogen Light', self.INIT_STOCK, self.PROD_TIME, self.BASE_VALUE, self.INIT_PRIZE, self.BASE_QUALITY, self.LICENSE_COST, actual_bom) 


class LED_Light(Product):
    """class specific for halogen lights, the second product"""

    INIT_STOCK = 0
    REQ_PLASTIC_BULBS = 1
    REQ_LED = 2
    REQ_PLASTIC_HOUSING = 1
    REQ_SOCKET = 1
    REQ_PACKAGING = 1
    PROD_TIME = 8/60  #in hour
    BASE_VALUE = 13.7
    INIT_PRIZE = 12.7
    BASE_QUALITY = 0.7
    LICENSE_COST = 1000000

    #1 x Transparent Plastic Bulb
    #1 x LED
    #1 x Plastic Housing
    #1 x Socket
    #1 x Packaging

    def __init__(self, bom):
        """uses the parent constructor and then adds all required materials to the material list"""
        req_list = [self.REQ_PLASTIC_BULBS, self.REQ_LED, self.REQ_PLASTIC_HOUSING, self.REQ_SOCKET, self.REQ_PACKAGING]
        actual_bom = [mat for mat in bom if 2 in mat.required_for]
        length = len(actual_bom)
        for i in range(length):
            # saves required amount and initial stock to the bom
            if i < length:
                actual_bom[i].required_amount = req_list[i]
                actual_bom[i].amount = req_list[i] * self.INIT_STOCK
            else:
                break
        super().__init__('LED Light', self.INIT_STOCK, self.PROD_TIME, self.BASE_VALUE, self.INIT_PRIZE, self.BASE_QUALITY, self.LICENSE_COST, actual_bom) 
        