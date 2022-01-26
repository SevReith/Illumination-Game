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
        return self._config['name']

    @name.setter
    def name(self, name):
        self._config['name'] = name

    @property
    def id(self):
        return self._config['id']

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, val):
        self._amount = val
        self.stock_amount_changed.emit(val)

    @property
    def production_time(self):
        return self._config['production_time']

    @production_time.setter
    def production_time(self, val):
        self._config['production_time'] = val

    @property
    def base_value(self):
        return self._config['base_value']

    @base_value.setter
    def base_value(self, val):
        self._config['base_value'] = val
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
        return self._config['base_quality']

    @base_quality.setter
    def base_quality(self, val):
        self._config['base_quality'] = val
        self.base_quality_changed.emit(val)

    @property
    def sales_price_influencer(self):
        return self._sales_price_influencer

    @sales_price_influencer.setter
    def sales_price_influencer(self, val):
        self._sales_price_influencer = val

    @property
    def license(self):
        return self._config['licence_cost']

    @license.setter
    def license(self, val):
        self._config['licence_cost'] = val

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

    def __init__(self, config, bom):
        super().__init__()        
        self._config = config        
        self._amount = config['init_stock']
        self._actual_value = config['base_value'] * (1 + config['base_quality'])
        self._sales_price = config['init_prize']
        self._sales_price_influencer = 1
        self._production_goal = 0
        self._is_active = False
        self._production_goal_flag = False
        self._bill_of_materials = bom
        self._material_cost_archive = []


class Light_Bulb(Product):
    """class specific for light bulbs, the starter product"""

    def __init__(self, config, material_list):
        """uses the parent constructor and then adds all required materials to the material list"""
        req_mat_list = config['bom']
        actual_bom = [mat for mat in material_list if (str(mat.id) in req_mat_list)]
        for i in range(len(actual_bom)):
            # saves required amount and initial stock to the bom
            actual_bom[i].required_amount = req_mat_list[f'{actual_bom[i].id}']
            actual_bom[i].amount = req_mat_list[f'{actual_bom[i].id}'] * config['init_stock']
        super().__init__(config, actual_bom)
        

class Halogen_Light(Product):
    """class specific for halogen lights, the second product"""

    def __init__(self, config, material_list):
        """uses the parent constructor and then adds all required materials to the material list"""
        req_mat_list = config['bom']
        actual_bom = [mat for mat in material_list if (str(mat.id) in req_mat_list)]
        for i in range(len(actual_bom)):
            # saves required amount and initial stock to the bom
            actual_bom[i].required_amount = req_mat_list[f'{actual_bom[i].id}']
            actual_bom[i].amount = req_mat_list[f'{actual_bom[i].id}'] * config['init_stock']
        super().__init__(config, actual_bom)


class LED_Light(Product):
    """class specific for halogen lights, the second product"""

    def __init__(self, config, material_list):
        """uses the parent constructor and then adds all required materials to the material list"""
        req_mat_list = config['bom']
        actual_bom = [mat for mat in material_list if (str(mat.id) in req_mat_list)]
        for i in range(len(actual_bom)):
            # saves required amount and initial stock to the bom
            actual_bom[i].required_amount = req_mat_list[f'{actual_bom[i].id}']
            actual_bom[i].amount = req_mat_list[f'{actual_bom[i].id}'] * config['init_stock']
        super().__init__(config, actual_bom)
        