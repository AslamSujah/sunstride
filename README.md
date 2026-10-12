# ☀️ SunStride: Screen-Free Outdoor Companion

**Submitted for Hacktoberfest Open-Source AI Challenge - Week 1: Touch Grass**

SunStride is an offline-first, screen-free outdoor session planner powered by open-weight local AI (Google Gemma via Ollama). Spend less time on screens and more time touching grass.

## 🌿 The Problem We Solve

Modern health tools keep us glued to vibrant screens:
- Checking live weather dashboards before outdoor activities
- Monitoring UV charts while walking
- Staring at fitness widgets during park visits

**SunStride flips the script:** You spend 10 seconds preparing on your laptop, then step outside screen-free with audio guidance.

## 🎯 How It Works

1. **Open SunStride** → Set your activity duration, type, and current UV level (10 seconds)
2. **Generate Briefing** → Local Gemma model creates a personalized audio script
3. **Hit Play** → Listen to the 30-second safety & mindfulness tip
4. **Put Phone Away** → Entire outdoor session with zero screen time
5. **Enjoy** → Audio reminders guide your walk, jog, or garden session

### Example Flow
```
Duration: 20 minutes
Activity: Mindful Walk
UV Level: Moderate (3-5)
        ↓
Gemma generates: "You're heading out for a peaceful 20-minute walk. 
The sun's moderate today—grab water and reapply sunscreen in 15 minutes. 
Notice the tree canopies above you. Phone goes in your pocket now. Enjoy!"
        ↓
You listen to audio, put phone away, walk for 20 minutes screen-free
```

## 🛠️ Technology Stack

| Component | Tool | Purpose |
|-----------|------|---------|
| **AI Model** | Google Gemma 2/3 (via Ollama) | Generates personalized outdoor briefings |
| **Agent Framework** | Python + ollama-python | Connects local inputs to LLM prompts |
| **Audio** | pyttsx3 / macOS `say` | Converts text to offline audio files |
| **UI** | Streamlit | Ultra-fast, distraction-free interface |
| **Storage** | SQLite | Local session logging (no cloud) |

## 💡 Why Open-Source AI?

✅ **100% Offline** — Works in airplane mode or remote areas with no cellular coverage  
✅ **Complete Privacy** — Location & habit data never leaves your device  
✅ **Zero Cost** — Local Gemma inference = $0.00 API costs  
✅ **Fine-Tunable** — Customize model behavior for your use case  

## 🚀 Quick Start

### Prerequisites
- **Python 3.9+**
- **Ollama** (download from https://ollama.ai)
- **macOS / Linux** (for `say` command; Windows uses `pyttsx3` fallback)

### Installation

1. **Pull the Gemma model:**
```bash
ollama pull gemma2
```

2. **Clone the repository:**
```bash
git clone https://github.com/AslamSujah/sunstride.git
cd sunstride
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the app:**
```bash
streamlit run app.py
```

5. **Open browser:**
```
http://localhost:8501
```

## 📖 Usage

1. **Set your outdoor session:**
   - Duration (5-60 minutes)
   - Activity type (Walk, Run, Gardening, etc.)
   - Current UV level (Low, Moderate, High, Very High)

2. **Click "Prepare My Session"**
   - Gemma generates a personalized briefing
   - Audio file is created and played
   - Session is logged locally

3. **Take the audio and go outside**
   - Put phone in pocket
   - Listen to the briefing on earphones
   - Enjoy your screen-free outdoor time

4. **Check your offline journal**
   - View past sessions (no cloud sync needed)
   - Track outdoor activity patterns

## 📁 Project Structure

```
sunstride/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── sunstride_journal.db      # Local SQLite database (auto-created)
├── README.md                 # This file
├── LICENSE                   # MIT License
└── .gitignore               # Git ignore patterns
```

## 🏆 Prize Category

**Best Use of Gemma:** Utilizes Google's open-weight Gemma model locally via Ollama to generate context-aware, screen-free outdoor activity audio scripts with zero external cloud dependencies.

## 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork the repo**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes**
4. **Commit** (`git commit -m 'Add amazing feature'`)
5. **Push** (`git push origin feature/amazing-feature`)
6. **Open a Pull Request**

### Ideas for Contributions
- 🌍 Add weather API integration (optional cloud mode)
- 🎵 Support for different audio voices/languages
- 📊 Enhanced analytics dashboard
- 🔄 Sync to fitness trackers (Apple Health, Google Fit)
- 🌤️ Local weather station integration
- 🎨 Improved UI/UX
- 📱 Mobile app version

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

- **Google Gemma** — Open-weight AI models powering our briefings
- **Ollama** — Local LLM inference engine
- **Streamlit** — Fast, interactive web UI framework
- **Hacktoberfest** — Supporting open-source innovation

## 📞 Support

Have questions? Open an [issue](https://github.com/AslamSujah/sunstride/issues) or start a [discussion](https://github.com/AslamSujah/sunstride/discussions).

---

**Made with ☀️ and 🌿 for the Hacktoberfest Open-Source AI Challenge**
