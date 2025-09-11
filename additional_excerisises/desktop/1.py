from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Kupa")
        self.setGeometry(0, 0, 1000, 500)
        self.setStyleSheet("""
        background-color: gray;                        
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()



        labels = [
            QLabel(f"Label {i}", self) for i in range(5)
        ]

        for i, label in enumerate(labels):
            label.setGeometry(0, 0, 1000, 100)
            label.setStyleSheet(f"""
            color: black
                                ;
            font-size: 100px;
            background-color: rgb({i*60},{i*40},{255-(i*50)});
            """)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label)

        central_widget.setLayout(layout)

        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
