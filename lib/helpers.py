from models.department import Department
from models.employee import Employee

def list_employees():
    """List all employees"""
    employees = Employee.get_all()
    for employee in employees:
        print(employee)

def find_employee_by_name():
    """Find employee by name"""
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f"Employee {name} not found")

def find_employee_by_id():
    """Find employee by id"""
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f"Employee {id_} not found")

def create_employee():
    """Create new employee"""
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = input("Enter the employee's department id: ")
    
    try:
        employee = Employee.create(name, job_title, department_id)
        print(f"Success: {employee}")
    except Exception as exc:
        print(f"Error creating employee: {exc}")

def update_employee():
    """Update existing employee"""
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    
    if not employee:
        print(f"Employee {id_} not found")
        return
    
    try:
        name = input("Enter the employee's new name: ")
        job_title = input("Enter the employee's new job title: ")
        department_id = input("Enter the employee's new department id: ")
        
        employee.name = name
        employee.job_title = job_title
        employee.department_id = department_id
        employee.update()
        
        print(f"Success: {employee}")
    except Exception as exc:
        print(f"Error updating employee: {exc}")

def delete_employee():
    """Delete employee"""
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    
    if employee:
        employee.delete()
        print(f"Employee {id_} deleted")
    else:
        print(f"Employee {id_} not found")

def list_department_employees():
    """List all employees in a department"""
    department_id = input("Enter the department's id: ")
    department = Department.find_by_id(department_id)
    
    if department:
        employees = department.employees()
        for employee in employees:
            print(employee)
    else:
        print(f"Department {department_id} not found")