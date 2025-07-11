# app/routes/transcribe.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.transcribe import start_transcription_job
from app.services.transcribe import get_transcription_status

router = APIRouter()

class TranscribeRequest(BaseModel):
    s3_url: str

@router.post("/transcribe")
def transcribe_audio(request: TranscribeRequest):
    job_name = start_transcription_job(request.s3_url)
    return {"message": "Transcription started", "job_name": job_name}

@router.get("/transcribe/status/{job_name}")
def transcription_status(job_name: str):
    status, transcript_url = get_transcription_status(job_name)
    return {
        "status": status,
        "transcript_url": transcript_url
    }
