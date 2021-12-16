from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from PyQt5.QtCore import QObject, pyqtSlot

class Summary_Controller(QObject):
    """Class to collect and plot all important data from all models."""

    def __init__(self, cap_model, fac_model, mar_model, prod_model, root_directory) -> None:
        super().__init__()

        self._model_capital = cap_model
        self._model_factory = fac_model
        self._model_market = mar_model
        self._model_product = prod_model
        self.root_directory = root_directory

    