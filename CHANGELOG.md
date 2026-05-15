# Changelog

All notable changes to ATAP will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] – 2025-05-15

### 🎉 First Release!

- **✨ Added**
  - Drawing canvas with smooth freehand brush and eraser.
  - 16 preset colours + large clickable colour buttons.
  - Three brush sizes (Small/Medium/Large) with toggle buttons.
  - Frame‑by‑frame animation system (add, delete, duplicate frames).
  - Bottom timeline with thumbnail previews.
  - Playback with adjustable FPS (1–12) and loop.
  - Undo/Redo per frame (up to 30 steps).
  - Save project (PNG frames + JSON metadata).
  - Open previously saved projects.
  - Export to GIF and MP4 via `imageio`.
  - Kid‑friendly UI with rounded buttons, emojis, and pastel colours.
  - Minimal menu bar (File: New, Save, Open, Export).

- **🛠 Technical**
  - Modular architecture: core/ (logic) and ui/ (presentation).
  - Frame storage using `QPixmap` and undo stacks.
  - Playback via `QTimer`.
  - Serialisation as folder of PNG images + `project.json`.

- **📝 Known Limitations**
  - No onion skinning (coming soon).
  - No touch‑specific gestures.
  - Only mouse/trackpad drawing supported.

---

## [Upcoming]
- Onion skinning (semi‑transparent previous/next frame).
- Built‑in stamp shapes (stars, hearts, animals).
- Sound effects on frame change.
- Dark/Light playful themes.
- Touchscreen support with multi‑touch drawing.
- Auto‑save recovery.