import streamlit as st
import re
import nltk
import pickle
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = stopwords.words('english')

def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [w for w in text if w not in stop_words]
    return ' '.join(text)

# Load PKL files
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.set_page_config(page_title="Movie Sentiment", page_icon="🎬")

st.title("🎬 Movie Review Sentiment Analysis")
review = st.text_area("Enter movie review")

if st.button("Analyze"):
    if review.strip():
        review_clean = clean_text(review)
        vector = vectorizer.transform([review_clean])
        prediction = model.predict(vector)[0]
        st.success(f"Sentiment: {prediction.upper()}")
    else:
        st.warning("Please enter a review")


