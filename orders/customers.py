from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.postgre_db import SessionLocal
import orders_db

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/place_order")
def place_order(name: str, phone_number: str, db: Session = Depends(get_db)):
    user_info = orders_db.save_user_info(db, name, phone_number)
    return {"message": "Order placed successfully", "user_info": user_info}
