class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class doctor(person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


class patient(person):
    def __init__(self, name, age, patient_id, disease):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.disease = disease

    def display(self):
        super().display()
        print("Patient ID:", self.patient_id)
        print("Disease:", self.disease)


class intern(doctor):
    def __init__(self, name, age, department, intern_id):
        super().__init__(name, age, department)
        self.intern_id = intern_id

    def display(self):
        super().display()
        print("Intern ID:", self.intern_id)


if __name__ == "__main__":
    doctor_obj = doctor("Dr. Amina", 42, "General Medicine")
    intern_obj = intern("Ravi", 24, "General Medicine", "INT1001")

    print("Doctor details:")
    doctor_obj.display()
    print("\nIntern details:")
    intern_obj.display()

    print("\nEnter patient details:")
    patient_name = input("Patient name: ") or "Sara"
    patient_age = input("Patient age: ") or "30"
    patient_id = input("Patient ID: ") or "P100"
    disease = input("Disease: ") or "Cold"

    patient_obj = patient(patient_name, patient_age, patient_id, disease)

    print("\nPatient details:")
    patient_obj.display()

    print("\nAll member details:")
    print("\nDoctor details:")
    doctor_obj.display()
    print("\nIntern details:")
    intern_obj.display()
    print("\nPatient details:")
    patient_obj.display()
