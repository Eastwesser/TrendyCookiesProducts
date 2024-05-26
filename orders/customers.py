from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.models import Order
from database import SessionLocal

app = FastAPI()


# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Route to get all orders
@app.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    return orders
