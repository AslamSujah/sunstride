#!/bin/bash

# SunStride Automatic Setup Script (Mac/Linux)
# This script sets up everything automatically

set -e  # Exit on error

echo "🌿 SunStride Setup Starting..."
echo ""

# Color codes for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Step 1: Check Python
echo "${BLUE}1. Checking Python installation...${NC}"
if ! command -v python3 &> /dev/null; then
    echo "${YELLOW}Python 3 not found. Please install Python 3.9+${NC}"
    exit 1
fi
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "${GREEN}✓ Python $PYTHON_VERSION found${NC}"
echo ""

# Step 2: Check Ollama
echo "${BLUE}2. Checking Ollama installation...${NC}"
if ! command -v ollama &> /dev/null; then
    echo "${YELLOW}Ollama not found. Installing...${NC}"
    curl -fsSL https://ollama.ai/install.sh | sh
    echo "${GREEN}✓ Ollama installed${NC}"
else
    echo "${GREEN}✓ Ollama found${NC}"
fi
echo ""

# Step 3: Create virtual environment
echo "${BLUE}3. Creating virtual environment...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "${GREEN}✓ Virtual environment created${NC}"
else
    echo "${GREEN}✓ Virtual environment already exists${NC}"
fi
echo ""

# Step 4: Activate virtual environment
echo "${BLUE}4. Activating virtual environment...${NC}"
source venv/bin/activate
echo "${GREEN}✓ Virtual environment activated${NC}"
echo ""

# Step 5: Install dependencies
echo "${BLUE}5. Installing dependencies...${NC}"
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1
echo "${GREEN}✓ Dependencies installed${NC}"
echo ""

# Step 6: Download Gemma model
echo "${BLUE}6. Downloading Gemma 2 model (this may take a few minutes)...${NC}"
echo "${YELLOW}Starting Ollama service...${NC}"
ollama serve &
OLLAMA_PID=$!
sleep 3  # Wait for Ollama to start

echo "${YELLOW}Pulling gemma2 model...${NC}"
ollama pull gemma2
echo "${GREEN}✓ Gemma 2 model ready${NC}"
echo ""

# Step 7: Launch app
echo "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo "${GREEN}✨ Setup Complete! Launching SunStride...${NC}"
echo "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "${BLUE}🌐 Your app will open in browser at: http://localhost:8501${NC}"
echo ""
sleep 2

# Kill background Ollama process (app will start it fresh)
kill $OLLAMA_PID 2>/dev/null || true

# Run the Streamlit app
streamlit run app.py
