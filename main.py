import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_app()

    def init_app(self):
        self.setWindowTitle("Clean Up Hitomi Files")
        self.resize(500, 500)
        self.init_position()
        self.init_Ui()
        self.show()

    def init_position(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_Ui(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyApp()
    sys.exit(app.exec_())
