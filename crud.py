import datetime
from sqlalchemy.orm import Session
import models, schemas

def get_messages(db: Session):
    return db.query(models.Message).all()

def send_message(db: Session, text, sender, assensment):
    timestamp = datetime.datetime.now()

    db_message = models.Message(sender=sender, timestamp=timestamp, text=text, assensment=assensment)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)

    return db_message