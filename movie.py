import streamlit as st
import re
import nltk
import pickle
from nltk.corpus import stopwords

# ---------- Page Config ----------
st.set_page_config(
    page_title="Movie Review Sentiment",
    page_icon="🎬",
    layout="centered"
)

# ---------- Resource Loading (Cached) ----------
@st.cache_resource
def load_resources():
    nltk.download('stopwords', quiet=True)
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    stop_words = set(stopwords.words('english'))
    return model, vectorizer, stop_words

model, vectorizer, stop_words = load_resources()

# ---------- Custom CSS ----------
st.markdown("""
<style>
/* Target the main app container for background */
[data-testid="stAppViewContainer"] { background-color: #0f172a; }
[data-testid="stHeader"] { background: transparent; }

/* Target the container(border=True) for card styling */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: #1e293b;
    padding: 25px;
    border-radius: 16px;
    border: 1px solid #334155 !important;
}

.title { text-align: center !important; font-size: 36px !important; font-weight: 700 !important; color: #38bdf8 !important; margin-bottom: 0px !important; }
.subtitle { text-align: center !important; color: #cbd5f5 !important; margin-bottom: 20px !important; }

/* Ensure button has high contrast */
[data-testid="stBaseButton-secondary"] {
    background-color: #38bdf8 !important;
    color: #0f172a !important;
    border: none;
}

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
def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [w for w in text if w not in stop_words]
    return ' '.join(text)

# ---------- UI ----------
with st.container(border=True):
    st.markdown("<h1 class='title'>🎬 Movie Review Sentiment Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>NLP-based Polarity Detection</p>", unsafe_allow_html=True)

    review_input = st.text_area(
        "✍️ Enter your movie review",
        height=150,
        placeholder="e.g., 'The cinematography was stunning and the acting was top-notch!'"
    )

    if st.button("🔍 Analyze Sentiment", use_container_width=True):
        if review_input.strip() == "":
            st.warning("Please enter a review")
        else:
            with st.spinner("Analyzing..."):
                clean_review = clean_text(review_input)
                vector = vectorizer.transform([clean_review])
                prediction = model.predict(vector)[0]

                if prediction == "positive":
                    st.markdown(
                        "<div class='result-positive' role='status' aria-live='polite'>😊 Positive Review</div>",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        "<div class='result-negative' role='status' aria-live='polite'>☹️ Negative Review</div>",
                        unsafe_allow_html=True
                    )
