from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit
from cesar import cesar_encrypt

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Szyfrowanie. Wykonane przez: 0000000000")
        self.setGeometry(50, 50, 1200, 700)
        self.setStyleSheet("""
QMainWindow{
    background-color: #5F9EA0;
}
""")

        self.initUI()

    def initUI(self):
        label_key_val = QLabel("Podaj wartość klucza", self)
        label_key_val.setGeometry(0, 0, 50, 25)

        key_text_edit = QTextEdit(self)
        key_text_edit.setGeometry(150, 70, 100, 25)
        key_text_edit.setCornerWidget(None)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
