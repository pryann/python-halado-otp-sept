class Employee:
    top_salary = 100_000

    __slots__ = ("first_name", "last_name", "job", "__yearly_salary")

    def __init__(self, first_name, last_name, job, yearly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.__yearly_salary = yearly_salary

    def get_yearly_salary(self):
        return f"{round(self.__yearly_salary, 2)} USD yearly"

    def set_yearly_salary(self, new_salary):
        # if new_salary > Employee.top_salary:
        #     self.__yearly_salary = Employee.top_salary
        # else:
        #     self.__yearly_salary = new_salary
        self.__yearly_salary = (
            Employee.top_salary if new_salary > Employee.top_salary else new_salary
        )


employee = Employee("John", "Doe", "Developer", 90_000)
print(employee.get_yearly_salary())
employee.set_yearly_salary(120_000)
print(employee.get_yearly_salary())
