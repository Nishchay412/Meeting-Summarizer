# app/routes/transcribe.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.transcribe import start_transcription_job

router = APIRouter()

class TranscribeRequest(BaseModel):
    s3_url: str

@router.post("/transcribe")
def transcribe_audio(request: TranscribeRequest):
    job_name = start_transcription_job(request.s3_url)
    return {"message": "Transcription started", "job_name": job_name}
