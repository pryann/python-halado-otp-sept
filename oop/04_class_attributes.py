class Student:
    school_name = "Berklee College of Music"
    students = []

    __slots__ = ("first_name", "last_name", "subjects", "__neptun_code")

    def __init__(self, first_name, last_name, subjects, neptun_code):
        self.first_name = first_name
        self.last_name = last_name
        self.subjects = subjects
        self.__neptun_code = neptun_code
        Student.students.append(self)

    def __average(self):
        return round(
            sum(subject["grade"] for subject in self.subjects) / len(self.subjects), 2
        )

    def __credits(self):
        return sum(
            subject["credit"] for subject in self.subjects if subject["grade"] > 1
        )

    def log_stats(self):
        print(
            f"{self.first_name} {self.last_name} average: {self.__average()}, credits: {self.__credits()}"
        )


student = Student(
    "John",
    "Doe",
    [
        {"name": "Math", "credit": 4, "grade": 3},
        {"name": "Physics", "credit": 5, "grade": 1},
        {"name": "History", "credit": 3, "grade": 3},
    ],
    "ABC123",
)

print(student.school_name)

student_2 = Student(
    "Jane",
    "Doe",
    [
        {"name": "Math", "credit": 4, "grade": 3},
        {"name": "Physics", "credit": 5, "grade": 1},
        {"name": "History", "credit": 3, "grade": 3},
    ],
    "XYZ789",
)

print(student_2.school_name)

print(Student.school_name)

print(Student.students)
print([student.first_name for student in Student.students])

# AttributeError: 'Student' object has no attribute 'average'
# print(student.__average())
print(student._Student__average())


# student.log_stats()
# AttributeError: 'Student' object has no attribute '__neptun_code'
# print(student.__neptun_code)
print(student._Student__neptun_code)
