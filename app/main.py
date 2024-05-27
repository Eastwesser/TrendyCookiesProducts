from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database.models import UserInfo
from app.data import products_data
from app.database.database import SessionLocal

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class OrderRequest(BaseModel):
    name: str
    phone_number: str
    product_title: str


def save_user_info(db: Session, name: str, phone_number: str):
    db_user_info = UserInfo(name=name, phone_number=phone_number)
    db.add(db_user_info)
    db.commit()
    db.refresh(db_user_info)
    return db_user_info


@app.get("/products", response_class=HTMLResponse)
async def get_products(request: Request):
    return templates.TemplateResponse(
        "products.html",
        {
            "request": request,
            "products_data": products_data
        }
    )


@app.post("/orders")
async def create_order(order_data: OrderRequest, db: Session = Depends(SessionLocal)):
    # Call the function to save user info
    order = save_user_info(db, order_data.name, order_data.phone_number)
    return JSONResponse(content={"message": "Order created successfully", "order": order})


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
