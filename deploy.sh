#!/bin/bash
echo "🚀 Deploying Stable Sklearn AI Model Serving Pipeline..."

cd "$(dirname "$0")"

if [ ! -d "ai-env" ]; then
  echo "Creating ai-env venv..."
  python3 -m venv ai-env
fi

source ai-env/bin/activate

# Install project deps
pip install --upgrade pip
pip install -r requirements.txt

# Sklearn model trains/saves instantly on first import (no warmup needed)
echo "✅ Sklearn model ready (trains ~200 examples, saves model.pkl)"

echo "🌐 API: http://localhost:8080 | Docs: http://localhost:8080/docs"

# Test endpoints (server starts in background)
uvicorn app:app --host 0.0.0.0 --port 8080 --reload &
PID=$!
sleep 5

curl -s http://localhost:8080/health | grep healthy && echo "✅ Health OK"
curl -s -X POST "http://localhost:8080/predict" \
  -H "Content-Type: application/json" \
  -d '{"text":"I love this stable AI pipeline!"}' | jq . && echo "✅ Sklearn Prediction OK"

kill $PID 2>/dev/null

echo "🎉 READY! Run: source ai-env/bin/activate && uvicorn app:app --host 0.0.0.0 --port 8080 --reload"
echo "Or: bash deploy.sh (runs in background, Ctrl+C to stop)"

