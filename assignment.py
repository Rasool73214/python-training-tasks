def find_topper(student_dict):
    if student_dict:
        topper = max(student_dict, key=student_dict.get)
        print("\nTopper:")
        print("Name:", topper)
        print("Marks:", student_dict[topper])
    else:
        print("No valid records found.")
students = {}
try:
    file = open("student.txt", "r")
    for line in file:
        try:
            name, marks = line.strip().split(",")
            students[name] = int(marks)
        except ValueError:
            print("Invalid record ignored:", line.strip())
    file.close()
except FileNotFoundError:
    print("student.txt file not found.")
print("\nStudent Dictionary:")
print(students)
find_topper(students)