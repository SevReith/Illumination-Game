import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

class Mpl_Canvas(FigureCanvas):
    """Matplotlib canvas container."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(Mpl_Canvas, self).__init__(self.fig)

    def plot_simple_graph(self, x_axis, y_axis, title:str ="", x_title:str ="", y_title:str =""):
        """Clear canvas, then plot x and y axes. x_axis and y_axis must be float arrays of the same size.
        Titles are for plot and axes are optional."""
        try:
            self.axes.clear()
        except AttributeError: 
            pass
        self.axes.plot(x_axis, y_axis)
        self.axes.set_title(title)
        self.axes.set_xlabel(x_title)
        self.axes.set_ylabel(y_title)
        self.draw()
