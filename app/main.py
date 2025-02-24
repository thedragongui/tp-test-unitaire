from fastapi import FastAPI
from app.routes import products, invoices, clients

app = FastAPI(
    title="API REST pour FIBRUS",
    description="API REST développée en FastAPI en suivant BDD et TDD.",
    version="1.0.0"
)

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(invoices.router, prefix="/invoices", tags=["Invoices"])
app.include_router(clients.router, prefix="/clients", tags=["Clients"])
