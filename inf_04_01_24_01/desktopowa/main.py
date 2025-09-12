from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QLineEdit,
    QRadioButton,
    QGroupBox,
    QLabel,
    QWidget,
    QFormLayout,
    QFrame
)
from PyQt6.QtGui import QPixmap
import sys


class MainWindow(QMainWindow):
    def init_ui(self):
        self.setGeometry(50, 50, 1000, 500)
        self.setWindowTitle("Wprowadzenie danych do paszportu. Wykonał: 00000000000")
        self.setStyleSheet("""
        QMainWindow {
            background-color: #5F9EA0;
        }
        QLineEdit, QPushButton {
            background-color: #F0FFFF;
        }
        """)

        # Personal data section 

        personal_data_fr = QFrame(self)
        personal_data_fr.setGeometry(50, 25, 400, 100)
        personal_data_fr.setStyleSheet("""
        QLineEdit {
            margin-left: 50;
        }
        """)
        personal_data_layout = QFormLayout(personal_data_fr)

        self.number_le = QLineEdit()
        self.first_name_le = QLineEdit()
        self.last_name_le = QLineEdit()

        personal_data_layout.addRow("Numer", self.number_le)
        personal_data_layout.addWidget(QWidget())
        personal_data_layout.addRow("Imię", self.first_name_le)
        personal_data_layout.addWidget(QWidget())
        personal_data_layout.addRow("Nazwisko", self.last_name_le)

        personal_data_fr.setLayout(personal_data_layout)


        # Eye colour section
        
        eye_colour_gb = QGroupBox("Kolor Oczu", self)
        eye_colour_gb.setGeometry(50, 150, 400, 140)
        eye_colour_gb.setStyleSheet("""
        QGroupBox {
            border: 3px solid #F0FFFF;
            border-radius: 3px;
        }
        QGroupBox::title {
            padding: 2px 2px;
            left: 10;
        }
        QRadioButton {
        margin-left: 20;
        }
        """)
        eye_colour_layout = QFormLayout(eye_colour_gb)

        blue_rd = QRadioButton('niebieskie')
        blue_rd.setChecked(True)
        green_rd = QRadioButton('zielone')
        brown_rd = QRadioButton('piwne')

        eye_colour_layout.addRow(blue_rd)
        eye_colour_layout.addRow(QWidget())
        eye_colour_layout.addRow(green_rd)
        eye_colour_layout.addRow(QWidget())
        eye_colour_layout.addRow(brown_rd)


        self.person_label = QLabel(self)
        self.person_label.setScaledContents(True)
        self.person_label.setGeometry(500, 35, 195 , 225)
        self.person_label.setPixmap(QPixmap("000-zdjecie.jpg"))


        self.fingerprint_label = QLabel(self)
        self.fingerprint_label.setScaledContents(True)
        self.fingerprint_label.setGeometry(750, 35, 150 , 225)
        self.fingerprint_label.setPixmap(QPixmap("000-odcisk.jpg"))

        # Submit button

        ok_btn = QPushButton("OK", self)
        ok_btn.setGeometry(600, 300, 300, 40)

    def __init__(self):
        super().__init__()
        self.init_ui()


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
