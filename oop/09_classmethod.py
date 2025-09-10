class Employee:
    company_name = "Evil Corp"
    employee_count = 0

    __slots__ = ("name", "salary")

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_info(self):
        return f"Employee Name: {self.name}, Salary: {self.salary} USD"

    @classmethod
    def get_company_info(cls):
        return f"Company: {cls.company_name}, total employees: {cls.employee_count}"


employee = Employee("Alice", 75_000)
print(employee.display_info())
print(Employee.company_name)
print(Employee.employee_count)
print(Employee.get_company_info())
