from fastapi import FastAPI

from Models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to Vengi's Tech World!!!"

Products = [
    Product(1, "Phone", "Budget friendly phone",99,10),
    Product(2, "Laptop", "Budget friendly Laptop",999,100),
    Product(3, "Tablet", "Budget friendly Tablet",48,10),
]


@app.get("/products")
def get_all_products():
    return Products