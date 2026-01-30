import streamlit as st
import re
import nltk
import pickle
from nltk.corpus import stopwords

nltk.download('stopwords')

# ---------- Page Config ----------
st.set_page_config(
    page_title="Movie Review Sentiment",
    page_icon="🎬",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0f172a;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
.header-card {
    background: #1e293b;
    padding: 30px;
    border-radius: 16px;
    margin-bottom: 25px;
    border: 1px solid #334155;
}
.title { text-align: center; font-size: 36px; font-weight: 700; color: #38bdf8; margin-top: 0; margin-bottom: 8px; }
.subtitle { text-align: center; color: #cbd5f5; margin-top: 0; margin-bottom: 0; font-size: 18px; }
.result-positive {
    background: #14532d; padding: 15px; border-radius: 12px;
    color: #86efac; text-align: center; font-size: 22px;
}
.result-negative {
    background: #7f1d1d; padding: 15px; border-radius: 12px;
    color: #fecaca; text-align: center; font-size: 22px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Text Cleaning ----------
stop_words = stopwords.words('english')

def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [w for w in text if w not in stop_words]
    return ' '.join(text)

# ---------- Load PKL Files (NO CSV) ----------
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------- UI ----------
# Header Section
st.markdown("""
<div class='header-card'>
    <h1 class='title'>🎬 Movie Review Sentiment Analysis</h1>
    <p class='subtitle'>NLP-based Polarity Detection</p>
</div>
""", unsafe_allow_html=True)

# Input Section
review_input = st.text_area(
    "✍️ Enter your movie review",
    height=150,
    placeholder="Write your thoughts about the movie here..."
)

# Analysis Section
if st.button("🔍 Analyze Sentiment", help="Click to analyze the sentiment of your review"):
    if not review_input.strip():
        st.warning("⚠️ Please enter a review before analyzing.")
    else:
        with st.spinner("Analyzing sentiment..."):
            clean_review = clean_text(review_input)
            vector = vectorizer.transform([clean_review])
            prediction = model.predict(vector)[0]

            if prediction == "positive":
                st.markdown("<div class='result-positive' role='status' aria-live='polite'>😊 Positive Review</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='result-negative' role='status' aria-live='polite'>☹️ Negative Review</div>", unsafe_allow_html=True)



