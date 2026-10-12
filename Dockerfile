FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive \
    OLLAMA_HOST=127.0.0.1:11434 \
    OLLAMA_MODEL=gemma3:1b \
    DATA_DIR=/app/data \
    PYTHONUNBUFFERED=1

WORKDIR /app

# zstd is REQUIRED by the Ollama installer. espeak-ng gives offline TTS on Linux.
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    zstd \
    python3 \
    python3-pip \
    espeak-ng \
    libespeak1 \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh
RUN ollama --version

# Bake the model into the image so startup is fast and reliable
RUN bash -c 'ollama serve & for i in $(seq 1 30); do curl -sf http://127.0.0.1:11434/api/tags >/dev/null && break; sleep 1; done; ollama pull "$OLLAMA_MODEL"; kill %1 || true'

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py start.sh ./
RUN mkdir -p /app/data

EXPOSE 8501

CMD ["bash", "/app/start.sh"]
