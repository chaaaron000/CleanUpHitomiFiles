from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TestQFileDialog(object):
    def _open_file_dialog(self):  # a function to open the dialog window
        result = str(QtWidgets.QFileDialog.getExistingDirectory())
        print(result)
        return result

    def setupUi(self, TestQFileDialog):
        TestQFileDialog.setObjectName("TestQFileDialog")
        TestQFileDialog.resize(700, 400)

        self.toolButtonOpenDialog = QtWidgets.QToolButton(TestQFileDialog)
        self.toolButtonOpenDialog.setGeometry(QtCore.QRect(620, 10, 50, 20))
        self.toolButtonOpenDialog.setObjectName("toolButtonOpenDialog")
        directory = self.toolButtonOpenDialog.clicked.connect(
            self._open_file_dialog)

        self.lineEdit = QtWidgets.QLineEdit(TestQFileDialog)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 600, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('{}'.format(directory))

        self.retranslateUi(TestQFileDialog)
        QtCore.QMetaObject.connectSlotsByName(TestQFileDialog)

    def retranslateUi(self, TestQFileDialog):
        _translate = QtCore.QCoreApplication.translate
        TestQFileDialog.setWindowTitle(_translate("TestQFileDialog", "Dialog"))
        self.toolButtonOpenDialog.setText(_translate("TestQFileDialog", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TestQFileDialog = QtWidgets.QDialog()
    ui = Ui_TestQFileDialog()
    ui.setupUi(TestQFileDialog)
    TestQFileDialog.show()
    sys.exit(app.exec_())
