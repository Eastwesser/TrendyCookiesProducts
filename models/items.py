from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    title: str
    text: str
    price: float
    weight: str
    image: str


@app.get("/api/products")
def get_products():
    # Получение данных из базы данных PostgreSQL
    products = [
        {
            "title": "Лучшие друзья",
            "text": "Печенье, с которого все началось! Наше фирменное печенье с шоколадной крошкой "
                    "и грецкими орехами хрустящее снаружи с достаточно толстой и липкой серединкой.",
            "price": 20,
            "weight": "2 шт./ 200 гр.",
            "image": "images/1.png"
        },
        # Добавьте остальные продукты
    ]
    return products
