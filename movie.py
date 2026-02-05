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
[data-testid="stHeader"] { background: rgba(0,0,0,0); }
[data-testid="stVerticalBlockBorderWrapper"] {
    background: #1e293b;
    padding: 25px;
    border-radius: 16px;
    border: 1px solid #334155;
}
.title { text-align: center; font-size: 32px; font-weight: 700; color: #38bdf8; margin-bottom: 0px; }
.subtitle { text-align: center; color: #cbd5f5; font-size: 16px; margin-bottom: 20px; }
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
with st.container(border=True):
    st.markdown("<div class='title'>🎬 Movie Review Sentiment Analysis</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>NLP-based Polarity Detection</div>", unsafe_allow_html=True)

    review_input = st.text_area(
        "✍️ Enter your movie review",
        height=150,
        placeholder="Type or paste your movie review here..."
    )

    if st.button("🔍 Analyze Sentiment", use_container_width=True):
        if not review_input.strip():
            st.warning("Please enter a review to analyze.")
        else:
            with st.spinner("Analyzing sentiment..."):
                clean_review = clean_text(review_input)
                vector = vectorizer.transform([clean_review])
                prediction = model.predict(vector)[0]

                if prediction == "positive":
                    st.markdown("<div class='result-positive' role='status' aria-live='polite'>😊 Positive Review</div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='result-negative' role='status' aria-live='polite'>☹️ Negative Review</div>", unsafe_allow_html=True)



