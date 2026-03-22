from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import model
import uvicorn

app = FastAPI(title="🤖 AI Sentiment Pipeline API", version="1.0")

class PredictRequest(BaseModel):
    text: str

@app.get("/")
async def home():
    return {
        "message": "🤖 AI Model Serving Pipeline LIVE!",
        "docs": "/docs",
        "predict": "/predict"
    }

@app.post("/predict")
async def predict(request: PredictRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    result = model.predict(request.text)
    return result

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
