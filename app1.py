import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import openai
import os
from dotenv import load_dotenv
import re

# Load your OpenAI key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Extract video ID from URL
def extract_video_id(url):
    match = re.search(r"v=([^&]+)", url)
    return match.group(1) if match else None

# Get transcript
def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([entry['text'] for entry in transcript])
    return full_text

# Summarize transcript
def summarize_text(text):
    prompt = f"Summarize the following YouTube transcript into bullet points:\n\n{text[:3000]}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=300
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("🎬 YouTube Transcript Summarizer")

url = st.text_input("Paste a YouTube video URL:")

if url:
    try:
        video_id = extract_video_id(url)
        transcript = get_transcript(video_id)
        summary = summarize_text(transcript)
        st.subheader("📝 Summary")
        st.write(summary)
    except Exception as e:
        st.error(f"Error: {e}")
