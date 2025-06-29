from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.customers import CustomerOut
from app.crud.customers import get_customers

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/customers", response_model=list[CustomerOut])
def read_customers(db: Session = Depends(get_db)):
    return get_customers(db)

