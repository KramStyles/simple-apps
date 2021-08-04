from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

import sys

class widget(QWidget):
    def __init__(self):
        super(widget, self).__init__()
        self.setWindowTitle('Hello From Head')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyle('')
    win = widget()
    sys.exit(app.exec_())
