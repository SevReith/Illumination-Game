import os, json
from PyQt5.QtWidgets import  QMdiArea, QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from Views import sub_win_production


class Product_View(QMdiArea):
    """Display a subwindow with production, product and material info.
    Takes the product model and controler as args."""

    prod_time_sender = pyqtSignal(float)
    prod_stock_sender = pyqtSignal(int, float)

    def __init__(self, pro_mdl, pro_ctrl, root):
        super().__init__()
        self.root_directory = root
        self._panel_production = sub_win_production.Ui_Form()
        self._panel_production.setupUi(self)

        self._model_product = pro_mdl
        self._controller_product = pro_ctrl

        self.update_lbl_prod_stock()
        self.update_lbl_prod_name()
        self.update_lbl_prod_goal()
        self.update_lbls_material_stock()
        for prod in self._model_product:
            self.load_desciption_texts(prod)
            self.update_lbls_characteristics(prod.id)
            self.update_lbls_bom(prod.id)

        #setup widgets
        self._panel_production.led_prod_goal.setValidator(QIntValidator())
        self._panel_production.led_prod_goal.returnPressed.connect(self.led_production_goal_entered)

        #listen to material model
        length = len(self._model_product[0].bill_of_materials)
        for i in range(length):
            #connects all material stocks to the material stock label update
            self._model_product[0].bill_of_materials[i].stock_changed.connect(self.update_lbls_material_stock)

        #listen to product model
        for i in range(len(self._model_product)):
            self._model_product[i].stock_amount_changed.connect(self.update_lbl_prod_stock)
            self._model_product[i].production_goal_changed.connect(self.update_lbl_prod_goal)
        
    @pyqtSlot(bool)
    def update_lbl_prod_name(self, prod = None):
        if prod == None:
            prod = self._controller_product.get_active_product_index()
        self._panel_production.lbl_cur_prod_name.setText(self._model_product[prod].name)

    @pyqtSlot(int)
    def update_lbl_prod_stock(self):
        prod = self._controller_product.get_active_product_index()
        self._panel_production.lbl_prod_in_stock_amount.setText(f'{self._model_product[prod].amount:,}')

    @pyqtSlot(int)
    def update_lbl_prod_capacity(self, tuc):
        self._panel_production.lbl_prod_capacity_amount.setText(f'{tuc:,}')

    @pyqtSlot(int)
    def update_lbl_prod_last_month(self, val):
        self._panel_production.lbl_prod_last_moth_amount.setText(f'{val:,}')

    @pyqtSlot(bool)
    def update_lbl_prod_goal(self):
        text = 'Max. Capacity'
        prod = self._controller_product.get_active_product_index()
        if self._model_product[prod].production_goal_flag:
            self._panel_production.lbl_prod_goal_amount.setText(f'{self._model_product[prod].production_goal:,}')
        else:
            self._panel_production.lbl_prod_goal_amount.setText(text)

    @pyqtSlot(int)
    def update_lbls_material_stock(self):
        """Load texts and current stock of all materials into Stock tab."""
        materials_in_use = []
        for prod in self._model_product:
            for mat in prod.bill_of_materials:
                if mat not in materials_in_use:
                    materials_in_use.append(mat)
        bom_length = len(materials_in_use)
        for i in range(bom_length):
            label = getattr(self._panel_production, f'lbl_mat_name{i + 1}')
            label.setText(f'{materials_in_use[i].name}:')
            label = getattr(self._panel_production, f'lbl_amount{i + 1}')
            label.setText(f'{materials_in_use[i].amount:,}')
        
    def update_lbls_characteristics(self, product):
        """Update the characteristic labels dnymically. Product gives the prodct list index of the active index.
        According to the index only the neccesarry tab is updated.
        0 = tab 3; 1 = tab 4; 2 tab 5"""
        tab = product + 3
        label_names = ['prod_time', 'actual_value', 'base_value', 'quality', 'license']
        values = [self._model_product[product].production_time * 60, self._model_product[product].actual_value, 
        self._model_product[product].base_value, self._model_product[product].base_quality, self._model_product[product].license] 
        for i in range(len(label_names)):
            label = getattr(self._panel_production, f'lbl_tab{tab}_{label_names[i]}')
            label.setText(f'{values[i]:,.2f}')

    def update_lbls_bom(self, product):
        """Update the characteristic labels dnymically. Product gives the prodct list index of the active index.
        According to the index only the neccesarry tab is updated.
        0 = tab 3; 1 = tab 4; 2 tab 5"""
        tab = product + 3
        bom_length = len(self._model_product[product].bill_of_materials)
        for i in range(bom_length):
            label = getattr(self._panel_production, f'lbl_txt_tab{tab}_mat{i + 1}')
            label.setText(f'{self._model_product[product].bill_of_materials[i].name}')
            label = getattr(self._panel_production, f'lbl_tab{tab}_mat{i + 1}')
            label.setText(f'{self._model_product[product].bill_of_materials[i].required_amount}')

    def get_prod_time(self):
        prod = self._controller_product.get_active_product_index()
        return self._model_product[prod].production_time

    def get_prod_stock(self):
        prod = self._controller_product.get_active_product_index()
        return self._model_product[prod].amount, self._model_product[prod].sales_price

    def get_price_influencer(self):
        prod = self._controller_product.get_active_product_index()
        return self._model_product[prod].sales_price_influencer

    @pyqtSlot(int)
    def set_product_stock(self, stock):
        prod = self._controller_product.get_active_product_index()
        self._model_product[prod].amount = stock

    def led_production_goal_entered(self):
        prod = self._controller_product.get_active_product_index()
        goal = int(self._panel_production.led_prod_goal.text())
        self._model_product[prod].production_goal = goal
        self._model_product[prod].production_goal_flag = True

    def product_license_clicked(self, prod: int, funds: float, credit_limit: int = 10000) -> int:
        """Check if there is enough funds available for the new product license, return -1 if not.
        If yes, display message to confirm license purchase."""
        cost = self._model_product[prod].license
        cost_flag = True if cost <= funds + credit_limit else False
        if cost_flag:
            reply = QMessageBox.question(self, 'Advanced Product!', f'That will cost {cost:,}???! Are you sure?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self._controller_product.activate_product(prod)
                self.update_lbl_prod_name(prod)
                self.update_lbl_prod_stock()
                return cost 
        elif not cost_flag:
            self.show_message_funds(cost)
        return -1

    def show_message_funds(self, cost: float):
        """displays a messagebox. takes cost"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Insufficient Funds!")
        msg.setInformativeText(f'Unfortunately we can not afford this now. We need {cost:,}???.')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        
    def load_desciption_texts(self, prod):
        label = getattr(self._panel_production, f'lbl_tab{prod.id + 3}_top')
        label.setText(f'{prod.description}')
