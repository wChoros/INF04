from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QRadioButton,
    QGroupBox,
    QFormLayout,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
    QMessageBox,
)
from PyQt6.QtGui import QPixmap
import sys
import os


class MainWindow(QMainWindow):
    def check_price(self):
        if self.postcard.isChecked():
            self.price_lbl.setText("Cena: 1 zł")
            self.image_lbl.setPixmap(
                QPixmap(str(os.path.join(os.path.dirname(__file__), "pocztowka.png")))
            )
        if self.letter.isChecked():
            self.price_lbl.setText("Cena: 1,5 zł")
            self.image_lbl.setPixmap(
                QPixmap(str(os.path.join(os.path.dirname(__file__), "list.png")))
            )
        if self.package.isChecked():
            self.price_lbl.setText("Cena: 10 zł")
            self.image_lbl.setPixmap(
                QPixmap(str(os.path.join(os.path.dirname(__file__), "paczka.png")))
            )

    def check_postal_code(self):
        msg = QMessageBox()
        are_all_numbers = True
        for letter in self.postal_code_le.text():
            if letter not in "123456789":
                are_all_numbers = False

        if not are_all_numbers:
            msg.setText("Kod pocztowy powinien się składać z samych cyfr")
            msg.setStandardButtons(QMessageBox.StandardButton.Close)

        elif len(self.postal_code_le.text()) != 5:
            msg.setText("Nieprawidłowa liczba cyfr w kodzie pocztowym")
            msg.setStandardButtons(QMessageBox.StandardButton.Close)

        else:
            msg.setText("Dane przesyłki zostały wprowadzone")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)

        msg.exec()

    def initUI(self):
        # Main Window section
        self.setWindowTitle("Nadaj Przesyłkę, PESEL: 00000000000")
        self.setGeometry(500, 500, 750, 350)
        self.setStyleSheet("""
        QGroupBox{
            border: 1px solid lightGray;
            border-radius: 3px;
        }
        """)

        # Delivery Section

        delivery_gb = QGroupBox("Rodzaj przesyłki", self)
        delivery_gb_layout = QFormLayout(delivery_gb)

        delivery_gb.setGeometry(50, 25, 200, 100)

        self.postcard = QRadioButton("Pocztówka")
        self.postcard.setChecked(True)
        self.letter = QRadioButton("List")
        self.package = QRadioButton("Paczka")

        delivery_gb_layout.addRow(QWidget())
        delivery_gb_layout.addRow(self.postcard)
        delivery_gb_layout.addRow(self.letter)
        delivery_gb_layout.addRow(self.package)

        delivery_gb.setLayout(delivery_gb_layout)

        check_price_btn = QPushButton("Sprawdź Cenę", self)
        check_price_btn.setGeometry(50, 135, 200, 25)
        check_price_btn.clicked.connect(self.check_price)

        self.image_lbl = QLabel(self)
        self.image_lbl.setPixmap(
            QPixmap(str(os.path.join(os.path.dirname(__file__), "pocztowka.png")))
        )
        self.image_lbl.setGeometry(50, 175, 100, 63)

        self.price_lbl = QLabel("Cena: 1 zł", self)
        self.price_lbl.setGeometry(175, 175, 125, 50)
        self.price_lbl.setObjectName("PriceLbl")
        self.price_lbl.setStyleSheet("""
        #PriceLbl {
            font-size: 18px;
            font-weight: bold;
        }
        """)

        # Address section

        address_gb = QGroupBox("Dane Adresowe", self)
        address_gb.setGeometry(350, 25, 350, 200)

        self.street_le = QLineEdit()
        self.postal_code_le = QLineEdit()
        self.city_le = QLineEdit()

        address_gb_layout = QFormLayout()

        address_gb_layout.addRow(QWidget())
        address_gb_layout.addRow(QWidget())
        address_gb_layout.addRow("Ulica z numerem", QWidget())
        address_gb_layout.addRow(self.street_le)
        address_gb_layout.addRow("Kod Pocztowy", QWidget())
        address_gb_layout.addRow(self.postal_code_le, QWidget())
        address_gb_layout.addRow("Miasto", QWidget())
        address_gb_layout.addRow(self.city_le)

        address_gb.setLayout(address_gb_layout)

        ## Submit Button

        submit_btn = QPushButton("Zatwierdź", self)
        submit_btn.setGeometry(50, 260, 650, 30)
        submit_btn.clicked.connect(self.check_postal_code)

    def __init__(self):
        super().__init__()
        self.initUI()


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
