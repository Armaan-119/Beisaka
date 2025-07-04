this is my first ever Project 


⎛⎝(•ⱅ•)⎠⎞ ⎛⎝(•ⱅ•)⎠⎞ 


**Note: This assistant is for personal/educational use. Do not use it for automation of tasks in violation of game or service policies.**
# Beisaka - Your Personal Desktop AI Assistant 🧠🎙️

**Beisaka** is a fully voice-controlled desktop assistant built using Python. It can recognize speech, perform tasks, search the web, automate screen interactions, run gaming commands, control Chrome, and much more.

---

## 🧩 Features

- 🎙️ **Speech Recognition** via microphone
- 🗣️ **Text-to-Speech (TTS)** responses using `pyttsx3`
- 🌐 **Wikipedia Integration** – ask questions like "Who is Albert Einstein?"
- 🖱️ **Mouse and Keyboard Control** – including typing, pressing, shortcuts
- 📸 **Screen Analysis with YOLOv7** – real-time object detection on screen
- 🕹️ **Gaming Commands** – supports Skyrim attack, block, shout, sprint (customizable)
- 📂 **Modular Commands** – all commands like mouse, shortcuts, Chrome, and game logic are modularized for better structure
- 🧠 **Disambiguation Handling** – intelligently handles multiple possible results from Wikipedia
- 💻 **App Control** – open/close Notepad, search YouTube/Google, and more
- 📷 **Screenshot Capture**
- 🔍 **Custom Web Searches**

---

## 📁 Folder Structure

```bash
.
├── ShoreKeeper.py              # Main assistant script
├── mouse_commands.py          # Mouse click, move, drag logic
├── button_use.py              # Shortcut and key press commands
├── screen_detector.py         # YOLOv7 screen detection
├── game_commands.py           # Skyrim or other game-specific inputs
├── chrome_shortcuts.py        # Chrome tab management & shortcuts
├── yolov7/                    # YOLOv7 model folder
├── yolov7.pt                  # Pretrained YOLOv7 model
└── README.md
