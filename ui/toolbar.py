"""Top toolbar with brush, eraser, undo, redo, play controls."""
from PyQt5.QtWidgets import QToolBar, QAction, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from core.tools import ToolType

class TopToolbar(QToolBar):
    def __init__(self, canvas, playback, parent=None):
        super().__init__("Tools", parent)
        self.setIconSize(QSize(36, 36))
        self.setMovable(False)

        # Use text with emoji because we have no icons; can replace with actual icons later
        self.brush_action = QAction("🖌️ Brush", self)
        self.brush_action.triggered.connect(lambda: canvas.set_tool(ToolType.BRUSH))
        self.addAction(self.brush_action)

        self.eraser_action = QAction("🧹 Eraser", self)
        self.eraser_action.triggered.connect(lambda: canvas.set_tool(ToolType.ERASER))
        self.addAction(self.eraser_action)

        self.addSeparator()

        self.undo_action = QAction("↩️ Undo", self)
        self.undo_action.triggered.connect(canvas.undo)
        self.addAction(self.undo_action)

        self.redo_action = QAction("↪️ Redo", self)
        self.redo_action.triggered.connect(canvas.redo)
        self.addAction(self.redo_action)

        self.addSeparator()

        self.play_action = QAction("▶️ Play", self)
        self.play_action.triggered.connect(playback.play)
        self.addAction(self.play_action)

        self.pause_action = QAction("⏸️ Pause", self)
        self.pause_action.triggered.connect(playback.pause)
        self.addAction(self.pause_action)

        self.stop_action = QAction("⏹️ Stop", self)
        self.stop_action.triggered.connect(playback.stop)
        self.addAction(self.stop_action)

        # Kid‑friendly styling
        self.setStyleSheet("""
            QToolBar {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #FFB6C1, stop:1 #FFC0CB);
                border-radius: 10px;
                padding: 6px;
                spacing: 10px;
            }
            QToolButton {
                background-color: #FFF0F5;
                border-radius: 12px;
                padding: 6px;
                font-size: 13pt;
                font-weight: bold;
            }
            QToolButton:hover {
                background-color: #FF69B4;
                color: white;
            }
        """)