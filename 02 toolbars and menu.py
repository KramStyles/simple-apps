import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QApplication, QLabel, QMainWindow, QStatusBar, QStyleFactory, QToolBar

class window(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(window, self).__init__(*args, **kwargs)

        self.setWindowTitle('My second window')
        label = QLabel('This is my second awesome trial on apps')
        label.setAlignment(Qt.AlignCenter)

        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        btnAction = QAction('Action Button', self)
        btnAction.setStatusTip('Action button touched')
        btnAction.triggered.connect(self.actionToolbar)
        btnAction.setCheckable(True)
        toolbar.addAction(btnAction)

        self.setCentralWidget(label)
        self.setStatusBar(QStatusBar(self))
        self.show()

    
    def actionToolbar(self, s):
        print(s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    print(QStyleFactory.keys())
    app.setStyle('Fusion')
    win = window()
    sys.exit(app.exec_())