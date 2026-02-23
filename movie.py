import streamlit as st
import pandas as pd
import re
import nltk
import pickle
import html
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

@st.cache_resource
def load_resources():
    nltk.download('stopwords')
    try:
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
        with open("vectorizer.pkl", "rb") as f:
            vectorizer = pickle.load(f)
        return model, vectorizer
    except FileNotFoundError:
        return None, None

model, vectorizer = load_resources()
if model is None:
    st.error("Model files not found. Please run the Jupyter notebook first.")
    st.stop()

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
    background-color: #1e293b !important;
    padding: 25px !important;
    border-radius: 16px !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    border: none !important;
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

# ---------- UI ----------
with st.container(border=True):
    st.markdown("<div class='title' role='heading' aria-level='1'>🎬 Movie Review Sentiment Analysis</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle' role='heading' aria-level='2'>NLP-based Polarity Detection</div><br>", unsafe_allow_html=True)

with st.form("search_form", border=False):
    movie_name = st.text_input(
        "✍️ Enter a Movie Name",
        placeholder="e.g. Inception, The Matrix..."
    )
    submit_button = st.form_submit_button("🔍 Analyze Sentiment")

if submit_button:
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
                
                escaped_name = html.escape(movie_name)
                st.markdown(f"### Results for '**{escaped_name}**'")
                st.write(f"Found exactly {total} review(s) mentioning this movie.")
                
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
                sentiment_html = ""
                if pos_count > neg_count and pos_count >= neu_count:
                    sentiment_html = "<div class='result-positive'><span role='img' aria-label='happy face'>😊</span> Overall Positive</div>"
                elif neg_count > pos_count and neg_count >= neu_count:
                    sentiment_html = "<div class='result-negative'><span role='img' aria-label='sad face'>☹️</span> Overall Negative</div>"
                else:
                    sentiment_html = "<div class='result-neutral'><span role='img' aria-label='neutral face'>😐</span> Overall Neutral</div>"

                st.markdown(f"<div role='status' aria-live='polite'>{sentiment_html}</div>", unsafe_allow_html=True)
