from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton, QFileDialog
from PyQt6.QtCore import Qt
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
    font-size: 15px;
}
QLabel{
    font-size: 25px;
    color: #FAEBD7;
}
#encrypted-label{
    font-size: 18px;
    color: black;
    border: 3px solid #FAEBD7;
    border-radius: 25px;
    color: white;
    padding: 20px;
                           
}
QPushButton {
    background-color: #ADD8E6;
}
""")

        self.initUI()

    def encrypt(self):
        try:
            self.encrypted_text_label.setText(cesar_encrypt(self.text_to_encrypt_te.toPlainText(), int(self.key_text_edit.toPlainText())))
        except Exception: 
            pass
    
    def openFileDialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Open File")
        file_dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        selected_files = None
        if file_dialog.exec():
            selected_files = file_dialog.filesSelected
        if selected_files:
            with open(selected_files[0], 'w') as file:
                file.write(self.encrypted_text_label.text())

    def initUI(self):
        label_1 = QLabel("Podaj wartość klucza", self)
        label_1.setGeometry(10, 10, 300, 25)

        self.key_text_edit = QTextEdit(self)
        self.key_text_edit.setGeometry(150, 70, 100, 27)
        self.key_text_edit.setCornerWidget(None)

        label_2 = QLabel("Podaj tekst", self)
        label_2.setGeometry(10, 200, 200, 35)

        self.text_to_encrypt_te = QTextEdit(self)
        self.text_to_encrypt_te.setGeometry(25, 250, 450, 300)


        encrypt_btn = QPushButton("Zaszyfruj" ,self)
        encrypt_btn.setGeometry(530, 400, 70, 25)
        encrypt_btn.clicked.connect(self.encrypt)

        label_3 = QLabel("Tekst Zaszyfrowany", self)
        label_3.setGeometry(650, 10, 300, 25)

        self.encrypted_text_label = QLabel("def", self)
        self.encrypted_text_label.setGeometry(650, 100, 500, 450)
        self.encrypted_text_label.setObjectName("encrypted-label")
        self.encrypted_text_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        save_btn = QPushButton("Zapisz szyfr w pliku",self)
        save_btn.setGeometry(800, 600, 200, 30)
        save_btn.clicked.connect(self.openFileDialog)

        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
