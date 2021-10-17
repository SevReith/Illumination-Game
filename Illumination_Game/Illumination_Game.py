"""https://namingconvention.org/python/
https://doc.qt.io/qtforpython-5/"""


from Layout import *
from GUI import *
from Market import *
from Material import *
from Product import *

global lightBulb

if __name__ == '__main__':
    lightBulb = Product('Light Bulb', 100)
    runGUI()
