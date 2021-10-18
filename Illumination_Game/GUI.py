
#from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt
from Illumination_Game import *

MAIN_WINDOW_WITH = 1200
MAIN_WINDOW_HEIGHT = 960
BUTTON_WITH = 280
BUTTON_HEIGHT = 60
BUTTON_X_MAX = 900
BUTTON_Y_MIN = 0
MAIN_LABEL_HEIGHT = 500

class GUI(QWidget):
    """GUI initiates the main window and any features on it. It relies on PyQT5 features, that
    were hand picked for the game."""

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        #adding main panel buttons
        secondButton = GUI.add_button(self, 'Forecast', BUTTON_HEIGHT * 2)
        self.button_end_turn = GUI.add_button(self, 'End Turn', 0)
        self.button_end_turn.clicked.connect(end_turn_clicked)

        #add main info panel in top left corner
        self.main_label = QLabel(self)
        self.main_label.setGeometry(0, 0, BUTTON_WITH, MAIN_LABEL_HEIGHT)

        self.setFixedSize(MAIN_WINDOW_WITH, MAIN_WINDOW_HEIGHT)
        self.setWindowTitle('Illumination Game')

    def add_button(self, name, x_offset, y_offset = 0):
        """name: text on button, x_offset: offset in -x direction in pixels, y_offset: offset in +y direction in pixels"""
        button = QPushButton(self)
        button.setText(name)
        button.setGeometry(BUTTON_Y_MIN - y_offset, BUTTON_X_MAX - x_offset, BUTTON_WITH, BUTTON_HEIGHT)
        return button
        


def initialize_product(prodName, initAmount):
    return Product(prodName, initAmount)

    
def start_gui():
    app = QApplication(sys.argv)
    gui = GUI()
    return app, gui
