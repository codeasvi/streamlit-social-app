import streamlit as st
import random
import pandas as pd

# -----------------------------
# PAGE SETUP
# -----------------------------
st.set_page_config(page_title="Social Media Trends", layout="wide")
st.title("📊 Social Media Trending Topics Analyzer")

st.caption("Click a trending topic to see instant analysis")

# -----------------------------
# TRENDING TOPICS (SIMULATED)
# -----------------------------
TRENDING_TOPICS = {
    "Facebook": ["Finance", "Crypto", "AI", "Stock Market", "Startups"],
    "Twitter": ["Breaking News", "Elections", "Tech Updates", "Crypto", "Sports"],
    "Reddit": ["Investing", "WallStreetBets", "AI Tools", "Career Advice", "Gaming"]
}

# -----------------------------
# WORD GENERATOR
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
# SHOW RESULT
# -----------------------------
def show_result(topic, platform):
    words = generate_words(topic, platform)
    freq = pd.Series(words).value_counts().head(15)

    st.subheader(f"{platform} Topic Analysis: **{topic}**")
    st.bar_chart(freq)
    st.success("✅ Trending topic analyzed")

# -----------------------------
# TABS
# -----------------------------
tab1, tab2, tab3 = st.tabs(["📘 Facebook", "🐦 Twitter", "👽 Reddit"])

# -----------------------------
# FACEBOOK TAB
# -----------------------------
with tab1:
    st.subheader("🔥 Facebook Trending Topics")

    for topic in TRENDING_TOPICS["Facebook"]:
        if st.button(topic, key=f"fb_{topic}"):
            show_result(topic, "Facebook")

# -----------------------------
# TWITTER TAB
# -----------------------------
with tab2:
    st.subheader("🔥 Twitter Trending Topics")

    for topic in TRENDING_TOPICS["Twitter"]:
        if st.button(topic, key=f"tw_{topic}"):
            show_result(topic, "Twitter")

# -----------------------------
# REDDIT TAB
# -----------------------------
with tab3:
    st.subheader("🔥 Reddit Trending Topics")

    for topic in TRENDING_TOPICS["Reddit"]:
        if st.button(topic, key=f"rd_{topic}"):
            show_result(topic, "Reddit")



