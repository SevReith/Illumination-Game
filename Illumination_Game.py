"""https://namingconvention.org/python/
https://doc.qt.io/qtforpython-5/"""

import sys
from Capital import *
from GUI import *


if __name__ == '__main__':
    #starts the game!
    app, main_gui = start_gui()
    main_gui.show()
    main_gui.update_main_label()
    sys.exit(app.exec_())