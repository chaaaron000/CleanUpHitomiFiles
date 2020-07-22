import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout, QPushButton


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Clean Up Hitomi Files")
        self.resize(500, 500)

        grid = QGridLayout()

        grid.addWidget(QLabel("히토미 다운로더 저장 폴더:"), 0, 0)
        grid.addWidget(QLabel("저장 폴더:"), 1, 0)
        clean_button = QPushButton("Clean Up")
        grid.addWidget(clean_button, 2, 0)

        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(clean_button)
        # hbox.addStretch(1)

        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)
        # vbox.addStretch(1)

        self.setLayout(grid)
        # self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    hitomi_app = MyApp()
    hitomi_app.show()
    sys.exit(app.exec_())
