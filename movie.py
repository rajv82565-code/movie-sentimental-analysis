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
    background-color: #0f172a !important;
}
[data-testid="stHeader"] {
    background: transparent !important;
}
[data-testid="stTextArea"] textarea {
    background-color: #1e293b !important;
    color: #cbd5e1 !important;
    border: 1px solid #334155 !important;
}
[data-testid="stButton"] button {
    background-color: #38bdf8 !important;
    color: #0f172a !important;
    font-weight: 600 !important;
}
h1.title { text-align: center; font-size: 36px; font-weight: 700; color: #38bdf8; margin-bottom: 0px; }
p.subtitle { text-align: center; color: #cbd5f5; font-size: 18px; margin-bottom: 25px; }
.result-positive {
    background: #064e3b; padding: 15px; border-radius: 12px;
    color: #6ee7b7; text-align: center; font-size: 22px;
    border: 1px solid #059669;
}
.result-negative {
    background: #7f1d1d; padding: 15px; border-radius: 12px;
    color: #fca5a5; text-align: center; font-size: 22px;
    border: 1px solid #b91c1c;
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
st.markdown("<h1 class='title'>🎬 Movie Review Sentiment Analysis</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>NLP-based Polarity Detection</p>", unsafe_allow_html=True)

review_input = st.text_area(
    "✍️ Enter your movie review",
    height=150,
    placeholder="The cinematography was breathtaking and the acting was top-notch. I highly recommend it!"
)

if st.button("🔍 Analyze Sentiment"):
    if review_input.strip() == "":
        st.warning("Please enter a review")
    else:
        with st.spinner("Analyzing sentiment..."):
            clean_review = clean_text(review_input)
            vector = vectorizer.transform([clean_review])
            prediction = model.predict(vector)[0]

        if prediction == "positive":
            st.markdown("<p class='result-positive' role='status' aria-live='polite'>😊 Positive Review</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='result-negative' role='status' aria-live='polite'>☹️ Negative Review</p>", unsafe_allow_html=True)



