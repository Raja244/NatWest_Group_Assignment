from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    name: str
    age: int
    department: str

employee_db = []

@app.get("/employees", response_model=List[Employee])
async def get_employees():
    return employee_db

@app.post("/employees", response_model=Employee, status_code=201)
async def create_employee(employee: Employee):
    employee_db.append(employee)
    return employee

@app.get("/employees/{employee_id}", response_model=Employee)
async def get_employee(employee_id: int):
    for emp in employee_db:
        if emp.id == employee_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

@app.put("/employees/{employee_id}", response_model=Employee)
async def update_employee(employee_id: int, employee: Employee):
    for emp in employee_db:
        if emp.id == employee_id:
            emp.name = employee.name
            emp.age = employee.age
            emp.department = employee.department
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")
