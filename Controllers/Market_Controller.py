from PyQt5.QtCore import QObject, pyqtSlot

class Market_Controller(QObject):
    """description of class"""

    def __init__(self, mar_mdl):
        super().__init__()

        self._model_marktet = mar_mdl
