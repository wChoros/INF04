# Desktop Apps

## PyQt template:
```python
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
```

## Labels

### Create Label
```python
from PyQt6.QtWidgets import QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        label = QLabel("Ruchanie", self)
```

### Set Stylesheet
```python
label.setStyleSheet("""
color: blue;
font-size: 100px;
background-color: rgb(10,10,10);
""")
```

### Size and alignment
```python
from PyQt6.QtCore import Qt

label.setGeometry(x, y, width, height)
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
```

## Layouts
```python
self.central_widget = QWidget()
self.setCentralWidget(self.central_widget)
```

```python
central_wiget.setLayout(layout)
```
### Form Layout
```python
layout = QFormLayout()
layout.addRow("label content (you can insert a label obect here)", button)
```

### Grid Layout
```python
layout = QGridLayout()
layout.addWidget(button)
```

### Box Layout
```python
layoutv = QVBoxLayout()
layouth = QHBoxLayout()

layout.addWidget(button)


```

## Images
```python
from PyQt6.QtGui import QPixmap
from PyQt6.QWidgets import QLabel

self.image = QLabel()
pixmap = QPixmap('cat.jpg')
self.image.setPixmap(pixmap)
image.setScaledContents(True)
```

## Button icons

```python
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

self.button = QPushButton(self)
self.button.setIcon(QIcon("image.png"))
self.button.setIconSize(QSize(100, 70))
```