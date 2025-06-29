from sqlalchemy import Column, String
from app.database import Base

class Customer(Base):
    __tablename__ = "customers"  # existing table name

    customer_id = Column(String(20), primary_key=True, index=True)
    company_name = Column(String(255))
    contact_name = Column(String(255))
    contact_title = Column(String(255))
    address = Column(String(255))
    city = Column(String(100))
    region = Column(String(100))
    postal_code = Column(String(20))
    country = Column(String(100))
    phone = Column(String(30))
    fax = Column(String(30))
