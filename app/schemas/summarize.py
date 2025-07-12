from pydantic import BaseModel

class SummarizeRequest(BaseModel):
    transcript_url: str
