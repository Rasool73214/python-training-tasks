class Employee:
    def __init__(self, emp_id, name, dept, salary):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.salary = salary
    def display(self):
        print("\nEmployee Details")
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Department  :", self.dept)
        print("Salary      :", self.salary) 
employees = []
n = int(input("How many employees do you want to enter? "))
for i in range(n):
    print("\nEnter details of Employee", i + 1)
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    emp = Employee(emp_id, name, dept, salary)
    employees.append(emp)
print("\n----- All Employee Details -----")
for emp in employees:
    emp.display()