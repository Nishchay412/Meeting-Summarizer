# app/services/transcribe.py

import uuid
from app.utils.aws_client import transcribe_client

def start_transcription_job(s3_url: str) -> str:
    job_name = f"meeting-transcribe-{uuid.uuid4().hex[:8]}"

    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={"MediaFileUri": s3_url},
        MediaFormat=s3_url.split('.')[-1],
        LanguageCode="en-US",
        OutputBucketName="meeting-summarizer-nishchay"
    )

    return job_name
