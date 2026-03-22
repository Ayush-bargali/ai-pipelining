import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import numpy as np

TRAIN_DATA = ['positive'] * 100 + ['negative'] * 100
TRAIN_LABELS = [1] * 100 + [0] * 100

class SentimentModel:
    def __init__(self):
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=10)),
            ('clf', LogisticRegression())
        ])
        self.pipeline.fit(TRAIN_DATA, TRAIN_LABELS)
    
    def predict(self, text: str):
        proba = self.pipeline.predict_proba([text])[0]
        confidence = np.max(proba)
        sentiment = 'POSITIVE' if proba[1] > proba[0] else 'NEGATIVE'
        return {'sentiment': sentiment, 'confidence': round(float(confidence), 4)}

model = SentimentModel()

