import json

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
    
    with open ("employees.txt", "a") as f:
        f.write(json.dumps(employees) + "\n")
    
    print("Employee Added Successfully!!")
    return

def  view_Employees():
    with open("employees.txt", "r") as f:
        count = 1
        for one_Employee in f:
            employee = json.loads(one_Employee)
            print("-----------------------------")
            print("Employee ", count)
            print(f"Name : {employee["name"]}\nID : {employee["id"]}\nSalary : {employee["salary"]}")
            count += 1
        

print(" Employee Salary Management System")
while True:
    print("\n1. Add Employee\n2. View Employees\n3. Exit")
    op = int(input("Choose Option: "))
    if(op==1): add_Employee()
    elif(op==2): view_Employees()
    elif(op==3): break
    else: print("Choose among 1, 2 and 3")