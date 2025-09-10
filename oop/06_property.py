class Employee:
    top_salary = 100_000

    __slots__ = ("first_name", "last_name", "job", "__yearly_salary")

    def __init__(self, first_name, last_name, job, yearly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.__yearly_salary = yearly_salary

    @property
    def yearly_salary(self):
        return f"{round(self.__yearly_salary, 2)} USD yearly"

    @yearly_salary.setter
    def yearly_salary(self, new_salary):
        # if new_salary > Employee.top_salary:
        #     self.__yearly_salary = Employee.top_salary
        # else:
        #     self.__yearly_salary = new_salary
        self.__yearly_salary = (
            Employee.top_salary if new_salary > Employee.top_salary else new_salary
        )

    @yearly_salary.deleter
    def yearly_salary(self):
        print(f"{self.first_name} {self.last_name}'s salary not paid!")
        del self.__yearly_salary


employee = Employee("John", "Doe", "Developer", 90_000)
print(employee.yearly_salary)
employee.yearly_salary = 120_000
print(employee.yearly_salary)

del employee.yearly_salary
# 'Employee' object has no attribute '_Employee__yearly_salary'
# print(employee.yearly_salary)

employee.yearly_salary = 80_000
print(employee.yearly_salary)
