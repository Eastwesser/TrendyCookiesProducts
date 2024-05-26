from sqlalchemy.orm import Session
from app.database.models import UserInfo


def save_user_info(db: Session, name: str, phone_number: str):
    db_user_info = UserInfo(name=name, phone_number=phone_number)
    db.add(db_user_info)
    db.commit()
    db.refresh(db_user_info)
    return db_user_info
