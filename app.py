import os
import json
import sqlite3
import subprocess
import streamlit as st
from ollama import Client

# Initialize local Ollama client (Runs 100% offline)
ollama_client = Client(host='http://127.0.0.1:11434')

def init_db():
    """Initialize SQLite database for session logging."""
    conn = sqlite3.connect("/app/data/sunstride_journal.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            duration INTEGER,
            uv_level TEXT,
            activity TEXT,
            briefing TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def generate_outdoor_briefing(duration_mins, uv_index, activity_type):
    """
    Uses local Gemma model to construct a 30-second spoken briefing.
    Designed specifically to be listened to, encouraging immediate screen shutdown.
    
    Args:
        duration_mins (int): Duration of outdoor activity in minutes
        uv_index (str): Current UV level (Low, Moderate, High, Very High)
        activity_type (str): Type of outdoor activity
    
    Returns:
        str: Generated briefing text from Gemma model
    """
    prompt = f"""
    You are an encouraging outdoor wellness coach.
    The user is going outside for a {duration_mins}-minute {activity_type}.
    The current estimated UV Index is {uv_index}.
    
    Task: Write a short, spoken audio script (under 50 words) that:
    1. Gives 1 practical UV/hydration safety tip.
    2. Suggests a simple mindfulness observation (e.g., notice tree rustles or wind).
    3. Tells them to put their device in their pocket right now.
    
    Keep it warm, direct, and conversational. Do not use hashtags or markdown symbols.
    """
    
    try:
        response = ollama_client.generate(
            model='gemma:2b',
            prompt=prompt,
            stream=False
        )
        return response['response'].strip()
    except Exception as e:
        st.error(f"Error generating briefing: {str(e)}")
        return "Step outside, breathe fresh air, and enjoy nature!"

def create_local_audio(script_text, output_file="/app/data/outdoor_briefing.wav"):
    """
    Generates an offline audio file using pyttsx3 (cross-platform).
    
    Args:
        script_text (str): Text to convert to speech
        output_file (str): Output audio file path
    
    Returns:
        str: Path to generated audio file
    """
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Slower, clearer speech
        engine.save_to_file(script_text, output_file)
        engine.runAndWait()
        return output_file
    except Exception as e:
        st.warning(f"⚠️ Audio generation issue: {str(e)}")
        return None

def log_session(duration, uv_level, activity, briefing):
    """
    Log outdoor session to local SQLite database.
    
    Args:
        duration (int): Duration in minutes
        uv_level (str): UV level category
        activity (str): Activity type
        briefing (str): Generated briefing text
    """
    try:
        conn = sqlite3.connect("/app/data/sunstride_journal.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sessions (duration, uv_level, activity, briefing) VALUES (?, ?, ?, ?)",
            (duration, str(uv_level), activity, briefing)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        st.error(f"Error logging session: {str(e)}")

# --- Streamlit UI Configuration ---
st.set_page_config(
    page_title="SunStride - Touch Grass",
    page_icon="☀️",
    layout="centered"
)

st.title("☀️ SunStride")
st.caption("Screen-Free Outdoor Companion | Powered by Local Gemma & Ollama")

# Initialize database
init_db()

# --- Main UI Section ---
st.subheader("10-Second Setup Before Going Outside")

col1, col2 = st.columns(2)
with col1:
    duration = st.slider("Outdoor Duration (mins)", 5, 60, 20)
    activity = st.selectbox(
        "Activity",
        ["Mindful Walk", "Trail Run", "Gardening", "Park Bench Rest", "Cycling", "Hiking"]
    )

with col2:
    uv_val = st.select_slider(
        "Current Sun / UV Level",
        options=["Low (1-2)", "Moderate (3-5)", "High (6-7)", "Very High (8+)"]
    )

if st.button("🚀 Prepare My Session & Lock Screen", use_container_width=True):
    with st.spinner("Generating local audio briefing with Gemma..."):
        try:
            # 1. Generate text briefing with local Gemma model
            briefing = generate_outdoor_briefing(duration, uv_val, activity)
            
            # 2. Convert text to local audio file
            audio_path = create_local_audio(briefing)
            
            # 3. Log session locally
            log_session(duration, uv_val, activity, briefing)
            
            st.success("✅ Briefing Ready!")
            
            st.write("🎙️ **Audio Script Preview:**")
            st.info(f'"{briefing}"')
            
            # Play audio if it was created
            if audio_path and os.path.exists(audio_path):
                with open(audio_path, 'rb') as audio_file:
                    st.audio(audio_file.read(), format="audio/wav")
            else:
                st.warning("⚠️ Audio file not generated, but text briefing ready above")
            
            st.warning("📱 **Now press Play, put your phone in your pocket, and Touch Grass!**")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}\n\nMake sure Ollama is running and Gemma model is loaded.")

# --- Offline Journal Section ---
st.divider()
st.subheader("📖 Your Outdoor Log (Offline)")

try:
    conn = sqlite3.connect("/app/data/sunstride_journal.db")
    cursor = conn.cursor()
    cursor.execute("SELECT duration, activity, created_at FROM sessions ORDER BY id DESC LIMIT 5")
    rows = cursor.fetchall()
    conn.close()
    
    if rows:
        for row in rows:
            st.write(f"🌿 **{row[1]}** ({row[0]} mins) — *{row[2]}*")
    else:
        st.write("No sessions logged yet. Take your first walk today! 🌱")
except Exception as e:
    st.error(f"Error reading journal: {str(e)}")

# --- Footer ---
st.divider()
st.caption("🌿 Made with ☀️ and love for Hacktoberfest Open-Source AI Challenge")
