import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def fetch_transcript_text(transcript_url: str) -> str:
    import requests
    res = requests.get(transcript_url)
    res.raise_for_status()
    data = res.json()
    return data["results"]["transcripts"][0]["transcript"]


def summarize_text(transcript_text: str) -> str:
    prompt = f"Summarize this meeting transcript:\n\n{transcript_text}"
    response = model.generate_content(prompt)
    return response.text
