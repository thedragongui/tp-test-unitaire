from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Invoice

router = APIRouter()

# Base de données simulée pour les factures
invoices_db: List[Invoice] = []

@router.post("/", response_model=Invoice)
def create_invoice(invoice: Invoice):
    invoices_db.append(invoice)
    return invoice

@router.get("/", response_model=List[Invoice])
def get_invoices():
    return invoices_db

@router.get("/{invoice_id}", response_model=Invoice)
def get_invoice(invoice_id: int):
    for invoice in invoices_db:
        if invoice.id == invoice_id:
            return invoice
    raise HTTPException(status_code=404, detail="Invoice not found")

@router.put("/{invoice_id}", response_model=Invoice)
def update_invoice(invoice_id: int, updated_invoice: Invoice):
    for index, invoice in enumerate(invoices_db):
        if invoice.id == invoice_id:
            invoices_db[index] = updated_invoice
            return updated_invoice
    raise HTTPException(status_code=404, detail="Invoice not found")

@router.delete("/{invoice_id}")
def delete_invoice(invoice_id: int):
    for invoice in invoices_db:
        if invoice.id == invoice_id:
            invoices_db.remove(invoice)
            return {"message": "Invoice deleted"}
    raise HTTPException(status_code=404, detail="Invoice not found")
