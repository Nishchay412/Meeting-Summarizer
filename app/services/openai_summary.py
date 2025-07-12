import requests
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def fetch_transcript_text(transcript_url: str) -> str:
    res = requests.get(transcript_url)
    res.raise_for_status()
    data = res.json()
    return data["results"]["transcripts"][0]["transcript"]

def summarize_text(text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a meeting assistant. Summarize the meeting in 5 bullet points."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()
