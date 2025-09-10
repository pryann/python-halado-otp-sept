class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


student = Student("John", "Doe")
print(student.first_name)
print(student.last_name)

student.first_name = "Jane"
print(student.first_name)

student_2 = Student("Alice", "Smith")
print(student_2.first_name)
print(student_2.last_name)

print(type(student))
