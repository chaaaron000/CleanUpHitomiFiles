import sys
from clean import clean_up
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QLabel, QGridLayout, QFileDialog, QMessageBox


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
        first_path_button = QPushButton("...", self)
        first_path_button.clicked.connect(
            self.get_path)
        self.first_label = QLabel("다운받은 폴더가 있는 디렉토리를 선택해주세요.", self)
        second_path_button = QPushButton("...", self)
        second_path_button.clicked.connect(self.get_path)
        self.second_label = QLabel("분류한 폴더를 저장할 디렉토리를 선택해주세요.", self)
        clean_button = QPushButton("Clean Up", self)
        clean_button.clicked.connect(self.clean)
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Error")
        self.msg.setText("경로를 선택해주세요!")

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.first_label, 0, 0)
        grid.addWidget(first_path_button, 0, 1)
        grid.addWidget(self.second_label, 1, 0)
        grid.addWidget(second_path_button, 1, 1)
        grid.addWidget(clean_button, 3, 0)

    def get_path(self):
        result = str(QFileDialog.getExistingDirectory())
        print(result)
        return result

    def clean(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyApp()
    sys.exit(app.exec_())
