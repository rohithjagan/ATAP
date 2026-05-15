# Contributing to ATAP 🥰

First off, thank you for considering contributing to ATAP!  
We want to keep this project as **friendly and simple** as the app itself.  
Whether you're fixing a bug, adding a feature, or improving the design, your help is appreciated.

## 🧒 Our Philosophy
- **Child‑centred**: Every change should make the app easier or more fun for a 4‑year‑old.
- **Visual first**: Buttons should be big, labels emoji‑based, colours playful.
- **No jargon**: Avoid technical terms in the UI (and in the code comments when possible!).
- **Performance**: Must run smoothly on low‑end school computers.

## 🛠 How to Contribute

### 1. Discuss First
Open an issue to talk about what you want to do. This prevents duplicate work and ensures the feature aligns with the project goals.

### 2. Fork & Branch
- Fork the repository.
- Create a branch with a descriptive name, e.g. `feature/onion-skinning` or `fix/playback-crash`.

### 3. Code Style
- Write **clear, commented code** – imagine a 10‑year‑old might read it.
- Use docstrings for every module and public function.
- Keep functions small and focused.
- Follow PEP 8 as much as possible, but readability beats strict adherence.

### 4. Test Manually
Since the app is GUI‑based, test your changes thoroughly:
- Draw rapid strokes – no crash.
- Switch frames during playback – no artefacts.
- Save and reload a project – all frames intact.
- Export a GIF with at least 5 frames.

### 5. Pull Request
- Provide a clear description of what you did and why.
- Attach screenshots or screen recordings if you changed the UI.
- Mention the related issue number.

## 🧩 Ideas for Contributions
- Add onion skinning (semi‑transparent previous frame overlay).
- Create a set of built‑in “stamp” shapes (stars, hearts, animals).
- Add sound effects (pop, boing) triggered by actions.
- Improve touchscreen support (multi‑touch drawing?).
- Translate the interface into other languages.
- Design a dark/light theme switcher.
- Write automated tests for the frame manager and save/load logic.

## 🧪 Development Setup
1. Clone your fork.
2. Create a virtual environment:  
   `python -m venv venv && source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python main.py`

## 📜 Code of Conduct
Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## ❓ Questions?
Open an issue with the label `question` – we’ll be happy to help!

---

**Let’s make animation accessible for the youngest creators! 🐣✨**