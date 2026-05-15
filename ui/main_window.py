"""Main window that assembles all UI components."""
import sys, os, json
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QSplitter, QLabel, QPushButton, QFileDialog,
                             QMessageBox, QAction, QMenuBar, QSlider)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon, QColor

from core.frame_manager import FrameManager
from core.canvas import DrawCanvas
from core.playback import PlaybackController
from core.exporter import export_gif, export_mp4
from core.tools import ToolType, COLOR_PALETTE, BRUSH_SIZES
from ui.toolbar import TopToolbar
from ui.timeline import TimelineWidget
from ui.widgets import ColorButton, BrushSizeButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ATAP - Animation Tool for Adorable Preschoolers 🥰")
        self.setMinimumSize(1024, 700)

        # Core objects
        self.frame_manager = FrameManager(800, 600)
        self.canvas = DrawCanvas(self.frame_manager)
        self.playback = PlaybackController(self.frame_manager)

        # Setup UI
        self._init_ui()
        self._connect_signals()
        self._apply_global_style()

        # Connect playback to canvas update
        self.playback.frame_changed.connect(self.on_playback_frame_changed)

    def _init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # 1. Menu bar (minimal)
        self._create_menu_bar()

        # 2. Top toolbar
        self.toolbar = TopToolbar(self.canvas, self.playback)
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

        # 3. Main area: left sidebar + canvas
        content_splitter = QSplitter(Qt.Horizontal)

        # Left sidebar
        self.left_sidebar = self._create_left_sidebar()
        content_splitter.addWidget(self.left_sidebar)

        # Canvas
        content_splitter.addWidget(self.canvas)
        content_splitter.setStretchFactor(0, 0)   # sidebar fixed
        content_splitter.setStretchFactor(1, 1)
        content_splitter.setSizes([180, 700])

        main_layout.addWidget(content_splitter, stretch=1)

        # 4. Bottom timeline
        self.timeline = TimelineWidget(self.frame_manager, self.canvas, self.playback)
        main_layout.addWidget(self.timeline, stretch=0)

    def _create_left_sidebar(self):
        """Left panel with colors and brush size."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(10)

        # Color palette
        color_label = QLabel("🎨 Colors")
        color_label.setStyleSheet("font-size: 14pt; font-weight: bold;")
        layout.addWidget(color_label)

        color_grid = QHBoxLayout()
        # Two rows of 8 colors
        for i, hexc in enumerate(COLOR_PALETTE):
            btn = ColorButton(hexc, 30)
            btn.clicked.connect(lambda _, c=hexc: self.canvas.set_color(QColor(c)))
            if i % 8 == 0:
                layout.addLayout(color_grid)
                color_grid = QHBoxLayout()
            color_grid.addWidget(btn)
        layout.addLayout(color_grid)

        layout.addSpacing(20)

        # Brush size
        size_label = QLabel("🖌️ Brush Size")
        size_label.setStyleSheet("font-size: 14pt; font-weight: bold;")
        layout.addWidget(size_label)

        size_btns = QHBoxLayout()
        self.brush_group = []
        for label, size_val in BRUSH_SIZES.items():
            btn = BrushSizeButton(label, size_val)
            btn.setCheckable(True)
            btn.clicked.connect(lambda _, s=size_val: self.canvas.set_brush_size(s))
            size_btns.addWidget(btn)
            self.brush_group.append(btn)
        # Set Medium as default
        self.brush_group[1].setChecked(True)
        layout.addLayout(size_btns)

        # FPS slider
        fps_label = QLabel("⏩ Speed (FPS)")
        fps_label.setStyleSheet("font-size: 12pt;")
        layout.addWidget(fps_label)
        self.fps_slider = QSlider(Qt.Horizontal)
        self.fps_slider.setRange(1, 12)
        self.fps_slider.setValue(6)
        self.fps_slider.valueChanged.connect(lambda v: self.playback.set_fps(v))
        layout.addWidget(self.fps_slider)

        layout.addStretch()
        return widget

    def _create_menu_bar(self):
        menubar = self.menuBar()
        menubar.setStyleSheet("QMenuBar { background-color: #FFB6C1; }")

        file_menu = menubar.addMenu("📁 File")

        new_action = QAction("✨ New Cartoon", self)
        new_action.triggered.connect(self.new_project)
        file_menu.addAction(new_action)

        save_action = QAction("💾 Save My Work", self)
        save_action.triggered.connect(self.save_project)
        file_menu.addAction(save_action)

        load_action = QAction("📂 Open Project", self)
        load_action.triggered.connect(self.load_project)
        file_menu.addAction(load_action)

        file_menu.addSeparator()

        export_gif_action = QAction("🎞️ Export as GIF", self)
        export_gif_action.triggered.connect(self.export_as_gif)
        file_menu.addAction(export_gif_action)

        export_mp4_action = QAction("🎥 Export as MP4", self)
        export_mp4_action.triggered.connect(self.export_as_mp4)
        file_menu.addAction(export_mp4_action)

    def _connect_signals(self):
        # Ensure timeline refreshes when frames change via toolbar
        pass

    def _apply_global_style(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #FFF5F5;
            }
            QLabel {
                font-family: 'Comic Sans MS', sans-serif;
            }
            QPushButton {
                font-family: 'Comic Sans MS', sans-serif;
            }
        """)

    def on_playback_frame_changed(self, frame_idx):
        # Update canvas to show playback frame (but don't change editing frame)
        # We'll temporarily override paintEvent? Better: just show the frame's pixmap
        # For simplicity, we'll set the canvas to display that frame while not changing current_index
        self.canvas.frame_manager.current_index = frame_idx
        self.canvas.update_frame_display()

    def new_project(self):
        reply = QMessageBox.question(self, "New", "Start a new cartoon? Unsaved work will be lost.",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.frame_manager = FrameManager(800, 600)
            self.canvas.frame_manager = self.frame_manager
            self.playback.frame_manager = self.frame_manager
            self.timeline.frame_manager = self.frame_manager
            self.timeline.refresh_thumbnails()
            self.canvas.update_frame_display()

    def save_project(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Choose folder to save")
        if not dir_path:
            return
        # Create a subfolder
        proj_name = "my_cartoon"
        save_dir = os.path.join(dir_path, proj_name)
        os.makedirs(save_dir, exist_ok=True)

        # Save frames as PNG images and metadata JSON
        metadata = {
            "fps": self.playback.fps,
            "frame_count": self.frame_manager.frame_count()
        }
        for i, frame in enumerate(self.frame_manager.frames):
            fname = f"frame_{i:04d}.png"
            frame.pixmap.save(os.path.join(save_dir, fname), "PNG")

        with open(os.path.join(save_dir, "project.json"), "w") as f:
            json.dump(metadata, f)

        QMessageBox.information(self, "Saved!", f"Your cartoon was saved in {save_dir}")

    def load_project(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Open project folder")
        if not dir_path:
            return
        json_path = os.path.join(dir_path, "project.json")
        if not os.path.exists(json_path):
            QMessageBox.warning(self, "Oops", "No project file found.")
            return
        with open(json_path, "r") as f:
            metadata = json.load(f)

        frames = []
        for i in range(metadata["frame_count"]):
            fname = f"frame_{i:04d}.png"
            pix = QPixmap(os.path.join(dir_path, fname))
            if pix.isNull():
                continue
            frames.append(pix)
        if not frames:
            QMessageBox.warning(self, "Oops", "No frame images found.")
            return

        # Rebuild frame manager
        new_fm = FrameManager(800, 600)
        from core.frame_manager import Frame
        new_fm.frames = []
        for pix in frames:
            f = Frame(pix)
            new_fm.frames.append(f)
        new_fm.current_index = 0
        self.frame_manager = new_fm
        self.canvas.frame_manager = new_fm
        self.playback.frame_manager = new_fm
        self.timeline.frame_manager = new_fm
        self.playback.set_fps(metadata.get("fps", 6))
        self.timeline.refresh_thumbnails()
        self.canvas.update_frame_display()
        QMessageBox.information(self, "Opened!", "Your project is ready.")

    def export_as_gif(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export GIF", "", "GIF (*.gif)")
        if path:
            export_gif(self.frame_manager, path, self.playback.fps)
            QMessageBox.information(self, "Exported!", f"GIF saved to {path}")

    def export_as_mp4(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export MP4", "", "MP4 (*.mp4)")
        if path:
            export_mp4(self.frame_manager, path, self.playback.fps)
            QMessageBox.information(self, "Exported!", f"MP4 saved to {path}")