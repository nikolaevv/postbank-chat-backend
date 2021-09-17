import datetime

import models
from database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

db_record = models.Message(
    text="Здравствуйте, я произвела частичное досрочное погашение кредита, но у меня уменьшился срок кредита, а не перерасчёт процентов, как сделать чтобы был именно платёж уменьшался?",
    timestamp=datetime.datetime.now(),
    assensment=50,
    sender="USER"
)

db.add(db_record)

db.commit()
db.close()