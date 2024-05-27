from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.data import products_data
from orders.orders_db import save_user_info

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/products", response_class=HTMLResponse)
async def get_products(request: Request):
    return templates.TemplateResponse(
        "products.html",
        {
            "request": request,
            "products_data": products_data
        }
    )


@app.post("/order")
async def create_order(request: Request, product_id: int = Form(...), name: str = Form(...), phone: str = Form(...)):
    order_id = save_user_info(product_id, name, phone)
    return {"message": f"Order for product with ID {product_id} created with order ID {order_id}"}


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
