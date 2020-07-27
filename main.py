import sys
from clean import clean_up
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QLabel, QGridLayout, QFileDialog, QMessageBox


class MyApp(QWidget):
    TARGET_PATH = ""
    GOAL_PATH = ""

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
        self.first_path_button = QPushButton("...", self)
        self.first_path_button.clicked.connect(self.get_target_path)
        self.first_label = QLabel("다운받은 폴더가 있는 디렉토리를 선택해주세요.", self)
        self.second_path_button = QPushButton("...", self)
        self.second_path_button.clicked.connect(self.get_goal_path)
        self.second_label = QLabel("분류한 폴더를 저장할 디렉토리를 선택해주세요.", self)
        self.clean_button = QPushButton("Clean Up", self)
        self.clean_button.clicked.connect(self.clean)
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Error")
        self.msg.setText("경로를 선택해주세요!")

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.first_label, 0, 0)
        grid.addWidget(self.first_path_button, 0, 1)
        grid.addWidget(self.second_label, 1, 0)
        grid.addWidget(self.second_path_button, 1, 1)
        grid.addWidget(self.clean_button, 3, 0)

    def get_target_path(self):
        self.TARGET_PATH = str(QFileDialog.getExistingDirectory())
        self.first_label.setText(self.TARGET_PATH)

    def get_goal_path(self):
        self.GOAL_PATH = str(QFileDialog.getExistingDirectory())
        self.second_label.setText(self.GOAL_PATH)

    def clean(self):
        if self.TARGET_PATH != "" and self.GOAL_PATH != "":
            clean_up(self.TARGET_PATH, self.GOAL_PATH)
        else:
            self.msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyApp()
    sys.exit(app.exec_())
