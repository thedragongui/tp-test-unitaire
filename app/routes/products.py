from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Product

router = APIRouter()

# Base de données simulée pour les produits
products_db: List[Product] = []

@router.post("/", response_model=Product)
def create_product(product: Product):
    products_db.append(product)
    return product

@router.get("/", response_model=List[Product])
def get_products():
    return products_db

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products_db):
        if product.id == product_id:
            products_db[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/{product_id}")
def delete_product(product_id: int):
    for product in products_db:
        if product.id == product_id:
            products_db.remove(product)
            return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")
