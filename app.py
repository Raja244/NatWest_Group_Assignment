import json
import os

from flask import Flask, jsonify, request

app = Flask(__name__)

# File to store employee data
EMPLOYEES_FILE = 'employees.json'

# Function to load employee data from file
def load_employees():
    if os.path.exists(EMPLOYEES_FILE):
        with open(EMPLOYEES_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                # Handle empty or invalid JSON file
                return []
    else:
        return []

# Function to save employee data to file
def save_employees(employees):
    with open(EMPLOYEES_FILE, 'w') as f:
        json.dump(employees, f, indent=4)

# Sample data to store employees
employees = load_employees()

# GET /employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees), 200

# POST /employees
@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400
    
    # Generate employee ID based on the last ID in the list
    last_id = employees[-1]['id'] if employees else '000'
    new_id = f"{int(last_id) + 1:03}"
    
    employee = {
        'id': new_id,
        'name': data.get('name'),
        'age': data.get('age'),
        'department': data.get('department')
    }
    employees.append(employee)
    save_employees(employees)
    return jsonify(employee), 201

# GET /employees/{employeeId}
@app.route('/employees/<employeeId>', methods=['GET'])
def get_employee(employeeId):
    for employee in employees:
        if employee.get('id') == employeeId:
            return jsonify(employee), 200
    return jsonify({'error': 'Employee not found'}), 404



# PUT /employees/{employeeId}
@app.route('/employees/<employeeId>', methods=['PUT'])
def update_employee(employeeId):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400
    
    for employee in employees:
        if employee.get('id') == employeeId:
            employee['name'] = data.get('name')
            employee['age'] = data.get('age')
            employee['department'] = data.get('department')
            save_employees(employees)
            return jsonify(employee), 200
    return jsonify({'error': 'Employee not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
