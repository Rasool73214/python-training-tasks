class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Basic Salary:", self.basic_salary)
    def bonus(self):
        if self.basic_salary >= 50000:
            bonus_amount = self.basic_salary * 0.10
        else:
            bonus_amount = self.basic_salary * 0.05
        print("Bonus Amount:", bonus_amount)
        print()
e1 = Employee(101, "ofiq", 60000)
e2 = Employee(102, "rasool", 45000)
e3 = Employee(103, "sravzz", 70000)
e4 = Employee(104, "lilly", 30000)
e5 = Employee(105, "sonu", 50000)
employees = [e1, e2, e3, e4, e5]
for emp in employees:
    emp.display()
    emp.bonus()