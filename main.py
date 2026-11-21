
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

import models
from database import engine, SessionLocal

# Create database table
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Employee input structure
class EmployeeCreate(BaseModel):
    name: str
    age: int
    department: str

@app.get("/")
def home():
    return {"message": "Employee Management API"}

# CREATE
@app.post("/employees")
def add_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = models.Employee(**employee.model_dump())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

# READ
@app.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()

# UPDATE
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

    if not existing:
        raise HTTPException(status_code=404, detail="Employee not found")

    existing.name = employee.name
    existing.age = employee.age
    existing.department = employee.department

    db.commit()
    db.refresh(existing)
    return existing

# DELETE
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    existing = db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

    if not existing:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(existing)
    db.commit()

    return {"message": "Employee deleted successfully"}
