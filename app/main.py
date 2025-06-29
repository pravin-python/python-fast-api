from fastapi import FastAPI
from app.routers import customers

app = FastAPI(
    title="Northwind API",
    description="FastAPI project using existing MySQL tables like `customers`",
    version="1.0.0",
    docs_url="/docs",         # Swagger UI (default)
    redoc_url="/redoc",       # ReDoc documentation
    openapi_url="/openapi.json"  # OpenAPI schema
)

app.include_router(customers.router, prefix="/api", tags=["Customers"])
