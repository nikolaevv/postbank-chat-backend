from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Form, File, UploadFile, Header, status
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

import models, schemas, crud
from database import SessionLocal, engine
import smtplib

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
) 

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/api/messages", response_model=List[schemas.Message])
def get_messages(db: Session = Depends(get_db)):
    messages = crud.get_messages(db)
    return messages

@app.post("/api/messages", response_model={})
def send_message(data: schemas.MessageSend, db: Session = Depends(get_db)):
    assensment = 100
    message = crud.send_message(db, data.text, data.sender, assensment)
    messages = crud.get_messages(db)
    return messages