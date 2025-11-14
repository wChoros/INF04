from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QMessageBox
import sys
import random
from PyQt6.QtCore import QTimer, Qt


GAME_TIME = 30
TILE_SIZE = 125

class TileButton(QPushButton):
    def __init__(self, parent, memory_card_color):
        super().__init__(parent)
        self.is_up = False
        self.setStyleSheet("background-color: #d8dee9")
        self.memory_card_color = memory_card_color

    def turn_up(self):
        self.is_up = True
        self.setStyleSheet(f"background-color: {self.memory_card_color}")

    def turn_down(self):
        self.is_up = False
        self.setStyleSheet("background-color: #d8dee9")


memory_colors = [
    "#bf616a",
    "#d08770",
    "#ebcb8b",
    "#a3be8c",
    "#b48ead",
    "#88c0d0",
]

memory_colors = memory_colors + memory_colors
random.shuffle(memory_colors)


class MainWindow(QMainWindow):
    def set_time_left(self):
        self.timer_label.setText(f"Time left: {round(self.time_left,2)}s")

    def handle_timer_tick(self):
        if self.is_timer_blocked:
            return

        if self.time_left > 0:
            self.time_left -= 0.01
            self.set_time_left()
            self.game_timer.start(10)
        else:
            self.inform_user(False)
            self.reset_game()

    def reset_game(self):
        self.curr_up_tile = None
        self.num_of_missmatches = 0
        self.tiles_blocked = False
        self.time_left = GAME_TIME
        self.is_timer_blocked = False
        self.game_timer.start(10)
        self.status_label.setText("Mismatched 0 times")
        for tile in self.tiles:
            tile.turn_down()

        random.shuffle(memory_colors)

        for i in range(3):
            for j in range(4):
                self.tiles[i * 4 + j].memory_card_color = memory_colors[i * 4 + j]

    def is_game_won(self):
        for tile in self.tiles:
            if not tile.is_up:
                return False
        return True

    def inform_user(self, is_positive=True):
        message = QMessageBox()
        message.setText(
            (
                "Congrats, u won."
                if is_positive
                else "Stupid looser, you cant win the chilish game xd."
            )
            + f"\nNum of missmatches: {self.num_of_missmatches}"
        )
        message.exec()

    def flip_in_time(self, first_idx, second_idx, time_period):
        def do_flip():
            self.tiles[first_idx].turn_down()
            self.tiles[second_idx].turn_down()
            self.tiles_blocked = False

        QTimer.singleShot(time_period * 1000, do_flip)

    def handle_click(self, button_index):
        if self.tiles[button_index].is_up or self.tiles_blocked:
            return
        self.tiles[button_index].turn_up()

        if self.curr_up_tile is not None:
            if (
                self.tiles[button_index].memory_card_color
                != self.tiles[self.curr_up_tile].memory_card_color
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
        self.is_timer_blocked = False
        self.time_left = GAME_TIME
        self.curr_up_tile = None
        self.num_of_missmatches = 0
        self.tiles_blocked = False

        self.restart_button = QPushButton("Restart", self)
        self.restart_button.setGeometry(10, 590, 150,100)
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
                self.tiles.append(TileButton(self, memory_colors[i * 4 + j]))
                self.tiles[-1].setGeometry(90 + j * (TILE_SIZE+5), i * (TILE_SIZE+5) + 90, TILE_SIZE, TILE_SIZE)
                self.tiles[-1].clicked.connect(
                    lambda _, index=(i * 4 + j): self.handle_click(index)
                )


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
