#!/usr/bin/env bash
set -e

ollama serve &

# Wait until Ollama is ready
for i in $(seq 1 60); do
  if curl -sf http://127.0.0.1:11434/api/tags >/dev/null; then
    break
  fi
  sleep 1
done

# No-op if the model is already baked into the image
ollama pull "${OLLAMA_MODEL:-gemma3:1b}"

# Render provides $PORT; default to 8501 elsewhere
exec streamlit run app.py \
  --server.port="${PORT:-8501}" \
  --server.address=0.0.0.0 \
  --server.headless=true
