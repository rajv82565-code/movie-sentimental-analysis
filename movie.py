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
[data-testid="stAppViewContainer"] { background-color: #0f172a; }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stVerticalBlockBorderWrapper"] { background: #1e293b; padding: 25px; border-radius: 16px; border: none !important; }
.title { text-align: center; font-size: 36px; font-weight: 700; color: #38bdf8 !important; margin-bottom: 0px; }
.subtitle { text-align: center; color: #cbd5f5 !important; font-size: 18px; margin-top: -10px; }
[data-testid="stButton"] button { background-color: #38bdf8; color: #0f172a; border-radius: 8px; font-weight: 600; width: 100%; }
.result-positive { background: #14532d; padding: 15px; border-radius: 12px; color: #86efac; text-align: center; font-size: 22px; }
.result-negative { background: #7f1d1d; padding: 15px; border-radius: 12px; color: #fecaca; text-align: center; font-size: 22px; }
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
with st.container(border=True):
    st.markdown("<h1 class='title'>🎬 Movie Review Sentiment Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>NLP-based Polarity Detection</p><br>", unsafe_allow_html=True)

    review_input = st.text_area(
        "✍️ Enter your movie review",
        height=150,
        placeholder="e.g., 'The cinematography was stunning and the acting was top-notch!'"
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
                st.markdown("<div class='result-positive' role='status' aria-live='polite'>😊 Positive Review</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='result-negative' role='status' aria-live='polite'>☹️ Negative Review</div>", unsafe_allow_html=True)



