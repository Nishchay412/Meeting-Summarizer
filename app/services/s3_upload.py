import uuid
from app.utils.aws_client import s3_client

BUCKET_NAME = "meeting-summarizer-nishchay"

def upload_file_to_s3(file_obj, filename: str, content_type: str) -> str:
    key = f"uploads/{uuid.uuid4()}_{filename}"

    s3_client.upload_fileobj(
        file_obj,
        BUCKET_NAME,
        key,
        ExtraArgs={"ContentType": content_type}
    )

    url = f"https://{BUCKET_NAME}.s3.eu-north-1.amazonaws.com/{key}"
    return url
