# 🎥 YouTube Transcription & Summarizer

A Python-based web app that extracts transcripts from YouTube videos and generates concise, AI-powered summaries using OpenAI's GPT models. Built with **Streamlit** for a simple web interface.

## ✨ Features

- 🔗 Input any public YouTube video URL
- 📝 Extracts and displays the full transcript
- 🧠 Summarizes the transcript using OpenAI's GPT
- 📋 Copy or download the summary
- 🌐 Clean and minimal Streamlit web UI

## 🚀 Live Demo

🔗 [Click here to try the app](https://your-app-link.streamlit.app)  
(*Replace with your deployed Streamlit link*)

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenAI GPT (via `openai` package)
- `youtube-transcript-api`
- `dotenv` for managing API keys

## 📦 Installation

```bash
git clone https://github.com/yourusername/yt-transcription-summarizer.git
cd yt-transcription-summarizer
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
