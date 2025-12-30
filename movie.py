import streamlit as st
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

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
body {
    background-color: #0f172a;
}
.card {
    background: #1e293b;
    padding: 25px;
    border-radius: 16px;
}
.title {
    text-align: center;
    font-size: 36px;
    font-weight: 700;
    color: #38bdf8;
}
.subtitle {
    text-align: center;
    color: #cbd5f5;
}
.result-positive {
    background: #14532d;
    padding: 15px;
    border-radius: 12px;
    color: #86efac;
    text-align: center;
    font-size: 22px;
}
.result-negative {
    background: #7f1d1d;
    padding: 15px;
    border-radius: 12px;
    color: #fecaca;
    text-align: center;
    font-size: 22px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Text Cleaning ----------
stop_words = stopwords.words('english')

def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    text = [word for word in text if word not in stop_words]
    return ' '.join(text)

# ---------- Load Dataset (FIXED LINE) ----------
data = pd.read_csv("IMDB Dataset.csv")   # ✅ FIXED
data['clean_review'] = data['review'].apply(clean_text)

# ---------- Vectorizer & Model ----------
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(data['clean_review'])
y = data['sentiment']

model = MultinomialNB()
model.fit(X, y)

# ---------- UI ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("<div class='title'>🎬 Movie Review Sentiment Analysis</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>NLP-based Polarity Detection</div><br>", unsafe_allow_html=True)

review_input = st.text_area("✍️ Enter your movie review", height=150)

if st.button("🔍 Analyze Sentiment"):
    if review_input.strip() == "":
        st.warning("Please enter a review")
    else:
        clean_review = clean_text(review_input)
        vector = vectorizer.transform([clean_review])
        prediction = model.predict(vector)[0]

        if prediction == "positive":
            st.markdown("<div class='result-positive'>😊 Positive Review</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result-negative'>☹️ Negative Review</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

