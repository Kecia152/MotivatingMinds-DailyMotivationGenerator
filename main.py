#Motivation generator 
import streamlit as st
import requests, os
from dotenv import load_dotenv
from datetime import datetime
from transformers import pipeline

# Loading env vars
load_dotenv()
IBM_API_KEY = os.getenv("WATSON_API_KEY")
PROJECT_ID = os.getenv("WATSON_PROJECT_ID")
MODEL_ID = "meta-llama/llama-2-13b-chat"
REGION = "us-south"
#sentiment analysis pipeline
sentiment = pipeline("sentiment-analysis")
# Frontend 
st.set_page_config(page_title="Motivating Minds", page_icon="💬")
st.markdown("""
    <style>
        .title { font-size: 2.2em; font-weight: bold; color: #2e8b57; }
        .subtle { color: #6c6c6c; font-size: 0.92em; }
        .quote-box {
            font-style: italic;
            color: #333;
            background: #f0f9f3;
            border-left: 4px solid #2e8b57;
            padding: 1em; margin: 1em 0; border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💬 Motivating Minds</div>', unsafe_allow_html=True)
st.markdown('<div class="subtle">Built with generative ai | Personalized with  Prompt Engineering</div>', unsafe_allow_html=True)
st.caption("An AI-powered, motivation generator 🌟")
st.markdown("Hi there 👋  \nFeeling a little off today? It’s okay — everyone does sometimes.  \nJust share your current state of mind, and I’ll bring in a spark of motivation .")

with st.form("mood_form"):
    st.subheader("✨ Let’s personalize your quote")
    col1, col2 = st.columns(2)
    mood = col1.selectbox("😌 How do you feel today?What's the current vibe?", [
        "Anxious or overwhelmed", "Low energy / demotivated", "Distracted or unfocused",
        "Happy and want more positivity", "Excited but nervous", "Worried about studies", "Lost or confused"
    ])
    tone = col2.selectbox("🎭 Choose the tone you like", [
        "Gentle", "Confident", "Poetic", "Funny", "Philosophical"
    ])
    submitted = st.form_submit_button("✨ Generate My Motivation!")

#quote history
if "quote_history" not in st.session_state:
    st.session_state.quote_history = []

#access token and motivation generation
def fetch_ibm_token(key):
    res = requests.post(
        "https://iam.cloud.ibm.com/identity/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"apikey": key, "grant_type": "urn:ibm:params:oauth:grant-type:apikey"}
    )
    return res.json().get("access_token", "")

def generate_motivation(mood, tone, token):
    prompt = f"Write a short, {tone.lower()} motivational quote meant to encourage someone who is currently feeling {mood.lower()}. The quote should feel personal and original — avoid common phrases or clichés."
    url = f"https://{REGION}.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    body = {
        "model_id": MODEL_ID, "input": prompt, "project_id": PROJECT_ID,
        "parameters": { "max_new_tokens": 80, "temperature": 0.85, "top_k": 60 }
    }
    res = requests.post(url, headers=headers, json=body)
    return res.json()["results"][0]["generated_text"].strip()

if submitted:
    with st.spinner("Talking to watsonx... crafting your spark 🔥"):
        try:
            token = fetch_ibm_token(IBM_API_KEY)
            quote = generate_motivation(mood, tone, token)
            result = sentiment(quote)[0]

            st.success("💡 Here's your personalized quote:")
            st.markdown(f'<div class="quote-box">{quote}</div>', unsafe_allow_html=True)
            st.caption(f"🧠 Sentiment: **{result['label']}** ({round(result['score']*100)}% confidence)")

            st.session_state.quote_history.append((quote, datetime.now().strftime("%I:%M %p").lstrip("0")))
        except Exception:
            st.error("❌ Oops! Something went wrong. Please retry or check your API.")

# Quote history
if st.session_state.quote_history:
    with st.expander("📜 My Quote Log"):
        for i, (q, t) in enumerate(reversed(st.session_state.quote_history)):
            st.markdown(f"**{i+1}.** *{q}*  \n_🕓 {t}_")

st.markdown("---")
st.markdown("Project Made with 💙 by kecia")
