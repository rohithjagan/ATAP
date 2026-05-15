"""Defines drawing tool types and shared constants."""
from enum import Enum, auto

class ToolType(Enum):
    BRUSH = auto()
    ERASER = auto()

# Kid‑friendly palette
COLOR_PALETTE = [
    "#FF0000", "#FF7F00", "#FFFF00", "#00FF00",
    "#0000FF", "#4B0082", "#8B00FF", "#FF1493",
    "#00FFFF", "#FFD700", "#FF69B4", "#7CFC00",
    "#000000", "#FFFFFF", "#808080", "#A0522D"
]

BRUSH_SIZES = {
    "Small": 4,
    "Medium": 10,
    "Large": 20
}

DEFAULT_BRUSH_SIZE = BRUSH_SIZES["Medium"]
DEFAULT_COLOR = "#000000"
DEFAULT_FPS = 6
MAX_UNDO = 30