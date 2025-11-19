from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QMessageBox
import sys
import random
from PyQt6.QtCore import QTimer, Qt, QSize
from PyQt6.QtGui import QIcon


GAME_TIME = 30
TILE_SIZE = 125


class TileButton(QPushButton):
    def __init__(self, parent, memory_card_image):
        super().__init__(parent)
        self.is_up = False
        self.setStyleSheet("background-color: #d8dee9")
        self.memory_card_image = memory_card_image
        self.setIcon(QIcon("./images/default.jpg"))
        self.setIconSize(QSize(TILE_SIZE, TILE_SIZE))

    def turn_up(self):
        self.is_up = True
        self.setIcon(QIcon(self.memory_card_image))

    def turn_down(self):
        self.is_up = False
        self.setStyleSheet("background-color: #d8dee9")
        self.setIcon(QIcon("./images/default.jpg"))


memory_images = [
    "./images/cantors_set.jpg",
    "./images/dragon_curve.jpg",
    "./images/fractal_tree.jpg",
    "./images/kochs_curve.jpg",
    "./images/sierpinsis_triangle.jpg",
    "./images/sierpinskis_carpet.jpg",
]

memory_images = memory_images + memory_images
random.shuffle(memory_images)


class MainWindow(QMainWindow):
    def set_time_left(self):
        self.timer_label.setText(f"Time left: {round(self.time_left, 2)}s")

    def handle_timer_tick(self):
        if self.is_timer_blocked or not self.first_click_happened:
            return

        if self.time_left > 0:
            self.time_left -= 0.01
            self.set_time_left()
            self.game_timer.start(10)
        else:
            self.inform_user(False)
            self.reset_game()

    def reset_game(self):
        self.status_label.setText("Mismatched 0 times")
        self.timer_label.setText(f"Time left: {GAME_TIME}s")
        self.first_click_happened = False
        self.curr_up_tile = None
        self.num_of_missmatches = 0
        self.tiles_blocked = False
        self.time_left = GAME_TIME
        self.is_timer_blocked = False
        self.game_timer.start(10)
        for tile in self.tiles:
            tile.turn_down()

        random.shuffle(memory_images)

        for i in range(3):
            for j in range(4):
                self.tiles[i * 4 + j].memory_card_image = memory_images[i * 4 + j]

    def is_game_won(self):
        for tile in self.tiles:
            if not tile.is_up:
                return False
        return True

    def inform_user(self, is_positive=True):
        message = QMessageBox()
        message.setText(
            (
                "Khhh, gratulacje, może policzysz teraz całki?"
                if is_positive
                else "Jak ty tego nie wygrałeś, przecież to jest trywialne?"
            )
            + f"\nIlość prób nietrafionych: {self.num_of_missmatches}"
        )
        message.exec()

    def flip_in_time(self, first_idx, second_idx, time_period):
        def do_flip():
            self.tiles[first_idx].turn_down()
            self.tiles[second_idx].turn_down()
            self.tiles_blocked = False

        QTimer.singleShot(time_period * 1000, do_flip)

    def handle_click(self, button_index):
        if not self.first_click_happened:
            self.first_click_happened = True
            self.game_timer.start(10)

        if self.tiles[button_index].is_up or self.tiles_blocked:
            return
        self.tiles[button_index].turn_up()

        if self.curr_up_tile is not None:
            if (
                self.tiles[button_index].memory_card_image
                != self.tiles[self.curr_up_tile].memory_card_image
            ):
                self.tiles_blocked = True
                self.num_of_missmatches += 1
                self.status_label.setText(f"Mismatched {self.num_of_missmatches} times")
                first = button_index
                second = self.curr_up_tile
                self.flip_in_time(first, second, 1)
            else:
                if self.is_game_won():
                    self.is_timer_blocked = True
                    self.inform_user(True)
                    self.reset_game()
            self.curr_up_tile = None

        else:
            self.curr_up_tile = button_index

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 700, 700)
        self.setStyleSheet("""
#timer, #status{
    font-size: 20px;
}
#timer{
    font-weight: bold;
}
QMainWindow{
    background-color: #2e3440;
    color: #eceff4;
}
QLabel{
    color: #eceff4;
}
QPushButton{
    background-color: #d8dee9;
    color: #3b4252;
}
""")
        self.first_click_happened = False
        self.is_timer_blocked = False
        self.time_left = GAME_TIME
        self.curr_up_tile = None
        self.num_of_missmatches = 0
        self.tiles_blocked = False

        self.restart_button = QPushButton("Restart", self)
        self.restart_button.setGeometry(10, 590, 150, 100)
        self.restart_button.clicked.connect(self.reset_game)

        self.status_label = QLabel("Mismatched 0 times", self)
        self.status_label.setGeometry(440, 625, 250, 150)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.status_label.setObjectName("status")

        self.timer_label = QLabel(self)
        self.set_time_left()
        self.timer_label.setGeometry(10, 10, 200, 50)
        self.timer_label.setObjectName("timer")
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.game_timer = QTimer()
        self.game_timer.start(10)
        self.game_timer.timeout.connect(self.handle_timer_tick)

        self.tiles: list[TileButton] = []

        for i in range(3):
            for j in range(4):
                self.tiles.append(TileButton(self, memory_images[i * 4 + j]))
                self.tiles[-1].setGeometry(
                    90 + j * (TILE_SIZE + 5),
                    i * (TILE_SIZE + 5) + 90,
                    TILE_SIZE,
                    TILE_SIZE,
                )
                self.tiles[-1].clicked.connect(
                    lambda _, index=(i * 4 + j): self.handle_click(index)
                )


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
