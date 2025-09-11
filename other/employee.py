import requests


class Employee:
    raise_amt = 1.05

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@company.com"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.salary = int(self.salary * Employee.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(
            f"https://company.com/{self.first_name}-{self.last_name}/{month}"
        )

        if response.ok:
            return response.text
        else:
            return "Bad Response!"
