"""Custom kid‑friendly widgets: ColorButton, BrushSizeSlider, etc."""
from PyQt5.QtWidgets import QPushButton, QSlider, QLabel, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class ColorButton(QPushButton):
    """A large colored circle that represents a selectable color."""
    def __init__(self, color_hex, size=30):
        super().__init__()
        self.color = QColor(color_hex)
        self.setFixedSize(size, size)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color_hex};
                border-radius: {size//2}px;
                border: 2px solid #FFB6C1;
            }}
            QPushButton:hover {{
                border: 3px solid #FF69B4;
            }}
        """)

class BrushSizeButton(QPushButton):
    """Toggle button for Small/Medium/Large."""
    def __init__(self, label, size_value):
        super().__init__(label)
        self.size_value = size_value
        self.setCheckable(True)
        self.setStyleSheet("""
            QPushButton {
                background-color: #FFDAB9;
                border-radius: 12px;
                padding: 8px;
                font-size: 12pt;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #FFB6C1; }
            QPushButton:checked { background-color: #FF69B4; color: white; }
        """)

class ThumbnailWidget(QWidget):
    """Custom widget to display frame thumbnails and allow selection."""
    # Will be implemented in timeline.py using QListWidget for simplicity.