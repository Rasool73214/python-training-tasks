
def count_high_salary(emp):
    count = 0
    for salary in emp.values():
        if salary > 50000:
            count += 1
    print("Employees earning more than 50000:", count)
employees = {}
try:
    file = open("employees.txt", "r")
    for line in file:
        try:
            name, salary = line.strip().split(",")
            employees[name] = int(salary)
        except ValueError:
            print("Invalid record ignored:", line.strip())

    file.close()

except FileNotFoundError:
    print("employees.txt file not found.")

print("\nEmployee Dictionary:")
print(employees)

count_high_salary(employees)