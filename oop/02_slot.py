class Student:
    __slots__ = ("first_name", "last_name")

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


student = Student("John", "Doe")
print(student.first_name)
print(student.last_name)

# AttributeError
student.age = 20
print(student.age)
