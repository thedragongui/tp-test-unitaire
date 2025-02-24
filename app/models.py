from pydantic import BaseModel, EmailStr
from typing import List

class Product(BaseModel):
    id: int
    name: str
    price: float

class Invoice(BaseModel):
    id: int
    product_ids: List[int]  # Liste d'IDs de produits
    total: float

class Client(BaseModel):
    id: int
    name: str
    email: EmailStr
