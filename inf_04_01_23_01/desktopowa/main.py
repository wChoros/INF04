from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QComboBox,
    QLineEdit,
    QFormLayout,
    QCheckBox,
    QSpinBox,
    QPushButton,
    QGroupBox,
    QMessageBox,
)
import sys
import random


def generate_password(num_of_chars, letters, numbers, specials):
    output = ""

    letter_chars = "qwertyuiopasdfghjklzxcvbnm"
    special_chars = "!@#$%^&*()_+-="

    for i in range(num_of_chars):
        if i == 0 and letters:
            output += letter_chars[random.randint(0, len(letter_chars) - 1)].upper()
        elif i == 1 and numbers:
            output += str(random.randint(0, 9))
        elif i == 2 and specials:
            output += special_chars[random.randint(0, len(special_chars) - 1)].upper()
        else:
            output += letter_chars[random.randint(0, len(letter_chars) - 1)]

    return output


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.password = ""

    def show_generated_password(self):
        self.password = generate_password(
            int(self.chars_spinbox.text()),
            self.letters_checkbox.isChecked(),
            self.numbers_checkbox.isChecked(),
            self.special_checkbox.isChecked(),
        )

        msg = QMessageBox()
        msg.setText(self.password)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def show_user_data(self):
        message = f"Dane pracownika: {self.first_name_line_edit.text()} {self.last_name_line_edit.text()}, {self.position_combo_box.currentText()} Hasło: {self.password}"
        msg = QMessageBox()
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def init_ui(self):
        self.setWindowTitle("Dodaj Pracownika")
        self.setGeometry(0, 0, 1000, 400)
        self.setStyleSheet("""
                           
        QMainWindow{
            background-color: #B0C4DE;
        }

        QGroupBox {
            border: 4px solid white;
            border-radius: 8px;
        }
                           
        QPushButton {
            border: 1px solid white;
            color:5 white;
            background-color: #4682B4;     
        }

        QLineEdit {
            margin-top: 10px;          
        }
                           
        QSpinBox {
            margin-top: 10px;          
        }
        """)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.left_form = QGroupBox("Dane pracownika", self.central_widget)
        self.left_form.setObjectName("leftForm")
        self.left_form_layout = QFormLayout()

        self.first_name_label = QLabel("Imię")
        self.last_name_label = QLabel("Nazwisko")
        self.position_label = QLabel("Stanowisko")

        self.first_name_line_edit = QLineEdit()
        self.last_name_line_edit = QLineEdit()
        self.position_combo_box = QComboBox()

        self.position_combo_box.addItems(
            ["Kierownik", "Starszy programista", "Młodszy programista", "Tester"]
        )

        self.position_combo_box.setStyleSheet("""

    margin-top: 10px;
""")

        self.left_form_layout.addRow(self.first_name_label, self.first_name_line_edit)
        self.left_form_layout.addRow(self.last_name_label, self.last_name_line_edit)
        self.left_form_layout.addRow(self.position_label, self.position_combo_box)

        self.left_form.setGeometry(50, 50, 300, 200)

        self.left_form.setLayout(self.left_form_layout)

        self.right_form = QGroupBox("Generowanie hasła", self.central_widget)
        self.right_form.setObjectName("rightForm")

        self.right_form_layout = QFormLayout()

        self.chars_spinbox = QSpinBox()
        self.letters_checkbox = QCheckBox()
        self.numbers_checkbox = QCheckBox()
        self.special_checkbox = QCheckBox()
        self.generate_button = QPushButton()
        self.generate_button.setText("Generuj Hasło")
        self.generate_button.setObjectName("generateButton")
        self.generate_button.setStyleSheet("""
#generateButton{
    margin: 0 70px;
}""")

        self.generate_button.clicked.connect(self.show_generated_password)

        self.letters_checkbox.setChecked(True)

        self.right_form_layout.addRow("Ile Znaków?", self.chars_spinbox)
        self.right_form_layout.addRow("Małe i wielkie litery", self.letters_checkbox)
        self.right_form_layout.addRow("Cyfry", self.numbers_checkbox)
        self.right_form_layout.addRow("Znaki specjalne", self.special_checkbox)
        self.right_form_layout.addRow(self.generate_button)

        self.right_form.setLayout(self.right_form_layout)

        self.right_form.setGeometry(400, 50, 300, 200)

        self.submit_button = QPushButton(self.central_widget)

        self.submit_button.setGeometry(250, 275, 250, 30)

        self.submit_button.setText("Zatwierdź")
        self.submit_button.clicked.connect(self.show_user_data)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
