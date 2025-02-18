from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/all_products/")
async def get_all_products():
    with open("data.json", encoding="utf-8") as f:
        data = json.load(f)
    return data


@app.get("/products/{product_name}")
async def get_product(product_name: str):
    with open("data.json", encoding="utf-8") as f:
        data = json.load(f)
    for product in data:
        print(product)
        if product.get("name", None) == product_name:
            return product
    return {"error": "Product not found"}


@app.get("/products/{product_name}/{product_field}")
async def get_product_field(product_name: str, product_field: str):
    with open("data.json", encoding="utf-8") as f:
        data = json.load(f)
    for product in data:
        if product.get("name", None) == product_name:
            return {product_field: product.get(product_field, "Field not found")}
    return {"error": "Product not found"}
