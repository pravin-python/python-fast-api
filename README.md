# 🚀 FastAPI + MySQL (Existing DB) - API

This project demonstrates how to build a FastAPI app connected to a MySQL database using SQLAlchemy and `mysqlclient`.  
It uses an existing table (`customers`) from a typical Northwind database schema **without recreating or deleting the table**.

---

## 📁 Project Structure

fastapi_project/
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── database.py # SQLAlchemy DB connection
│ ├── models/
│ │ └── customers.py # SQLAlchemy model (mapped to existing table)
│ ├── schemas/
│ │ └── customers.py # Pydantic schema for API response
│ ├── crud/
│ │ └── customers.py # Database queries
│ ├── routers/
│ │ └── customers.py # API endpoint
│ └── init.py
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-mysql-northwind.git
cd fastapi-mysql-northwind

pip install -r requirements.txt


sudo apt install libmysqlclient-dev python3-dev

uvicorn app.main:app --reload
