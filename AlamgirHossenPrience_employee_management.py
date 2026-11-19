with open ("employees.txt", "a") as f:
    f.write("")

def add_Employee():
    name = input("Enter Employee name: ")
    id = int(input("Enter Employee ID: "))
    salary = int(input("Enter Employee Salary: "))
    
    employees = {
        "name": name,
        "id": id,
        "salary": salary,
    }
    
    return employees

print(add_Employee())
    
