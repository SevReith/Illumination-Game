"""Main Game Module."""

import sys, os

from PyQt5.QtWidgets import QApplication
from Models.Capital import Capital
from Models.Factory import Factory
from Models.Layout import Fixed_Position_Layout
from Models.Market import Market
from Models.Material import *
from Models.Product import Halogen_Light, LED_Light, Light_Bulb
from Views.Main_View import Main_View
from Views.Capital_View import Capital_View
from Views.Factory_View import Factory_View
from Views.Market_View import Market_View
from Views.Product_View import Product_View
from Controllers.Capital_Controller import Capital_Controller
from Controllers.Main_Controller import Main_Controller
from Controllers.Layout_Controller import Layout_Controller
from Controllers.Market_Controller import Market_Controller
from Controllers.Material_Controller import Material_Controller
from Controllers.Product_Controller import Product_Controller


class Game_App(QApplication):
    """Initializes the game app as a QApplication."""

    def __init__(self, sys_argv):
        """Initialize all models, views and controllers."""
        super(Game_App, self).__init__(sys_argv)
        # initialize game model
        self.model_capital = Capital()
        self.model_layout = self.create_layouts()
        self.model_factory = Factory("Schulmeisterwerke", self.model_layout)
        self.model_market = Market()
        self.model_material = self.create_materials()
        self.model_product = self.create_products(self.model_material)
        # initialize game controler
        self.layout_controller = Layout_Controller(self.model_layout)
        self.material_controller = Material_Controller(self.model_material)
        self.product_controller = Product_Controller(self.model_product)
        self.main_controller = Main_Controller(self.model_capital, self.model_factory, self.model_market, self.product_controller, self.layout_controller)
        # initialize game views
        self.market_view = Market_View(self.model_capital, self.model_market, self.model_product, self.model_material, self.main_controller, self.product_controller, self.material_controller)
        self.factory_view = Factory_View(self.model_factory, self.model_product, self.model_material, self.layout_controller, self.material_controller, self.product_controller)
        self.product_view = Product_View(self.model_product, self.product_controller)
        self.capital_view = Capital_View(self.model_capital)
        self.main_view = Main_View(self.model_capital, self.model_factory, self.model_market, self.main_controller, self.factory_view, self.market_view, self.product_view, self.capital_view)

        # show main window
        self.main_view.show()

    def create_layouts(self):
        """Create the starter layouts. returns a list of these layouts."""
        lay_list = []
        lay_list.append(Fixed_Position_Layout('Fixed Position Layout'))
        lay_list.append(Fixed_Position_Layout('Fixed Position Layout'))
        return lay_list

    def create_materials(self):
        """Create the starker materials. returns a list of these materials."""
        mat_list = []
        mat_list.append(Glass_Bulb())
        mat_list.append(Coiled_Filament())
        mat_list.append(Lead_In_Wires())
        mat_list.append(Socket())
        mat_list.append(Protective_Gas())
        mat_list.append(Packaging())
        return mat_list

    def create_products(self, material_list):
        """Create the starker products. returns a list of these products."""
        prod_list = []
        prod_list.append(Light_Bulb(material_list))
        prod_list[0].is_active = True
        prod_list.append(Halogen_Light(material_list))
        prod_list.append(LED_Light(material_list))
        return prod_list


if __name__ == '__main__':
    # starts the game!
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"  # counters the viscious windows dpi scaling!
    app = Game_App(sys.argv)
    sys.exit(app.exec_())
