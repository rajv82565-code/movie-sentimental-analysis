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
    background-color: transparent !important;
}
[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #1e293b !important;
    border: 1px solid #334155 !important;
    border-radius: 16px !important;
    padding: 10px !important;
}
.title { text-align: center; font-size: 36px !important; font-weight: 700 !important; color: #38bdf8 !important; margin-bottom: 0px !important; }
.subtitle { text-align: center; color: #94a3b8 !important; font-size: 18px !important; margin-bottom: 20px !important; }
.result-positive {
    background: #14532d; padding: 15px; border-radius: 12px;
    color: #86efac; text-align: center; font-size: 22px; margin-top: 20px;
}
.result-negative {
    background: #7f1d1d; padding: 15px; border-radius: 12px;
    color: #fecaca; text-align: center; font-size: 22px; margin-top: 20px;
}
[data-testid="stButton"] button {
    background-color: #38bdf8 !important;
    color: #0f172a !important;
    border: none !important;
}
[data-testid="stButton"] button:hover {
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
    st.markdown("""
        <h1 class='title'>🎬 Movie Review Sentiment Analysis</h1>
        <p class='subtitle'>NLP-based Polarity Detection</p>
    """, unsafe_allow_html=True)

    review_input = st.text_area(
        "✍️ Enter your movie review",
        height=150,
        placeholder="e.g., 'The cinematography was stunning and the acting was top-notch!'"
    )

    if st.button("🔍 Analyze Sentiment"):
        if review_input.strip() == "":
            st.warning("Please enter a review")
        else:
            clean_review = clean_text(review_input)
            vector = vectorizer.transform([clean_review])
            prediction = model.predict(vector)[0]

            if prediction == "positive":
                st.markdown("<div role='status' aria-live='polite' class='result-positive'>😊 Positive Review</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div role='status' aria-live='polite' class='result-negative'>☹️ Negative Review</div>", unsafe_allow_html=True)



