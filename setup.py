#!/usr/bin/env python3
"""
SunStride Automatic Setup Script (Windows/Cross-platform)
This script sets up everything automatically
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

# Color codes
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
NC = '\033[0m'

def print_step(step, message):
    print(f"{BLUE}{step}. {message}...{NC}")

def print_success(message):
    print(f"{GREEN}✓ {message}{NC}\n")

def print_error(message):
    print(f"{RED}✗ {message}{NC}")
    sys.exit(1)

def check_command(cmd):
    """Check if command exists in PATH"""
    return shutil.which(cmd) is not None

def run_command(cmd, description=""):
    """Run shell command and handle errors"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0 and description:
            print_error(f"{description}: {result.stderr}")
        return result.returncode == 0
    except Exception as e:
        if description:
            print_error(f"{description}: {str(e)}")
        return False

print(f"{BLUE}\n🌿 SunStride Setup Starting...\n{NC}")

# Step 1: Check Python
print_step(1, "Checking Python installation")
if sys.version_info < (3, 9):
    print_error(f"Python 3.9+ required. You have {sys.version}")
print_success(f"Python {sys.version.split()[0]} found")

# Step 2: Check Ollama
print_step(2, "Checking Ollama installation")
if not check_command('ollama'):
    print(f"{YELLOW}Ollama not found. Please install from https://ollama.ai{NC}")
    print(f"{YELLOW}After installation, restart this script.{NC}")
    sys.exit(1)
print_success("Ollama found")

# Step 3: Create virtual environment
print_step(3, "Creating virtual environment")
venv_path = Path('venv')
if not venv_path.exists():
    run_command(f"{sys.executable} -m venv venv", "Virtual environment creation")
    print_success("Virtual environment created")
else:
    print_success("Virtual environment already exists")

# Step 4: Determine activation command
if sys.platform == 'win32':
    venv_activate = r'venv\Scripts\activate.bat && '
else:
    venv_activate = 'source venv/bin/activate && '

# Step 5: Install dependencies
print_step(5, "Installing dependencies")
run_command(f"{venv_activate}{sys.executable} -m pip install --upgrade pip", "Pip upgrade")
run_command(f"{venv_activate}{sys.executable} -m pip install -r requirements.txt", "Dependency installation")
print_success("Dependencies installed")

# Step 6: Download Gemma model
print_step(6, "Downloading Gemma 2 model (this may take a few minutes)")
print(f"{YELLOW}Pulling gemma2 model...{NC}")
run_command(f"ollama pull gemma2", "Gemma 2 download")
print_success("Gemma 2 model ready")

# Step 7: Launch app
print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
print(f"{GREEN}✨ Setup Complete! Launching SunStride...{NC}")
print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
print(f"\n{BLUE}🌐 Your app will open in browser at: http://localhost:8501{NC}\n")

import time
time.sleep(2)

# Run the Streamlit app
if sys.platform == 'win32':
    os.system(f"{venv_activate}{sys.executable} -m streamlit run app.py")
else:
    os.system(f"source venv/bin/activate && streamlit run app.py")
