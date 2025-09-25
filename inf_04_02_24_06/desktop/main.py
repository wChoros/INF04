from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QPushButton,
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QSize
import sys


class Song:
    def __init__(
        self,
        author: str = None,
        name: str = None,
        number_of_tracks: int = None,
        year: int = None,
        downloads: int = None,
    ):
        self.author = author
        self.name = name
        self.number_of_tracks = number_of_tracks
        self.year = year
        self.downloads = downloads


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moje dźwięki, Wykonał: 00000000000")
        self.setGeometry(50, 50, 1100, 300)
        self.load_songs()
        self.initUI()

    def set_texts(self):
        self.author_label.setText(self.songs[self.curr_song].author)
        self.name_label.setText(self.songs[self.curr_song].name)
        self.tracks_year_label.setText(
            f"{self.songs[self.curr_song].number_of_tracks} utworów         {self.songs[self.curr_song].year}"
        )
        self.downloads_label.setText(f"{self.songs[self.curr_song].downloads}")

    def increment_number_of_downloads(self):
        self.songs[self.curr_song].downloads += 1
        self.downloads_label.setText(f"{self.songs[self.curr_song].downloads}")

    def switch_to_next_song(self):
        if len(self.songs) - 1 != self.curr_song:
            self.curr_song += 1
        else:
            self.curr_song = 0
        self.set_texts()

    def switch_to_previous_song(self):
        if self.curr_song != 0:
            self.curr_song -= 1
        else:
            self.curr_song = len(self.songs) - 1
        self.set_texts()

    def initUI(self):
        # Main Window
        self.setStyleSheet("""
QMainWindow {
    background-color: #2E8B57;
}

QLabel {
    color: white;
}

QLabel#author {
    font-size: 50px;
}
QLabel#name {
    font-size: 30px;
    font-style: italic;
}

QLabel#tracks_year {
    font-size: 20px;
    color: #61D918;
}
QLabel#downloads {
    font-size: 20px;
    color: #61D918;
}
QPushButton {
    background-color: #61D918;
    font-weight: bold;
    font-size: 20px;
}

""")

        vinyl_pixmap = QPixmap("data/obraz.png")

        self.left_btn = QPushButton(self)
        self.left_btn.setIcon(QIcon("data/obraz3.png"))
        self.left_btn.setObjectName("left_btn")
        self.left_btn.setIconSize(QSize(102, 70))
        self.left_btn.setGeometry(25, self.height() // 2 - 35, 95, 70)
        self.left_btn.clicked.connect(self.switch_to_previous_song)

        self.right_btn = QPushButton(self)
        self.right_btn.setObjectName("right_btn")
        self.right_btn.setIcon(QIcon("data/obraz2.png"))
        self.right_btn.setIconSize(QSize(102, 70))
        self.right_btn.setGeometry(self.width() - 125, self.height() // 2 - 35, 95, 70)
        self.right_btn.clicked.connect(self.switch_to_next_song)

        self.vinyl_img = QLabel(self)
        self.vinyl_img.setPixmap(vinyl_pixmap)
        self.vinyl_img.setGeometry(150, 25, 200, 200)

        self.author_label = QLabel(self.songs[self.curr_song].author, self)
        self.name_label = QLabel(self.songs[self.curr_song].name, self)
        self.tracks_year_label = QLabel(
            f"{self.songs[self.curr_song].number_of_tracks} utworów         {self.songs[self.curr_song].year}",
            self,
        )
        self.downloads_label = QLabel(f"{self.songs[self.curr_song].downloads}", self)

        self.author_label.setGeometry(370, 0, 1000, 150)
        self.author_label.setObjectName("author")
        self.name_label.setGeometry(370, 55, 500, 150)
        self.name_label.setObjectName("name")
        self.tracks_year_label.setGeometry(370, 100, 500, 150)
        self.tracks_year_label.setObjectName("tracks_year")
        self.downloads_label.setGeometry(150, 190, 500, 150)
        self.downloads_label.setObjectName("downloads")

        self.download_btn = QPushButton("Pobierz", self)
        self.download_btn.setGeometry(290, 245, 100, 40)

        self.download_btn.clicked.connect(self.increment_number_of_downloads)

    def load_songs(self):
        self.curr_song = 0
        self.songs = []
        with open("data/Data.txt") as file:
            line = file.readline().strip()
            while line:
                song = Song()
                song.author = line
                song.name = file.readline().strip()
                song.number_of_tracks = file.readline().strip()
                song.year = file.readline().strip()
                song.downloads = int(file.readline().strip())

                self.songs.append(song)

                line = file.readline()
                line = file.readline().strip()


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
