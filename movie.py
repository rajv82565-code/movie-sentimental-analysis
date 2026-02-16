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
[data-testid="stVerticalBlockBorderWrapper"] { background: #1e293b; border-radius: 16px; border: 1px solid #334155; }
.title { text-align: center; font-size: 36px !important; font-weight: 700; color: #38bdf8; margin-bottom: 0px; }
.subtitle { text-align: center; color: #ffffff; font-size: 18px; margin-bottom: 25px; }
.result-positive {
    background: #14532d; padding: 15px; border-radius: 12px;
    color: #86efac; text-align: center; font-size: 22px; margin-top: 20px;
}
.result-negative {
    background: #7f1d1d; padding: 15px; border-radius: 12px;
    color: #fecaca; text-align: center; font-size: 22px; margin-top: 20px;
}
[data-testid="stButton"] button { background-color: #38bdf8; color: #0f172a; font-weight: 600; }
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
    st.markdown("<p class='subtitle'>NLP-based Polarity Detection</p>", unsafe_allow_html=True)

    review_input = st.text_area("✍️ Enter your movie review", height=150, placeholder="e.g. This movie was a masterpiece of storytelling...")

    if st.button("🔍 Analyze Sentiment", use_container_width=True):
        if review_input.strip() == "":
            st.warning("Please enter a review")
        else:
            with st.spinner("Analyzing sentiment..."):
                clean_review = clean_text(review_input)
                vector = vectorizer.transform([clean_review])
                prediction = model.predict(vector)[0]

                res_class = "result-positive" if prediction == "positive" else "result-negative"
                res_text = "😊 Positive Review" if prediction == "positive" else "☹️ Negative Review"
                st.markdown(f"<div class='{res_class}' role='status' aria-live='polite'>{res_text}</div>", unsafe_allow_html=True)



