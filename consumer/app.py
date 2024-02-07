from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    name: str
    age: int
    department: str

@app.get("/dashboard/employees", response_model=List[Employee])
async def get_dashboard_employees():
    # Here you'd have your logic to fetch employees from Employee Service
    # For the sake of simplicity, let's return a dummy list
    dummy_employees = [
        Employee(name="John Doe", age=30, department="IT"),
        Employee(name="Jane Smith", age=35, department="HR")
    ]
    return dummy_employees
