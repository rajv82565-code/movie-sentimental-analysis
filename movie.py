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
[data-testid="stAppViewContainer"] { background-color: #0f172a !important; }
[data-testid="stVerticalBlockBorderWrapper"] {
    background: #1e293b !important;
    padding: 25px !important;
    border-radius: 16px !important;
    border: 1px solid #334155 !important;
}
.title { text-align: center; font-size: 36px !important; font-weight: 700 !important; color: #38bdf8 !important; margin-bottom: 0px !important; }
.subtitle { text-align: center; color: #ffffff !important; margin-bottom: 20px !important; opacity: 0.8; }
[data-testid="stWidgetLabel"] p { color: #ffffff !important; opacity: 0.9 !important; }
.result-positive {
    background: #14532d; padding: 15px; border-radius: 12px;
    color: #86efac; text-align: center; font-size: 22px;
}
.result-negative {
    background: #7f1d1d; padding: 15px; border-radius: 12px;
    color: #fecaca; text-align: center; font-size: 22px;
}
[data-testid="stBaseButton-secondary"] {
    background-color: #38bdf8 !important;
    color: #0f172a !important;
    border: none !important;
}
[data-testid="stBaseButton-secondary"]:hover {
    background-color: #7dd3fc !important;
    color: #0f172a !important;
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
    st.markdown("<h1 class='title'>🎬 Movie Review Sentiment Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>NLP-based Polarity Detection</p>", unsafe_allow_html=True)

    review_input = st.text_area(
        "✍️ Enter your movie review",
        height=150,
        placeholder="I absolutely loved this movie! The acting was superb and the plot kept me on the edge of my seat..."
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



