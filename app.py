import streamlit as st
import random
import pandas as pd

# -----------------------------
# PAGE SETUP
# -----------------------------
st.set_page_config(page_title="Social Media Analyzer", layout="wide")
st.title("🌐 Social Media Topic Analyzer")

# -----------------------------
# USER INPUT
# -----------------------------
topic = st.text_input("Enter a topic", value="finance")

if not topic.strip():
    st.warning("Please enter a topic to see results.")
    st.stop()

# -----------------------------
# DATA GENERATION
# -----------------------------
def generate_words(topic, platform):
    base = [topic, "market", "growth", "trend", "analysis", "economy"]
    bias = {
        "Facebook": ["community", "share", "group"],
        "Twitter": ["tweet", "hashtag", "viral"],
        "Reddit": ["upvote", "comment", "discussion"]
    }
    return random.choices(base + bias[platform], k=500)

# -----------------------------
# VISUALIZATION
# -----------------------------
def show_chart(words, platform):
    freq = pd.Series(words).value_counts().head(15)
    st.subheader(f"{platform} Keyword Frequency")
    st.bar_chart(freq)
    st.success("✅ Results updated")

# -----------------------------
# TABS
# -----------------------------
tab1, tab2, tab3 = st.tabs(["Facebook", "Twitter", "Reddit"])

with tab1:
    fb_words = generate_words(topic, "Facebook")
    show_chart(fb_words, "Facebook")

with tab2:
    tw_words = generate_words(topic, "Twitter")
    show_chart(tw_words, "Twitter")

with tab3:
    rd_words = generate_words(topic, "Reddit")
    show_chart(rd_words, "Reddit")

