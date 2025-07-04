# app/routes/summarize.py

from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    return {"filename": file.filename}
