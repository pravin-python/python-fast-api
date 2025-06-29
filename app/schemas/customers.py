from pydantic import BaseModel

class CustomerOut(BaseModel):
    customer_id: str
    company_name: str | None = None
    contact_name: str | None = None
    contact_title: str | None = None
    address: str | None = None
    city: str | None = None
    region: str | None = None
    postal_code: str | None = None
    country: str | None = None
    phone: str | None = None
    fax: str | None = "this is"

    class Config:
        orm_mode = True
