from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

from src.data.load_data import load_jsonl

data = load_jsonl("data/annotations/annotated_data.jsonl")

texts = [d["text"] for d in data]
labels = [d["label"] for d in data]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

print("Model trained")
