from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QComboBox, QMessageBox
from PyQt6.QtCore import Qt
import sys
import random


class MainWindow(QMainWindow):
    def switch_bit(self, bit_position):
        self.bit_values[bit_position] = not self.bit_values[bit_position]
        self.sum_bits()

    def sum_bits(self):
        value = 0
        for i, is_active in enumerate(self.bit_values):
            value += pow(2, i) if is_active else 0

        self.curr_number = value
        self.total_label.setText(f"Total: {self.curr_number}")
        self.check_for_win()

    def check_for_win(self):
        if self.curr_number == self.target_number:
            message_box = QMessageBox(
                QMessageBox.Icon.NoIcon, "", "Correct! Well done, Now try another"
            )
            message_box.exec()
            self.reset_game()

    def reset_game(self):
        self.curr_number = 0
        self.target_number = random.randint(0, 510)
        self.bit_values = [False for _ in range(9)]

        for bit_combo in self.bit_combos:
            bit_combo.blockSignals(True)
            bit_combo.setCurrentText("0")
            bit_combo.blockSignals(False)

        self.what_is_label.setText(f"What is - {self.target_number} - in Binary?")
        self.total_label.setText(f"Total: {self.curr_number}")

        self.check_for_win()

    def __init__(self):
        super().__init__()
        self.target_number = random.randint(0, 510)
        self.curr_number = 0
        self.setStyleSheet("""
QMainWindow{
    background-color: #2b2b2b;
}
QLabel{
    font-size: 35px;
}
#title{
    color: white;
}
#whatis{
    color: green;
}
#total{
    color: white;
}
""")
        self.setWindowTitle("Binary Calculator")
        self.setGeometry(50, 50, 900, 600)
        title = QLabel("Binary Calculator Game", self)
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setGeometry(self.width() // 2 - 200, 20, 400, 100)
        self.what_is_label = QLabel(
            f"What is - {self.target_number} - in Binary?", self
        )
        self.what_is_label.setObjectName("whatis")
        self.what_is_label.setGeometry(self.width() // 2 - 200, 200, 400, 100)
        self.what_is_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.total_label = QLabel("Total: 0", self)
        self.total_label.setObjectName("total")
        self.total_label.setGeometry(self.width() // 2 - 200, 250, 400, 100)
        self.total_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        colors = [
            "#8b7b87",
            "#978ba0",
            "#9d9d91",
            "#a39787",
            "#958f8a",
            "#aa9b84",
            "#96a083",
            "#987f94",
            "#aa85a8",
        ]

        self.bit_combos = []
        self.bit_values = [False for _ in range(9)]
        for i in range(9):
            bit_label = QLabel(str(pow(2, 8 - i)), self)
            bit_label.setGeometry(50 + (i * 90), 110, 75, 45)
            bit_label.setStyleSheet(f"background-color: {colors[i]};")
            bit_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            self.bit_combos.insert(0, QComboBox(self))
            self.bit_combos[0].addItems(["0", "1"])
            self.bit_combos[0].setGeometry(50 + (i * 90), 160, 75, 45)
            self.bit_combos[0].setStyleSheet(f"background-color: {colors[i]};")
            self.bit_combos[0].currentTextChanged.connect(
                lambda x, pos=(8 - i): self.switch_bit(pos)
            )

        self.check_for_win()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
