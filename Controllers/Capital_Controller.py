from PyQt5.QtCore import QObject, pyqtSlot

class Capital_Controller(QObject):
    """description of class"""

    def __init__(self, cap_model):
        super().__init__()

        self._model_capital = cap_model
    

    @pyqtSlot(int)
    def subtract(self, number):
        cap = self._model_capital.amount
        cap -= round(number, 2)
        self._model_capital.amount = cap
        self._model_capital.total_cost_archive(round(number, 2))

    @pyqtSlot(int)
    def add(self, number):
        self.amount += round(number, 2)
        self.total_income_archive.append(number)
        