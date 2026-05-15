"""Main drawing canvas that handles mouse events and paints the current frame."""
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap, QPainterPath
from core.tools import ToolType

class DrawCanvas(QWidget):
    def __init__(self, frame_manager, parent=None):
        super().__init__(parent)
        self.frame_manager = frame_manager
        self.tool = ToolType.BRUSH
        self.brush_color = QColor("#000000")
        self.brush_size = 10
        self.drawing = False
        self.last_point = QPoint()
        # For smooth strokes we'll use QPainterPath
        self.current_path = None
        self.setMinimumSize(400, 300)
        self.setMouseTracking(False)
        self.setCursor(Qt.CrossCursor)
        self.setStyleSheet("background-color: #FFFFFF; border: 2px solid #FFB6C1;")

    def set_tool(self, tool: ToolType):
        self.tool = tool

    def set_color(self, color: QColor):
        self.brush_color = color

    def set_brush_size(self, size: int):
        self.brush_size = size

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()
            # Save state for undo before modifying the frame
            self.frame_manager.current_frame.save_state()
            # Begin a new path for smooth drawing
            self.current_path = QPainterPath()
            self.current_path.moveTo(event.pos())
            self.update()

    def mouseMoveEvent(self, event):
        if self.drawing:
            # Draw onto the frame’s pixmap
            painter = QPainter(self.frame_manager.current_frame.pixmap)
            painter.setRenderHint(QPainter.Antialiasing)

            if self.tool == ToolType.BRUSH:
                pen = QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            else:  # Eraser: paint with white
                pen = QPen(Qt.white, self.brush_size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)

            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            painter.end()

            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawing:
            self.drawing = False
            self.current_path = None
            self.update()

    def paintEvent(self, event):
        """Draw the current frame pixmap onto the widget."""
        painter = QPainter(self)
        pix = self.frame_manager.current_frame.pixmap
        if pix:
            painter.drawPixmap(self.rect(), pix)
        # Optionally draw a cursor preview? Omitted for simplicity.
        painter.end()

    def clear_frame(self):
        """Fill current frame with white after saving state."""
        self.frame_manager.current_frame.save_state()
        self.frame_manager.current_frame.pixmap.fill(Qt.white)
        self.update()

    def undo(self):
        if self.frame_manager.current_frame.undo():
            self.update()

    def redo(self):
        if self.frame_manager.current_frame.redo():
            self.update()

    def update_frame_display(self):
        """Refresh the canvas when frame changes."""
        self.update()