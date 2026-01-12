from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import sys
from random import randint


class MainWindow(QMainWindow):
    def reset_game(self):
        self.this_score = 0
        self.game_score = 0
        for cube in self.cubes:
            cube.setPixmap(QPixmap("./pliki1/question.jpg"))
        self.this_score_lbl.setText("Wynik tego losowania: 0")
        self.game_score_lbl.setText("Wynik gry: 0")

    def throw_cubes(self):
        self.this_score = 0
        for cube in self.cubes:
            throw = randint(1, 6)
            cube.setPixmap(QPixmap(f"./pliki1/k{throw}.jpg"))
            self.this_score += throw
        self.game_score += self.this_score
        self.this_score_lbl.setText(f"Wynik tego losowania: {self.this_score}")
        self.game_score_lbl.setText(f"Wynik gry: {self.game_score}")

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 600, 1000)
        self.setStyleSheet("""
#header {
    background-color: #A52A2A;
    color: white;
    font-size: 35px;
}
QMainWindow {
    background-color: #F5F5DC;
}
QPushButton {
    background-color: #D2691E;
    color: white;
}
""")
        self.game_score = 0
        self.this_score = 0
        self.header_lbl = QLabel("Gra w kości. Autor: 00000000000", self)
        self.header_lbl.setGeometry(0, 0, 600, 100)
        self.header_lbl.setObjectName("header")
        self.header_lbl.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.throw_btn = QPushButton("RZUĆ KOŚĆMI", self)
        self.throw_btn.setGeometry(250, 150, 100, 50)
        self.throw_btn.clicked.connect(self.throw_cubes)

        self.cubes: list[QLabel] = [
            QLabel(self) for _ in range(5)
        ]
        for i, cube in enumerate(self.cubes):
            cube.setPixmap(QPixmap("./pliki1/question.jpg"))
            cube.setScaledContents(True)
            cube.setGeometry(150 + (i*60), 250, 50, 50)

        self.this_score_lbl = QLabel("Wynik tego losowania: 0", self)
        self.this_score_lbl.setGeometry(200, 300, 200, 50)
        self.this_score_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.game_score_lbl = QLabel("Wynik gry: 0", self)
        self.game_score_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.game_score_lbl.setGeometry(200, 350, 200, 50)

        self.reset_btn = QPushButton("RESETUJ WYNIK", self)
        self.reset_btn.setGeometry(250, 400, 100, 50)
        self.reset_btn.clicked.connect(self.reset_game)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
