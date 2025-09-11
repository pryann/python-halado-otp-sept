import unittest
from my_lib import summa, subtract, divide


class TestMyLib(unittest.TestCase):
    def test_summa(self):
        self.assertEqual(summa(2, 3), 5)
        self.assertEqual(summa(-5, 5), 0)
        self.assertEqual(summa(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(-5, 5), -10)
        self.assertEqual(subtract(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(7, 3), 2.3333333333333335)
        self.assertRaises(ValueError, divide, 5, 0)


if __name__ == "__main__":
    unittest.main()
