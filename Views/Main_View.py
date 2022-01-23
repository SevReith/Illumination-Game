"""Main View Module. Connects main Controllers, other views and models."""

import os, subprocess
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from Views import Main_Window

class Main_View(QMainWindow):
    """View for Capital, Market, Factory models."""

    def __init__(self, cap_model, fac_model, mar_model, main_ctrl, fac_view, mar_view, prod_view, cap_view, sum_view, root_directory):
        """Intitalize Main View.
        
        Contains the Main Controller
        Capital, Factory and Market Model
        Factory, Market, Product and Capital View
        """
        super().__init__()
        #load main window
        self._ui = Main_Window.Ui_MainWindow()
        self._ui.setupUi(self)
        #load and save background image
        path = os.path.join(root_directory, 'Resources', 'Images', 'Factory_old_Top_1300x900.png')
        img = QImage(path)
        pixmap = QPixmap(img)
        self._ui.lbl_factory_blueprint.setPixmap(pixmap)

        self._model_capital = cap_model
        self._model_factory = fac_model
        self._model_market = mar_model
        self._controller_main = main_ctrl
        self._view_capital = cap_view
        self._view_factory = fac_view
        self._view_market = mar_view
        self._view_production = prod_view
        self._view_summary = sum_view
        self.root_directory = root_directory

        #connect widgets to main controller and other views
        self._ui.button_help.clicked.connect(self.button_help_clicked)
        self._ui.button_end_turn.clicked.connect(self.button_end_turn_clicked)
        self._ui.button_end_turn.clicked.connect(self.hide_panels)
        self._ui.button_factory.clicked.connect(self.button_factory_clicked)
        self._ui.button_market.clicked.connect(self.button_market_clicked)
        self._ui.button_accounting.clicked.connect(self.button_accounting_clicked)
        self._ui.rbtn_production.clicked.connect(self.rdbutton_production_clicked)

        #connect product to main controller and vice versa
        self._view_production.prod_time_sender.connect(self._controller_main.calculate_total_time_unit_capacity)
        self._view_production.prod_stock_sender.connect(self._controller_main.calculate_sales)
        self._controller_main.production_capacity_calculated.connect(self._view_production.update_lbl_prod_capacity)
        self._controller_main.send_new_prod_stock.connect(self._view_production.set_product_stock)

        #connect widgets on factory panel
        self._view_factory._panel_factory.btn_increase_factory.clicked.connect(self.sub_btn_increase_factory_clicked)
        self._view_factory._panel_factory.btn_tab2_build_fixed_pos_lay.clicked.connect(self.sub_btn_build_fixed_pos_layout_clicked)
        self._view_factory._panel_factory.btn_tab2_dismantle_fixed_pos_lay.clicked.connect(self.sub_btn_destroy_fixed_pos_lay_clicked)
        self._view_factory._panel_factory.btn_tab3_build_process_lay.clicked.connect(self.sub_btn_build_process_layout_clicked)
        self._view_factory._panel_factory.btn_tab3_dismantle_process_lay.clicked.connect(self.sub_btn_destroy_process_lay_clicked)
        self._view_factory._panel_factory.btn_tab3_add_department.clicked.connect(self.sub_btn_add_dept_process_clicked)
        self._view_factory._panel_factory.btn_tab4_build_cellular_lay.clicked.connect(self.sub_btn_build_cellular_layout_clicked)
        self._view_factory._panel_factory.btn_tab4_add_department.clicked.connect(self.sub_btn_add_dept_cellular_clicked)
        self._view_factory._panel_factory.btn_tab5_dismantle_cellular_lay.clicked.connect(self.sub_btn_destroy_cellular_lay_clicked)
        self._view_factory._panel_factory.btn_tab5_build_line_lay.clicked.connect(self.sub_btn_build_line_layout_clicked)
        self._view_factory._panel_factory.btn_tab5_dismantle_line_lay.clicked.connect(self.sub_btn_destroy_line_lay_clicked)

        #connect widgets to production panel
        self._view_production._panel_production.btn_tab4_license.clicked.connect(self.sub_btn_halogen_license_clicked)
        self._view_production._panel_production.btn_tab5_license.clicked.connect(self.sub_btn_led_license_clicked)

        # connect widgets to summary view
        self._view_capital._panel_accounting.btn_tab1_show_summary.clicked.connect(self.sub_btn_show_summary_clicked)

        #listen to capital model
        self._model_capital.capital_changed.connect(self.on_capital_changed)

        #listen to factory model
        self._model_factory.cur_turn_changed.connect(self.on_turn_changed)
        self._model_factory.factory_characteristics_changed.connect(self.on_factory_characteristics_changed)
        self._model_factory.products_manufacured.connect(self._view_production.update_lbl_prod_last_month)

        #update labels inititlly
        self._view_factory.update_fac_tab1_top_lbl(f'{self._model_factory.name}\n\nProduct: {self._view_factory._model_product[0].name}\
            \nCurrent Production Layout: {self._model_factory.layout_list[0].layout_name}')
        self._view_factory.update_fac_tab1_midleft_lbl(self._model_factory.size, self._model_factory.free_space, self._model_factory.total_cost, 
                                                       self._model_factory.fixed_cost_per_m2, self._model_capital.currency_sign)
        self.on_capital_changed(self._model_capital.amount)
        self.on_turn_changed()
        self._controller_main.calculate_total_time_unit_capacity(self._view_production.get_prod_time())
        self._controller_main.generate_sales_forecast()
        

    def button_accounting_clicked(self):
        turns = self._model_factory.current_turn
        x_axis = self._view_summary.calculate_xaxis_with_turns(turns)
        y_axis = self._view_summary.calculate_profit(turns)
        self._view_capital.update_plot_profit(x_axis, y_axis[1])
        self._view_capital.show()
        
    @pyqtSlot(int)
    def on_capital_changed(self, value):
        self._ui.lbl_capital.setText(f'Capital: \t{value:,.2f}{self._model_capital.currency_sign}')

    @pyqtSlot()
    def on_turn_changed(self):
        self._ui.lbl_turn.setText(f'Turn {self._model_factory.current_turn} of {self._model_factory.final_turn}')

    @pyqtSlot()
    def button_factory_clicked(self):
        self._view_factory.show()

    def sub_btn_build_fixed_pos_layout_clicked(self):
        """calls message box in factory view to confirm building. if successful, calls
        function in main controller to create FPL-Object"""
        flag = self._view_factory.build_fixed_pos_layout_clicked(self._model_factory.free_space, self._model_capital.amount)
        if flag:
            self._controller_main.build_fixed_pos_layout()

    def sub_btn_build_process_layout_clicked(self):
        """calls message box in factory view to confirm building. if successful, calls
        function in main controller to create PL-Object"""
        flag = self._view_factory.build_process_layout_clicked(self._model_factory.free_space, self._model_capital.amount)
        if flag:
            self._controller_main.build_process_layout()

    def sub_btn_build_cellular_layout_clicked(self):
        """calls message box in factory view to confirm building. if successful, calls
        function in main controller to create CL-Object"""
        flag = self._view_factory.build_cellular_layout_clicked(self._model_factory.free_space, self._model_capital.amount)
        if flag:
            self._controller_main.build_cellular_layout()

    def sub_btn_build_line_layout_clicked(self):
        """calls message box in factory view to confirm building. if successful, calls
        function in main controller to create LL-Object"""
        flag = self._view_factory.build_line_layout_clicked(self._model_factory.free_space, self._model_capital.amount)
        if flag:
            self._controller_main.build_line_layout()

    def sub_btn_add_dept_process_clicked(self):
        """calls message box in factory view to confirm building. if successful, adds a
        department to the process layout and subtracts the cost."""
        cost, space = self._view_factory.add_dept_process(self._model_factory.free_space, self._model_capital.amount)
        if not cost == -1:
            self._model_capital.amount -= cost
            self._model_factory.free_space -= space
            self._view_factory.update_lbl_process_departments(True)

    def sub_btn_add_dept_cellular_clicked(self):
        """calls message box in factory view to confirm building. if successful, adds a
        department to the cellular layout and subtracts the cost."""
        cost, space = self._view_factory.add_dept_cellular(self._model_factory.free_space, self._model_capital.amount)
        if not cost == -1:
            self._model_capital.amount -= cost
            self._model_factory.free_space -= space
            self._view_factory.update_lbl_cellular_departments(True)

    def sub_btn_increase_factory_clicked(self):
        """adds a specified number of m2 to the factories size. 
        returns the new size and the building cost."""
        size, cost = self._view_factory.increase_factory(self._model_factory.STANDARD_ADD_COST_M2, self._model_capital.currency_sign, 
                                                         self._model_capital.amount)
        self._controller_main.build_factory_space(size, cost)

    def sub_btn_destroy_fixed_pos_lay_clicked(self):
        flag, name = self._view_factory.delete_fixed_pos_layout()
        if flag:
            self._controller_main.destroy_layout(name)

    def sub_btn_destroy_process_lay_clicked(self):
        flag, name = self._view_factory.delete_process_layout()
        if flag:
            self._controller_main.destroy_layout(name)

    def sub_btn_destroy_cellular_lay_clicked(self):
        flag, name = self._view_factory.delete_cellular_layout()
        if flag:
            self._controller_main.destroy_layout(name)

    def sub_btn_destroy_line_lay_clicked(self):
        flag, name = self._view_factory.delete_line_layout()
        if flag:
            self._controller_main.destroy_layout(name)

    @pyqtSlot(int, int, float, float)
    def on_factory_characteristics_changed(self, size, free_size, total_cost, fixed_cost):
        self._view_factory.update_fac_tab1_midleft_lbl(size, free_size, total_cost, fixed_cost, self._model_capital.currency_sign)

    def button_market_clicked(self):
        self._view_market.show()

    def rdbutton_production_clicked(self):
        self._view_production.show()

    def sub_btn_halogen_license_clicked(self):
        cost = self._view_production.product_license_clicked(1, self._model_capital.amount)
        if not cost == -1:
            self._model_capital.amount -= cost
            self._view_market.update_lbl_bottom()
            self._controller_main.calculate_total_time_unit_capacity(self._view_production.get_prod_time())

    def sub_btn_led_license_clicked(self):
        cost = self._view_production.product_license_clicked(2, self._model_capital.amount)
        if not cost == -1:
            self._model_capital.amount -= cost
            self._view_market.update_lbl_bottom()
            self._controller_main.calculate_total_time_unit_capacity(self._view_production.get_prod_time())

    def sub_btn_show_summary_clicked(self):
        self._view_summary.create_yearly_summary()
        self._view_summary.show()
    
    def hide_panels(self):
        """Hide all subwindows."""
        self._view_factory.hide()
        self._view_market.hide()
        self._view_production.hide()
        self._view_capital.hide()

    def button_end_turn_clicked(self):
        stock, price = self._view_production.get_prod_stock()
        self._controller_main.calculate_turn_end(stock, price, self._view_production.get_price_influencer(), self._view_production.get_prod_time())

    def button_help_clicked(self):
        """Open the game manual pdf."""
        path = os.path.join(self.root_directory, 'Resources', 'Manual_Illumination_Game.pdf')
        subprocess.Popen(path, shell=True)
