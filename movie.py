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
[data-testid="stVerticalBlockBorderWrapper"] { background-color: #1e293b; border-radius: 16px; border: 1px solid #334155; padding: 20px; }
.title { text-align: center; font-size: 36px !important; color: #38bdf8 !important; }
.subtitle { text-align: center; color: #cbd5f5 !important; margin-bottom: 20px; }
[data-testid="stWidgetLabel"] p { color: #cbd5f5 !important; }
.result-positive { background: #14532d; padding: 20px; border-radius: 12px; color: #86efac; text-align: center; font-size: 22px; }
.result-negative { background: #7f1d1d; padding: 20px; border-radius: 12px; color: #fecaca; text-align: center; font-size: 22px; }
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
    review_input = st.text_area("✍️ Enter your movie review", height=150, placeholder="e.g., The cinematography was breathtaking...")
    if st.button("🔍 Analyze Sentiment", use_container_width=True):
        if not review_input.strip(): st.warning("Please enter a review.")
        else:
            with st.spinner("Analyzing..."):
                prediction = model.predict(vectorizer.transform([clean_text(review_input)]))[0]
                cls = "result-positive" if prediction == "positive" else "result-negative"
                emoji = "😊" if prediction == "positive" else "☹️"
                st.markdown(f"<div class='{cls}' role='status' aria-live='polite'>{emoji} {prediction.title()} Review</div>", unsafe_allow_html=True)



