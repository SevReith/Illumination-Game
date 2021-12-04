from PyQt5.QtCore import QObject, pyqtSlot

class Material_Controller(QObject):
    """description of class"""

    def __init__(self, mat_model):
        super().__init__()

        self._model_material = mat_model
