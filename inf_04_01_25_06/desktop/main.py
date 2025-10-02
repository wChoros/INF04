from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QWidget,
    QSlider,
    QPushButton,
)
from PyQt6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        (super().__init__(),)
        self.setGeometry(50, 50, 1000, 500)
        self.setStyleSheet("""
#color_widget {
    background-color: white;
}
QMainWindow {
    background-color: #FFF8DC;
}
#download_button {
    background-color: #CD853F;
}
#download_label {
    background-color: #FFFFFF;
}
""")
        self.initUI()

    def display_colors(self):
        red = str(self.red_slider.value())
        green = str(self.green_slider.value())
        blue = str(self.blue_slider.value())

        self.r_value_label.setText(red)
        self.g_value_label.setText(green)
        self.b_value_label.setText(blue)

        self.color_widget.setStyleSheet(
            """
#color_widget {
    background-color: """
            + f"rgb({self.red_slider.value()}, {self.green_slider.value()}, {self.blue_slider.value()})"
            + "}"
        )

    def download_colors(self):
        red = str(self.red_slider.value())
        green = str(self.green_slider.value())
        blue = str(self.blue_slider.value())

        self.download_label.setStyleSheet(
            """
#download_label {
    background-color: """
            + f"rgb({red}, {green}, {blue})"
            + """
}
"""
        )
        self.download_label.setText(f"{red}, {green}, {blue}")

    def initUI(self):
        self.color_widget = QWidget(self)
        self.color_widget.setObjectName("color_widget")
        self.color_widget.setGeometry(25, 10, self.width() - 50, 40)

        label = QLabel("Dobierz kolor suwakami i zapisz przyciskiem", self)
        label.setGeometry(25, 60, 200, 20)

        rlabel = QLabel("R", self)
        rlabel.setGeometry(25, 105, 20, 20)

        self.r_value_label = QLabel("255", self)
        self.r_value_label.setGeometry(self.width() - 25, 105, 20, 20)

        self.red_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.red_slider.setTickInterval(1)
        self.red_slider.setMaximum(255)
        self.red_slider.setValue(255)
        self.red_slider.setGeometry(50, 100, self.width() - 100, 40)
        self.red_slider.valueChanged.connect(self.display_colors)

        glabel = QLabel("G", self)
        glabel.setGeometry(25, 155, 20, 20)

        self.g_value_label = QLabel("255", self)
        self.g_value_label.setGeometry(self.width() - 25, 155, 20, 20)

        self.green_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.green_slider.setTickInterval(1)
        self.green_slider.setMaximum(255)
        self.green_slider.setValue(255)
        self.green_slider.setGeometry(50, 150, self.width() - 100, 40)
        self.green_slider.valueChanged.connect(self.display_colors)

        blabel = QLabel("B", self)
        blabel.setGeometry(25, 205, 20, 20)

        self.b_value_label = QLabel("255", self)
        self.b_value_label.setGeometry(self.width() - 25, 205, 20, 20)

        self.blue_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.blue_slider.setTickInterval(1)
        self.blue_slider.setMaximum(255)
        self.blue_slider.setValue(255)

        self.blue_slider.setGeometry(50, 200, self.width() - 100, 40)
        self.blue_slider.valueChanged.connect(self.display_colors)

        self.download_button = QPushButton("Pobierz", self)
        self.download_button.setObjectName("download_button")
        self.download_button.setGeometry(self.width() // 2 - 100, 250, 200, 40)
        self.download_button.clicked.connect(self.download_colors)

        self.download_label = QLabel("255, 255, 255", self)
        self.download_label.setObjectName("download_label")
        self.download_label.setGeometry(self.width() // 2 - 100, 300, 200, 40)
        self.download_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
