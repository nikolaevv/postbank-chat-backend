from datetime import datetime, date
from typing import Optional
from choices import Sender
from pydantic import BaseModel

class Message(BaseModel):
    id: int
    text: str
    timestamp: datetime
    assensment: Optional[int]
    is_answered: bool
    sender: Sender

    class Config:
        orm_mode = True

class MessageSend(BaseModel):
    text: str
    sender: Sender