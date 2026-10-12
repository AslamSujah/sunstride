# ⚡ SunStride - Quick Start Guide

**Get SunStride running in 3 minutes!**

---

## 🚀 Option 1: Easiest (Automatic Setup Script)

### Mac/Linux Users:

```bash
# 1. Clone the repository
git clone https://github.com/AslamSujah/sunstride.git
cd sunstride

# 2. Run the setup script (it does everything)
bash setup.sh

# 3. Done! Your app will open automatically in browser
```

### Windows Users:

```bash
# 1. Clone the repository
git clone https://github.com/AslamSujah/sunstride.git
cd sunstride

# 2. Run the setup script
python setup.py

# 3. Done! Your app will open automatically in browser
```

---

## 🐳 Option 2: Docker (Recommended for Cloud)

```bash
# 1. Clone the repository
git clone https://github.com/AslamSujah/sunstride.git
cd sunstride

# 2. Build and run with Docker
docker-compose up

# 3. Open browser to: http://localhost:8501
```

**Requirements:** Docker Desktop installed

---

## 📝 Option 3: Manual Setup (If scripts don't work)

### Prerequisites:
- Python 3.9 or higher
- Ollama installed (https://ollama.ai)

### Steps:

```bash
# 1. Clone repository
git clone https://github.com/AslamSujah/sunstride.git
cd sunstride

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
# OR on Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download Gemma model (one-time, ~2GB)
ollama pull gemma2

# 5. Start Ollama (in a new terminal)
ollama serve

# 6. Run the app (in original terminal)
streamlit run app.py

# 7. Browser opens automatically to http://localhost:8501
```

---

## ✅ Troubleshooting

### "Ollama not found"
- Download from https://ollama.ai
- Restart terminal after installation

### "Port 8501 already in use"
```bash
streamlit run app.py --server.port 8502
```

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### Audio not working
- Mac: Uses native `say` command ✓
- Linux: Install `espeak`: `sudo apt-get install espeak`
- Windows: Uses pyttsx3 (should work automatically)

---

## 🎯 Using SunStride

1. **Set your session:**
   - Duration (5-60 minutes)
   - Activity type (Walk, Run, etc.)
   - UV level (Low, Moderate, High, Very High)

2. **Click "Prepare My Session"**
   - AI generates personalized briefing
   - Audio file is created

3. **Press Play & Go Outside**
   - Listen to audio
   - Put phone in pocket
   - Enjoy screen-free outdoor time!

---

## 🆘 Still Having Issues?

Open an issue: https://github.com/AslamSujah/sunstride/issues

**Include:**
- Your OS (Mac/Linux/Windows)
- Python version: `python --version`
- Error message (copy-paste)

---

**Made with ☀️ and 🌿 for Hacktoberfest**
