from sqlalchemy.orm import Session
from config.database import Session

def get_db() -> Session:
    db = Session()
    try:
        yield db
    finally:
        db.close()