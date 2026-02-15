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
h1 { text-align: center; font-size: 36px !important; font-weight: 700 !important; color: #38bdf8 !important; }
.subtitle { text-align: center; color: #ffffff; margin-bottom: 2rem; }
[data-testid="stWidgetLabel"] p { color: #ffffff !important; }
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
    st.markdown("<h1>🎬 Movie Review Sentiment Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>NLP-based Polarity Detection</p>", unsafe_allow_html=True)

    review_input = st.text_area(
        "✍️ Enter your movie review",
        height=150,
        placeholder="e.g., The cinematography was stunning and the acting was top-notch!"
    )

    if st.button("🔍 Analyze Sentiment", use_container_width=True):
        if review_input.strip() == "":
            st.warning("Please enter a review before analyzing.")
        else:
            with st.spinner("Analyzing sentiment..."):
                clean_review = clean_text(review_input)
                vector = vectorizer.transform([clean_review])
                prediction = model.predict(vector)[0]

                result_html = f"""
                <div role="status" aria-live="polite" class='result-{"positive" if prediction == "positive" else "negative"}'>
                    {"😊 Positive Review" if prediction == "positive" else "☹️ Negative Review"}
                </div>
                """
                st.markdown(result_html, unsafe_allow_html=True)



