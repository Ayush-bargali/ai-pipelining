# 🤖 Stable Sklearn AI Sentiment Pipeline

Production-ready FastAPI service for sentiment analysis using **sklearn** (TF-IDF + LogisticRegression). No torch, no downloads, instant startup.

## 🚀 Architecture
- model.py → Trains sklearn pipeline and saves model.pkl
- app.py → FastAPI app with /predict, /health, /docs
- requirements.txt → Dependencies
- deploy.sh → Setup + run script

## ⚡ Quick Start
```bash
bash deploy.sh
🌐 API Endpoints
GET / → Info
GET /docs → Swagger UI
POST /predict → {"text": "I love this!"}
GET /health → Status
🧠 Model
TF-IDF + LogisticRegression
~85–90% accuracy (demo data)
Fast & lightweight (no GPU needed)
🛠 Tech Stack
FastAPI | Sklearn | Python | ML
👨‍💻 Ayush Bargali

---

## 🚀 Now run these commands

```bash id="h23k8p"
git add README.md
git rebase --continue
git push origin main