from typing import List
from pydantic import BaseModel

class EmailInput(BaseModel):
    subject: str
    body: str
    sender: str
    urls: List[str]
