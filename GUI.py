from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QInputDialog, QMessageBox, QRadioButton, QLineEdit, QMdiArea, QGridLayout 
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QImage, QPixmap
from Illumination_Game import *
from Capital import *
from Factory import *
from GUI import *
from Layout import *
from Market import *
from Material import *
from Product import *



class GUI(QMainWindow):
    """GUI initiates the main window and any features on it. It also start the game engine."""

    MAIN_WINDOW_WIDTH = 1600
    MAIN_WINDOW_HEIGHT = 900
    BUTTON_WIDTH = 300
    BUTTON_HEIGHT = 60
    BUTTON_X_MAX = 840
    BUTTON_Y_MIN = 0
    MAIN_LABEL_HEIGHT = 300

    def __init__(self):
        super().__init__()
        #initialize core attributes
        self.current_turn = 0
        self.final_turn = 100
        self.capital = None
        self.market = None
        self.factory =  None
        self.product_list = []
        self.material_list = []
        self.panel_list = []
        self.init_gui()

    def init_gui(self):
        #add factory background image
        pixmap_label = QLabel()
        pixmap_label.setAlignment(Qt.AlignRight)
        img = QImage("Factory_old_Top_1300x900.png")
        pixmap = QPixmap(img)
        pixmap_label.setPixmap(pixmap)
        self.setCentralWidget(pixmap_label)

        #assign values to core attributes
        cap, fac, prod, mar = initialize_game_core_components()
        self.capital = cap
        self.factory = fac
        self.product_list.append(prod)
        self.market = mar

        #adding main panel buttons
        self.factory_button = GUI.create_button(self, 'Factory', GUI.BUTTON_HEIGHT * 3)
        self.factory_button.clicked.connect(self.button_factory_clicked)
        self.forecast_button = GUI.create_button(self, 'Forecast', GUI.BUTTON_HEIGHT * 2)
        self.forecast_button.clicked.connect(self.button_forecast_clicked)
        self.button_end_turn = GUI.create_button(self, 'End Turn', 0)
        self.button_end_turn.clicked.connect(self.button_end_turn_clicked)

        #add main info panel in top left corner
        self.main_label = QLabel(self)
        self.main_label.setFont(QFont("Times", 18, QFont.Bold))        
        self.main_label.setGeometry(0, 0, GUI.BUTTON_WIDTH, GUI.MAIN_LABEL_HEIGHT)

        #adding radio buttons on production panel
        self.production_radio_button = GUI.create_radio_button(self, 'Production', 'Production')
        self.production_radio_button.clicked.connect(self.production_button_clicked)
        self.production_radio_button.move(1070, 380)

        self.setFixedSize(GUI.MAIN_WINDOW_WIDTH, GUI.MAIN_WINDOW_HEIGHT)
        self.setWindowTitle('Illumination Game')

        #create sub windows, panels
        self.panel_list.append(GUI.create_panel(self))

    def create_button(self, name, x_offset, y_offset = 0):
        """name: text on button, x_offset: offset in -x direction in pixels, y_offset: offset in +y direction in pixels"""
        button = QPushButton(self)
        button.setText(name)
        button.setGeometry(GUI.BUTTON_Y_MIN - y_offset, GUI.BUTTON_X_MAX - x_offset, GUI.BUTTON_WIDTH, GUI.BUTTON_HEIGHT)
        return button

    def create_radio_button(self, name, text):
        radio_button = QRadioButton(self)
        radio_button.setObjectName(name)
        radio_button.setText(text)
        return radio_button

    def create_panel(self):
        self.panel_list.append(Panel("Production Menu"))

    def calculate_everything(self):
        """any necessary calculation at the end of a turn is made here"""
        total_prod_cap = self.factory.calculate_production(self.product_list[0].production_time)
        new_products = total_prod_cap if not self.product_list[0].production_goal_set else min(total_prod_cap, self.product_list[0].production_goal)
        sales = new_products * self.market.generate_sales_modifier()
        self.product_list[0].add_products(new_products - sales)
        profit = sales * self.product_list[0].base_value
        cost = self.factory.calculate_fixed_cost()
        self.capital.add(profit)   
        self.capital.subtract(cost)
        #debug printer
        print('new_products: %s, \nactual sales: %s, sales modifier: %s, \nProfit: %s, Cost: %s' 
              %(new_products, sales, self.market.sales_modifer, profit, cost))

    def update_main_label(self):
        lbl_text = "Turn " + str(self.current_turn) + " of " + str(self.final_turn) + "\nCapital: " + str(self.capital.amount) + " €"
        self.main_label.setText(lbl_text)

    def button_factory_clicked(self):
        pass

    def button_forecast_clicked(self):
        """shows a message box with the current forecast"""
        forecast = self.market.get_current_forecast()
        title = "This month's forecast: " + str(forecast)
        text = "Of course our sales department is practically unfaillable in it's forecasts!"
        msg_Box = QMessageBox()
        msg_Box.setText(title)
        msg_Box.setInformativeText(text)
        msg_Box.exec()

    def button_end_turn_clicked(self):
        """end the current turn. updates turn counter and calls game update functions"""
        #increment turn by 1
        self.current_turn += 1

        #core game calculations
        self.calculate_everything()
        self.market.generate_sales_forecast(0)

        #resetting values
        self.product_list[0].production_goal_set = False

        #gui updates
        self.update_main_label()

    def production_button_clicked(self):
        self.panel_list[0].show()
        
        #goal, ok = QInputDialog.getText(self, 'Production', 'How many Light bulbs do you want to manufacture?')
        #if ok:
        #    print(str(goal))
        #    self.product_list[0].production_goal_set = True
        #    self.product_list[0].production_goal = int(goal)
        

class Panel(QMdiArea):
    """creates free sub panels above the main window"""

    STANDARD_PANEL_WIDTH = 500
    STANDARD_PANEL_HEIGHT = 500

    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.adjust_size()
        layout = QGridLayout()
        self.lbl = QLabel("Production Layout")
        self.button1 = QPushButton(self)
        self.button1.setText("Test")
        layout.addWidget(self.lbl, 0, 2, 3, 3)
        layout.addWidget(self.button1, 3, 4)
        self.setLayout(layout)

    def adjust_size(self, width = STANDARD_PANEL_WIDTH, height = STANDARD_PANEL_HEIGHT):
        self.resize(width, height)

    def add_label(self, text, width, height):
        pass

   
def initialize_game_core_components():
    """initializes the core objects neccesary for the game start. returns these object in order:
        capital, factory, product, market"""
    capital = Capital()
    starter_layout = Fixed_Position_Layout("Fixed Position Layout")
    factory = Factory("Schulmeisterwerke", starter_layout)
    product = Light_Bulb()
    market = Market()
    market.generate_sales_forecast(0)
    return capital, factory, product, market   

    
def start_gui():
    app = QApplication(sys.argv)
    gui = GUI()
    return app, gui