from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import Qt

import sys


class widget(QMainWindow):
    def __init__(self):
        super(widget, self).__init__()

        self.set_up()
        self.show()

    def set_up(self):
        self.setWindowTitle('Hello From Head')
        label = QLabel("This is awesome!!!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyle('')
    win = widget()
    sys.exit(app.exec_())
