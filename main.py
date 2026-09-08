from fastapi import FastAPI

from Models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to Vengi's Tech World!!!"

# Products = [
#     Product(1, "Phone", "Budget friendly phone",99,10),
#     Product(2, "Laptop", "Budget friendly Laptop",999,100),
#     Product(3, "Tablet", "Budget friendly Tablet",48,10),
# ]

Products = [
    Product(id=1, name="Phone", description="Budget friendly phone", price=99, quantity=10),
    Product(id=2, name="Laptop", description="Budget friendly Laptop", price=999, quantity=100),
    Product(id=3, name="Tablet", description="Budget friendly Tablet", price=48, quantity=10),
]

@app.get("/products")
def get_all_products():
    return Products

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in Products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}

@app.post("/products")
def add_product(product: Product):
    Products.append(product)
    return {"message": "Product added successfully"}

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(Products):
        if product.id == product_id:
            Products[index] = updated_product
            return {"message": "Product updated successfully"}
    return {"error": "Product not found"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(Products):
        if product.id == product_id:
            del Products[index]
            return {"message": "Product deleted successfully"}
    return {"error": "Product not found"}