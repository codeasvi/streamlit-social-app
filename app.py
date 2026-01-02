import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Social Media Analyzer", layout="wide")
st.title("🌐 Social Media Topic Analyzer")

topic = st.text_input("Enter a topic", "finance")

def generate_words(topic, platform):
    base = [topic, "market", "growth", "trend", "analysis", "economy"]
    bias = {
        "Facebook": ["community", "share", "group"],
        "Twitter": ["tweet", "hashtag", "viral"],
        "Reddit": ["upvote", "comment", "discussion"]
    }
    return random.choices(base + bias[platform], k=500)

def show_chart(words, platform):
    freq = pd.Series(words).value_counts().head(15)
    st.subheader(f"{platform} Keyword Frequency")
    st.bar_chart(freq)

tab1, tab2, tab3 = st.tabs(["Facebook", "Twitter", "Reddit"])

with tab1:
    show_chart(generate_words(topic, "Facebook"), "Facebook")

with tab2:
    show_chart(generate_words(topic, "Twitter"), "Twitter")

with tab3:
    show_chart(generate_words(topic, "Reddit"), "Reddit")
