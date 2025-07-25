from fastapi import APIRouter, UploadFile, File, Query, HTTPException
from app.services.s3_upload import upload_file_to_s3
from io import BytesIO
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from app.schemas.summarize import SummarizeRequest
from app.services.openai_summary import fetch_transcript_text, summarize_text
from app.services.openai_summary import summarize_text
from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    contents = await file.read()
    buffer = BytesIO(contents)

    s3_url = upload_file_to_s3(buffer, file.filename, file.content_type)

    return {
        "message": "File uploaded successfully",
        "s3_url": s3_url
    }


import requests

def get_transcript_text_from_url(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    transcript_json = response.json()
    return transcript_json["results"]["transcripts"][0]["transcript"]


@router.get("/transcript")
def get_transcript(transcript_url: str = Query(..., description="URL to the AWS transcript JSON")):
    try:
        res = requests.get(transcript_url)
        res.raise_for_status()
        data = res.json()
        transcript = data["results"]["transcripts"][0]["transcript"]
        return {"transcript": transcript}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch transcript: {str(e)}")
    




    
@router.post("/summarize")
def summarize(transcript_url: str = Body(..., embed=True)):
    try:
        transcript_text = fetch_transcript_text(transcript_url)
        summary = summarize_text(transcript_text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to summarize: {str(e)}")
