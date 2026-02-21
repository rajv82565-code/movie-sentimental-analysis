import pandas as pd
import re
import nltk
import pickle
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('stopwords')
stop_words = stopwords.words('english')

def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [w for w in text if w not in stop_words]
    return ' '.join(text)

print("Loading data...")
data = pd.read_csv("IMDB Dataset.csv")

print("Cleaning text...")
data['clean_review'] = data['review'].apply(clean_text)

print("Vectorizing...")
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(data['clean_review'])
y = data['sentiment']

print("Training model...")
model = MultinomialNB()
model.fit(X, y)

print("Saving models...")
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model & Vectorizer saved successfully")
