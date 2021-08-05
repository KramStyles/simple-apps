from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QStyleFactory
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QContextMenuEvent

import sys


class widget(QMainWindow):
    def __init__(self):
        super(widget, self).__init__()

        self.set_up()
        self.show()

    def set_up(self):
        self.windowTitleChanged.connect(self.onWindowChanged)
        self.windowTitleChanged.connect(self.custom_fn)
        self.windowTitleChanged.connect(lambda m: self.custom_fn(a='Chimere'))

        self.setWindowTitle('Hello From Head')
        label = QLabel("This is awesome!!!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

    # def contextMenuEvent(self, event: QContextMenuEvent) -> None:
    #     print('This prints this statement and still runs the context menu')  
    #     return super().contextMenuEvent(event)

    def contextMenuEvent(self, event):
        print('Context menu Called up')
        return super(widget, self).contextMenuEvent(event)

    def onWindowChanged(self, title):
        print(title)
        # This prints the window title. it accepts a string

    def custom_fn(self, a="Michael", b="Time to go"):
        print(a, b)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    # print(QStyleFactory.keys())
    app.setStyle('Fusion')
    win = widget()
    sys.exit(app.exec_())
