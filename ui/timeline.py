"""Bottom timeline showing frame thumbnails with add/delete/duplicate buttons."""
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                             QListWidget, QListWidgetItem, QPushButton, QLabel)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap

class TimelineWidget(QWidget):
    def __init__(self, frame_manager, canvas, playback, parent=None):
        super().__init__(parent)
        self.frame_manager = frame_manager
        self.canvas = canvas
        self.playback = playback

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)

        # Buttons row
        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("➕ New Frame")
        self.btn_del = QPushButton("❌ Delete")
        self.btn_dup = QPushButton("📋 Duplicate")
        for btn in (self.btn_add, self.btn_del, self.btn_dup):
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #FFDAB9;
                    border-radius: 10px;
                    padding: 6px 12px;
                    font-size: 11pt;
                    font-weight: bold;
                }
                QPushButton:hover { background-color: #FFB6C1; }
            """)
            btn_layout.addWidget(btn)
        layout.addLayout(btn_layout)

        # Frame list
        self.frame_list = QListWidget()
        self.frame_list.setFlow(QListWidget.LeftToRight)   # horizontal layout
        self.frame_list.setIconSize(QSize(80, 60))
        self.frame_list.setSpacing(5)
        self.frame_list.setSelectionMode(QListWidget.SingleSelection)
        self.frame_list.currentRowChanged.connect(self.on_frame_selected)
        self.frame_list.setMaximumHeight(100)
        self.frame_list.setStyleSheet("""
            QListWidget {
                background-color: #FFF0F5;
                border: 2px solid #FFB6C1;
                border-radius: 10px;
            }
            QListWidget::item:selected {
                border: 3px solid #FF69B4;
                border-radius: 8px;
            }
        """)
        layout.addWidget(self.frame_list)

        # Frame counter label
        self.counter_label = QLabel("Frame: 1/1")
        self.counter_label.setAlignment(Qt.AlignCenter)
        self.counter_label.setStyleSheet("font-size: 10pt; color: #FF69B4;")
        layout.addWidget(self.counter_label)

        # Connections
        self.btn_add.clicked.connect(self.add_frame)
        self.btn_del.clicked.connect(self.delete_frame)
        self.btn_dup.clicked.connect(self.duplicate_frame)

        # Listen to playback frame changes
        self.playback.frame_changed.connect(self.highlight_play_frame)

        self.refresh_thumbnails()

    def refresh_thumbnails(self):
        """Rebuild thumbnail list from frame manager."""
        self.frame_list.blockSignals(True)
        self.frame_list.clear()
        for i, frame in enumerate(self.frame_manager.frames):
            thumb = frame.pixmap.scaled(80, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            item = QListWidgetItem(QIcon(thumb), f" {i+1}")
            self.frame_list.addItem(item)
        self.frame_list.setCurrentRow(self.frame_manager.current_index)
        self.counter_label.setText(f"Frame: {self.frame_manager.current_index+1}/{self.frame_manager.frame_count()}")
        self.frame_list.blockSignals(False)

    def add_frame(self):
        self.frame_manager.add_frame()
        self.refresh_thumbnails()
        self.canvas.update_frame_display()

    def delete_frame(self):
        if self.frame_manager.delete_frame():
            self.refresh_thumbnails()
            self.canvas.update_frame_display()

    def duplicate_frame(self):
        self.frame_manager.duplicate_frame()
        self.refresh_thumbnails()
        self.canvas.update_frame_display()

    def on_frame_selected(self, index):
        if index >= 0:
            self.frame_manager.goto_frame(index)
            self.canvas.update_frame_display()
            self.counter_label.setText(f"Frame: {index+1}/{self.frame_manager.frame_count()}")

    def highlight_play_frame(self, play_index):
        """Visually indicate playback position without moving selection."""
        # We can simply select the item without emitting signal
        self.frame_list.blockSignals(True)
        self.frame_list.setCurrentRow(play_index)
        self.frame_list.blockSignals(False)
        # also update counter
        self.counter_label.setText(f"▶️ Playing: {play_index+1}/{self.frame_manager.frame_count()}")