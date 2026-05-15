"""Export animation frames to GIF or video using Pillow/imageio."""
import os
from PyQt5.QtGui import QImage
from PIL import Image
import imageio

def qpixmap_to_pil(pixmap):
    """Convert QPixmap to PIL Image."""
    image = pixmap.toImage()
    buffer = image.bits().asstring(image.byteCount())
    pil_image = Image.frombuffer("RGBA", (image.width(), image.height()), buffer, "raw", "BGRA", 0, 1)
    return pil_image.convert("RGB")

def export_gif(frame_manager, filepath, fps=6):
    """Export all frames as an animated GIF."""
    pil_images = [qpixmap_to_pil(frame.pixmap) for frame in frame_manager.frames]
    if not pil_images:
        return False
    # imageio v3 syntax
    imageio.mimsave(filepath, pil_images, format='GIF', duration=1000/fps)
    return True

def export_mp4(frame_manager, filepath, fps=6):
    """Export as MP4 using imageio-ffmpeg plugin."""
    pil_images = [qpixmap_to_pil(frame.pixmap) for frame in frame_manager.frames]
    imageio.mimsave(filepath, pil_images, fps=fps, codec='libx264')
    return True