class Student:
    __slots__ = ("first_name", "last_name", "subjects")

    def __init__(self, first_name, last_name, subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.subjects = subjects

    def average(self):
        return round(
            sum(subject["grade"] for subject in self.subjects) / len(self.subjects), 2
        )

    def credits(self):
        return sum(
            subject["credit"] for subject in self.subjects if subject["grade"] > 1
        )


student = Student(
    "John",
    "Doe",
    [
        {"name": "Math", "credit": 4, "grade": 3},
        {"name": "Physics", "credit": 5, "grade": 1},
        {"name": "History", "credit": 3, "grade": 3},
    ],
)
print(student.first_name)
print(student.last_name)
print(student.average())
print(student.credits())
