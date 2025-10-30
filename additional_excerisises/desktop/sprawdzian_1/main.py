from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QGroupBox,
    QPlainTextEdit,
    QLabel,
    QPushButton,
    QGridLayout,
    QWidget,
    QFileDialog,
)
from PyQt6.QtGui import QPixmap
import sys
import os
from PIL import Image, ImageDraw, ImageFont


def create_image_with_text(
    top_text, bottom_text, text_color, output_path="images/output.png"
):
    # Create 500x500 black image
    img = Image.new("RGB", (500, 500), color="black")
    draw = ImageDraw.Draw(img)

    # Try bold font (fallback to default)
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 16)
    except IOError:
        font = ImageFont.load_default()

    # Get image size
    W, H = img.size

    # Helper to center text horizontally
    def center_text(text, y):
        w, h = draw.textbbox((0, 0), text, font=font)[2:]
        draw.text(((W - w) / 2, y), text, fill=text_color, font=font)

    # Draw texts
    center_text(top_text, 20)
    center_text(bottom_text, H - 40)

    # Save
    img.save(output_path)
    print(f"Saved {output_path}")


# Example:
# create_image_with_text("Hello", "World", "red")


class MainWindow(QMainWindow):
    def open_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Open File")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                selected_file = selected_files[0]
                print(selected_file)
                self.image_label.setPixmap(QPixmap(selected_file))

    def save_image(self):
        top_text = self.top_text_edit.toPlainText()
        bottom_text = self.bottom_text_edit.toPlainText()
        color = self.current_color
        if not os.path.exists("images"):
            os.makedirs("images")
        create_image_with_text(top_text, bottom_text, color)

        opened_image = QPixmap("images/output.png")
        self.image_label.setPixmap(opened_image)

    def change_color(self, color_name):
        self.current_color = color_name
        print(f"Selected color: {color_name}")

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Image Creator")
        self.setGeometry(50, 50, 870, 650)
        self.setStyleSheet("""

""")
        self.current_color = "black"

        self.left_group = QGroupBox("Add Texts", self)
        self.left_group.setGeometry(20, 50, 400, 500)

        self.top_text_edit = QPlainTextEdit(self.left_group)
        self.top_text_edit.setGeometry(30, 70, 350, 70)
        top_text_label = QLabel("Top text", self.left_group)
        top_text_label.setGeometry(30, 55, 50, 15)

        self.bottom_text_edit = QPlainTextEdit(self.left_group)
        self.bottom_text_edit.setGeometry(30, 170, 350, 70)
        bottom_text_label = QLabel("Bottom text", self.left_group)
        bottom_text_label.setGeometry(30, 155, 100, 15)

        change_colour_label = QLabel("Change Colour", self.left_group)
        change_colour_label.setGeometry(30, 300, 100, 15)

        self.buttons = []
        self.colors = ["black", "white", "yellow", "red", "purple", "aqua"]

        buttons_grid = QGridLayout()
        buttons_widget = QWidget(self.left_group)
        buttons_widget.setGeometry(30, 320, 130, 100)

        self.buttons = []
        positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
        for color_name in self.colors:
            btn = QPushButton(buttons_widget)
            btn.clicked.connect(lambda checked, cn=color_name: self.change_color(cn))
            btn.setStyleSheet(f"background-color: {color_name};")
            self.buttons.append(btn)

        for btn, (r, c) in zip(self.buttons, positions):
            buttons_grid.addWidget(btn, r, c)

        buttons_widget.setLayout(buttons_grid)

        self.open_button = QPushButton("Open", self)
        self.open_button.setGeometry(170, 565, 100, 70)
        self.open_button.clicked.connect(self.open_image)

        self.save_button = QPushButton("Save", self)
        self.save_button.setGeometry(600, 565, 100, 70)
        self.save_button.clicked.connect(self.save_image)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(450, 50, 400, 500)
        self.image_label.setScaledContents(True)
        self.image_label.setPixmap(QPixmap("images/instrument.jpg"))


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
