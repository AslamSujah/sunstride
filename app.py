import os
import shutil
import sqlite3
import subprocess
import sys

import streamlit as st
from ollama import Client

MODEL = os.environ.get("OLLAMA_MODEL", "gemma3:1b")
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "127.0.0.1:11434")
if not OLLAMA_HOST.startswith("http"):
    OLLAMA_HOST = f"http://{OLLAMA_HOST}"
DATA_DIR = os.environ.get("DATA_DIR", "data")
DB_PATH = os.path.join(DATA_DIR, "sunstride_journal.db")

os.makedirs(DATA_DIR, exist_ok=True)
ollama_client = Client(host=OLLAMA_HOST)


def db():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            duration INTEGER,
            uv_level TEXT,
            activity TEXT,
            briefing TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


def generate_outdoor_briefing(duration_mins, uv_index, activity_type):
    prompt = f"""
You are an encouraging outdoor wellness coach.
The user is going outside for a {duration_mins}-minute {activity_type}.
The current estimated UV Index is {uv_index}.

Write a short spoken audio script (under 50 words) that:
1. Gives 1 practical UV/hydration safety tip.
2. Suggests a simple mindfulness observation (e.g., notice tree rustles or wind).
3. Tells them to put their device in their pocket right now.

Keep it warm, direct and conversational. No hashtags or markdown symbols.
"""
    response = ollama_client.generate(model=MODEL, prompt=prompt)
    return response["response"].strip()


def create_local_audio(text):
    """Offline TTS to a WAV file. Returns path or None."""
    out = os.path.join(DATA_DIR, "outdoor_briefing.wav")
    try:
        if sys.platform == "darwin" and shutil.which("say"):
            subprocess.run(
                ["say", "-o", out, "--data-format=LEI16@22050", text], check=True
            )
            return out
        for exe in ("espeak-ng", "espeak"):
            if shutil.which(exe):
                subprocess.run([exe, "-w", out, text], check=True)
                return out
        import pyttsx3

        engine = pyttsx3.init()
        engine.save_to_file(text, out)
        engine.runAndWait()
        return out if os.path.exists(out) else None
    except Exception as e:
        st.warning(f"Audio generation failed: {e}")
        return None


def log_session(duration, uv_level, activity, briefing):
    conn = db()
    conn.execute(
        "INSERT INTO sessions (duration, uv_level, activity, briefing) VALUES (?, ?, ?, ?)",
        (duration, str(uv_level), activity, briefing),
    )
    conn.commit()
    conn.close()


st.set_page_config(page_title="SunStride - Touch Grass", page_icon="☀️")
st.title("☀️ SunStride")
st.caption("Screen-Free Outdoor Companion | Powered by Local Gemma & Ollama")

init_db()

st.subheader("10-Second Setup Before Going Outside")
col1, col2 = st.columns(2)
with col1:
    duration = st.slider("Outdoor Duration (mins)", 5, 60, 20)
    activity = st.selectbox(
        "Activity",
        ["Mindful Walk", "Trail Run", "Gardening", "Park Bench Rest", "Cycling", "Hiking"],
    )
with col2:
    uv_val = st.select_slider(
        "Current Sun / UV Level",
        options=["Low (1-2)", "Moderate (3-5)", "High (6-7)", "Very High (8+)"],
    )

if st.button("🚀 Prepare My Session & Lock Screen", use_container_width=True):
    with st.spinner(f"Generating briefing with {MODEL}..."):
        try:
            briefing = generate_outdoor_briefing(duration, uv_val, activity)
        except Exception as e:
            st.error(f"Could not reach Ollama or model '{MODEL}': {e}")
            st.stop()
        audio_path = create_local_audio(briefing)
        log_session(duration, uv_val, activity, briefing)

    st.success("Briefing Ready!")
    st.write("🎙️ **Audio Script Preview:**")
    st.info(f'"{briefing}"')
    if audio_path:
        with open(audio_path, "rb") as f:
            st.audio(f.read(), format="audio/wav")
    else:
        st.warning("No audio generated, but your text briefing is above.")
    st.warning("📱 **Press Play, put your phone in your pocket, and Touch Grass!**")

st.divider()
st.subheader("📖 Your Outdoor Log (Offline)")
conn = db()
rows = conn.execute(
    "SELECT duration, activity, created_at FROM sessions ORDER BY id DESC LIMIT 5"
).fetchall()
conn.close()
if rows:
    for d, a, c in rows:
        st.write(f"🌿 **{a}** ({d} mins) — *{c}*")
else:
    st.write("No sessions logged yet. Take your first walk today!")
