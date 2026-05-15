# 🥰 ATAP – Animation Tool for Adorable Preschoolers

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/PyQt-5-green.svg)](https://www.riverbankcomputing.com/software/pyqt/)

A colourful, safe, and **extremely simple** 2D frame‑by‑frame animation software designed for children aged 4‑8.  
Built with **Python** and **PyQt5**, ATAP brings the joy of cartoon creation to preschoolers – no reading required, no complicated tools, just pure creative fun!

![ATAP Screenshot](docs/screenshot.png) *(placeholder – add a real screenshot)*

## ✨ Why ATAP?
- 🎨 **Kid‑first design** – huge buttons, emojis, rounded shapes, and a candy‑coloured interface.
- 🖱️ **Mouse‑only operation** – perfect for little hands on a mouse or touchpad.
- 🛡️ **Safe** – no internet, no ads, no accidental data loss.
- 🎬 **Frame‑by‑frame animation** – draw, flip, and play your own cartoon.
- 💾 **Save & open** – continue your masterpiece later.
- 📤 **Export** – turn your animation into a GIF or video to share with family.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or newer
- pip

### Installation
```bash
git clone https://github.com/yourusername/ATAP.git
cd ATAP
pip install -r requirements.txt
python main.py

That’s it! The app opens directly in drawing mode – no setup needed.

# 🎬 Features Walkthrough

## 🖌️ Drawing Canvas

- Smooth freehand drawing with anti-aliasing.
- Large, easy-to-use Brush and Eraser tools.
- Choose from 16 bright colours – just click a circle.
- Three brush sizes:
  - Small
  - Medium
  - Large
  - (or use the slider)
- Undo / Redo every stroke with a single click.

---

## 🎞️ Animation Timeline

- Add new blank frames, delete frames, or duplicate existing ones.
- See tiny thumbnails of each frame at the bottom.
- Click any thumbnail to jump to that frame and keep drawing.

---

## ▶️ Playback

- Press **Play** to watch your movie come alive.
- Adjust the speed with the FPS slider (**1–12 frames per second**).
- Loops automatically until you press **Stop**.

---

## 💾 Save & Load

- Save your whole project as a folder of PNG images + a `project.json` file.
- Reopen any saved folder later – exactly where you left off.

---

## 🎞️ Export

- Export as **GIF** – perfect for sharing in messages or social media.
- Export as **MP4 video** – higher quality for presentations.

---

# 📁 Project Structure

```text
ATAP/
├── assets/              # Placeholder for custom icons / sounds
├── core/                # All the logic (canvas, frames, playback, exporter)
├── ui/                  # PyQt5 interface (main window, toolbar, timeline)
├── saves/               # Default folder for saved projects (created automatically)
├── main.py              # Launch the app
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── .env.example
└── CHANGELOG.md

# 🧠 How It Works (for Developers)

- Frames are stored as `QPixmap` objects inside a `Frame` class, each with its own undo/redo stack.
- Drawing happens directly on the current frame’s pixmap using `QPainter`.
- Undo saves a copy of the entire pixmap before each stroke; undo restores the previous copy.
- Playback uses a `QTimer` to cycle through frame indices and temporarily display the corresponding pixmap.
- Saving serialises each frame as a PNG and writes metadata to a JSON file. Loading rebuilds frames from those images.
- Export converts `QPixmap → PIL Image → GIF/MP4` via `imageio`.

---

# 🧩 Extending the App

- Onion skinning – overlay previous/next frame with transparency.
- Sticker stamps – drag-and-drop pre-made images onto the canvas.
- Sound effects – play a note on each frame change using `QMediaPlayer`.
- More tools – shapes, fill bucket, text.
- Touchscreen support – already works on Windows touch devices, but can be enhanced.

---

# 🤝 Contributing

We welcome contributions that make ATAP even more adorable and easy to use!

Please read:

- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`

---

# 📜 License

This project is licensed under the **MIT License** – see the `LICENSE` file.

---

# 🙏 Acknowledgements

- Built with **PyQt5**
- GIF/MP4 export powered by **imageio**
- Inspired by **FlipaClip** and **Pencil2D**, but redesigned for tiny creators.

---

Happy animating! 🐻🎬