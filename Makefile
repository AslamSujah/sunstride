.PHONY: help install run run-docker clean docker-build docker-logs

help:
	@echo "SunStride - Available Commands:"
	@echo ""
	@echo "  make install      - Install all dependencies"
	@echo "  make run          - Run the app locally"
	@echo "  make run-docker   - Run with Docker Compose"
	@echo "  make docker-build - Build Docker images"
	@echo "  make docker-logs  - View Docker logs"
	@echo "  make clean        - Remove virtual env and cache files"
	@echo ""

install:
	@echo "Installing dependencies..."
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt
	@echo "✓ Dependencies installed"

run:
	@echo "Starting SunStride..."
	. venv/bin/activate && streamlit run app.py

run-docker:
	@echo "Starting with Docker Compose..."
	docker-compose up

docker-build:
	@echo "Building Docker images..."
	docker-compose build

docker-logs:
	docker-compose logs -f sunstride

clean:
	@echo "Cleaning up..."
	rm -rf venv __pycache__ .pytest_cache .streamlit
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Cleaned"
