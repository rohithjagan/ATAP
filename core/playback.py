"""Playback controller using QTimer for frame switching."""
from PyQt5.QtCore import QTimer, QObject, pyqtSignal

class PlaybackController(QObject):
    """Manages playback state: play, pause, stop, FPS."""
    frame_changed = pyqtSignal(int)   # new frame index
    playback_started = pyqtSignal()
    playback_paused = pyqtSignal()
    playback_stopped = pyqtSignal()

    def __init__(self, frame_manager, fps=6):
        super().__init__()
        self.frame_manager = frame_manager
        self.fps = fps
        self.timer = QTimer()
        self.timer.timeout.connect(self._next_frame)
        self.playing = False
        self.current_play_index = 0

    def play(self):
        if not self.playing and self.frame_manager.frame_count() > 0:
            self.playing = True
            self.current_play_index = 0
            self.frame_changed.emit(0)
            self.timer.start(1000 // self.fps)
            self.playback_started.emit()

    def pause(self):
        if self.playing:
            self.timer.stop()
            self.playing = False
            self.playback_paused.emit()

    def stop(self):
        self.timer.stop()
        self.playing = False
        self.current_play_index = 0
        self.frame_changed.emit(0)
        self.playback_stopped.emit()

    def set_fps(self, fps):
        self.fps = fps
        if self.playing:
            self.timer.setInterval(1000 // self.fps)

    def _next_frame(self):
        """Advance frame, loop back to start."""
        count = self.frame_manager.frame_count()
        if count == 0:
            return
        self.current_play_index = (self.current_play_index + 1) % count
        self.frame_changed.emit(self.current_play_index)