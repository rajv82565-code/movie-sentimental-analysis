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

@st.cache_data
def load_data():
    try:
        return pd.read_csv("IMDB Dataset.csv")
    except FileNotFoundError:
        return pd.DataFrame(columns=["review", "sentiment"])

df = load_data()

# ---------- Custom CSS (React-style) ----------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0f172a;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
[data-testid="stVerticalBlockBorderWrapper"] {
    background: #1e293b;
    border: 1px solid #334155 !important;
    border-radius: 16px;
    padding: 10px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}
.title {
    text-align: center;
    font-size: 36px !important;
    font-weight: 700 !important;
    color: #38bdf8 !important;
    margin-bottom: 0.5rem !important;
}
.subtitle {
    text-align: center;
    color: #cbd5f5 !important;
    font-size: 1.1rem !important;
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
.result-neutral {
    background: #475569;
    padding: 15px;
    border-radius: 12px;
    color: #e2e8f0;
    text-align: center;
    font-size: 22px;
}
.stat-box {
    background: #334155;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    margin: 10px 0;
}
.stat-value {
    font-size: 32px;
    font-weight: 700;
}
.stat-label {
    font-size: 16px;
    color: #cbd5e1;
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
    text = text.lower()
    text = text.split()
    text = [word for word in text if word not in stop_words]
    return ' '.join(text)

# ---------- Load Model and Vectorizer ----------
import pickle
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
except FileNotFoundError:
    st.error("Model files not found. Please run the Jupyter notebook first.")
    st.stop()

# ---------- UI ----------
with st.container(border=True):
    st.markdown("<h1 class='title'>🎬 Movie Review Sentiment Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>NLP-based Polarity Detection</p><br>", unsafe_allow_html=True)

    movie_name = st.text_input(
        "✍️ Enter a Movie Name",
        placeholder="e.g. The Dark Knight, Inception, Toy Story...",
        help="Type a movie title to analyze sentiment from our dataset of 50k IMDB reviews."
    )

    if st.button("🔍 Analyze Sentiment", use_container_width=True):
        if movie_name.strip() == "":
            st.warning("Please enter a movie name")
        else:
            with st.spinner(f"Searching for reviews mentioning '{movie_name}'..."):
                # Search dataset for reviews containing the movie name
                relevant_reviews = df[df['review'].str.contains(movie_name, case=False, na=False)]
                
                if len(relevant_reviews) == 0:
                    st.warning(f"No reviews found in the dataset for '{movie_name}'. Please try another movie.")
                else:
                    reviews_text = relevant_reviews['review'].tolist()

                    # Transform data and predict probabilities
                    clean_reviews = [clean_text(r) for r in reviews_text]
                    vectors = vectorizer.transform(clean_reviews)
                    probs = model.predict_proba(vectors)

                    pos_count = 0
                    neg_count = 0
                    neu_count = 0

                    # We have two classes: likely 0 is negative and 1 is positive
                    # Let's dynamically check classes just in case
                    pos_idx = list(model.classes_).index("positive")
                    neg_idx = list(model.classes_).index("negative")

                    for prob in probs:
                        if prob[pos_idx] > 0.6:
                            pos_count += 1
                        elif prob[neg_idx] > 0.6:
                            neg_count += 1
                        else:
                            neu_count += 1

                    total = len(reviews_text)

                    st.markdown(f"### Results for '**{movie_name}**'")
                    st.markdown(f"<div role='status' aria-live='polite'>Found exactly {total} review(s) mentioning this movie.</div>", unsafe_allow_html=True)

                    # Display Results
                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.markdown(f"""
                        <div class='stat-box'>
                            <div class='stat-label'>Positive</div>
                            <div class='stat-value' style='color: #86efac;'>{pos_count}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    with col2:
                        st.markdown(f"""
                        <div class='stat-box'>
                            <div class='stat-label'>Neutral</div>
                            <div class='stat-value' style='color: #e2e8f0;'>{neu_count}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    with col3:
                        st.markdown(f"""
                        <div class='stat-box'>
                            <div class='stat-label'>Negative</div>
                            <div class='stat-value' style='color: #fca5a5;'>{neg_count}</div>
                        </div>
                        """, unsafe_allow_html=True)

                    st.markdown("<br>", unsafe_allow_html=True)

                    # Overall sentiment logic
                    if pos_count > neg_count and pos_count >= neu_count:
                        st.markdown("<div class='result-positive' role='img' aria-label='Overall Positive'>😊 Overall Positive</div>", unsafe_allow_html=True)
                    elif neg_count > pos_count and neg_count >= neu_count:
                        st.markdown("<div class='result-negative' role='img' aria-label='Overall Negative'>☹️ Overall Negative</div>", unsafe_allow_html=True)
                    else:
                        st.markdown("<div class='result-neutral' role='img' aria-label='Overall Neutral'>😐 Overall Neutral</div>", unsafe_allow_html=True)
