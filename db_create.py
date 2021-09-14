import datetime

from app import models
from app.database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

db_record = models.Message(
    
)

db.add(db_record)

db.commit()
db.close()