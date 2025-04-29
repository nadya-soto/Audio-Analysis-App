# classifier.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

def train_model():
    data = {
        "text": [
            "I need help with my rent",
            "I'm being harassed at work",
            "I can't afford my bills",
            "My landlord is not responding",
            "I'm worried about debt",
            "Someone stole my identity"
        ],
        "label": [
            "housing",
            "legal",
            "financial",
            "housing",
            "financial",
            "legal"
        ]
    }
    df = pd.DataFrame(data)
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(df["text"], df["label"])
    return model 

def predict_category(model, text):
    return model.predict([text])[0]
