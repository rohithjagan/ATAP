"""Manages the collection of frames as QPixmap objects."""
from PyQt5.QtGui import QPixmap, QColor, QPainter
from PyQt5.QtCore import Qt, QSize
from copy import deepcopy
from core.tools import MAX_UNDO

class Frame:
    """A single frame with image data and optional metadata."""
    def __init__(self, pixmap: QPixmap = None, width=800, height=600):
        if pixmap:
            self.pixmap = pixmap
        else:
            self.pixmap = QPixmap(width, height)
            self.pixmap.fill(Qt.white)   # need Qt imported, fix later
        # Undo/redo stacks for this frame
        self.undo_stack = []
        self.redo_stack = []

    def snapshot(self) -> QPixmap:
        """Return a copy of the current pixmap."""
        return self.pixmap.copy()

    def save_state(self):
        """Push current state onto undo stack, clear redo stack."""
        self.undo_stack.append(self.snapshot())
        if len(self.undo_stack) > MAX_UNDO:
            self.undo_stack.pop(0)   # limit stack size
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.snapshot())
            self.pixmap = self.undo_stack.pop()
            return True
        return False

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.snapshot())
            self.pixmap = self.redo_stack.pop()
            return True
        return False

class FrameManager:
    """Collection of frames with add/delete/duplicate/navigate."""
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.frames = [Frame(width=self.width, height=self.height)]
        self.current_index = 0

    @property
    def current_frame(self) -> Frame:
        return self.frames[self.current_index]

    def add_frame(self, after_current=True):
        """Insert a new blank frame after current (or at end)."""
        new_frame = Frame(width=self.width, height=self.height)
        if after_current:
            idx = self.current_index + 1
            self.frames.insert(idx, new_frame)
            self.current_index = idx
        else:
            self.frames.append(new_frame)
            self.current_index = len(self.frames) - 1

    def delete_frame(self):
        """Delete current frame if more than one remains."""
        if len(self.frames) <= 1:
            return False
        del self.frames[self.current_index]
        if self.current_index >= len(self.frames):
            self.current_index = len(self.frames) - 1
        return True

    def duplicate_frame(self):
        """Duplicate the current frame and insert after it."""
        dup = Frame(self.current_frame.snapshot(), self.width, self.height)
        idx = self.current_index + 1
        self.frames.insert(idx, dup)
        self.current_index = idx

    def goto_frame(self, index):
        if 0 <= index < len(self.frames):
            self.current_index = index

    def frame_count(self):
        return len(self.frames)

    def all_pixmaps(self):
        """Return list of current pixmaps for export."""
        return [f.pixmap for f in self.frames]