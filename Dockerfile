# Use Ubuntu base (Ollama needs proper OS)
FROM ubuntu:22.04

# Set working directory
WORKDIR /app

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV OLLAMA_HOST=127.0.0.1:11434

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip \
    curl \
    wget \
    git \
    espeak \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama with CORRECT URL (not ollama.ai - that's old!)
RUN curl -fsSL https://ollama.com/install.sh | sh

# Verify Ollama installed
RUN which ollama && ollama --version

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY README.md .

# Create data directory
RUN mkdir -p /app/data

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Start both Ollama and Streamlit
CMD bash -c '\
    echo "Starting Ollama service..." && \
    ollama serve &\
    OLLAMA_PID=$! && \
    sleep 5 && \
    echo "Pulling Gemma 3 1B model (smaller, faster)..." && \
    ollama pull gemma:2b && \
    echo "Model ready! Starting Streamlit..." && \
    streamlit run app.py --server.port=8501 --server.address=0.0.0.0 --server.enableCORS=false && \
    wait $OLLAMA_PID
'
