from unittest import main, TestCase
from unittest.mock import patch, Mock
from employee import Employee


class TestEmployee(TestCase):
    def setUp(self):
        self.employee = Employee("John", "Doe", 50_000)

    def test_email(self):
        self.assertEqual(self.employee.email, "john.doe@company.com")

    def test_full_name(self):
        self.assertEqual(self.employee.full_name, "John Doe")

    def test_apply_raise(self):
        self.employee.apply_raise()
        self.assertEqual(self.employee.salary, 52_500)

    @patch("requests.get")
    def test_monthly_schedule_ok_response(self, mock_get):
        mock_response = Mock()
        mock_response.ok = True
        mock_response.text = "Mothly schedule content"
        mock_get.return_value = mock_response

        result = self.employee.monthly_schedule("May")
        self.assertEqual(result, mock_response.text)

    @patch("requests.get")
    def test_monthly_schedule_bad_response(self, mock_get):
        mock_response = Mock()
        mock_response.ok = False
        mock_get.return_value = mock_response

        result = self.employee.monthly_schedule("June")
        self.assertEqual(result, "Bad Response!")


if __name__ == "__main__":
    main()
