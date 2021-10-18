"""https://namingconvention.org/python/
https://doc.qt.io/qtforpython-5/"""

import sys
from Capital import *
from GUI import *
from Layout import *
from Market import *
from Material import *
from Product import *


capital = Capital()
starter_layout = FixedPositionLayout("Fixed Position Layout", 30, 0.2)
bulb = Product('Light Bulb', 100, 5/60, 3.8)

def end_turn_clicked():
    calculate_production()
    update_main_label()
    print(bulb.productName, bulb.getProductAmount(), sep=': ')


def calculate_production():
    new_products = starter_layout.calculate_time_unit_capacity(bulb.production_time)
    sales = new_products * 0.8
    bulb.addProduct(new_products - sales)
    capital.add(sales * bulb.base_value)


def update_main_label():
    main_gui.main_label.setText(str(capital.amount))


if __name__ == '__main__':
    app, main_gui = start_gui()
    main_gui.main_label.setText(str(capital.amount))
    main_gui.show()

    sys.exit(app.exec_())
    
