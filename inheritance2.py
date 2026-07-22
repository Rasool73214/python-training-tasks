class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_person(self):
        print(f"{self.name}'s age is {self.age}")
class student(person):
    def __init__(self,rollnum,course):
        self.rollnum = rollnum
        self.course = course
    def display_student(self):
        print(f"the student with roll no. {self.rollnum} is studying {self.course}")
person("ofiq",20).display_person()
student(21,"AI").display_student()