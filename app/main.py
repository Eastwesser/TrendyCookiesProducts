from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.data import products_data
from app.database.models import Base, Product

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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
