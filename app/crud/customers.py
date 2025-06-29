from sqlalchemy.orm import Session
from app.models.customers import Customer

def get_customers(db: Session):
    return db.query(Customer).all()
