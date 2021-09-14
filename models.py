from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.types import DateTime, Text, Enum, Date
from sqlalchemy.orm import relationship
from database import Base
from choices import Sender

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, index=True, nullable=True)
    timestamp = Column(DateTime)
    assensment = Column(Integer, index=True, nullable=True)
    is_answered = Column(Boolean, default=False)
    sender = Column(Enum(Sender))