# HandGame — Rock Paper Scissors Detector (Webcam + YOLOv8)

A small project that detects the hand game **Rock / Paper / Scissors** from your webcam using **YOLOv8 (Ultralytics)**.  

---

## ✨ Features
- 🎥 Real-time detection from your webcam  
- 🤖 Powered by YOLOv8 (via the `ultralytics` package)  
- ⚡ Simple setup and execution  

---

## ⚙️ Requirements
- Python **3.8+**  
- A working webcam  
- Internet connection (to install dependencies & YOLOv8 weights on first run)  

---

## 🚀 Installation & Run

Run these commands **step by step** in your project folder:

```bash
# 1. Create a virtual environment
python -m venv venv

# 2. Activate the virtual environment (Windows)
venv/Scripts/activate

# (For macOS/Linux use: source venv/bin/activate)

# 3. Install YOLOv8 (Ultralytics)
pip install ultralytics

# 4. Run the application
python ./app.py
