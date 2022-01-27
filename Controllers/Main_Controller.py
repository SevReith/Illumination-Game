import os, subprocess
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from random import Random
from Models.Layout import *


class Main_Controller(QObject):
    """controls capital, factory and market"""

    production_capacity_calculated = pyqtSignal(int)
    send_new_prod_stock = pyqtSignal(int)

    def __init__(self, cap_model, fac_model, mar_model, prod_ctlr, lay_ctrl, root_directory):
        super().__init__()

        self._model_capital = cap_model
        self._model_factory = fac_model
        self._model_market = mar_model
        self._controller_product = prod_ctlr
        self._controller_layout = lay_ctrl
        self.random_number_generater = Random()
        self.root_directory = root_directory
        self.tutorial_flag = True

        # create first forecast
        self.calculate_fixed_cost()

    def build_fixed_pos_layout(self) -> None:
        """creates a new Fixed Position Layout, adds it to the factories layout list and sets the building cost"""
        lay = Fixed_Position_Layout(self._model_factory._layout_config['Fixed_Position_Layout'])
        lay.built_in_turn = self._model_factory.current_turn
        lay.activation_turn = self._model_factory.current_turn + lay.building_time
        lay.is_active = False
        self._model_factory.nb_fixed_position += 1
        self._model_factory.free_space -= lay.required_space
        self._model_factory.add_layout_to_list(lay)
        self._model_capital.amount -= lay.building_cost
        self._model_capital.current_building_cost += lay.building_cost

    def build_process_layout(self) -> None:
        """creates a new Process Layout, adds it to the factories layout list and sets the building cost"""
        lay = Process_Layout(self._model_factory._layout_config['Process_Layout'])
        lay.built_in_turn = self._model_factory.current_turn
        lay.activation_turn = self._model_factory.current_turn + lay.building_time
        lay.is_active = False
        self._model_factory.nb_process += 1
        self._model_factory.free_space -= lay.required_space
        self._model_factory.add_layout_to_list(lay)
        self._model_capital.amount -= lay.building_cost
        self._model_capital.current_building_cost += lay.building_cost

    def build_cellular_layout(self) -> None:
        """creates a new Cellular Layout, adds it to the factories layout list and sets the building cost"""
        lay = Cellular_Layout(self._model_factory._layout_config['Cellular_Layout'])
        lay.built_in_turn = self._model_factory.current_turn
        lay.activation_turn = self._model_factory.current_turn + lay.building_time
        lay.is_active = False
        self._model_factory.nb_cellular += 1
        self._model_factory.free_space -= lay.required_space
        self._model_factory.add_layout_to_list(lay)
        self._model_capital.amount -= lay.building_cost
        self._model_capital.current_building_cost += lay.building_cost

    def build_line_layout(self) -> None:
        """creates a new Line Layout, adds it to the factories layout list and sets the building cost"""
        lay = Line_Layout(self._model_factory._layout_config['Line_Layout'])
        lay.built_in_turn = self._model_factory.current_turn
        lay.activation_turn = self._model_factory.current_turn + lay.building_time
        lay.is_active = False
        self._model_factory.nb_line += 1
        self._model_factory.free_space -= lay.required_space
        self._model_factory.add_layout_to_list(lay)
        self._model_capital.amount -= lay.building_cost
        self._model_capital.current_building_cost += lay.building_cost

    def check_for_layout_activation(self) -> None:
        """Check if there is a layout to be activated. Compares current turn with activation turn."""
        length = len(self._model_factory.layout_list)
        for i in range(length):
            if not self._model_factory.layout_list[i].is_active and self._model_factory.layout_list[i].activation_turn == self._model_factory.current_turn:
                self._model_factory.layout_list[i].is_active = True
                info_text = f'A new {self._model_factory.layout_list[i].name} has been finished and is ready for production!'
                self.display_notification_message('Layout built!', info_text)

    def build_factory_space(self, size:int, cost:int) -> None:
        """gets size and cost from main view. stores them in factory/capital respectively"""
        self._model_factory.size += int(size)
        self._model_factory.free_space += int(size)
        self._model_capital.amount -= cost
        self._model_capital.current_building_cost += cost

    def destroy_layout(self, name:str) -> None:
        """Check if layout exists with name. Delete if existing and adjust counter."""
        for i in range(len(self._model_factory.layout_list)):
            if self._model_factory.layout_list[i].name == name:
                self._model_factory.free_space += self._model_factory.layout_list[i].required_space
                del self._model_factory.layout_list[i]
                if name == 'Fixed Position Layout':
                    self._model_factory.nb_fixed_position -= 1
                elif name == 'Process Layout':
                    self._model_factory.nb_process -= 1
                elif name == 'Cellular Layout':
                    self._model_factory.nb_cellular -= 1
                elif name == 'Line Layout':
                    self._model_factory.nb_line -= 1
                break
        # immediately updates the production capacity after a layout is dismantled.
        active_prod = self._controller_product.get_active_product_index()
        self.calculate_total_time_unit_capacity(self._controller_product._model_product[active_prod].production_time)

    def calculate_fixed_cost(self) -> None:
        """calculates the fixed cost for the entire factory. The space occupied by production layouts,
        is calculated with the according production time modifiers.
        Returns the total cost."""
        cost = 0
        remaining_size = self._model_factory.size
        for layout in self._model_factory.layout_list:
            if layout.is_active:
                cost += layout.size * self._model_factory.fixed_cost_per_m2 * layout.maintenance_cost_modifier
                remaining_size -= layout.size
        cost += remaining_size * self._model_factory.fixed_cost_per_m2
        self._model_factory.total_cost = cost
        cost_arch = self._model_factory.fixed_cost_archive
        cost_arch.append(cost)
        self._model_factory.fixed_cost_archive = cost_arch
        return cost

    def calculate_total_time_unit_capacity(self, prod_time:float) -> None:
        """calculates tuc for all active layouts. working month / (production time *(1 + layout production time modifier))"""
        total_time_unit_capacity = 0
        for layout in self._model_factory.layout_list:
            if layout.is_active:
                total_time_unit_capacity += layout.calculate_tuc(self._model_factory.working_month, prod_time)
        self._model_factory.current_tuc = int(total_time_unit_capacity)
        self.production_capacity_calculated.emit(int(total_time_unit_capacity))

    def calculate_production(self) -> None:
        """calculates the effective production from all exisiting layouts for one product. 
        returns the total production capacity."""
        # calculate uc and get tuc
        new_products = 0
        total_time_unit_capacity = self._model_factory.current_tuc
        unit_capacity = self._controller_product.calculate_unit_capacity()
        prod_goal = self._controller_product._model_product[0].production_goal
        # get min of tuc and uc but cannot be lower than 0
        if self._controller_product._model_product[0].production_goal_flag:
            new_products = max(min(total_time_unit_capacity,
                               unit_capacity, prod_goal), 0)
        else:
            new_products = max(min(total_time_unit_capacity, unit_capacity), 0)
        # reduce material stock
        self._controller_product.reduce_material_stocks(new_products)
        # safe production into archive
        prod_archive = self._model_factory.production_archive
        prod_archive.append(new_products)
        self._model_factory.production_archive = prod_archive

    def calculate_sales(self, stock:int, price:float, price_influencer:float) -> None:
        """Call the generate sales function. Calculate stock and income and save them to the archive."""
        sales = self.generate_sales_modifier(price_influencer)
        stock += int(self._model_factory.production_archive[-1])
        sales = stock if not sales <= stock else sales
        new_stock = stock - sales
        income = sales * price
        self._model_capital.amount += income
        income_archive = self._model_capital.total_income_archive
        income_archive.append(income)
        self._model_capital.total_income_archive = income_archive
        self.send_new_prod_stock.emit(new_stock)
        self.calculate_store_market_data(sales, income)

    def calculate_store_market_data(self, sales:float, income:float) -> None:
        """adds one line to the sales archive dict. cumulates sales, sales volume and calculates yearly marketvolume"""
        # cumulate mothly sales income. reset every 12 turns (months)
        self._model_market.add_item_to_sales_archive(
            {'turn': 0, 'year': 0, 'units': 0, 'volume': 0, 'units cumulated': 0, 'volume cumulated': 0, 'share cumulated': 0})
        sa_archive = self._model_market.sales_archive
        length = len(sa_archive)
        cur_turn = self._model_factory.current_turn
        year_flag = cur_turn % 13 == 0
        sa_archive[length - 1]['turn'] = cur_turn
        sa_archive[length - 1]['year'] = sa_archive[length - 2]['year'] if not year_flag else (sa_archive[length - 1]['year'] + 1)
        sa_archive[length - 1]['units'] = sales
        sa_archive[length - 1]['volume'] = income
        sa_archive[length - 1]['units cumulated'] = sa_archive[length - 2]['units cumulated'] + sales if not year_flag else sales
        sa_archive[length - 1]['volume cumulated'] = sa_archive[length - 2]['volume cumulated'] + income if not year_flag else income
        sa_archive[length - 1]['share cumulated'] = sa_archive[length - 1]['volume cumulated'] / self._model_market.total_marketvolume_p_month * 100
        self._model_market.sales_archive = sa_archive
        if cur_turn % 12 == 0 and not cur_turn == 0:
            self._model_market.yearly_summary_flag = True
            self.generate_yearly_marketvolume_growth()

    def generate_yearly_marketvolume_growth(self, min=90, max=130, step=1) -> None:
        """calculates marketvolume growth between -10% and +30% randomly per year. stores the new volume yearly and monthly"""
        marketvolume = self._model_market.marketvolume_annually * \
            (self.random_number_generater.randrange(min, max, step) / 100)
        self._model_market.total_marketvolume_p_month = marketvolume / 12
        self._model_market.marketvolume_annually = marketvolume

    def generate_sales_forecast(self, min=95, max=125, step=1) -> None:
        """generates random forecast bewtween min and max."""
        sales = self._model_market.get_last_month_sales_units() if not self._model_factory.current_turn == 0 else self._model_factory.current_tuc
        sales = self._model_factory.current_tuc / 4 if sales == 0 else sales
        forecast = int(sales * (1 + self._model_market.average_monthly_sales_growth_rate *
                       self._model_market.random_number_generater.randrange(min, max, step) / 100))
        self._model_market.add_item_to_forecasted_archive(forecast)
        self._model_market.forecasted_sales = forecast

    def generate_sales_modifier(self, price_influencer, min=96, max=125, step=1) -> int:
        """takes the latest forecast with price influencer and applies a random sales modifier to it (96-125%)
        returns modified sales -> int"""
        fc = self._model_market.get_last_forecast()
        sales_modifier = self._model_market.random_number_generater.randrange(min, max, step) / 100
        self._model_market.sales_modifier = sales_modifier
        return int((fc + (price_influencer * fc)) * sales_modifier)

    def calculate_end_turn_helper(self, stock, price, price_influencer, prod_time) -> None:
        # buy materials before calculating production
        self.check_for_layout_activation()
        mats_to_buy = self._model_factory.current_tuc if not self._controller_product._model_product[0].production_goal_flag else self._controller_product._model_product[0].production_goal
        cost = self._controller_product.increase_material_stocks(mats_to_buy)
        self.calculate_total_time_unit_capacity(prod_time)
        self.calculate_production()        
        self.calculate_sales(stock, price, price_influencer)
        fixed_cost = self.calculate_fixed_cost()
        total_cost = cost + fixed_cost
        # incomes are calculated in function calculate_sales
        self._model_capital.amount -= total_cost
        # building cost are already deducted during building. they only need to be added to the archive.
        total_cost += self._model_capital.current_building_cost
        cost_archive = self._model_capital.total_cost_archive
        cost_archive.append(total_cost)
        self._model_capital.total_cost_archive = cost_archive
        # save cost detail
        self._model_capital.add_latest_cost_detail_to_archive(fixed_cost, cost, self._model_capital.current_building_cost)
        self._model_capital.current_building_cost = 0

        # hide all open windows
        for i in range(len(self._controller_product._model_product)):
            self._controller_product._model_product[i].production_goal_flag = False
            self.generate_sales_forecast()

        # increment current turn
        self._model_factory.current_turn += 1

        # chek for tutorial display
        if self.tutorial_flag:
            self.open_tutorial_pdfs(self._model_factory.current_turn)

    def calculate_turn_end(self, stock, price, price_influencer, prod_time) -> None:
        """end the current turn. updates turn counter and calls game update functions"""
        # check winning condicton
        if self.check_winning_condition():
            self.display_notification_message('CONGRATULATIONS!', 
            f'You dominate the illuminate market! There is no competitor even close to you!\n You win!\nStrangely the authorities do not seem to be that enlighted...')    

        if self._model_factory.final_turn == self._model_factory.current_turn:
            # allows player to choose to play for another 60 turns
            answer = self.ask_yes_or_no("The End?", 'You have competed for 5 years! Do you want to play another 5 years?')
            if answer:
                self._model_factory.final_turn += 60
                self.calculate_end_turn_helper(stock, price, price_influencer, prod_time)
            else:
                # if player chooses no, nothing happens anymore. the current windows stays responsive, but cannot progress in turns
                pass
        else:
            self.calculate_end_turn_helper(stock, price, price_influencer, prod_time) 

    def check_winning_condition(self) -> bool:
        """compares current marketshare to winning marketshare. returns True if current is equal or larger"""
        sa_archive = self._model_market.sales_archive
        try:
            return self._model_market.winning_marketshare <= sa_archive[-1]['share cumulated']
        except IndexError:
            return False

    def open_tutorial_pdfs(self, cur_turn:int) -> None:
        """Open the tutorial pdf of the current turn."""
        path = os.path.join(self.root_directory,'Resources', 'Tutorial', f'turn{cur_turn}.pdf')
        if os.path.exists(path):
            subprocess.Popen(path, shell=True)

    def ask_yes_or_no(self, title:str, text:str) -> bool:
        """Ask a yes or no question to the player. Takes title and text inputs.
        Returns True, if player clicked yes, Fals in any other case."""
        msg = QMessageBox()
        reply = QMessageBox.question(msg, title, text,
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            return True
        else:
            return False

    def display_notification_message(self, title:str, text:str) -> None:
        """Display standard message box with title and text, only with OK-button."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(title)
        msg.setInformativeText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()   
