import streamlit as st
import requests
from transformers import pipeline
from fastapi import FastAPI
import webbrowser

# Loading an emotion analysis model from Hugging Face
emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)

# Spotify search URL base
SPOTIFY_SEARCH_URL = "https://open.spotify.com/search/"

def analyze_emotion(text):
    # Get the predicted emotion from the classifier
    result = emotion_pipeline(text)
    # Convert label to lowercase for consistency
    emotion = result[0]['label'].lower()
    
    # Mapping model's output to your desired emotion categories
    mapping = {
        "anger": "anger",
        "disgust": "anger",
        "fear": "anxiety",
        "joy": "happy",
        "neutral": "calm",
        "sadness": "sadness",
        "love" : "love"
    }
    # Default to the classifier's label if not explicitly mapped
    return mapping.get(emotion, emotion)

def get_spotify_search_url(emotion):
    return f"{SPOTIFY_SEARCH_URL}{emotion}"

# FastAPI app definition
app = FastAPI()

@app.get("/get_playlist")
def get_playlist(text: str):
    emotion = analyze_emotion(text)
    search_url = get_spotify_search_url(emotion)
    return {"emotion": emotion, "spotify_url": search_url}

# Streamlit UI
st.title("🎵 Emotion-Based Playlist Generator")
user_input = st.text_area("Enter your mood or thoughts:")

    
if st.button("Generate Playlist"):
    if user_input.strip():
        emotion = analyze_emotion(user_input)
        search_url = get_spotify_search_url(emotion)

        st.success(f"Detected Emotion: **{emotion.capitalize()}**")
        st.markdown(f"[🎧 Open Spotify Playlist]({search_url})", unsafe_allow_html=True)

        # Open in a browser (optional for local use)
        webbrowser.open(search_url)
    else:
        st.warning("Please enter some text to analyze your mood.")