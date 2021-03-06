"""Main Game Module."""

import sys, os, json

from PyQt5.QtWidgets import QApplication
from Models.Capital import Capital
from Models.Factory import Factory
from Models.Layout import * # they are used in def create_layouts0
from Models.Market import Market
from Models.Material import * # they are used in def create_materials
from Models.Product import Halogen_Light, LED_Light, Light_Bulb # they are used in def create_products
from Views.Main_View import Main_View
from Views.Capital_View import Capital_View
from Views.Factory_View import Factory_View
from Views.Market_View import Market_View
from Views.Product_View import Product_View
from Views.Summary_View import Summary_View
# from Controllers.Capital_Controller import Capital_Controller
from Controllers.Main_Controller import Main_Controller
from Controllers.Layout_Controller import Layout_Controller
# from Controllers.Market_Controller import Market_Controller
from Controllers.Material_Controller import Material_Controller
from Controllers.Product_Controller import Product_Controller


class Game_App(QApplication):
    """Initializes the game app as a QApplication."""

    def __init__(self, sys_argv):
        """Initialize all models, views and controllers."""
        # get path of Main.py script, strip Main.py and use the path as root path
        root_directory = os.path.realpath(__file__)
        self.root_directory = root_directory[:root_directory.find('Main.py')].strip()
        # read standard configuration
        path = os.path.join(self.root_directory, 'Resources','Standard_Config.json')
        self.config = None
        if os.path.exists(path):
            with open(path, encoding='utf-8') as config_file:
                self.config = json.load(config_file)
        else:
            # Exit program, if config file cannot be loaded.
            sys.exit('Error: Configuration File could not be loaded!')

        super(Game_App, self).__init__(sys_argv)
        # initialize game model
        self.model_capital = Capital(self.config['Capital'])
        self.model_layout = self.create_layouts(self.config['Layout'])
        self.model_factory = Factory(self.config['Factory'], self.config['Layout'], self.model_layout)
        self.model_market = Market(self.config['Market'])
        self.model_material = self.create_materials(self.config['Material'])
        self.model_product = self.create_products(self.model_material, self.config['Product'])
        # initialize game controler
        self.layout_controller = Layout_Controller(self.model_layout)
        self.material_controller = Material_Controller(self.model_material)
        self.product_controller = Product_Controller(self.model_product)
        self.main_controller = Main_Controller(self.model_capital, self.model_factory, self.model_market, self.product_controller, self.layout_controller, self.root_directory)
        # initialize game views
        self.market_view = Market_View(self.model_capital, self.model_market, self.model_product, self.model_material, self.main_controller, self.product_controller, self.material_controller)
        self.factory_view = Factory_View(self.model_factory, self.model_product, self.model_material, self.layout_controller, self.material_controller, self.product_controller, self.root_directory)
        self.product_view = Product_View(self.model_product, self.product_controller, self.root_directory)
        self.capital_view = Capital_View(self.model_capital)
        self.summary_view = Summary_View(self.model_capital, self.model_factory, self.model_market, self.model_product, self.root_directory)
        self.main_view = Main_View(self.model_capital, self.model_factory, self.model_market, self.main_controller, self.factory_view, self.market_view, self.product_view, 
            self.capital_view, self.summary_view, self.root_directory)

        # show main window
        self.main_view.show()

    def create_layouts(self, config):
        """Create the starter layouts. returns a list of these layouts."""
        lay_list = []
        for layout in config:
            if config[layout]['init_number'] > 0:
                for i in range(config[layout]['init_number']):
                    layout_constructor = globals()[layout]
                    lay_list.append(layout_constructor(config[layout]))
        return lay_list

    def create_materials(self, config):
        """Create the starker materials. returns a list of these materials."""
        mat_list = []
        for mat in config:
            # call the material constructor out of the global list, with the names from the config file
            material_constructor = globals()[mat]
            mat_list.append(material_constructor(config[mat]))
        return mat_list

    def create_products(self, material_list, config):
        """Create the starker products. returns a list of these products."""
        prod_list = []
        for prod in config:
            # call the product constructor out of the global list, with the names from the config file
            product_Constructor = globals()[prod]
            prod_list.append(product_Constructor(config[f'{prod}'], material_list))
        prod_list[0].is_active = True
        return prod_list


if __name__ == '__main__':
    # start the game!
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"  # counters the viscious windows dpi scaling! 15" monitor is minimally recommended.
    app = Game_App(sys.argv)
    tutorial = app.main_controller.ask_yes_or_no('Welome Player!', f'Do you want to play with help from the tutorial in the first turns?')
    if tutorial:
        app.main_controller.tutorial_flag = True 
        app.main_controller.open_tutorial_pdfs(0)
    else:
        app.main_controller.tutorial_flag = False
    sys.exit(app.exec_())
