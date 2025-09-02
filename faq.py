import streamlit as st
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("punkt")
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# -------------------
# Sample FAQs
# -------------------
faq_data = {
    "What is your return policy?": "You can return any item within 30 days of purchase with a valid receipt.",
    "Do you offer international shipping?": "Yes, we ship to over 50 countries worldwide.",
    "How can I track my order?": "You can track your order by logging into your account and checking the 'My Orders' section.",
    "What payment methods do you accept?": "We accept credit cards, debit cards, PayPal, and net banking.",
    "How do I contact customer support?": "You can reach us via email at support@example.com or call 1800-123-456."
}

questions = list(faq_data.keys())
answers = list(faq_data.values())

# -------------------
# Preprocessing function
# -------------------
def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    tokens = [w for w in tokens if w not in stop_words and w not in string.punctuation]
    return " ".join(tokens)

processed_questions = [preprocess(q) for q in questions]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_questions)

# -------------------
# Chatbot function
# -------------------
def get_answer(user_input):
    user_input = preprocess(user_input)
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    idx = similarity.argmax()
    return answers[idx]

# -------------------
# Streamlit UI
# -------------------
st.title("💬 FAQ Chatbot")

user_query = st.text_input("Ask me a question:")

if st.button("Get Answer"):
    if user_query.strip():
        response = get_answer(user_query)
        st.success(response)
    else:
        st.warning("Please enter a question.")
