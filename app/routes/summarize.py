# app/routes/summarize.py

from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    return {"filename": file.filename}


from fastapi import APIRouter, UploadFile, File
from app.services.s3_upload import upload_file_to_s3
from io import BytesIO

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
