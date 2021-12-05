from PyQt5.QtCore import QObject, pyqtSlot

class Product_Controller(QObject):
    """description of class"""

    def __init__(self, prod_model):
        super().__init__()

        self._model_product = prod_model

        #listen to product model
        for i in range(3):
            self._model_product[i].base_value_changed.connect(self.calculate_actual_value)
            self._model_product[i].base_quality_changed.connect(self.calculate_actual_value)
            self._model_product[i].actual_value_changed.connect(self.calculate_sales_price_influencer)
            self._model_product[i].sales_price_changed.connect(self.calculate_sales_price_influencer)

        self.calculate_sales_price_influencer()

    def get_active_product_index(self):
        """Loop over product list and return the index of active product. 
        Returns -1 if nothing is found."""
        i = 0
        for prod in self._model_product:
            if prod.is_active:
                return i
            i += 1
            return -1

    @pyqtSlot(float)
    def calculate_sales_price_influencer(self):
        active_prod = self.get_active_product_index()
        """calculates the sales price influencer as proportion of sales price to actual value."""
        difference = 1 - self._model_product[active_prod].sales_price / self._model_product[active_prod].actual_value 
        if difference <= - 1:
            #difference larger than -1 results in 100% less sales
            self._model_product[active_prod].sales_price_influencer = -1
        elif difference <= -0.7:
            #difference larger -0.7 results lineary in 10% less sales per 10% difference
            #also between -0.6 and -0.7 there is a 40% sales loss
            self._model_product[active_prod].sales_price_influencer = difference
        elif difference < 0:
            #difference larger than -0 results lineary in 5% less sales per 10% difference
            self._model_product[active_prod].sales_price_influencer = difference / 2
        elif difference <= 0.5:
             #difference smaller than 0.5 results lineary in 20% more sales per 10% difference
             self._model_product[active_prod].sales_price_influencer = difference * 2           
        else:
            #difference larger than 0.5 results in 100% more sales
            self._model_product[active_prod].sales_price_influencer = 1            
    
    @pyqtSlot(float)
    def calculate_actual_value(self):
        active_prod = self.get_active_product_index()
        self._model_product[active_prod].actual_value = self._model_product[active_prod].base_value * 1 + self._model_product[active_prod].base_quality

    def calculate_unit_capacity(self):
        """calculates the uc (how much can be produced with available material). return uc (int)"""
        uc = 9999999999
        active_prod = self.get_active_product_index()
        for mat in self._model_product[active_prod].bill_of_materials:
            stock = mat.amount / mat.required_amount
            if stock < uc:
                uc = stock
        return int(uc)

    def reduce_material_stocks(self, produced):
        """reduces the material stock in all bom-items."""
        active_prod = self.get_active_product_index()
        length = len(self._model_product[active_prod].bill_of_materials)
        for i in range(length):
            self._model_product[active_prod].bill_of_materials[i].amount -= produced * self._model_product[active_prod].bill_of_materials[i].required_amount

    def increase_material_stocks(self, tuc):
        """Buy enough material for either the TUC or production goal.
        Return raw material cost --> float"""
        active_prod = self.get_active_product_index()
        to_produce = tuc if not self._model_product[active_prod].production_goal_flag else self._model_product[active_prod].production_goal
        cost = 0
        length = len(self._model_product[active_prod].bill_of_materials)
        for i in range(length):
            new_material = self._model_product[active_prod].bill_of_materials[i].amount - (to_produce * self._model_product[active_prod].bill_of_materials[i].required_amount)
            new_material = 0 if new_material >= 0 else abs(new_material)
            self._model_product[active_prod].bill_of_materials[i].amount += new_material
            cost += new_material * self._model_product[active_prod].bill_of_materials[i].price
        cost_archive = self._model_product[active_prod].material_cost_archive
        cost_archive.append(cost)
        self._model_product[active_prod].material_cost_archive = cost_archive
        return cost

    def activate_product(self, prod):
        old_prod = self.get_active_product_index()
        self._model_product[old_prod].is_active = False
        self._model_product[prod].is_active = True
        