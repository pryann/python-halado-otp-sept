import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("John", "Doe", 50_000)

    def test_email(self):
        self.assertEqual(self.employee.email, "john.doe@company.com")

    def test_full_name(self):
        self.assertEqual(self.employee.full_name, "John Doe")


if __name__ == "__main__":
    unittest.main()
