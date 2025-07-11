# app/main.py

from fastapi import FastAPI
from app.routes import summarize, transcribe

app = FastAPI()

app.include_router(summarize.router)
app.include_router(transcribe.router)
